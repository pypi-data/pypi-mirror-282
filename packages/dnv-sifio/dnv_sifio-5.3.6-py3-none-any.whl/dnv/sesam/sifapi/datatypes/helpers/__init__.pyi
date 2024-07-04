from typing import overload
import typing

import DNV.Sesam.SifApi.DataTypes.Helpers
import System


class SifMaterialHelpers(System.Object):
    """This class has no documentation."""

    def ComputeGamma(self, ql: typing.List[float]) -> float:
        ...

    def ComputeGammaElas86(self, ql: typing.List[float]) -> float:
        ...

    def ComputeNormalStressTransformation(self, angle: float) -> typing.List[float]:
        ...

    def ComputeShearStressTransformation(self, angle: float) -> typing.List[float]:
        ...

    def ComputeShearStressTransformationRearranged(self, angle: float) -> typing.List[float]:
        ...

    @overload
    def ComputeTheBlockDiagonalStressTransformation(self, angle: float) -> typing.List[float]:
        ...

    @overload
    def ComputeTheBlockDiagonalStressTransformation(self, a: typing.List[float], aShear: typing.List[float]) -> typing.List[float]:
        ...


