import math
import random

import keras
import tensorflow as tf

import mlable.utils

# LOSS ########################################################################

# ACCURACY ####################################################################

def token_accuracy(y_true: tf.Tensor, y_pred: tf.Tensor, group: int=4) -> tuple:
    __shape = mlable.utils.normalize_shape(list(y_true.shape))
    # category indexes
    __yt = tf.argmax(y_true, axis=-1)
    __yp = tf.argmax(y_pred, axis=-1)
    # matching
    __match = tf.equal(__yt, __yp)
    # group all the predictions for a given token
    if group and group > 1:
        # split
        __shape[-1] = mlable.utils.divide_dim(dim_l=shape[-1], dim_r=group)
        __shape.append(group)
        # reshape
        __match = tf.reshape(__match, shape=__shape)
        # the token prediction is right if ALL its byte predictions are right
        __match = tf.reduce_all(__match, axis=-1)
    # cast
    __total = tf.convert_to_tensor(math.prod(list(__match.shape)), dtype=tf.dtypes.int32)
    __match = tf.cast(__match, type=tf.dtypes.int32)
    # sum
    return (__total, tf.reduce_sum(__match))

class TokenAccuracy(tf.keras.metrics.Metric):
    def __init__(self, token_dim: int=4, name='token_accuracy', **kwargs):
        # init
        super(TokenAccuracy, self).__init__(name=name, **kwargs)
        # token size
        self._token = token_dim
        # state
        self._total = self.add_weight(shape=(), dtype=tf.dtypes.int32, name='total', initializer='zeros')
        self._correct = self.add_weight(shape=(), dtype=tf.dtypes.int32, name='correct', initializer='zeros')

    def reset_state(self) -> None:
        self._total.assign(0)
        self._correct.assign(0)

    def update_state(self, y_true: tf.Tensor, y_pred: tf.Tensor, sample_weight: tf.Tensor=None) -> None:
        __total, __correct = token_accuracy(y_true=y_true, y_pred=y_pred, group=self._token)
        # actually update
        self._total.assign_add(__total)
        self._correct.assign_add(__correct)

    def result(self) -> tf.Tensor:
        return self._correct / self._total

@keras_export("keras.metrics.categorical_accuracy")
def categorical_accuracy(y_true, y_pred):
    y_true = ops.argmax(y_true, axis=-1)

    reshape_matches = False
    y_pred = ops.convert_to_tensor(y_pred)
    y_true = ops.convert_to_tensor(y_true, dtype=y_true.dtype)

    y_true_org_shape = ops.shape(y_true)
    y_pred_rank = len(y_pred.shape)
    y_true_rank = len(y_true.shape)

    # If the shape of y_true is (num_samples, 1), squeeze to (num_samples,)
    if (
        (y_true_rank is not None)
        and (y_pred_rank is not None)
        and (len(y_true.shape) == len(y_pred.shape))
    ):
        y_true = ops.squeeze(y_true, -1)
        reshape_matches = True
    y_pred = ops.argmax(y_pred, axis=-1)

    # If the predicted output and actual output types don't match, force cast
    # them to match.
    if y_pred.dtype != y_true.dtype:
        y_pred = ops.cast(y_pred, dtype=y_true.dtype)
    matches = ops.cast(ops.equal(y_true, y_pred), backend.floatx())
    if reshape_matches:
        matches = ops.reshape(matches, y_true_org_shape)
    return matches


@keras_export("keras.metrics.CharacterAccuracy")
class CharacterAccuracy(reduction_metrics.MeanMetricWrapper):
    def __init__(self, name="categorical_accuracy", dtype=None):
        super().__init__(fn=categorical_accuracy, name=name, dtype=dtype)
        # Metric should be maximized during optimization.
        self._direction = "up"

    def get_config(self):
        return {"name": self.name, "dtype": self.dtype}