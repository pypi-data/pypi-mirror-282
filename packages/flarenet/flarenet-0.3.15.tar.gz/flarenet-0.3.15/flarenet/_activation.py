import flarejax as fj
from jaxtyping import Array, Float, jaxtyped

import jax.nn as jnn

__all__ = [
    "ELU",
    "GLU",
    "HardSigmoid",
    "HardSiLU",
    "HardTanh",
    "LeakyReLU",
    "LogSigmoid",
    "LogSoftmax",
    "LogSumExp",
    "OneHot",
    "ReLU",
    "ReLU6",
    "SeLU",
    "Sigmoid",
    "SiLU",
    "Softmax",
    "SoftPlus",
    "SoftSign",
    "SparsePlus",
    "SquarePlus",
    "Standardize",
]


class ELU(fj.Module):
    __module_name = "flarenet.ELU"

    @fj.typecheck
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.elu(x)


class GELU(fj.Module):
    __module_name = "flarenet.GELU"

    @fj.typecheck
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.gelu(x)


class GLU(fj.Module):
    __module_name = "flarenet.GLU"

    axis: int = fj.field(default=-1, static=True)

    @fj.typecheck
    def __call__(self, x: Float[Array, "..."]) -> Float[Array, "..."]:
        return jnn.glu(x, self.axis)


class HardSigmoid(fj.Module):
    __module_name = "flarenet.HardSigmoid"

    @fj.typecheck
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.hard_sigmoid(x)


class HardSiLU(fj.Module):
    __module_name = "flarenet.HardSiLU"

    @fj.typecheck
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.hard_silu(x)


class HardTanh(fj.Module):
    __module_name = "flarenet.HardTanh"

    @fj.typecheck
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.hard_tanh(x)


class LeakyReLU(fj.Module):
    __module_name = "flarenet.LeakyReLU"

    negative_slope: float = fj.field(default=0.01, static=True)

    @fj.typecheck
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.leaky_relu(x, self.negative_slope)


class LogSigmoid(fj.Module):
    __module_name = "flarenet.LogSigmoid"

    @fj.typecheck
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.log_sigmoid(x)


class LogSoftmax(fj.Module):
    __module_name = "flarenet.LogSoftmax"

    @fj.typecheck
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.log_softmax(x, axis=-1)


class LogSumExp(fj.Module):
    __module_name = "flarenet.LogSumExp"

    @fj.typecheck
    def __call__(self, x: Float[Array, "..."]) -> Float[Array, "..."]:
        return jnn.logsumexp(x, axis=-1)


class Standardize(fj.Module):
    __module_name = "flarenet.Standardize"

    axis: int = fj.field(default=-1, static=True)

    @fj.typecheck
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.standardize(x, axis=self.axis)


class OneHot(fj.Module):
    __module_name = "flarenet.OneHot"

    num_classes: int = fj.field(static=True)
    axis: int = fj.field(default=-1, static=True)

    @fj.typecheck
    def __call__(
        self,
        x: Float[Array, "*b"],
    ) -> Float[Array, "*b {self.dim}"]:
        return jnn.one_hot(x, self.num_classes, axis=self.axis)


class ReLU(fj.Module):
    __module_name = "flarenet.ReLU"

    @fj.typecheck
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.relu(x)


class ReLU6(fj.Module):
    __module_name = "flarenet.ReLU6"

    @fj.typecheck
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.relu6(x)


class SeLU(fj.Module):
    __module_name = "flarenet.SeLU"

    @fj.typecheck
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.selu(x)


class Sigmoid(fj.Module):
    __module_name = "flarenet.Sigmoid"

    @fj.typecheck
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.sigmoid(x)


class SoftSign(fj.Module):
    __module_name = "flarenet.SoftSign"

    @fj.typecheck
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.soft_sign(x)


class Softmax(fj.Module):
    __module_name = "flarenet.Softmax"

    axis: int = fj.field(default=-1, static=True)

    @fj.typecheck
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.softmax(x, axis=self.axis)


class SoftPlus(fj.Module):
    __module_name = "flarenet.SoftPlus"

    @fj.typecheck
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.softplus(x)


class SparsePlus(fj.Module):
    __module_name = "flarenet.SparsePlus"

    @fj.typecheck
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.sparse_plus(x)


class SiLU(fj.Module):
    __module_name = "flarenet.SiLU"

    @fj.typecheck
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.silu(x)


class SquarePlus(fj.Module):
    __module_name = "flarenet.SquarePlus"

    @fj.typecheck
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        return jnn.squareplus(x)


class SquareReLU(fj.Module):
    __module_name = "flarenet.SquareReLU"

    @fj.typecheck
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        x = jnn.relu(x)
        return x * x


class Softcap(fj.Module):
    __module_name = "flarenet.Softcap"

    cap: float = fj.field(static=True)

    @jaxtyped(typechecker=fj.typecheck)
    def __call__(self, x: Float[Array, "*s"]) -> Float[Array, "*s"]:
        x = x / self.cap
        x = jnn.tanh(x)
        x = x * self.cap
        return x
