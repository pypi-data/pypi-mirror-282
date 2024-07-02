import warnings

import keras as k
import tensorflow as tf

from pidgan.players.classifiers import Classifier
from pidgan.players.discriminators import Discriminator
from pidgan.players.generators import Generator
from pidgan.utils.checks import checkMetrics, checkOptimizer

MIN_LOG_VALUE = 1e-6
MAX_LOG_VALUE = 1.0


class GAN(k.Model):
    def __init__(
        self,
        generator,
        discriminator,
        use_original_loss=True,
        injected_noise_stddev=0.0,
        feature_matching_penalty=0.0,
        referee=None,
        name="GAN",
        dtype=None,
    ) -> None:
        super().__init__(name=name, dtype=dtype)
        self._loss_name = "GAN original loss"

        self._metrics = list()
        self._train_metrics = None
        self._model_is_built = False

        # Generator
        if not isinstance(generator, Generator):
            raise TypeError(
                f"`generator` should be a pidgan's Generator, "
                f"instead {type(generator)} passed"
            )
        self._generator = generator
        self._g_loss_state = k.metrics.Mean(name="g_loss")
        self._metrics += [self._g_loss_state]

        # Discriminator
        if not isinstance(discriminator, Discriminator):
            raise TypeError(
                f"`discriminator` should be a pidgan's Discriminator, "
                f"instead {type(discriminator)} passed"
            )
        self._discriminator = discriminator
        self._d_loss_state = k.metrics.Mean(name="d_loss")
        self._metrics += [self._d_loss_state]

        # Flag to use the original loss
        assert isinstance(use_original_loss, bool)
        self._use_original_loss = use_original_loss

        # Referee network and loss
        if referee is not None:
            if not isinstance(referee, Classifier):
                if not isinstance(referee, Discriminator):
                    raise TypeError(
                        f"`referee` should be a pidgan's Classifier "
                        f"(or Discriminator), instead "
                        f"{type(referee)} passed"
                    )
            self._referee = referee
            self._referee_loss = k.losses.BinaryCrossentropy()
            self._r_loss_state = k.metrics.Mean(name="r_loss")
            self._metrics += [self._r_loss_state]
        else:
            self._referee = None
            self._referee_loss = None

        # Noise standard deviation
        assert isinstance(injected_noise_stddev, (int, float))
        assert injected_noise_stddev >= 0.0
        self._inj_noise_std = float(injected_noise_stddev)

        # Feature matching penalty
        assert isinstance(feature_matching_penalty, (int, float))
        assert feature_matching_penalty >= 0.0
        self._feature_matching_penalty = float(feature_matching_penalty)

    def build(self, input_shape) -> None:
        super().build(input_shape=input_shape)
        self._train_metrics = checkMetrics(self._train_metrics)
        self._model_is_built = True

    def compile(
        self,
        metrics=None,
        generator_optimizer="rmsprop",
        discriminator_optimizer="rmsprop",
        generator_upds_per_batch=1,
        discriminator_upds_per_batch=1,
        referee_optimizer=None,
        referee_upds_per_batch=None,
    ) -> None:
        super().compile(weighted_metrics=[])

        # Metrics
        if not self._model_is_built:
            self._train_metrics = metrics
            self.build(input_shape=[])
            if self._train_metrics is not None:
                self._metrics += self._train_metrics
        else:
            if metrics is not None:
                warnings.warn(
                    "The `metrics` argument is ignored when the model is "
                    "built before to be compiled. Consider to move the first model "
                    "calling after the `compile()` method to fix this issue.",
                    category=UserWarning,
                    stacklevel=1,
                )

        # Gen/Disc optimizers
        self._g_opt = checkOptimizer(generator_optimizer)
        self._d_opt = checkOptimizer(discriminator_optimizer)

        # Generator updates per batch
        assert isinstance(generator_upds_per_batch, (int, float))
        assert generator_upds_per_batch >= 1
        self._g_upds_per_batch = int(generator_upds_per_batch)

        # Discriminator updates per batch
        assert isinstance(discriminator_upds_per_batch, (int, float))
        assert discriminator_upds_per_batch >= 1
        self._d_upds_per_batch = int(discriminator_upds_per_batch)

        # Referee settings
        if self._referee is not None:
            referee_optimizer = (
                referee_optimizer if referee_optimizer is not None else "rmsprop"
            )
            self._r_opt = checkOptimizer(referee_optimizer)
            if referee_upds_per_batch is not None:
                assert isinstance(referee_upds_per_batch, (int, float))
                assert referee_upds_per_batch >= 1
            else:
                referee_upds_per_batch = 1
            self._r_upds_per_batch = int(referee_upds_per_batch)
        else:
            self._r_opt = None
            self._r_upds_per_batch = None

    def call(self, x, y=None) -> tuple:
        g_out = self._generator(x)
        d_out_gen = self._discriminator((x, g_out))
        if y is None:
            if self._referee is not None:
                r_out_gen = self._referee((x, g_out))
                return g_out, d_out_gen, r_out_gen
            else:
                return g_out, d_out_gen
        else:
            d_out_ref = self._discriminator((x, y))
            if self._referee is not None:
                r_out_gen = self._referee((x, g_out))
                r_out_ref = self._referee((x, y))
                return g_out, (d_out_gen, d_out_ref), (r_out_gen, r_out_ref)
            else:
                return g_out, (d_out_gen, d_out_ref)

    def summary(self, **kwargs) -> None:
        print("_" * 65)
        self._generator.summary(**kwargs)
        self._discriminator.summary(**kwargs)
        if self._referee is not None:
            self._referee.summary(**kwargs)

    def train_step(self, *args, **kwargs):
        if k.backend.backend() == "tensorflow":
            return self._tf_train_step(*args, **kwargs)
        elif k.backend.backend() == "torch":
            raise NotImplementedError(
                "`train_step()` not implemented for the PyTorch backend"
            )
        elif k.backend.backend() == "jax":
            raise NotImplementedError(
                "`train_step()` not implemented for the Jax backend"
            )

    @staticmethod
    def _unpack_data(data) -> tuple:
        if len(data) == 3:
            x, y, sample_weight = data
        else:
            x, y = data
            sample_weight = None
        return x, y, sample_weight

    def _tf_train_step(self, data) -> dict:
        x, y, sample_weight = self._unpack_data(data)

        for _ in range(self._d_upds_per_batch):
            self._tf_d_train_step(x, y, sample_weight)
        for _ in range(self._g_upds_per_batch):
            self._tf_g_train_step(x, y, sample_weight)
        if self._referee is not None:
            for _ in range(self._r_upds_per_batch):
                self._tf_r_train_step(x, y, sample_weight)

        return self._update_metric_states(x, y, sample_weight)

    def _tf_g_train_step(self, x, y, sample_weight=None) -> None:
        with tf.GradientTape() as tape:
            loss = self._compute_g_loss(x, y, sample_weight, training=True, test=False)

        trainable_vars = self._generator.trainable_weights
        gradients = tape.gradient(loss, trainable_vars)
        self._g_opt.apply_gradients(zip(gradients, trainable_vars))

        threshold = self._compute_threshold(self._discriminator, x, y, sample_weight)
        self._g_loss_state.update_state(loss + threshold)

    def _tf_d_train_step(self, x, y, sample_weight=None) -> None:
        with tf.GradientTape() as tape:
            loss = self._compute_d_loss(x, y, sample_weight, training=True, test=False)

        trainable_vars = self._discriminator.trainable_weights
        gradients = tape.gradient(loss, trainable_vars)
        self._d_opt.apply_gradients(zip(gradients, trainable_vars))

        threshold = self._compute_threshold(self._discriminator, x, y, sample_weight)
        self._d_loss_state.update_state(loss - threshold)

    def _tf_r_train_step(self, x, y, sample_weight=None) -> None:
        with tf.GradientTape() as tape:
            loss = self._compute_r_loss(x, y, sample_weight, training=True, test=False)

        trainable_vars = self._referee.trainable_weights
        gradients = tape.gradient(loss, trainable_vars)
        self._r_opt.apply_gradients(zip(gradients, trainable_vars))

        self._r_loss_state.update_state(loss)

    def _update_metric_states(self, x, y, sample_weight) -> None:
        metric_states = {
            "g_loss": self._g_loss_state.result(),
            "d_loss": self._d_loss_state.result(),
        }
        if self._referee is not None:
            metric_states.update({"r_loss": self._r_loss_state.result()})
        if self._train_metrics is not None:
            g_out = self._generator(x, training=False)
            x_concat = k.ops.concatenate([x, x], axis=0)
            y_concat = k.ops.concatenate([y, g_out], axis=0)
            d_out = self._discriminator((x_concat, y_concat), training=False)
            d_ref, d_gen = k.ops.split(d_out, 2, axis=0)
            for metric in self._train_metrics:
                metric.update_state(
                    y_true=d_ref, y_pred=d_gen, sample_weight=sample_weight
                )
                metric_states.update({metric.name: metric.result()})
        return metric_states

    def _prepare_trainset(
        self, x, y, sample_weight=None, training_generator=True
    ) -> tuple:
        batch_size = k.ops.cast(k.ops.shape(x)[0] / 2, dtype="int32")
        x_ref, x_gen = k.ops.split(x[: batch_size * 2], 2, axis=0)
        y_ref = y[:batch_size]
        y_gen = self._generator(x_gen, training=training_generator)

        if sample_weight is not None:
            w_ref, w_gen = k.ops.split(sample_weight[: batch_size * 2], 2, axis=0)
        else:
            w_ref, w_gen = k.ops.split(k.ops.ones(shape=(batch_size * 2,)), 2, axis=0)

        return (x_ref, y_ref, w_ref), (x_gen, y_gen, w_gen)

    @staticmethod
    def _standard_loss_func(
        discriminator,
        trainset_ref,
        trainset_gen,
        inj_noise_std=0.0,
        training_discriminator=False,
        original_loss=True,
        generator_loss=True,
    ) -> tf.Tensor:
        x_ref, y_ref, w_ref = trainset_ref
        x_gen, y_gen, w_gen = trainset_gen

        x_concat = k.ops.concatenate([x_ref, x_gen], axis=0)
        y_concat = k.ops.concatenate([y_ref, y_gen], axis=0)

        if inj_noise_std > 0.0:
            rnd_noise = k.random.normal(
                shape=k.ops.shape(y_concat),
                mean=0.0,
                stddev=inj_noise_std,
                dtype=y_concat.dtype,
            )
            y_concat += rnd_noise

        d_out = discriminator((x_concat, y_concat), training=training_discriminator)
        d_ref, d_gen = k.ops.split(d_out, 2, axis=0)

        real_loss = k.ops.sum(
            w_ref[:, None] * k.ops.log(k.ops.clip(d_ref, MIN_LOG_VALUE, MAX_LOG_VALUE))
        ) / k.ops.sum(w_ref)
        if original_loss:
            fake_loss = k.ops.sum(
                w_gen[:, None]
                * k.ops.log(k.ops.clip(1.0 - d_gen, MIN_LOG_VALUE, MAX_LOG_VALUE))
            ) / k.ops.sum(w_gen)
        else:
            fake_loss = k.ops.sum(
                -w_gen[:, None]
                * k.ops.log(k.ops.clip(d_gen, MIN_LOG_VALUE, MAX_LOG_VALUE))
            )

        if generator_loss:
            return tf.stop_gradient(real_loss) + fake_loss
        else:
            return -(real_loss + fake_loss)

    def _compute_g_loss(
        self, x, y, sample_weight=None, training=True, test=False
    ) -> tf.Tensor:
        trainset_ref, trainset_gen = self._prepare_trainset(
            x, y, sample_weight, training_generator=training
        )
        g_loss = self._standard_loss_func(
            discriminator=self._discriminator,
            trainset_ref=trainset_ref,
            trainset_gen=trainset_gen,
            inj_noise_std=self._inj_noise_std,
            training_discriminator=False,
            original_loss=self._use_original_loss,
            generator_loss=True,
        )
        if not test:
            g_loss += self._compute_feature_matching(
                x, y, sample_weight, training_generator=training
            )
        return g_loss

    def _compute_d_loss(
        self, x, y, sample_weight=None, training=True, test=False
    ) -> tf.Tensor:
        trainset_ref, trainset_gen = self._prepare_trainset(
            x, y, sample_weight, training_generator=False
        )
        return self._standard_loss_func(
            discriminator=self._discriminator,
            trainset_ref=trainset_ref,
            trainset_gen=trainset_gen,
            inj_noise_std=self._inj_noise_std,
            training_discriminator=training,
            original_loss=True,
            generator_loss=False,
        )

    def _compute_r_loss(
        self, x, y, sample_weight=None, training=True, test=False
    ) -> tf.Tensor:
        trainset_ref, trainset_gen = self._prepare_trainset(
            x, y, sample_weight, training_generator=False
        )
        x_ref, y_ref, w_ref = trainset_ref
        x_gen, y_gen, w_gen = trainset_gen

        x_concat = k.ops.concatenate([x_ref, x_gen], axis=0)
        y_concat = k.ops.concatenate([y_ref, y_gen], axis=0)

        r_out = self._referee((x_concat, y_concat), training=training)
        r_ref, r_gen = k.ops.split(r_out, 2, axis=0)

        real_loss = self._referee_loss(
            k.ops.ones_like(r_ref), r_ref, sample_weight=w_ref
        )
        fake_loss = self._referee_loss(
            k.ops.zeros_like(r_gen), r_gen, sample_weight=w_gen
        )
        return (real_loss + fake_loss) / 2.0

    def _compute_feature_matching(
        self, x, y, sample_weight=None, training_generator=True
    ) -> tf.Tensor:
        if self._feature_matching_penalty > 0.0:
            trainset_ref, trainset_gen = self._prepare_trainset(
                x, y, sample_weight, training_generator=training_generator
            )
            x_ref, y_ref, _ = trainset_ref
            x_gen, y_gen, _ = trainset_gen

            x_concat = k.ops.concatenate([x_ref, x_gen], axis=0)
            y_concat = k.ops.concatenate([y_ref, y_gen], axis=0)

            if self._inj_noise_std is not None:
                if self._inj_noise_std > 0.0:
                    rnd_noise = k.random.normal(
                        shape=(k.ops.shape(y_ref)[0] * 2, k.ops.shape(y_ref)[1]),
                        mean=0.0,
                        stddev=self._inj_noise_std,
                        dtype=y_ref.dtype,
                    )
                    y_concat += rnd_noise

            d_feat_out = self._discriminator.hidden_feature((x_concat, y_concat))
            d_feat_ref, d_feat_gen = k.ops.split(d_feat_out, 2, axis=0)

            feat_match_term = k.ops.norm(d_feat_ref - d_feat_gen, axis=-1) ** 2
            return self._feature_matching_penalty * k.ops.mean(feat_match_term)
        else:
            return 0.0

    def _prepare_trainset_threshold(self, x, y, sample_weight=None) -> tuple:
        batch_size = k.ops.cast(k.ops.shape(x)[0] / 2, dtype="int32")
        x_ref_1, x_ref_2 = k.ops.split(x[: batch_size * 2], 2, axis=0)
        y_ref_1, y_ref_2 = k.ops.split(y[: batch_size * 2], 2, axis=0)

        if sample_weight is not None:
            w_ref_1, w_ref_2 = k.ops.split(sample_weight[: batch_size * 2], 2, axis=0)
        else:
            w_ref_1, w_ref_2 = k.ops.split(
                k.ops.ones(shape=(batch_size * 2,)), 2, axis=0
            )

        return (x_ref_1, y_ref_1, w_ref_1), (x_ref_2, y_ref_2, w_ref_2)

    def _compute_threshold(self, discriminator, x, y, sample_weight=None) -> tf.Tensor:
        trainset_ref_1, trainset_ref_2 = self._prepare_trainset_threshold(
            x, y, sample_weight
        )
        return self._standard_loss_func(
            discriminator=discriminator,
            trainset_ref=trainset_ref_1,
            trainset_gen=trainset_ref_2,
            inj_noise_std=0.0,
            training_discriminator=False,
            original_loss=True,
            generator_loss=False,
        )

    def test_step(self, data) -> dict:
        x, y, sample_weight = self._unpack_data(data)

        threshold = self._compute_threshold(self._discriminator, x, y, sample_weight)

        g_loss = self._compute_g_loss(x, y, sample_weight, training=False, test=True)
        self._g_loss_state.update_state(g_loss + threshold)

        d_loss = self._compute_d_loss(x, y, sample_weight, training=False, test=True)
        self._d_loss_state.update_state(d_loss - threshold)

        if self._referee is not None:
            r_loss = self._compute_r_loss(
                x, y, sample_weight, training=False, test=True
            )
            self._r_loss_state.update_state(r_loss)

        return self._update_metric_states(x, y, sample_weight)

    def generate(self, x, seed=None) -> tf.Tensor:
        return self._generator.generate(x, seed=seed)

    @property
    def loss_name(self) -> str:
        return self._loss_name

    @property
    def generator(self) -> Generator:
        return self._generator

    @property
    def discriminator(self) -> Discriminator:
        return self._discriminator

    @property
    def use_original_loss(self) -> bool:
        return self._use_original_loss

    @property
    def injected_noise_stddev(self) -> float:
        return self._inj_noise_std

    @property
    def feature_matching_penalty(self) -> float:
        return self._feature_matching_penalty

    @property
    def referee(self):  # TODO: add Union[None, Discriminator]
        return self._referee

    @property
    def metrics(self) -> list:
        return self._metrics

    @property
    def generator_optimizer(self) -> k.optimizers.Optimizer:
        return self._g_opt

    @property
    def discriminator_optimizer(self) -> k.optimizers.Optimizer:
        return self._d_opt

    @property
    def generator_upds_per_batch(self) -> int:
        return self._g_upds_per_batch

    @property
    def discriminator_upds_per_batch(self) -> int:
        return self._d_upds_per_batch

    @property
    def referee_optimizer(self):  # TODO: add Union[None, Optimizer]
        return self._r_opt

    @property
    def referee_upds_per_batch(self):  # TODO: add Union[None, int]
        return self._r_upds_per_batch
