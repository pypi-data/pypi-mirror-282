import abc
import typing
import warnings
from typing import overload

import System
import System.Collections
import System.Collections.Generic
import System.IO

import DNV.Sesam.SifApi.Core

DNV_Sesam_SifApi_Core_ComparableIndex = typing.Any
DNV_Sesam_SifApi_Core_ComparablePair = typing.Any
DNV_Sesam_SifApi_Core_ComparableTriplet = typing.Any
DNV_Sesam_SifApi_Core_ISifIndex = typing.Any

DNV_Sesam_SifApi_Core_CachedKeyValueSortedDictionary_TKey = typing.TypeVar("DNV_Sesam_SifApi_Core_CachedKeyValueSortedDictionary_TKey")
DNV_Sesam_SifApi_Core_CachedKeyValueSortedDictionary_TValue = typing.TypeVar("DNV_Sesam_SifApi_Core_CachedKeyValueSortedDictionary_TValue")
DNV_Sesam_SifApi_Core_CachedKeyValueSortedDictionary_CheckThatEqualsWork_T = typing.TypeVar("DNV_Sesam_SifApi_Core_CachedKeyValueSortedDictionary_CheckThatEqualsWork_T")
DNV_Sesam_SifApi_Core_ComparableIndex_T = typing.TypeVar("DNV_Sesam_SifApi_Core_ComparableIndex_T")
DNV_Sesam_SifApi_Core_ComparablePair_T = typing.TypeVar("DNV_Sesam_SifApi_Core_ComparablePair_T")
DNV_Sesam_SifApi_Core_ComparableTriplet_T = typing.TypeVar("DNV_Sesam_SifApi_Core_ComparableTriplet_T")
DNV_Sesam_SifApi_Core_ConcurrentPool_T = typing.TypeVar("DNV_Sesam_SifApi_Core_ConcurrentPool_T")
DNV_Sesam_SifApi_Core_CoreDefinitions_GetString_T = typing.TypeVar("DNV_Sesam_SifApi_Core_CoreDefinitions_GetString_T")
DNV_Sesam_SifApi_Core_IBackingStorageDictionary_TValue = typing.TypeVar("DNV_Sesam_SifApi_Core_IBackingStorageDictionary_TValue")
DNV_Sesam_SifApi_Core_IDataTypeTableLookUp_T = typing.TypeVar("DNV_Sesam_SifApi_Core_IDataTypeTableLookUp_T")
DNV_Sesam_SifApi_Core_ITableOfContents_T = typing.TypeVar("DNV_Sesam_SifApi_Core_ITableOfContents_T")
DNV_Sesam_SifApi_Core_Pair_T = typing.TypeVar("DNV_Sesam_SifApi_Core_Pair_T")
DNV_Sesam_SifApi_Core_Pair_TU = typing.TypeVar("DNV_Sesam_SifApi_Core_Pair_TU")
DNV_Sesam_SifApi_Core_Pair_TV = typing.TypeVar("DNV_Sesam_SifApi_Core_Pair_TV")
DNV_Sesam_SifApi_Core_PairList_T = typing.TypeVar("DNV_Sesam_SifApi_Core_PairList_T")
DNV_Sesam_SifApi_Core_SetInsertionOrder_T = typing.TypeVar("DNV_Sesam_SifApi_Core_SetInsertionOrder_T")


class BucketFileOneSizes(System.Object):
    """This class has no documentation."""

    SizeIndicesInt: int = 4

    SizeIndicesPair: int = 8

    SizeIndicesTriple: int = 12

    SizeBucketInt: int = ...

    SizeBucketPair: int = ...

    SizeBucketTriple: int = ...


class CachedKeyValueSortedDictionary(typing.Generic[DNV_Sesam_SifApi_Core_CachedKeyValueSortedDictionary_TKey, DNV_Sesam_SifApi_Core_CachedKeyValueSortedDictionary_TValue], System.Collections.Generic.SortedDictionary[DNV_Sesam_SifApi_Core_CachedKeyValueSortedDictionary_TKey, DNV_Sesam_SifApi_Core_CachedKeyValueSortedDictionary_TValue]):
    """This class has no documentation."""

    def Add(self, key: DNV_Sesam_SifApi_Core_CachedKeyValueSortedDictionary_TKey, value: DNV_Sesam_SifApi_Core_CachedKeyValueSortedDictionary_TValue) -> None:
        ...

    @staticmethod
    def CheckThatEqualsWork(a: DNV_Sesam_SifApi_Core_CachedKeyValueSortedDictionary_CheckThatEqualsWork_T, b: DNV_Sesam_SifApi_Core_CachedKeyValueSortedDictionary_CheckThatEqualsWork_T) -> bool:
        ...

    def TryGetValue(self, key: DNV_Sesam_SifApi_Core_CachedKeyValueSortedDictionary_TKey, value: typing.Optional[DNV_Sesam_SifApi_Core_CachedKeyValueSortedDictionary_TValue]) -> typing.Union[bool, DNV_Sesam_SifApi_Core_CachedKeyValueSortedDictionary_TValue]:
        ...


class ICompareIndex(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def Equal(self, idx: DNV.Sesam.SifApi.Core.ICompareIndex) -> bool:
        ...

    def GreaterThan(self, idx: DNV.Sesam.SifApi.Core.ICompareIndex) -> bool:
        ...

    def GreaterThanOrEqual(self, idx: DNV.Sesam.SifApi.Core.ICompareIndex) -> bool:
        ...

    def LessThan(self, idx: DNV.Sesam.SifApi.Core.ICompareIndex) -> bool:
        ...

    def LessThanOrEqual(self, idx: DNV.Sesam.SifApi.Core.ICompareIndex) -> bool:
        ...

    def NotEqual(self, idx: DNV.Sesam.SifApi.Core.ICompareIndex) -> bool:
        ...


class ComparableIndex(typing.Generic[DNV_Sesam_SifApi_Core_ComparableIndex_T], System.IComparable[DNV_Sesam_SifApi_Core_ComparableIndex], DNV.Sesam.SifApi.Core.ICompareIndex):
    """This class has no documentation."""

    @property
    def X(self) -> DNV_Sesam_SifApi_Core_ComparableIndex_T:
        ...

    def __init__(self, x: DNV_Sesam_SifApi_Core_ComparableIndex_T) -> None:
        ...

    @overload
    def CompareTo(self, obj: typing.Any) -> int:
        ...

    @overload
    def CompareTo(self, other: DNV.Sesam.SifApi.Core.ComparableIndex[DNV_Sesam_SifApi_Core_ComparableIndex_T]) -> int:
        ...

    @overload
    def CompareTo(self, other: DNV.Sesam.SifApi.Core.ComparableIndex[DNV_Sesam_SifApi_Core_ComparableIndex_T]) -> int:
        ...

    def Equal(self, idx: DNV.Sesam.SifApi.Core.ICompareIndex) -> bool:
        ...

    def Equals(self, obj: typing.Any) -> bool:
        ...

    def GetHashCode(self) -> int:
        ...

    def GreaterThan(self, idx: DNV.Sesam.SifApi.Core.ICompareIndex) -> bool:
        ...

    def GreaterThanOrEqual(self, idx: DNV.Sesam.SifApi.Core.ICompareIndex) -> bool:
        ...

    def LessThan(self, idx: DNV.Sesam.SifApi.Core.ICompareIndex) -> bool:
        ...

    def LessThanOrEqual(self, idx: DNV.Sesam.SifApi.Core.ICompareIndex) -> bool:
        ...

    def NotEqual(self, idx: DNV.Sesam.SifApi.Core.ICompareIndex) -> bool:
        ...


class ComparablePair(typing.Generic[DNV_Sesam_SifApi_Core_ComparablePair_T], System.IComparable[DNV_Sesam_SifApi_Core_ComparablePair], DNV.Sesam.SifApi.Core.ICompareIndex):
    """A generic pair that implements IComparable."""

    @property
    def X(self) -> DNV_Sesam_SifApi_Core_ComparablePair_T:
        ...

    @property
    def Y(self) -> DNV_Sesam_SifApi_Core_ComparablePair_T:
        """Gets or sets the y."""
        ...

    def __init__(self, x: DNV_Sesam_SifApi_Core_ComparablePair_T, y: DNV_Sesam_SifApi_Core_ComparablePair_T) -> None:
        ...

    @overload
    def CompareTo(self, obj: typing.Any) -> int:
        ...

    @overload
    def CompareTo(self, other: DNV.Sesam.SifApi.Core.ComparablePair[DNV_Sesam_SifApi_Core_ComparablePair_T]) -> int:
        """
        The compare to.
        
        :param other: The other.
        :returns: The int.
        """
        ...

    @overload
    def CompareTo(self, other: DNV.Sesam.SifApi.Core.ComparablePair[DNV_Sesam_SifApi_Core_ComparablePair_T]) -> int:
        ...

    def Equal(self, idx: DNV.Sesam.SifApi.Core.ICompareIndex) -> bool:
        ...

    def Equals(self, obj: typing.Any) -> bool:
        ...

    def GetHashCode(self) -> int:
        ...

    def GreaterThan(self, idx: DNV.Sesam.SifApi.Core.ICompareIndex) -> bool:
        ...

    def GreaterThanOrEqual(self, idx: DNV.Sesam.SifApi.Core.ICompareIndex) -> bool:
        ...

    def LessThan(self, idx: DNV.Sesam.SifApi.Core.ICompareIndex) -> bool:
        ...

    def LessThanOrEqual(self, idx: DNV.Sesam.SifApi.Core.ICompareIndex) -> bool:
        ...

    def NotEqual(self, idx: DNV.Sesam.SifApi.Core.ICompareIndex) -> bool:
        ...


class ComparableTriplet(typing.Generic[DNV_Sesam_SifApi_Core_ComparableTriplet_T], System.IComparable[DNV_Sesam_SifApi_Core_ComparableTriplet], DNV.Sesam.SifApi.Core.ICompareIndex):
    """This class has no documentation."""

    @property
    def PairYZ(self) -> DNV.Sesam.SifApi.Core.ComparablePair[DNV_Sesam_SifApi_Core_ComparableTriplet_T]:
        ...

    @property
    def X(self) -> DNV_Sesam_SifApi_Core_ComparableTriplet_T:
        ...

    @property
    def Y(self) -> DNV_Sesam_SifApi_Core_ComparableTriplet_T:
        ...

    @property
    def Z(self) -> DNV_Sesam_SifApi_Core_ComparableTriplet_T:
        ...

    def __init__(self, x: DNV_Sesam_SifApi_Core_ComparableTriplet_T, y: DNV_Sesam_SifApi_Core_ComparableTriplet_T, z: DNV_Sesam_SifApi_Core_ComparableTriplet_T) -> None:
        ...

    @overload
    def CompareTo(self, obj: typing.Any) -> int:
        ...

    @overload
    def CompareTo(self, other: DNV.Sesam.SifApi.Core.ComparableTriplet[DNV_Sesam_SifApi_Core_ComparableTriplet_T]) -> int:
        ...

    @overload
    def CompareTo(self, other: DNV.Sesam.SifApi.Core.ComparableTriplet[DNV_Sesam_SifApi_Core_ComparableTriplet_T]) -> int:
        ...

    def Equal(self, idx: DNV.Sesam.SifApi.Core.ICompareIndex) -> bool:
        ...

    def Equals(self, obj: typing.Any) -> bool:
        ...

    def GetHashCode(self) -> int:
        ...

    def GreaterThan(self, idx: DNV.Sesam.SifApi.Core.ICompareIndex) -> bool:
        ...

    def GreaterThanOrEqual(self, idx: DNV.Sesam.SifApi.Core.ICompareIndex) -> bool:
        ...

    def LessThan(self, idx: DNV.Sesam.SifApi.Core.ICompareIndex) -> bool:
        ...

    def LessThanOrEqual(self, idx: DNV.Sesam.SifApi.Core.ICompareIndex) -> bool:
        ...

    def NotEqual(self, idx: DNV.Sesam.SifApi.Core.ICompareIndex) -> bool:
        ...

    def ToString(self) -> str:
        ...


class ConcurrentPool(typing.Generic[DNV_Sesam_SifApi_Core_ConcurrentPool_T], System.Object):
    """Object pool"""

    def __init__(self, factoryMethod: typing.Callable[[], DNV_Sesam_SifApi_Core_ConcurrentPool_T]) -> None:
        """
        Creates a new pool.
        
        :param factoryMethod: The factory method.
        """
        ...

    def CheckIn(self, instance: DNV_Sesam_SifApi_Core_ConcurrentPool_T) -> None:
        """
        Check in the specified instance.
        
        :param instance: The instance.
        """
        ...

    def CheckOut(self) -> DNV_Sesam_SifApi_Core_ConcurrentPool_T:
        """
        Check out a new instance.
        
        :returns: Instance of T.
        """
        ...


class IControlInterlock(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def SetInterlockFalse(self) -> None:
        ...

    def SetInterlockTrue(self) -> bool:
        ...


class ControlInterlock(System.Object, DNV.Sesam.SifApi.Core.IControlInterlock):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    def SetInterlockFalse(self) -> None:
        ...

    def SetInterlockTrue(self) -> bool:
        ...


class Constants(System.Object):
    """The constants."""

    Megabyte: int = ...

    Mebibyte: int = ...

    UserDataSifDef: str = "UserData.sifdef"

    BeginDataTypes: str = "BEG:DATATYPES"

    EndDataTypes: str = "END:DATATYPES"

    CommentDataTypes: str = "#"

    NotALegalIndex: int = ...

    NoMoreDataSets: int = ...

    NoMorePositions: int = ...

    AddressNotFound: int = ...

    ZeroAddress: int = ...

    Zero: int = 0

    Count: int = 1
    """The count."""

    FourCount: int = 4
    """The 4 count."""

    Long0008: int = ...
    """The long 0008."""

    Int2051: int = 2051
    """PTAB fortran compatibility number."""

    Int0008: int = 8
    """The int 0008. To avoid cast."""

    LongFive: int = ...
    """The long five."""

    LongFour: int = ...
    """The long four."""

    LongTwo: int = ...
    """The long two."""

    LongOne: int = ...
    """The long one."""

    NameIend: str = "IEND    "
    """The end of header name tag."""

    NameAllocate: str = "ALLOCATE"
    """The start of allocate name tag."""

    NameFileName: str = "FILENAME"
    """The start of filename name tag."""

    NameExtend: str = "EXTEND  "
    """The start of norsam name tag."""

    NameIext: str = "IEXT    "
    """The start of norsam name tag."""

    NameNorsam: str = "NORSAM  "
    """The start of norsam name tag."""

    NamePtab: str = "PTAB    "
    """The pointer table name tag."""

    NameResults: str = "RESULTS "
    """The name results."""

    NameScratch: str = "SCRATCH "
    """The name scratch."""

    Offset: int = 0

    NSPI: int = 2


class Point:
    """
    A light weight point definition.
    Implementations of algorithms using "Point : Point" is found in "PointAlgorithms".
    "PointAlgorithms" is part of "DNV.Sesam.SifApi.Core".
    """

    @property
    def Id(self) -> int:
        ...

    @Id.setter
    def Id(self, value: int):
        ...

    @property
    def X(self) -> float:
        ...

    @property
    def Y(self) -> float:
        ...

    @property
    def Z(self) -> float:
        ...

    @property
    def Xyz(self) -> typing.List[float]:
        ...

    @overload
    def __init__(self, x: float, y: float, z: float = ...) -> None:
        ...

    @overload
    def __init__(self, id: int, x: float, y: float, z: float = ...) -> None:
        ...

    @overload
    def __init__(self, id: int, xyz: typing.List[float]) -> None:
        ...

    @overload
    def UpdatePoint(self, id: int, x: float, y: float, z: float = ...) -> None:
        ...

    @overload
    def UpdatePoint(self, x: float, y: float, z: float = ...) -> None:
        ...


class CoreDefinitions(System.Object):
    """This class has no documentation."""

    class SesamFiniteElementType(System.Enum):
        """This class has no documentation."""

        NoElementType = -1

        BEPS = 2

        CSTA = 3

        ILST = 6

        IQQE = 8

        LQUA = 9

        TESS = 10

        GMAS = 11

        GLMA = 12

        GLDA = 13

        BEAS = 15

        AXIS = 16

        AXDA = 17

        GSPR = 18

        GDAM = 19

        IHEX = 20

        LHEX = 21

        SECB = 22

        BTSS = 23

        FQUS = 24

        FTRS = 25

        SCTS = 26

        MCTS = 27

        SCQS = 28

        MCQS = 29

        IPRI = 30

        ITET = 31

        TPRI = 32

        TETR = 33

        LCTS = 34

        LCQS = 35

        TRSI18 = 36

        TRSI15 = 37

        TRSI12 = 38

        GLSH = 40

        AXCS = 41

        AXLQ = 42

        AXLS = 43

        AXQQ = 44

        CTCP = 51

        CTCL = 52

        CTAL = 53

        CTCC = 54

        CTAQ = 55

        CTLQ = 56

        CTCQ = 57

        CTMQ = 58

        FTAS = 59

        FQAS = 60

        HCQS = 61

        THTS = 63

        THQS = 64

        MATR = 70

        GHEX = 100

    class BoundaryConditionCodes(System.Enum):
        """This class has no documentation."""

        FreeToStay = 0
        """free to stay."""

        FixedAtZero = 1
        """fixed at zero displacement, temperature, etc."""

        Prescribed = 2
        """prescribed displacement, temperature, velocity, acceleration, etc. different from zero."""

        LinearlyDependent = 3
        """linearly dependent."""

        RetainedDegree = 4
        """retained degree of freedom, i.e. at a supernode."""

    class NodeComponents(System.Enum):
        """This class has no documentation."""

        X = 1

        Y = 1

        Z = 2

        Rx = 3

        Ry = 4

        Rz = 5

    class NodeResultType(System.Enum):
        """This class has no documentation."""

        Acceleration = 0

        Displacement = 1

        Velocity = 2

        ModalLoadFactor = 3

    class ElementResultType(System.Enum):
        """This class has no documentation."""

        Stress = 0

        Force = 1

    class RdstressCompRef(System.Enum):
        """Components referenced on data type RDSTRESS (and PDSTRESS)"""

        Sigxx = 1
        """Normal stress x-direction"""

        Sigyy = 1
        """Normal stress y-direction"""

        Sigzz = 2
        """Normal stress z-direction"""

        Tauxy = 3
        """Shear stress in y-direction, yz-plane"""

        Tauxz = 4
        """Shear stress in z-direction, yz-plane"""

        Tauyz = 5
        """Shear stress in z-direction, xz-plane"""

        Sigmx = 6
        """Membrane stress x-direction"""

        Sigmy = 7
        """Membrane stress y-direction"""

        Sigbyx = 8
        """Normal bending stress, yz-plane, around y"""

        Sigbzx = 9
        """Normal bending stress, yz-plane, around z"""

        Sigbxy = 10
        """Normal bending stress, xz-plane, around x"""

        Sigbzy = 11
        """Normal bending stress, xz-plane, around z"""

        Sigbxz = 12
        """Normal bending stress, xy-plane, around x"""

        Sigbyz = 13
        """Normal bending stress, xy-plane, around y"""

        Taubxy = 14
        """Shear bending stress, yz-plane, y-direction"""

        Taubxz = 15
        """Shear bending stress, yz-plane, z-direction"""

        Taubyx = 16
        """Shear bending stress, xz-plane, x-direction"""

        Taubyz = 17
        """Shear bending stress, xz-plane, z-direction"""

        Taubzx = 18
        """Shear bending stress, xy-plane, x-direction"""

        Taubzy = 19
        """Shear bending stress, xy-plane, y-direction"""

        Tautxy = 20
        """Torsional shear, yz-plane, y-direction"""

        Tautxz = 21
        """Torsional shear, yz-plane, z-direction"""

        Tautzy = 22
        """Torsional shear, xy-plane, y-direction"""

        Sigrr = 23
        """Normal stress radial direction"""

        Taurz = 24
        """Shear stress for axis-symmetry"""

        Hoop = 25
        """Hoop stress for axis-symmetry"""

        PSig1 = 26
        """First principal stress component"""

        PSig2 = 27
        """Second principal stress component"""

        PSig3 = 28
        """Third principal stress component"""

        SigEff = 29
        """Equivalent effective stress component"""

    class RdforcesCompRef(System.Enum):
        """Components referenced on data type RDFORCES"""

        Nxx = 1
        """Normal force x-direction, yz-plane"""

        Nxy = 1
        """Shear force y-direction, yz-plane"""

        Nxz = 2
        """Shear force z-direction, yz-plane"""

        Nyx = 3
        """Shear force x-direction, xz-plane"""

        Nyy = 4
        """Normal force y-direction, xz-plane"""

        Nyz = 5
        """Shear force z-direction, xz-plane"""

        Nzx = 6
        """Shear force x-direction, xy-plane"""

        Nzy = 7
        """Shear force y-direction, xy-plane"""

        Nzz = 8
        """Normal force z-direction, xy-plane"""

        Mxx = 9
        """Torsion moment around x-axis, yz-plane"""

        Mxy = 10
        """Bending moment around y-axis, yz-plane"""

        Mxz = 11
        """Bending moment around z-axis, yz-plane"""

        Myx = 12
        """Bending moment around x-axis, xz-plane"""

        Myy = 13
        """Torsion moment around y-axis, xz-plane"""

        Myz = 14
        """Bending moment around z-axis, xz-plane"""

        Mzx = 15
        """Bending moment around x-axis, xy-plane"""

        Mzy = 16
        """Bending moment around y-axis, xy-plane"""

        Mzz = 17
        """Torsion moment around z-axis, xy-plane"""

    class RdelnforCompRef(System.Enum):
        """Components referenced on data type RDELNFOR"""

        Px = 1
        """Force in x-direction"""

        Py = 2
        """Force in y-direction"""

        Pz = 3
        """Force in z-direction"""

        Mx = 4
        """Moment about x-axis"""

        My = 5
        """Moment about y-axis"""

        Mz = 6
        """Moment about z-axis"""

    class RdstrainCompRef(System.Enum):
        """Components referenced on data type RDSTRAIN"""

        Epsxx = 1
        """Normal strain x-direction"""

        Epsyy = 1
        """Normal strain y-direction"""

        Epszz = 2
        """Normal strain z-direction"""

        Gamxy = 3
        """Shear strain in y-direction, yz-plane"""

        Gamxz = 4
        """Shear strain in z-direction, yz-plane"""

        Gamyz = 5
        """Shear strain in z-direction, xz-plane"""

        Epsmx = 6
        """Membrane strain x-direction"""

        Epsmy = 7
        """Membrane strain y-direction"""

        Epsbyx = 8
        """Normal bending strain, yz-plane, around y"""

        Epsbzx = 9
        """Normal bending strain, yz-plane, around z"""

        Epsbxy = 10
        """Normal bending strain, xz-plane, around x"""

        Epsbzy = 11
        """Normal bending strain, xz-plane, around z"""

        Epsbxz = 12
        """Normal bending strain, xy-plane, around x"""

        Epsbyz = 13
        """Normal bending strain, xy-plane, around y"""

        Gambxy = 14
        """Shear bending strain, yz-plane, y-direction"""

        Gambxz = 15
        """Shear bending strain, yz-plane, z-direction"""

        Gambyx = 16
        """Shear bending strain, xz-plane, x-direction"""

        Gambyz = 17
        """Shear bending strain, xz-plane, z-direction"""

        Gambzx = 18
        """Shear bending strain, xy-plane, x-direction"""

        Gambzy = 19
        """Shear bending strain, xy-plane, y-direction"""

        Gamtxy = 20
        """Torsional shear, yz-plane, y-direction"""

        Gamtxz = 21
        """Torsional shear, yz-plane, z-direction"""

        Gamtzy = 22
        """Torsional shear, xy-plane, y-direction"""

        Epsrr = 23
        """Normal strain radial direction"""

        Gamrz = 24
        """Shear strain for axis-symmetry"""

        Hoop = 25
        """Hoop strain for axis-symmetry"""

    class FatiguePropertyNames(System.Object):
        """This class has no documentation."""

        Component: str = "Component = "

        # Cannot convert to Python: None: str = "None"

        CHORD_SIDE: str = "CHORD-SIDE"

        BRACE_SIDE: str = "BRACE-SIDE"

        BOTH_SIDES: str = "BOTH-SIDES"

        SECTION: str = "SECTION"

        ASSIGNED: str = "ASSIGNED"

    class CardType(System.Enum):
        """This class has no documentation."""

        BASICTEXTCARD = 0

        TDTEXTCARD = 1

        CARD = 2

    class SifFileType(System.Enum):
        """This class has no documentation."""

        SifType = 0

        SiuType = 1

        SifOrSiuType = 2

        SinType = 3

    class SinDataIndexType(System.Enum):
        """This class has no documentation."""

        UnknownIndex = -3

        IndexMustBeDefined = -2

        NoIndexTypeDefined = -1

        NoReference = 0

        OneDimensional = 1

        TwoDimensional = 2

        ThreeDimensional = 3

        IIFNoReference = 20

        IIFOneReference1DataField = 21

        IIFTwoReference12DataField = 22

        IIFOneReference2DataField = 31

        IIFNoReferenceDateText = 40

        RIFOneReference = 41

        RIFTwoReference = 42

        IIFOneReference1ManyWithTheSameReference = 51

        IIFTwoReference15ManyWithTheSameReference = 52

    class EngineeringAdaptions(System.Enum):
        """This class has no documentation."""

        # Cannot convert to Python: None = 0

        All = 1

    class ReadMethod(System.Enum):
        """Methods available for reading Sin files. Introduced in "DNV.Sesam.Sif.ResultInterpreter"."""

        Standard = 0

        FlatIron = 1

        FlatFile = 2

    class SesamCoreContext(System.Enum):
        """Sif.Api is used from Sesam or from Sesam Core."""

        Sesam = 0

        SesamCore = 1

    class SesamCoreMethodOption(System.Enum):
        """This class has no documentation."""

        First = 0

        Second = 1

    class SesamFatigueHotSpotExtrapolationType(System.Enum):
        """This class has no documentation."""

        Linear = 0

        SteepStressGradients = 1

    class SesamFatigueHotSpotInterpolationType(System.Enum):
        """This class has no documentation."""

        Averaged = 0

        Linear = 1

    class SesamFatigueHotSpotEffectiveStressMethod(System.Enum):
        """
        Whether proportional, or non-proportional loading is assumed.
        "HotSpotPlate" is defined in section "4.3.4.1 Typical plated structures" of RP-C203, Edition September 2019, Amended September 2021.
        "HotSpotPlateMultiDir" is defined in section "F.12 Comm. 4.3.4 Multidirectional fatigue analysis" of RP-C203, Edition September 2019, Amended September 2021.
        """

        HotSpotPlate = 0

        HotSpotPlateMultiDir = 1

    class SesamFatigueHotSpotType(System.Enum):
        """Hot spot action. Whether bending action (bending + membrane) or only membrane action should be considered when stresses are computed for a hot spot."""

        Bending = 0

        Membrane = 1

    class SesamFatigueHotSpotEffectiveStressMethodS4341(System.Enum):
        """Whether to use method A or method B as defined in section "4.3.4.1 Typical plated structures" of RP-C203, Edition September 2019, Amended September 2021."""

        A = 0

        B = 1

    class SesamFatigueHotSpotPatchType(System.Enum):
        """Which type of hot spot patch that is assumed. 1 x 2, 2 x 2, 1 x 3 or 2 x 3."""

        Standard1x2 = 0

        Standard2x2 = 1

        Standard1x3 = 2

        Standard2x3 = 3

        Automatic = 4

    class SesamFatigueCheckPointType(System.Enum):
        """Sesam fatigue check point type."""

        HotSpotCheck = 0

        ElementCheck = 1

        JointCheck = 2

    class SesamFatigueHotSpotPlateMultiDirEquivalentStressMethod(System.Enum):
        """The crack mode assumed when the damage is computed."""

        PlateMultiDir = 0

        BasicShear = 1

        Both = 2

    class SesamFatigueHotSpotRpc203AlphaMethod(System.Enum):
        """Detail category for "HotSpotPlate" as defined in Table A-3 of RP-C203, Edition September 2019, Amended September 2021."""

        C = 0

        C1 = 1

        C2 = 2

        UserDefined = 3

    class SesamFatigueAngleUnit(System.Enum):
        """Whether an angle is in unit degrees or radians."""

        Deg = 0

        Rad = 1

    class SesamFatigueElementCheck(System.Enum):
        """This class has no documentation."""

        ElementStressPoints = 0

        ElementSurfaces = 1

        ElementCorners = 2

        CentreStressPoints = 3

        CentreSurfacePoints = 4

        ElementMiddlePlane = 5

        ElementMembrane = 6

        CentroidElement = 7

        CentroidMembrane = 8

        CentreAndLine = 9

    class SesamFiniteElementTypeDimension(System.Enum):
        """This class has no documentation."""

        NoDimension = -1

        Point = 0

        Dim1Db = 1

        Dim1Dm = 11

        Dim2Ds = 2

        Dim2Dm = 21

        Dim3D = 3

    class Area(System.Enum):
        """This class has no documentation."""

        Centre = 0

        Corner = 1

        Points = 2

    class ElementLine(System.Enum):
        """Line definitions are unique for each Sesam Finite Element type, consult the "Sesam_Input_Interface_Format.pdf" manual."""

        NotDefined = -1

        Line1 = 1

        Line2 = 2

        Line3 = 3

        Line4 = 4

        Line5 = 5

        Line6 = 6

        OnlyElementCornerNodeIsConnectedToEdge = 7

        InternalEdgeWhichIsDiscarded = 8

        EdgeIsNotInThisElement = 9

    class ElementSide(System.Enum):
        """Side definitions are unique for each Sesam Finite Element type, consult the "Sesam_Input_Interface_Format.pdf" manual."""

        NotDefined = -1

        Both = 1

        BothSurface = 2

        LowerPoint = 3

        LowerSurface = 4

        Middle = 5

        UpperPoint = 6

        UpperSurface = 7

    class SesamFatigueCheckPointSide(System.Enum):
        """This class has no documentation."""

        NotDefined = -1

        BothSide = 1

        NegativeZSide = 2

        MiddleSide = 3

        PositiveZSide = 4

        NotSetSide = 5

    class Method(System.Enum):
        """This class has no documentation."""

        Extrapolate = 0

        Interpolate = 1

        ResultPoint = 2

        NotNeeded = 3

    class Action(System.Enum):
        """This class has no documentation."""

        NoAction = 0

        Axial = 1

        Bending = 2

        Membrane = 3

        Shell = 4

        Solid = 5

    class StressState(System.Enum):
        """This class has no documentation."""

        PlaneStressState = 0

        ThickShellStressState = 1

        SolidStressState = 2

    n75: int = 75

    n130: int = 130

    NAMEFORMAT16: str = "FORMAT16"

    NAMEFORMAT24: str = "FORMAT24"

    NAMESINEXT: str = ".SIN"

    NotInitializedSifIndex: int = -1

    NAMEBLANK: str = "        "

    NAMEBNDOFTOP: str = "BNDOFTOP"

    NAMEBNTRCOSTOP: str = "BNTRCOSTOP"

    NAMEACFD: str = "ACFD    "

    NAMEADDATA: str = "ADDATA  "

    NAMEAMATRIX: str = "AMATRIX "

    NAMEAMDACCL: str = "AMDACCL "

    NAMEAMDDAMP: str = "AMDDAMP "

    NAMEAMDDISP: str = "AMDDISP "

    NAMEAMDFREQ: str = "AMDFREQ "

    NAMEAMDLOAD: str = "AMDLOAD "

    NAMEAMDMASS: str = "AMDMASS "

    NAMEAMDSTIFF: str = "AMDSTIFF"

    NAMEAMDVELO: str = "AMDVELO "

    NAMEAME: str = "AME     "

    NAMEASTR: str = "ASTR    "

    NAMEBAHAMAS: str = "BAHAMAS "

    NAMEBEDRAG1: str = "BEDRAG1 "

    NAMEBEISTE: str = "BEISTE  "

    NAMEBELFIX: str = "BELFIX  "

    NAMEBELLAX: str = "BELLAX  "

    NAMEBELLO2: str = "BELLO2  "

    NAMEBELOAD1: str = "BELOAD1 "

    NAMEBEMASS1: str = "BEMASS1 "

    NAMEBEUSLO: str = "BEUSLO  "

    NAMEBEUVLO: str = "BEUVLO  "

    NAMEBEWAKIN: str = "BEWAKIN "

    NAMEBEWALO1: str = "BEWALO1 "

    NAMEBGRAV: str = "BGRAV   "

    NAMEBLDEP: str = "BLDEP   "

    NAMEBNACCLO: str = "BNACCLO "

    NAMEBNBCD: str = "BNBCD   "

    NAMEBNDISPL: str = "BNDISPL "

    NAMEBNDOF: str = "BNDOF   "

    NAMEBNIEQ: str = "BNIEQ   "

    NAMEBNINCO: str = "BNINCO  "

    NAMEBNLOAD: str = "BNLOAD  "

    NAMEBNLOAX: str = "BNLOAX  "

    NAMEBNMASS: str = "BNMASS  "

    NAMEBNTEMP: str = "BNTEMP  "

    NAMEBNTRCOS: str = "BNTRCOS "

    NAMEBNWALO: str = "BNWALO  "

    NAMEBQDP: str = "BQDP    "

    NAMEBRIGAC: str = "BRIGAC  "

    NAMEBRIGDI: str = "BRIGDI  "

    NAMEBRIGVE: str = "BRIGVE  "

    NAMEBROT: str = "BROT    "

    NAMEBSELL: str = "BSELL   "

    NAMECADATA: str = "CADATA  "

    NAMECPDATA: str = "CPDATA  "

    NAMEDATE: str = "DATE    "

    NAMEGBARM: str = "GBARM   "

    NAMEGBEAMG: str = "GBEAMG  "

    NAMEGBOX: str = "GBOX    "

    NAMEGCHAN: str = "GCHAN   "

    NAMEGCHANR: str = "GCHANR  "

    NAMEGCOORD: str = "GCOORD  "

    NAMEGCROINT: str = "GCROINT "

    NAMEGDOBO: str = "GDOBO   "

    NAMEGECC: str = "GECC    "

    NAMEGECCEN: str = "GECCEN  "

    NAMEGELINT: str = "GELINT  "

    NAMEGELMNT1: str = "GELMNT1 "

    NAMEGELMNT2: str = "GELMNT2 "

    NAMEGELREF1: str = "GELREF1 "

    NAMEGELSTRP: str = "GELSTRP "

    NAMEGELTH: str = "GELTH   "

    NAMEGGELDES: str = "GGELDES "

    NAMEGIORH: str = "GIORH   "

    NAMEGIORHR: str = "GIORHR  "

    NAMEGLMASS: str = "GLMASS  "

    NAMEGLSEC: str = "GLSEC   "

    NAMEGLSECR: str = "GLSECR  "

    NAMEGNODE: str = "GNODE   "

    NAMEGPGBOX: str = "GPGBOX  "

    NAMEGPGDOW: str = "GPGDOW  "

    NAMEGPIPE: str = "GPIPE   "

    NAMEGSEPSPEC: str = "GSEPSPEC"

    NAMEGSETMEMB: str = "GSETMEMB"

    NAMEGSLAYER: str = "GSLAYER "

    NAMEGSLPLATE: str = "GSLPLATE"

    NAMEGSLSOLID: str = "GSLSOLID"

    NAMEGSLSTIFF: str = "GSLSTIFF"

    NAMEGTONP: str = "GTONP   "

    NAMEGUNIVEC: str = "GUNIVEC "

    NAMEGUSYI: str = "GUSYI   "

    NAMEHIERARCH: str = "HIERARCH"

    NAMEHSUPSTAT: str = "HSUPSTAT"

    NAMEHSUPTRAN: str = "HSUPTRAN"

    NAMEIDENT: str = "IDENT   "

    NAMEIEND: str = "IEND    "

    NAMEMAXDMP: str = "MAXDMP  "

    NAMEMAXSPR: str = "MAXSPR  "

    NAMEMCNT: str = "MCNT    "

    NAMEMGDAMP: str = "MGDAMP  "

    NAMEMGLDAMP: str = "MGLDAMP "

    NAMEMGLMASS: str = "MGLMASS "

    NAMEMGMASS: str = "MGMASS  "

    NAMEMGSPRNG: str = "MGSPRNG "

    NAMEMISOAL: str = "MISOAL  "

    NAMEMISOEML: str = "MISOEML "

    NAMEMISOHL: str = "MISOHL  "

    NAMEMISOHNL: str = "MISOHNL "

    NAMEMISOPL: str = "MISOPL  "

    NAMEMISOSEL: str = "MISOSEL "

    NAMEMISTEL: str = "MISTEL  "

    NAMEMORSMEL: str = "MORSMEL "

    NAMEMORSSEL: str = "MORSSEL "

    NAMEMORSSOL: str = "MORSSOL "

    NAMEMSHGLSP: str = "MSHGLSP "

    NAMEMTEMP: str = "MTEMP   "

    NAMEMTENONL: str = "MTENONL "

    NAMEMTRMEL: str = "MTRMEL  "

    NAMEMTRSEL: str = "MTRSEL  "

    NAMEMTRSOL: str = "MTRSOL  "

    NAMEPDFATPRP: str = "PDFATPRP"

    NAMEPDSTRESS: str = "PDSTRESS"

    NAMEPVFATDAM: str = "PVFATDAM"

    NAMEPVSTRESS: str = "PVSTRESS"

    NAMERBLODCMB: str = "RBLODCMB"

    NAMERDELNFOR: str = "RDELNFOR"

    NAMERDFATDMG: str = "RDFATDMG"

    NAMERDFORCES: str = "RDFORCES"

    NAMERDIELCOR: str = "RDIELCOR"

    NAMERDMLFACT: str = "RDMLFACT"

    NAMERDNODBOC: str = "RDNODBOC"

    NAMERDNODREA: str = "RDNODREA"

    NAMERDNODRES: str = "RDNODRES"

    NAMERDNODSUM: str = "RDNODSUM"

    NAMERDPOINTS: str = "RDPOINTS"

    NAMERDRESCMB: str = "RDRESCMB"

    NAMERDRESREF: str = "RDRESREF"

    NAMERDSERIES: str = "RDSERIES"

    NAMERDSOIDSP: str = "RDSOIDSP"

    NAMERDSOILDI: str = "RDSOILDI"

    NAMERDSOIPRF: str = "RDSOIPRF"

    NAMERDSTRAIN: str = "RDSTRAIN"

    NAMERDSTRESS: str = "RDSTRESS"

    NAMERDTRANS: str = "RDTRANS "

    NAMERSUMLOAD: str = "RSUMLOAD"

    NAMERSUMMASS: str = "RSUMMASS"

    NAMERSUMREAC: str = "RSUMREAC"

    NAMERSUPTRAN: str = "RSUPTRAN"

    NAMERVABSCIS: str = "RVABSCIS"

    NAMERVELNFOR: str = "RVELNFOR"

    NAMERVFATDAM: str = "RVFATDAM"

    NAMERVFATDMG: str = "RVFATDMG"

    NAMERVFATDMH: str = "RVFATDMH"

    NAMERVFATPRP: str = "RVFATPRP"

    NAMERVFORCES: str = "RVFORCES"

    NAMERVMCCRUN: str = "RVMCCRUN"

    NAMERVMPCCR: str = "RVMPCCR "

    NAMERVMPFOR: str = "RVMPFOR "

    NAMERVMPMAP: str = "RVMPMAP "

    NAMERVNODACC: str = "RVNODACC"

    NAMERVNODDIS: str = "RVNODDIS"

    NAMERVNODREA: str = "RVNODREA"

    NAMERVNODVEL: str = "RVNODVEL"

    NAMERVORDINA: str = "RVORDINA"

    NAMERVSERIES: str = "RVSERIES"

    NAMERVSNCURV: str = "RVSNCURV"

    NAMERVSOILAY: str = "RVSOILAY"

    NAMERVSOILBM: str = "RVSOILBM"

    NAMERVSOILBS: str = "RVSOILBS"

    NAMERVSOILDM: str = "RVSOILDM"

    NAMERVSOILPY: str = "RVSOILPY"

    NAMERVSOILQZ: str = "RVSOILQZ"

    NAMERVSOILTZ: str = "RVSOILTZ"

    NAMERVSTRAIN: str = "RVSTRAIN"

    NAMERVSTRESS: str = "RVSTRESS"

    NAMESCONCEPT: str = "SCONCEPT"

    NAMESCONMESH: str = "SCONMESH"

    NAMESCONPLIS: str = "SCONPLIS"

    NAMESPROCODE: str = "SPROCODE"

    NAMESPROECCE: str = "SPROECCE"

    NAMESPROHYDR: str = "SPROHYDR"

    NAMESPROMATR: str = "SPROMATR"

    NAMESPROORIE: str = "SPROORIE"

    NAMESPROPILE: str = "SPROPILE"

    NAMESPROSECT: str = "SPROSECT"

    NAMESPROSEGM: str = "SPROSEGM"

    NAMESPROSELE: str = "SPROSELE"

    NAMESPROSOIL: str = "SPROSOIL"

    NAMETDBODNAM: str = "TDBODNAM"

    NAMETDCCNOM: str = "TDCCNOM "

    NAMETDCCRUN: str = "TDCCRUN "

    NAMETDELEM: str = "TDELEM  "

    NAMETDFATDAM: str = "TDFATDAM"

    NAMETDLOAD: str = "TDLOAD  "

    NAMETDMATER: str = "TDMATER "

    NAMETDNODE: str = "TDNODE  "

    NAMETDPVFATD: str = "TDPVFATD"

    NAMETDRESREF: str = "TDRESREF"

    NAMETDRSNAM: str = "TDRSNAM "

    NAMETDRSPNAM: str = "TDRSPNAM"

    NAMETDSCATTE: str = "TDSCATTE"

    NAMETDSCONC: str = "TDSCONC "

    NAMETDSECT: str = "TDSECT  "

    NAMETDSERIES: str = "TDSERIES"

    NAMETDSETNAM: str = "TDSETNAM"

    NAMETDSNCURV: str = "TDSNCURV"

    NAMETDSUPNAM: str = "TDSUPNAM"

    NAMETEXT: str = "TEXT    "

    NAMETSCATTER: str = "TSCATTER"

    NAMETSLAYER: str = "TSLAYER "

    NAMETSOILPRF: str = "TSOILPRF"

    NAMEUNITS: str = "UNITS   "

    NAMEW1ACCELE: str = "W1ACCELE"

    NAMEW1EXFORC: str = "W1EXFORC"

    NAMEW1MATRIX: str = "W1MATRIX"

    NAMEW1MOTION: str = "W1MOTION"

    NAMEW1PANEL: str = "W1PANEL "

    NAMEW1PANPRE: str = "W1PANPRE"

    NAMEW1POINT: str = "W1POINT "

    NAMEW1SFORCE: str = "W1SFORCE"

    NAMEW1VELOCI: str = "W1VELOCI"

    NAMEW2EXFDIF: str = "W2EXFDIF"

    NAMEW2EXFSUM: str = "W2EXFSUM"

    NAMEW2FLUDIF: str = "W2FLUDIF"

    NAMEW2FLUSUM: str = "W2FLUSUM"

    NAMEW2HDRIFT: str = "W2HDRIFT"

    NAMEW2MDRIFT: str = "W2MDRIFT"

    NAMEW2MOTDIF: str = "W2MOTDIF"

    NAMEW2MOTSUM: str = "W2MOTSUM"

    NAMEW2WDDMAT: str = "W2WDDMAT"

    NAMEWBODCON: str = "WBODCON "

    NAMEWBODY: str = "WBODY   "

    NAMEWCURRPRF: str = "WCURRPRF"

    NAMEWDRESREF: str = "WDRESREF"

    NAMEWDWACHAR: str = "WDWACHAR"

    NAMEWFKPOINT: str = "WFKPOINT"

    NAMEWFLUIDKN: str = "WFLUIDKN"

    NAMEWGLOBDEF: str = "WGLOBDEF"

    NAMEWGRESPON: str = "WGRESPON"

    NAMEWHYCOEL: str = "WHYCOEL "

    NAMEWHYPREL: str = "WHYPREL "

    NAMEWINPUT: str = "WINPUT  "

    NAMEWMRPOINT: str = "WMRPOINT"

    NAMEWSCATTER: str = "WSCATTER"

    NAMEWSECTION: str = "WSECTION"

    NAMEWSURFACE: str = "WSURFACE"

    NAMEWWASUMLO: str = "WWASUMLO"

    NAMEWWAWIKIN: str = "WWAWIKIN"

    NAMEWWGTBUOY: str = "WWGTBUOY"

    NAMEWWINDPRF: str = "WWINDPRF"

    @staticmethod
    def ConvertXiEtaToAreaUnitCoordinates(xiEta: DNV.Sesam.SifApi.Core.Point) -> DNV.Sesam.SifApi.Core.Point:
        """
        Converts from unit domain xi, eta coordinates to unit domain area coordinates.
        
        :param xiEta: The unit domain point in xi-eta coordinates to convert to a unit domain point in area coordinates.
        """
        ...

    @staticmethod
    def ConvertXiEtaToAreaUnitCoordinatesSesam(xiEta: DNV.Sesam.SifApi.Core.Point) -> DNV.Sesam.SifApi.Core.Point:
        """
        Converts from unit domain xi, eta coordinates to unit domain area coordinates.
        
        :param xiEta: The unit domain point in xi-eta coordinates to convert to a unit domain point in area coordinates.
        """
        ...

    @staticmethod
    def ElementCheckPointUnitDomainCorner(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> System.Collections.Generic.List[DNV.Sesam.SifApi.Core.Point]:
        """This method does not give corner points in the numbering schemes used in SesamCore. Use instead"""
        warnings.warn("This method does not give corner points in the numbering schemes used in SesamCore. Use instead", DeprecationWarning)

    @staticmethod
    def ElementCheckPointUnitDomainCornerCartesian(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> System.Collections.Generic.List[DNV.Sesam.SifApi.Core.Point]:
        """
        The unit domain coordinates for the Sesam Finite Elements and Sesam Core Elements.
        This method delivers Cartesian coordinates (xi,eta) for the triangles and the quadrilaterals.
        
        :returns: A list of points holding the unit domain corner coordinates.
        """
        ...

    @staticmethod
    def ElementNodeCountAndBasisDefinitions(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType, NumberOfNodes: typing.Optional[int], NumberOfBasisFunctions: typing.Optional[int], NumberOfSpaceDimensions: typing.Optional[int]) -> typing.Union[None, int, int, int]:
        ...

    @staticmethod
    def GetAListOfAllResultsDataTypes() -> System.Collections.Generic.List[str]:
        ...

    @staticmethod
    def GetAllNodalPointUnitDomainCoordinatesInDefinedOrder(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> System.Collections.Generic.List[DNV.Sesam.SifApi.Core.Point]:
        """
        *** NOTICE: For results processing only - for operator generation, the function "UnitDomain" MUST be used.
        Further notice that this function is now only used in the unit tests for the Sesam Core Elements.
        Gets all nodal point unit domain coordinates in defined order.
        
        :param elementType: Type of the element.
        """
        ...

    @staticmethod
    def GetBlanks(numberOfBlanks: int) -> str:
        ...

    @staticmethod
    def GetCardType(name: str) -> int:
        """:returns: This method returns the int value of a member of the DNV.Sesam.SifApi.Core.CoreDefinitions.CardType enum."""
        ...

    @staticmethod
    def GetElementHasMidsideNodes(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> bool:
        ...

    @staticmethod
    def GetFiniteElementLoadTypes(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> System.Collections.Generic.List[str]:
        ...

    @staticmethod
    def GetFiniteElementNodeProperties() -> System.Collections.Generic.List[str]:
        ...

    @staticmethod
    def GetFiniteElementProperties(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> System.Collections.Generic.List[str]:
        ...

    @staticmethod
    def GetFirstByteAtSiuFile() -> int:
        ...

    @staticmethod
    @overload
    def GetFloatsFromData(data: typing.List[float]) -> System.Collections.Generic.IEnumerable[int]:
        ...

    @staticmethod
    @overload
    def GetFloatsFromData(data: typing.List[float], byteList: typing.List[int], offsetBytes: int) -> None:
        ...

    @staticmethod
    @overload
    def GetIndexInfo(data: typing.List[float], indexToIndexInfo: typing.List[int]) -> typing.List[int]:
        ...

    @staticmethod
    @overload
    def GetIndexInfo(name: str, data: typing.List[float], indexInfo: typing.Optional[typing.List[int]]) -> typing.Union[bool, typing.List[int]]:
        ...

    @staticmethod
    def GetIndexInfoAlwaysLengthFirstData(name: str, data: typing.List[float], indexInfo: typing.Optional[typing.List[int]]) -> typing.Union[bool, typing.List[int]]:
        ...

    @staticmethod
    def GetIndexToIndexInfo(name: str, indexInfo: typing.Optional[typing.List[int]]) -> typing.Union[bool, typing.List[int]]:
        ...

    @staticmethod
    def GetInfoAboutIndexInfo(name: str) -> int:
        ...

    @staticmethod
    def GetIntegerArrayFromBytes(arrayLength: int, headerAreaBytes: typing.List[int], nextPosition: int) -> typing.List[int]:
        ...

    @staticmethod
    def GetLastByteAtSiuFile() -> int:
        ...

    @staticmethod
    def GetListOfAllSifDataTypes() -> System.Collections.Generic.List[str]:
        ...

    @staticmethod
    def GetNodalPointUnitDomainCornerNodeCoordinates(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> System.Collections.Generic.List[DNV.Sesam.SifApi.Core.Point]:
        """
        *** NOTICE: For results processing only - for operator generation, the function "UnitDomain" MUST be used be used for triangles.
        Gets the nodal point unit domain corner node coordinates.
        
        :param elementType: Type of the element.
        """
        ...

    @staticmethod
    def GetNodalPointUnitDomainMidSideCoordinates(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> System.Collections.Generic.List[DNV.Sesam.SifApi.Core.Point]:
        """
        *** NOTICE: For results processing only - for operator generation, the function "UnitDomain" MUST be used for triangles.
        Gets the nodal point unit domain mid side coordinates - but not used for solids since the midside nodes are not part of the extrapolation procedure for the solids.
        
        :param elementType: Type of the element.
        """
        ...

    @staticmethod
    def GetPairsIndexInfo(name: str, data: System.Collections.Generic.List[float], indexInfo: typing.Optional[DNV.Sesam.SifApi.Core.ComparablePair[int]], switchIndices: bool = False) -> typing.Union[bool, DNV.Sesam.SifApi.Core.ComparablePair[int]]:
        ...

    @staticmethod
    def GetRdfatdmgHotSpotFatigueProperties(iparam: int) -> str:
        ...

    @staticmethod
    def GetRdfatdmgPositionFatigueProperties(iparam: int, param: int) -> str:
        ...

    @staticmethod
    def GetRvfatdamIfatypAndIresData(ifatyp: int, ires: int) -> str:
        ...

    @staticmethod
    def GetRvfatdamIjointProperty(Ijoint: int) -> str:
        ...

    @staticmethod
    def GetRvfatdamOrRvfatdmgInameProperty(Iname: int, wantLongString: bool = True) -> str:
        ...

    @staticmethod
    def GetRvfatdamProperties(iparam: int, param: float) -> str:
        ...

    @staticmethod
    def GetSesamFiniteElementTypeDimension(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> int:
        """:returns: This method returns the int value of a member of the DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementTypeDimension enum."""
        ...

    @staticmethod
    def GetSifDataPairsIndexInfo(isSifDataType: bool, name: str, data: typing.List[float], indexInfo: typing.Optional[DNV.Sesam.SifApi.Core.ComparableTriplet[int]], pushIndices: bool = False, switchIndices: bool = False) -> typing.Union[int, DNV.Sesam.SifApi.Core.ComparableTriplet[int]]:
        ...

    @staticmethod
    def GetSifDataTypeMergeOrder(name: str) -> int:
        ...

    @staticmethod
    def GetSifIndexSetOrder(reversed: bool, name: str, defaultSifIndexSetOrder: typing.List[int], infoAboutIndexOrder: int) -> typing.List[int]:
        ...

    @staticmethod
    def GetSinDataIndexType(dataGroupTableTypeDefinitionCode: int) -> int:
        """:returns: This method returns the int value of a member of the DNV.Sesam.SifApi.Core.CoreDefinitions.SinDataIndexType enum."""
        ...

    @staticmethod
    def GetSinDataTypeDefinitionCode(name: str) -> int:
        """:returns: This method returns the int value of a member of the DNV.Sesam.SifApi.Core.CoreDefinitions.SinDataIndexType enum."""
        ...

    @staticmethod
    def GetSingleIndexInfo(name: str, data: System.Collections.Generic.List[float], indexInfo: typing.Optional[int]) -> typing.Union[bool, int]:
        ...

    @staticmethod
    def GetString(name: str, t: System.Collections.Generic.IReadOnlyCollection[DNV_Sesam_SifApi_Core_CoreDefinitions_GetString_T]) -> str:
        ...

    @staticmethod
    def GetStringFromByteArray(inputDataBytes: typing.List[int], startIndex: int, lengthOfString: int) -> str:
        ...

    @staticmethod
    def GetTheBytes(lineToWrite: str, cardType: DNV.Sesam.SifApi.Core.CoreDefinitions.CardType, length: int) -> typing.List[int]:
        ...

    @staticmethod
    def GetUnitDomainBottomAndTopCoordinates(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> System.Collections.Generic.List[DNV.Sesam.SifApi.Core.Point]:
        """
        Gets the unit domain bottom surface and top surface coordinates at the centroid of the element.
        Operation is not defined for 1D-elements BEAS, BTSS & TESS.
        
        :param elementType: Type of the element.
        :returns: The xi-eta-gamma triple for a Sesam Finite Element.
        """
        ...

    @staticmethod
    def GetUnitDomainCentroidNaturalCoordinates(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> DNV.Sesam.SifApi.Core.Point:
        """
        Gets the unit domain centroid natural coordinates.
        Operation is not defined for 1D-elements and 3D-elements.
        
        :param elementType: Type of the element.
        :returns: The zeta_1-zeta_2-gamma triple for triangle Sesam Finite Elements or the xi-eta-gamma triple for square Sesam Finite Elements.
        """
        ...

    @staticmethod
    def GetUnitDomainLowerAndUpperCentreNaturalCoordinates(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> System.Collections.Generic.List[DNV.Sesam.SifApi.Core.Point]:
        """
        Gets the unit domain lower surface and upper surface coordinates at the centroid of the element.
        Operation is not defined for 1D-elements and 3D-elements.
        
        :param elementType: Type of the element.
        :returns: The zeta_1-zeta_2-gamma triple for triangle Sesam Finite Elements or the xi-eta-gamma triple for square Sesam Finite Elements.
        """
        ...

    @staticmethod
    def HasRdpoints(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> bool:
        ...

    @staticmethod
    def HasRvforces(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> bool:
        ...

    @staticmethod
    def HasRvstrain(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> bool:
        ...

    @staticmethod
    def HasRvstress(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> bool:
        ...

    @staticmethod
    def Is10NodedSolid(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> bool:
        ...

    @staticmethod
    def Is15NodedSolid(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> bool:
        ...

    @staticmethod
    def Is1DElement(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> bool:
        ...

    @staticmethod
    def Is1DElementBeam(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> bool:
        ...

    @staticmethod
    def Is1DElementTruss(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> bool:
        ...

    @staticmethod
    def Is20NodedSolid(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> bool:
        ...

    @staticmethod
    def Is2DElement(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> bool:
        ...

    @staticmethod
    def Is2DElementMembrane(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> bool:
        ...

    @staticmethod
    def Is2DElementShell(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> bool:
        ...

    @staticmethod
    def Is2DElementThickShell(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> bool:
        ...

    @staticmethod
    def Is3DElement(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> bool:
        ...

    @staticmethod
    def Is3NodedMembrane(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> bool:
        ...

    @staticmethod
    def Is3NodedShell(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> bool:
        ...

    @staticmethod
    def Is4NodedMembrane(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> bool:
        ...

    @staticmethod
    def Is4NodedShell(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> bool:
        ...

    @staticmethod
    def Is4NodedSolid(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> bool:
        ...

    @staticmethod
    def Is6NodedMembrane(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> bool:
        ...

    @staticmethod
    def Is6NodedShell(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> bool:
        ...

    @staticmethod
    def Is6NodedSolid(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> bool:
        ...

    @staticmethod
    def Is8NodedMembrane(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> bool:
        ...

    @staticmethod
    def Is8NodedShell(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> bool:
        ...

    @staticmethod
    def Is8NodedSolid(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> bool:
        ...

    @staticmethod
    def IsASolid(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> bool:
        """
        Determines whether the element is a solid.
        
        :param elementType: Sesam finite element type of the element.
        :returns: true if [is a solid] [the specified element type]; otherwise, false.
        """
        ...

    @staticmethod
    def IsATriangle(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> bool:
        """
        Determines whether the element is a triangle.
        
        :param elementType: Sesam finite element type of the element.
        :returns: true if [is a triangle] [the specified element type]; otherwise, false.
        """
        ...

    @staticmethod
    def IsBlank(name: str) -> bool:
        ...

    @staticmethod
    def IsDataTypeRepeatedOnIndex(dataGroupTableTypeDefinitionCode: int) -> bool:
        ...

    @staticmethod
    def IsImplementedInSestra(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> bool:
        ...

    @staticmethod
    def IsLengthFirstDataType(name: str) -> bool:
        ...

    @staticmethod
    def IsModelDataTypesToReadFromResultFile(name: str) -> bool:
        ...

    @staticmethod
    def IsOrderedOnIndex(cardName: str) -> bool:
        ...

    @staticmethod
    def IsResultDataTypesToReadFromResultFile(name: str) -> bool:
        ...

    @staticmethod
    def IsSifBasicTextDataType(name: str) -> bool:
        ...

    @staticmethod
    def IsSifDataType(name: str) -> bool:
        ...

    @staticmethod
    def IsSifDataTypeOrBlank(name: str) -> bool:
        ...

    @staticmethod
    def IsSifDataTypeWithReversedIndexSetOrder(name: str) -> bool:
        ...

    @staticmethod
    def IsSifHydroDataType(name: str) -> bool:
        ...

    @staticmethod
    def IsSifLoadDataType(name: str) -> bool:
        ...

    @staticmethod
    def IsSifLoadTypeToConvertToBeamElementLoad(name: str) -> bool:
        ...

    @staticmethod
    def IsSifMaterialDataType(name: str) -> bool:
        ...

    @staticmethod
    def IsSifModelDataType(name: str) -> bool:
        ...

    @staticmethod
    def IsSifResultDataType(name: str) -> bool:
        ...

    @staticmethod
    def IsSifResultDefinitionDataType(name: str) -> bool:
        ...

    @staticmethod
    def IsSifSectionDataType(name: str) -> bool:
        ...

    @staticmethod
    def IsSifTdTextDataType(name: str) -> bool:
        ...

    @staticmethod
    def IsTableDataIndexPair(name: str) -> bool:
        ...

    @staticmethod
    @overload
    def MinusDataTypeDefinition(name: str, sifRef: typing.List[float], sifCardData: typing.Optional[typing.List[float]]) -> typing.Union[bool, typing.List[float]]:
        ...

    @staticmethod
    @overload
    def MinusDataTypeDefinition(name: str, numberOfEntries: int, sifCardData: typing.Optional[typing.List[float]]) -> typing.Union[bool, typing.List[float]]:
        ...

    @staticmethod
    def MinusDataTypeDefinitionTwo(name: str, first: int, secnd: int, sifCardData: typing.Optional[typing.List[float]]) -> typing.Union[bool, typing.List[float]]:
        ...

    @staticmethod
    def RdstressCompRefComponentOnIndex(component: int) -> int:
        """:returns: This method returns the int value of a member of the DNV.Sesam.SifApi.Core.CoreDefinitions.RdstressCompRef enum."""
        ...

    @staticmethod
    def RdstressCompRefDescription(component: DNV.Sesam.SifApi.Core.CoreDefinitions.RdstressCompRef) -> str:
        ...

    @staticmethod
    def ResizeAndShiftLeft(arrayIn: typing.List[float]) -> typing.List[float]:
        ...

    @staticmethod
    def ResizeAndShiftRight(arrayIn: typing.List[float]) -> typing.List[float]:
        ...

    @staticmethod
    def UnitDomain(elementType: DNV.Sesam.SifApi.Core.CoreDefinitions.SesamFiniteElementType) -> System.Collections.Generic.List[DNV.Sesam.SifApi.Core.Point]:
        """
        The unit domain coordinates for the Sesam Finite Elements and Sesam Core Elements.
        It's important to notice that this method delivers area coordinates (zeta1,zeta2) for the triangles.
        Accordingly, it cannot be used in the "Fatigue Check Point Element" "Element Corner" computations of SesamCore since the stress routines accept (xi,eta) coordinates.
        
        :param elementType: The Sesam finite element type.
        """
        ...

    @staticmethod
    def UnitDomainTriangle() -> System.Collections.Generic.List[DNV.Sesam.SifApi.Core.Point]:
        """
        The unit domain coordinates for the Sesam Finite Elements and Sesam Core Elements.
        It's important to notice that this method delivers area coordinates (zeta1,zeta2) for the triangles.
        Accordingly, it cannot be used in the "Fatigue Check Point Element" "Element Corner" computations of SesamCore since the stress routines accept (xi,eta) coordinates.
        
        :returns: A list of points holding the unit domain corner coordinates.
        """
        ...

    @staticmethod
    def UnitDomainTriangle2() -> System.Collections.Generic.List[DNV.Sesam.SifApi.Core.Point]:
        """
        The unit domain coordinates for the Sesam Finite Elements and Sesam Core Elements.
        It's important to notice that this method delivers area coordinates (zeta1,zeta2) for the triangles.
        Accordingly, it cannot be used in the "Fatigue Check Point Element" "Element Corner" computations of SesamCore since the stress routines accept (xi,eta) coordinates.
        
        :returns: A list of points holding the unit domain corner and mid-side coordinates.
        """
        ...


class DataTypeInfo(System.Object):
    """This class has no documentation."""

    @property
    def Name(self) -> str:
        ...

    @property
    def IsLengthFirst(self) -> bool:
        ...

    @property
    def IndexToIndexInfo(self) -> typing.List[int]:
        ...

    @property
    def NumberOfIndices(self) -> int:
        ...

    @property
    def IsReversedIndexSetOrder(self) -> bool:
        ...

    @property
    def IsSifTdTextDataType(self) -> bool:
        ...

    @property
    def IsSifDataType(self) -> bool:
        ...

    @overload
    def __init__(self, name: str, isLengthFirst: bool, indexToIndexInfo: typing.List[int], numberOfIndices: int, isReversedIndexSetOrder: bool, isSifTdTextDataType: bool) -> None:
        ...

    @overload
    def __init__(self, name: str, isLengthFirst: bool, isSifDataType: bool, isSifTdTextDataType: bool) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...


class ElementLevel:
    """This class has no documentation."""

    @property
    def ElementIdentifier(self) -> int:
        """Gets the element identifier."""
        ...

    @property
    def ElementLine(self) -> int:
        """
        Gets the element line.
        
        This property contains the int value of a member of the DNV.Sesam.SifApi.Core.CoreDefinitions.ElementLine enum.
        """
        ...

    def __init__(self, elementIdentifier: int, elementLine: DNV.Sesam.SifApi.Core.CoreDefinitions.ElementLine) -> None:
        ...

    @staticmethod
    def Compare(a: DNV.Sesam.SifApi.Core.ElementLevel, b: DNV.Sesam.SifApi.Core.ElementLevel) -> bool:
        """
        Compares to element level entries a and b.
        
        :param a: Entry a.
        :param b: Entry b.
        """
        ...


class ElementLevelHelper(System.Object):
    """This class has no documentation."""

    @staticmethod
    def CompareElementLevelStructure(expectedList: System.Collections.Generic.SortedDictionary[int, System.Collections.Generic.List[DNV.Sesam.SifApi.Core.ElementLevel]], actualList: System.Collections.Generic.SortedDictionary[int, System.Collections.Generic.List[DNV.Sesam.SifApi.Core.ElementLevel]]) -> bool:
        ...


class IBaseHeader(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def Name(self) -> str:
        """Gets the name. Where name is a Norsam binary file name field."""
        ...

    def Create(self, headerAreaBytes: typing.List[int], start: int) -> None:
        """
        The create.
        
        :param headerAreaBytes: The header area bytes.
        :param start: The start.
        """
        ...

    def Write(self, sw: System.IO.StreamWriter) -> None:
        ...


class IAllocateHeader(DNV.Sesam.SifApi.Core.IBaseHeader, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def IALOP(self) -> int:
        """Gets IALOP: Allocation system option."""
        ...

    @IALOP.setter
    @abc.abstractmethod
    def IALOP(self, value: int):
        """Gets IALOP: Allocation system option."""
        ...

    @property
    @abc.abstractmethod
    def IPFILE(self) -> int:
        ...

    @IPFILE.setter
    @abc.abstractmethod
    def IPFILE(self, value: int):
        ...

    @property
    @abc.abstractmethod
    def IPSL(self) -> int:
        """Gets IPSL: Pointer, within the file, to the penultimate free area."""
        ...

    @IPSL.setter
    @abc.abstractmethod
    def IPSL(self, value: int):
        """Gets IPSL: Pointer, within the file, to the penultimate free area."""
        ...

    @property
    @abc.abstractmethod
    def IPSEL(self) -> int:
        """Gets IPSEL: Pointer to the last word of the penultimate free area."""
        ...

    @IPSEL.setter
    @abc.abstractmethod
    def IPSEL(self, value: int):
        """Gets IPSEL: Pointer to the last word of the penultimate free area."""
        ...

    @property
    @abc.abstractmethod
    def IPBEL(self) -> int:
        """Gets IPBEL: Pointer, within the file, to the last free area."""
        ...

    @IPBEL.setter
    @abc.abstractmethod
    def IPBEL(self, value: int):
        """Gets IPBEL: Pointer, within the file, to the last free area."""
        ...

    @property
    @abc.abstractmethod
    def IPLU(self) -> int:
        """Gets IPLU: Pointer to the lowest allocatable word."""
        ...

    @IPLU.setter
    @abc.abstractmethod
    def IPLU(self, value: int):
        """Gets IPLU: Pointer to the lowest allocatable word."""
        ...

    @property
    @abc.abstractmethod
    def IPAFI(self) -> int:
        """Gets IPAFI: Pointer, within MRC, see data type NORSAM, to the account of internal free areas."""
        ...

    @IPAFI.setter
    @abc.abstractmethod
    def IPAFI(self, value: int):
        """Gets IPAFI: Pointer, within MRC, see data type NORSAM, to the account of internal free areas."""
        ...


class IAllocateHeaderWriter(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def AddressToIPSL(self) -> int:
        """Gets AddressToIPSL: I.e. address to the Pointer, within the file, to the penultimate free area."""
        ...

    @property
    @abc.abstractmethod
    def AddressToIPSEL(self) -> int:
        """Gets AddressToIPSEL: I.e. address to the Pointer to the last word of the penultimate free area."""
        ...

    @property
    @abc.abstractmethod
    def AddressToIPBEL(self) -> int:
        """Gets AddressToIPBEL: I.e. address to the Pointer, within the file, to the last free area."""
        ...

    @property
    @abc.abstractmethod
    def AddressToIPHU(self) -> int:
        """Gets AddressToIPHU: I.e. address to the Pointer, within the file, to the highest updateable word."""
        ...

    @property
    @abc.abstractmethod
    def AddressToIPLU(self) -> int:
        """Gets AddressToIPLU: I.e. address to the Pointer to the lowest allocatable word."""
        ...

    @property
    @abc.abstractmethod
    def AddressToIPAFI(self) -> int:
        """Gets AddressToIPAFI: I.e. address to the Pointer, within MRC, see data type NORSAM, to the account of internal free areas."""
        ...


class IDataGroupTableDimension(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def First(self) -> int:
        """Gets or sets the first."""
        ...

    @First.setter
    @abc.abstractmethod
    def First(self, value: int):
        """Gets or sets the first."""
        ...

    @property
    @abc.abstractmethod
    def Second(self) -> int:
        """Gets or sets the second."""
        ...

    @Second.setter
    @abc.abstractmethod
    def Second(self, value: int):
        """Gets or sets the second."""
        ...

    @property
    @abc.abstractmethod
    def Third(self) -> int:
        """Gets or sets the third."""
        ...

    @Third.setter
    @abc.abstractmethod
    def Third(self, value: int):
        """Gets or sets the third."""
        ...

    def DimensionsToBeDecoded(self, tableDimension: int, numberOfReferenceValues: int = 0) -> None:
        """
        The dimensions to be decoded.
        
        :param tableDimension: The table dimension.
        :param numberOfReferenceValues: The number of reference values.
        """
        ...


class IDataGroupTable(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def AllocatedDimension(self) -> DNV.Sesam.SifApi.Core.IDataGroupTableDimension:
        """Gets or sets the allocated dimension."""
        ...

    @property
    @abc.abstractmethod
    def AssignedDimension(self) -> DNV.Sesam.SifApi.Core.IDataGroupTableDimension:
        """Gets or sets the assigned dimension."""
        ...

    @property
    @abc.abstractmethod
    def DataGroupName(self) -> str:
        """Gets the data group name."""
        ...

    @property
    @abc.abstractmethod
    def DataGroupTableAddress(self) -> int:
        """Gets the data group table address."""
        ...

    @DataGroupTableAddress.setter
    @abc.abstractmethod
    def DataGroupTableAddress(self, value: int):
        """Gets the data group table address."""
        ...

    @property
    @abc.abstractmethod
    def DataGroupTableTypeDefinitionCode(self) -> int:
        """Gets the data group table type definition code."""
        ...

    @property
    @abc.abstractmethod
    def DataGroupTypeCode(self) -> int:
        """Gets the data group type code."""
        ...

    @property
    @abc.abstractmethod
    def NumberOfBytesDecoded(self) -> int:
        """Gets the number of bytes decoded."""
        ...

    @property
    @abc.abstractmethod
    def NumberOfFields(self) -> int:
        """Gets the number of fields."""
        ...

    @property
    @abc.abstractmethod
    def RawDataGroupTableAddress(self) -> int:
        """Gets the raw data group table address."""
        ...

    @property
    @abc.abstractmethod
    def NumberOfDataGroups(self) -> int:
        """Gets the number of data sets added for this data group."""
        ...

    def UpdateAssignedDimension(self, indexInfo: typing.List[int]) -> None:
        """Updates the assigned dimensions as we add data types."""
        ...


class ISifDataBase(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def Ident(self) -> str:
        """Gets the name of the data type"""
        ...

    @property
    @abc.abstractmethod
    def Data(self) -> typing.List[float]:
        """Get the numeric data (relevant for non-text data types)"""
        ...

    @property
    @abc.abstractmethod
    def TextList(self) -> System.Collections.Generic.List[str]:
        """Get a list of text data (relevant for text data types)"""
        ...

    @TextList.setter
    @abc.abstractmethod
    def TextList(self, value: System.Collections.Generic.List[str]):
        """Get a list of text data (relevant for text data types)"""
        ...


class ISifData(DNV.Sesam.SifApi.Core.ISifDataBase, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __getitem__(self, i: int) -> float:
        """
        Get or set an element of the numeric data array
        
        :param i: The element number to get or set
        :returns: An element of the numeric data array.
        """
        ...

    def __setitem__(self, i: int, value: float) -> None:
        """
        Get or set an element of the numeric data array
        
        :param i: The element number to get or set
        :returns: An element of the numeric data array.
        """
        ...

    @overload
    def SetData(self, data: System.Collections.Generic.IEnumerable[float]) -> None:
        """
        Set the numeric data
        
        :param data: The numeric data
        """
        ...

    @overload
    def SetData(self, data: System.Collections.Generic.IEnumerable[float]) -> None:
        """
        Set the numeric data
        
        :param data: The numeric data
        """
        ...

    def ToString(self) -> str:
        """Get a string representation of the data type"""
        ...


class IBackingStorage(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def NextPosition(self) -> int:
        ...

    def AddData(self, data: typing.List[float], numberOfSetsLeft: int, positionToPreviousSet: int) -> None:
        ...

    def Close(self) -> None:
        ...

    def FlushBuffer(self) -> None:
        ...

    def GetData(self, position: int, numberOfSetsLeft: typing.Optional[int], positionToPreviousSet: typing.Optional[int]) -> typing.Union[typing.List[float], int, int]:
        ...

    @overload
    def GetDataListOfPositions(self, name: str, positions: System.Collections.Generic.List[int], addChainedData: bool) -> System.Collections.Generic.List[DNV.Sesam.SifApi.Core.ISifData]:
        ...

    @overload
    def GetDataListOfPositions(self, dataGroupTable: DNV.Sesam.SifApi.Core.IDataGroupTable, positions: typing.List[int], sizeToRead: int, addChainedData: bool) -> System.Collections.Generic.List[DNV.Sesam.SifApi.Core.ISifData]:
        ...

    @overload
    def GetDataListOfPositions(self, dataGroupTable: DNV.Sesam.SifApi.Core.IDataGroupTable, positions: System.Collections.Generic.List[int], addChainedData: bool) -> System.Collections.Generic.List[DNV.Sesam.SifApi.Core.ISifData]:
        ...

    def GetDataNonStruct(self, position: int) -> typing.List[float]:
        ...

    @overload
    def GetDataOnPosition(self, name: str, position: int, addChainedData: bool) -> System.Collections.Generic.List[DNV.Sesam.SifApi.Core.ISifData]:
        ...

    @overload
    def GetDataOnPosition(self, dataGroupTable: DNV.Sesam.SifApi.Core.IDataGroupTable, position: int, addChainedData: bool) -> System.Collections.Generic.List[DNV.Sesam.SifApi.Core.ISifData]:
        ...

    def GetDataOnPositionAndPositionOfChainedData(self, name: str, position: int) -> System.ValueTuple[DNV.Sesam.SifApi.Core.ISifData, int]:
        ...

    def GetNumberOfSetsLeft(self, positionToPreviousSet: int) -> int:
        ...


class ISifIndex(System.IEquatable[DNV_Sesam_SifApi_Core_ISifIndex], System.IComparable[DNV_Sesam_SifApi_Core_ISifIndex], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def FirstIndex(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def SecndIndex(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def ThirdIndex(self) -> int:
        ...

    def CompareIndexAndReturnTrueIfOtherIsBigger(self, other: DNV.Sesam.SifApi.Core.ISifIndex, swapFirstAndSecondIndex: bool = False) -> bool:
        """
        Compares two indices and returns true if other is bigger.
        
        :param other: The index to be compared against.
        :param swapFirstAndSecondIndex: If the first and second index should swap order in compare this parameter must be set to true.
        :returns: true if other is bigger.
        """
        ...

    def CompareIndicesAndUpdateThisIfOtherIsBigger(self, other: DNV.Sesam.SifApi.Core.ISifIndex, swapFirstAndSecondIndex: bool = False) -> None:
        """
        Compares two indices and update the current one if other is bigger.
        
        :param other: The index to be compared against.
        :param swapFirstAndSecondIndex: If the first and second index should swap order in compare this parameter must be set to true.
        """
        ...

    def CompareTwoIndices(self, other: DNV.Sesam.SifApi.Core.ISifIndex) -> int:
        ...

    def GetAsBytes(self) -> typing.List[int]:
        ...

    def GetNextIndex(self, binaryBucketReader: System.IO.BinaryReader) -> DNV.Sesam.SifApi.Core.ISifIndex:
        ...

    def NoIndex(self) -> bool:
        ...

    def ReadIndexAndCompare(self, binaryBucketReader: System.IO.BinaryReader) -> bool:
        ...

    def SetNoIndex(self) -> DNV.Sesam.SifApi.Core.ISifIndex:
        ...

    def SizeOfIndexPackage(self) -> int:
        """Number of bytes for an index, when the index is written to file."""
        ...

    def SizeOfIndices(self) -> int:
        ...

    def WriteIndex(self, binaryBucketWriter: System.IO.BinaryWriter) -> None:
        ...


class IBackingStorageDictionary(typing.Generic[DNV_Sesam_SifApi_Core_IBackingStorageDictionary_TValue], System.IDisposable, typing.Iterable[System.Collections.Generic.List[DNV_Sesam_SifApi_Core_IBackingStorageDictionary_TValue]], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def Count(self) -> int:
        ...

    def Add(self, key: DNV.Sesam.SifApi.Core.ISifIndex, value: DNV_Sesam_SifApi_Core_IBackingStorageDictionary_TValue) -> None:
        ...

    def Clear(self) -> None:
        ...

    def Close(self) -> None:
        ...

    def ContainsKey(self, key: DNV.Sesam.SifApi.Core.ISifIndex) -> bool:
        ...

    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.List[DNV_Sesam_SifApi_Core_IBackingStorageDictionary_TValue]]:
        ...

    def Remove(self, key: DNV.Sesam.SifApi.Core.ISifIndex) -> bool:
        ...

    def TryGetValue(self, key: DNV.Sesam.SifApi.Core.ISifIndex, value: typing.Optional[DNV_Sesam_SifApi_Core_IBackingStorageDictionary_TValue]) -> typing.Union[bool, DNV_Sesam_SifApi_Core_IBackingStorageDictionary_TValue]:
        ...

    def TryGetValueAll(self, key: DNV.Sesam.SifApi.Core.ISifIndex, value: typing.Optional[System.Collections.Generic.List[DNV_Sesam_SifApi_Core_IBackingStorageDictionary_TValue]]) -> typing.Union[bool, System.Collections.Generic.List[DNV_Sesam_SifApi_Core_IBackingStorageDictionary_TValue]]:
        ...

    def TryGetValueDequeue(self, key: DNV.Sesam.SifApi.Core.ISifIndex, value: typing.Optional[System.Collections.Generic.List[DNV_Sesam_SifApi_Core_IBackingStorageDictionary_TValue]]) -> typing.Union[bool, System.Collections.Generic.List[DNV_Sesam_SifApi_Core_IBackingStorageDictionary_TValue]]:
        ...


class SifIndexType(System.Enum):
    """This class has no documentation."""

    NoIndex = 0

    OneIndex = 1

    TwoIndex = 2

    ThreeIndex = 3

    UnknownIndex = 4


class IBucketFile(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def FirstTimeRead(self) -> bool:
        ...

    @FirstTimeRead.setter
    @abc.abstractmethod
    def FirstTimeRead(self, value: bool):
        ...

    def Add(self, id: DNV.Sesam.SifApi.Core.ISifIndex, data: typing.List[float], numberOfSetsLeft: int, positionToPreviousSet: int) -> None:
        ...

    def AddDataOnlyNonStruct(self, data: typing.List[float], numberOfSetsLeft: int, positionToPreviousSet: int) -> int:
        ...

    def AddLinkedDataWithRepeatedIndex(self, data: typing.List[float], numberOfSetsLeft: int, positionToPreviousDataSet: int) -> int:
        ...

    def Close(self) -> None:
        ...

    def CreateSetInsertionOrderOfNonZeroPositions(self, sifIndexType: DNV.Sesam.SifApi.Core.SifIndexType, numberOfEntriesInBucketStructure: int, nextPosition: int, numberOfDataSetsToRead: int, onFirstDim: bool = True) -> System.Collections.Generic.List[int]:
        ...

    def FlushBuffer(self) -> None:
        ...

    @overload
    def Get(self, name: str, position: int, addChainedData: bool) -> System.Collections.Generic.List[DNV.Sesam.SifApi.Core.ISifData]:
        ...

    @overload
    def Get(self, name: str, positions: System.Collections.Generic.List[int], addChainedData: bool) -> System.Collections.Generic.List[DNV.Sesam.SifApi.Core.ISifData]:
        ...

    @overload
    def Get(self, dataGroupTable: DNV.Sesam.SifApi.Core.IDataGroupTable, position: int, addChainedData: bool) -> System.Collections.Generic.List[DNV.Sesam.SifApi.Core.ISifData]:
        ...

    @overload
    def Get(self, dataGroupTable: DNV.Sesam.SifApi.Core.IDataGroupTable, positions: System.Collections.Generic.List[int], addChainedData: bool) -> System.Collections.Generic.List[DNV.Sesam.SifApi.Core.ISifData]:
        ...

    def GetAllDataCardInBucket(self, name: str, startPositionAtFile: int, numberOfEntriesInBucket: int, sifIndexType: DNV.Sesam.SifApi.Core.SifIndexType) -> System.Collections.Generic.List[DNV.Sesam.SifApi.Core.ISifData]:
        ...

    def GetAllFromListOfPositions(self, name: str, listOfPositions: System.Collections.Generic.IEnumerable[int], sizeToRead: int, addChainedData: bool = False) -> System.Collections.Generic.List[DNV.Sesam.SifApi.Core.ISifData]:
        ...

    def GetNextFilePosition(self) -> int:
        ...

    def GetNextForWhichRepeatedIndexIsLegal(self, positionToStartOfLinkedList: int) -> System.Collections.Generic.List[typing.List[float]]:
        ...

    def GetNextPositionInBucket(self, startPositionAtFile: int, sifIndexType: DNV.Sesam.SifApi.Core.SifIndexType) -> int:
        ...

    def GetNonStruct(self, position: int) -> typing.List[float]:
        ...

    def GetNumberOfSetsLeft(self, positionToPreviousSet: int) -> int:
        ...

    def GetPosition(self, startPositionAtFile: int, numberOfEntriesInBucket: int, iSifIndex: DNV.Sesam.SifApi.Core.ISifIndex) -> int:
        ...

    def GetPositionForLinkedDataWithRepeatedIndex(self, startPositionAtFile: int, numberOfEntriesInBucket: int, iSifIndex: DNV.Sesam.SifApi.Core.ISifIndex, storagePositionForNewPosition: typing.Optional[int]) -> typing.Union[int, int]:
        ...

    def UpdatePositionForLinkedDataWithRepeatedIndex(self, storagePositionForNewPosition: int, positionToThisDataSet: int) -> None:
        ...

    def WriteId(self, id: DNV.Sesam.SifApi.Core.ISifIndex, position: int) -> None:
        ...


class ISifDataTypeDimension(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def Position(self) -> int:
        ...

    @Position.setter
    @abc.abstractmethod
    def Position(self, value: int):
        ...

    @property
    @abc.abstractmethod
    def IndexType(self) -> int:
        """This property contains the int value of a member of the DNV.Sesam.SifApi.Core.SifIndexType enum."""
        ...

    @property
    @abc.abstractmethod
    def GetListOnIndex(self) -> System.Collections.Generic.Dictionary[DNV.Sesam.SifApi.Core.ISifIndex, typing.List[int]]:
        ...

    @property
    @abc.abstractmethod
    def NumberOfIndices(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def MaxFirstIndex(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def MinFirstIndex(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def MaxSecndIndex(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def MinSecndIndex(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def MaxThirdIndex(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def MinThirdIndex(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def IndexRepeatCode(self) -> int:
        """This property contains the int value of a member of the DNV.Sesam.SifApi.Core.SifIndexRepeatCode enum."""
        ...

    @overload
    def AddIndex(self) -> None:
        ...

    @overload
    def AddIndex(self, sifIndex: DNV.Sesam.SifApi.Core.ISifIndex) -> None:
        ...

    @overload
    def AddIndex(self, sifIndex: DNV.Sesam.SifApi.Core.ISifIndex, arr: typing.Optional[typing.List[int]]) -> typing.Union[None, typing.List[int]]:
        ...

    @overload
    def AddIndex(self, name: str, sifIndex: DNV.Sesam.SifApi.Core.ISifIndex, position: int) -> None:
        ...

    def ClearLists(self) -> None:
        ...

    def Close(self) -> None:
        ...

    def UpdateArr(self, arr: typing.List[int]) -> None:
        ...


class ITableOfContents(typing.Generic[DNV_Sesam_SifApi_Core_ITableOfContents_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def Name(self) -> str:
        """Gets the name of the data type."""
        ...

    @Name.setter
    @abc.abstractmethod
    def Name(self, value: str):
        """Gets the name of the data type."""
        ...

    @property
    @abc.abstractmethod
    def Count(self) -> int:
        """Gets the allocated number of data arrays."""
        ...

    @property
    @abc.abstractmethod
    def AssignedCount(self) -> int:
        """Gets the assigned number of data arrays."""
        ...

    @property
    @abc.abstractmethod
    def FirstIndex(self) -> int:
        """Gets the first maximal, or allocated index."""
        ...

    @property
    @abc.abstractmethod
    def SecndIndex(self) -> int:
        """Gets the second maximal, or allocated index."""
        ...

    @property
    @abc.abstractmethod
    def ThirdIndex(self) -> int:
        """Gets the third maximal, or allocated index."""
        ...

    @property
    @abc.abstractmethod
    def AllIndices(self) -> typing.List[int]:
        """Gets all maximal, or allocated indices."""
        ...

    @property
    @abc.abstractmethod
    def IndexType(self) -> int:
        """
        Gets the Sif index type of the data type
        
        This property contains the int value of a member of the DNV.Sesam.SifApi.Core.SifIndexType enum.
        """
        ...

    @property
    @abc.abstractmethod
    def IndexRepeatCode(self) -> int:
        """
        Gets the Sif index repeat code of the data type
        
        This property contains the int value of a member of the DNV.Sesam.SifApi.Core.SifIndexRepeatCode enum.
        """
        ...

    @property
    @abc.abstractmethod
    def DataTypeDefinitionCode(self) -> int:
        """
        Gets the Sin data index type of the data type
        
        This property contains the int value of a member of the DNV.Sesam.SifApi.Core.CoreDefinitions.SinDataIndexType enum.
        """
        ...


class IDataTypeTableLookUp(typing.Generic[DNV_Sesam_SifApi_Core_IDataTypeTableLookUp_T], DNV.Sesam.SifApi.Core.ITableOfContents[DNV_Sesam_SifApi_Core_IDataTypeTableLookUp_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def MergeFileNumbers(self) -> System.Collections.Generic.List[int]:
        ...

    def Add(self, toAdd: DNV.Sesam.SifApi.Core.IDataTypeTableLookUp[DNV_Sesam_SifApi_Core_IDataTypeTableLookUp_T]) -> None:
        ...

    def Compare(self, toCompare: DNV.Sesam.SifApi.Core.IDataTypeTableLookUp[DNV_Sesam_SifApi_Core_IDataTypeTableLookUp_T], numberOfSignificantIndices: int) -> None:
        ...

    def CompareTo(self, other: DNV.Sesam.SifApi.Core.IDataTypeTableLookUp[DNV_Sesam_SifApi_Core_IDataTypeTableLookUp_T]) -> bool:
        ...

    def GetFirstIndexIncrement(self, mergeFileNumber: int) -> int:
        ...

    def GetSecndIndexIncrement(self, mergeFileNumber: int) -> int:
        ...

    def GetThirdIndexIncrement(self, mergeFileNumber: int) -> int:
        ...

    def HasThisMergeFileNumber(self, mergeFileNumber: int) -> bool:
        ...

    def Merge(self, toMerge: DNV.Sesam.SifApi.Core.IDataTypeTableLookUp[DNV_Sesam_SifApi_Core_IDataTypeTableLookUp_T], numberOfSignificantIndices: int) -> None:
        ...

    def MergeFirst(self, numberOfSignificantIndices: int) -> None:
        """Used when a data type previously where not added to the table of contents for the merged file."""
        ...

    def SetFirstIndexIncrement(self, toIndex: int, indexIncrement: int) -> None:
        ...

    def SetMergeFileNumber(self, mergeFileNumber: int) -> None:
        ...

    def SetSecndIndexIncrement(self, toIndex: int, indexIncrement: int) -> None:
        ...

    def SetThirdIndexIncrement(self, toIndex: int, indexIncrement: int) -> None:
        ...

    def ToStringCompare(self) -> str:
        ...

    def UpdateAssignedCount(self, increment: int) -> None:
        ...

    def UpdateAssignedCountAndMaxFirstIndex(self, increment: int, maxFirstIndex: int) -> None:
        ...


class ISifBucketDefinitionIndex(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def FirstIndexInBucket(self) -> DNV.Sesam.SifApi.Core.ISifIndex:
        ...

    @property
    @abc.abstractmethod
    def LastIndexInBucket(self) -> DNV.Sesam.SifApi.Core.ISifIndex:
        ...


class ISifBucketDefinition(System.IDisposable, metaclass=abc.ABCMeta):
    """ISifBucketDefinition - the contents of a bucket."""

    @property
    @abc.abstractmethod
    def Index(self) -> DNV.Sesam.SifApi.Core.ISifBucketDefinitionIndex:
        ...

    @property
    @abc.abstractmethod
    def HasRepeatedIndex(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def StartPositionAtFile(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def MaximalNumberOfEntriesInBucket(self) -> int:
        """Gets or sets the maximal number of entries in bucket not counting repeated index sets."""
        ...

    @MaximalNumberOfEntriesInBucket.setter
    @abc.abstractmethod
    def MaximalNumberOfEntriesInBucket(self, value: int):
        """Gets or sets the maximal number of entries in bucket not counting repeated index sets."""
        ...

    @property
    @abc.abstractmethod
    def CurrentNumberOfEntriesInBucket(self) -> int:
        """Gets or sets the current number of entries in bucket counting all index sets added to the bucket."""
        ...

    @CurrentNumberOfEntriesInBucket.setter
    @abc.abstractmethod
    def CurrentNumberOfEntriesInBucket(self, value: int):
        """Gets or sets the current number of entries in bucket counting all index sets added to the bucket."""
        ...

    @property
    @abc.abstractmethod
    def CurrentNumberOfBytesInBucket(self) -> int:
        ...

    @CurrentNumberOfBytesInBucket.setter
    @abc.abstractmethod
    def CurrentNumberOfBytesInBucket(self, value: int):
        ...

    def Close(self) -> None:
        ...

    @overload
    def IncrementCurrentNumberOfEntriesInBucket(self) -> None:
        ...

    @overload
    def IncrementCurrentNumberOfEntriesInBucket(self, sifIndex: DNV.Sesam.SifApi.Core.ISifIndex) -> None:
        ...

    def UpdateMinMaxIndexIfNeeded(self, sifIndex: DNV.Sesam.SifApi.Core.ISifIndex) -> None:
        ...


class ISifBucketFileAdministrator(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def AllDataInMemory(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def TotalNumberOfEntriesInBucketStructure(self) -> int:
        ...

    @overload
    def Add(self, id: DNV.Sesam.SifApi.Core.ISifIndex, data: typing.List[float]) -> None:
        ...

    @overload
    def Add(self, id: DNV.Sesam.SifApi.Core.ISifIndex, position: int) -> None:
        ...

    def AddData(self, data: typing.List[float], numberOfSetsLeft: int, positionToPreviousSet: int) -> int:
        """For sif/siu data."""
        ...

    def AddDataForWhichRepeatedIndexIsLegal(self, id: DNV.Sesam.SifApi.Core.ISifIndex, data: typing.List[float], firstTime: bool) -> None:
        ...

    def AddForOneBucketOnly(self, id: DNV.Sesam.SifApi.Core.ISifIndex, data: typing.List[float]) -> None:
        ...

    def Close(self) -> None:
        """Close/Dispose the resources used by the component."""
        ...

    def Complete(self) -> None:
        ...

    def CompleteSinBucketStructure(self) -> None:
        ...

    def CreateBucket(self, first: DNV.Sesam.SifApi.Core.ISifIndex, last: DNV.Sesam.SifApi.Core.ISifIndex, numberOfEntries: int) -> None:
        """
        For sin data.
        
        :param first: First index in bucket.
        :param last: Lasts index in bucket.
        :param numberOfEntries: Number of entries in bucket.
        """
        ...

    def CreateBuckets(self, list: System.Collections.Generic.Dictionary[DNV.Sesam.SifApi.Core.ISifIndex, typing.List[int]]) -> None:
        """
        Marked as obsolete. Not to be used in new implementations.
        Computes the bucket structure for search by index on data in the model.
        
        :param list: Sorted list of indices in the model.
        """
        ...

    def CreateSetInsertionOrderOfNonZeroPositions(self, sifIndexType: DNV.Sesam.SifApi.Core.SifIndexType, numberOfDataSetsToRead: int, onFirstDim: bool = True) -> System.Collections.Generic.List[int]:
        """"""
        ...

    def FlushBuffer(self) -> None:
        """Flush in-memory data to backing storage if needed."""
        ...

    def GetAllDataCardInBucket(self, name: str, sifBucketDefinition: DNV.Sesam.SifApi.Core.ISifBucketDefinition, sifIndexType: DNV.Sesam.SifApi.Core.SifIndexType) -> System.Collections.Generic.List[DNV.Sesam.SifApi.Core.ISifData]:
        """"""
        ...

    def GetAllFromListOfPositions(self, name: str, listOfPositions: System.Collections.Generic.IEnumerable[int], sizeToRead: int, addChainedData: bool = False) -> System.Collections.Generic.List[DNV.Sesam.SifApi.Core.ISifData]:
        """"""
        ...

    @overload
    def GetData(self, id: DNV.Sesam.SifApi.Core.ISifIndex, fillDataInMemory: bool, alwaysThrowWhenIndexIsMissing: bool = False) -> typing.List[float]:
        """
        For sif/siu data.
        
        :param id: Index to data in the model.
        :param fillDataInMemory: Add data in memory - lru garbage collection.
        :param alwaysThrowWhenIndexIsMissing: For debugging - should be left "false".
        """
        ...

    @overload
    def GetData(self, id: DNV.Sesam.SifApi.Core.ISifIndex, dataGroupTable: DNV.Sesam.SifApi.Core.IDataGroupTable, fillDataInMemory: bool, alwaysThrowWhenIndexIsMissing: bool = False) -> typing.List[float]:
        """
        For sin data.
        
        :param id: Index to data in the model.
        :param dataGroupTable: The pointer table that provides addresses to data in the model on a sin-file.
        :param fillDataInMemory: Add data in memory - lru garbage collection.
        :param alwaysThrowWhenIndexIsMissing: For debugging - should be left "false".
        """
        ...

    @overload
    def GetDataCard(self, id: DNV.Sesam.SifApi.Core.ISifIndex, dataGroupTable: DNV.Sesam.SifApi.Core.IDataGroupTable, fillDataInMemory: bool, dataFound: typing.Optional[bool]) -> typing.Union[System.Collections.Generic.List[DNV.Sesam.SifApi.Core.ISifData], bool]:
        """
        For sin data in list - general - holds standard data and text data - For SuperElementResult.
        
        :param id: Index to data in the model.
        :param dataGroupTable: The pointer table that provides addresses to data in the model on a sin-file.
        :param fillDataInMemory: Add data in memory - lru garbage collection.
        """
        ...

    @overload
    def GetDataCard(self, id: DNV.Sesam.SifApi.Core.ISifIndex, name: str, fillDataInMemory: bool, dataFound: typing.Optional[bool]) -> typing.Union[System.Collections.Generic.List[DNV.Sesam.SifApi.Core.ISifData], bool]:
        """
        For sif/siu data in list - general - holds standard data and text data - For SuperElementResult.
        
        :param id: Index to data in the model.
        :param name: Data type name.
        :param fillDataInMemory: Add data in memory - lru garbage collection.
        """
        ...

    def GetNextDataCard(self, name: str, sifIndexType: DNV.Sesam.SifApi.Core.SifIndexType) -> System.Collections.Generic.List[DNV.Sesam.SifApi.Core.ISifData]:
        """"""
        ...

    def SetFirstTimeReadAll(self) -> None:
        ...

    def StoreBucketInformation(self, id: DNV.Sesam.SifApi.Core.ISifIndex, position: int) -> None:
        """
        For sin data. Add index and position to the bucket.
        
        :param id: Index to data in the model.
        :param position: Position to data at sin for this id.
        """
        ...


class IBucketIndexAdministrator(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def TableLookUp(self) -> System.Collections.Generic.SortedDictionary[str, DNV.Sesam.SifApi.Core.IDataTypeTableLookUp[int]]:
        ...

    def AddDimension(self, name: str, dataTypeDimension: DNV.Sesam.SifApi.Core.ISifDataTypeDimension) -> None:
        ...

    @overload
    def AddToLookUp(self, name: str, dataGroupTable: DNV.Sesam.SifApi.Core.IDataGroupTable) -> None:
        ...

    @overload
    def AddToLookUp(self, name: str, count: int, maxFirstIndex: int, maxSecndIndex: int, maxThirdIndex: int) -> None:
        ...

    def CreateBuckets(self, sifFileType: DNV.Sesam.SifApi.Core.CoreDefinitions.SifFileType, modelData: System.Collections.Generic.SortedDictionary[str, DNV.Sesam.SifApi.Core.ISifBucketFileAdministrator]) -> None:
        ...

    def GetDimension(self, name: str, dataTypeDimension: typing.Optional[DNV.Sesam.SifApi.Core.ISifDataTypeDimension]) -> typing.Union[bool, DNV.Sesam.SifApi.Core.ISifDataTypeDimension]:
        ...

    def GetTableLookUp(self, cardName: str, tableLookUp: typing.Optional[DNV.Sesam.SifApi.Core.IDataTypeTableLookUp[int]]) -> typing.Union[bool, DNV.Sesam.SifApi.Core.IDataTypeTableLookUp[int]]:
        ...


class IDataGroupTableArray(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def DataGroupAddresses(self) -> System.Collections.Generic.List[int]:
        ...

    @property
    @abc.abstractmethod
    def FirstTimeRead(self) -> bool:
        ...

    @FirstTimeRead.setter
    @abc.abstractmethod
    def FirstTimeRead(self, value: bool):
        ...

    def Create(self, sinFileStream: System.IO.Stream, dataGroupTable: DNV.Sesam.SifApi.Core.IDataGroupTable) -> None:
        ...

    def CreateFullIndexSetOfAddresses(self, sinFileStream: System.IO.Stream, dataGroupTable: DNV.Sesam.SifApi.Core.IDataGroupTable, numberOfAddressesToRead: int) -> System.Collections.Generic.List[int]:
        ...

    def CreateSetInsertionOrderOfNonZeroPositions(self, sinFileStream: System.IO.Stream, dataGroupTable: DNV.Sesam.SifApi.Core.IDataGroupTable, numberOfAddressesToRead: int, onFirstDim: bool = True) -> System.Collections.Generic.List[int]:
        ...

    @overload
    def CreateSetOfAddresses(self, listOfAddresses: typing.List[int], sinFileStream: System.IO.Stream, dataGroupTable: DNV.Sesam.SifApi.Core.IDataGroupTable, numberOfAddressesToRead: int, sizeToRead: typing.Optional[int], onFirstDim: bool = True) -> typing.Union[None, int]:
        ...

    @overload
    def CreateSetOfAddresses(self, sinFileStream: System.IO.Stream, dataGroupTable: DNV.Sesam.SifApi.Core.IDataGroupTable, numberOfAddressesToRead: int, onFirstDim: bool = True) -> System.Collections.Generic.List[int]:
        ...

    def CreateSetOfNonzeroAddresses(self, listOfAddresses: typing.List[int], sinFileStream: System.IO.Stream, dataGroupTable: DNV.Sesam.SifApi.Core.IDataGroupTable, numberOfAddressesToRead: int, sizeToRead: typing.Optional[int], onFirstDim: bool = True) -> typing.Union[None, int]:
        ...


class ICreateBucketIndexData(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def Name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def BucketFileAdm(self) -> DNV.Sesam.SifApi.Core.ISifBucketFileAdministrator:
        ...

    @property
    @abc.abstractmethod
    def DataGroupTableArray(self) -> DNV.Sesam.SifApi.Core.IDataGroupTableArray:
        ...

    @property
    @abc.abstractmethod
    def SetOfAddresses(self) -> typing.List[int]:
        ...

    @property
    @abc.abstractmethod
    def NumberOfAddressesRead(self) -> int:
        ...

    @NumberOfAddressesRead.setter
    @abc.abstractmethod
    def NumberOfAddressesRead(self, value: int):
        ...

    @property
    @abc.abstractmethod
    def NumberOfAddressesUsed(self) -> int:
        ...

    @NumberOfAddressesUsed.setter
    @abc.abstractmethod
    def NumberOfAddressesUsed(self, value: int):
        ...

    @property
    @abc.abstractmethod
    def Idx(self) -> int:
        ...

    @Idx.setter
    @abc.abstractmethod
    def Idx(self, value: int):
        ...

    @property
    @abc.abstractmethod
    def FirstIndexInBucket(self) -> DNV.Sesam.SifApi.Core.ISifIndex:
        ...

    @FirstIndexInBucket.setter
    @abc.abstractmethod
    def FirstIndexInBucket(self, value: DNV.Sesam.SifApi.Core.ISifIndex):
        ...

    @property
    @abc.abstractmethod
    def LastIndexInBucket(self) -> DNV.Sesam.SifApi.Core.ISifIndex:
        ...

    @LastIndexInBucket.setter
    @abc.abstractmethod
    def LastIndexInBucket(self, value: DNV.Sesam.SifApi.Core.ISifIndex):
        ...

    @property
    @abc.abstractmethod
    def NumberOfEntriesInCurrentBucket(self) -> int:
        ...

    @NumberOfEntriesInCurrentBucket.setter
    @abc.abstractmethod
    def NumberOfEntriesInCurrentBucket(self, value: int):
        ...

    @property
    @abc.abstractmethod
    def Count(self) -> int:
        ...

    @Count.setter
    @abc.abstractmethod
    def Count(self, value: int):
        ...

    @property
    @abc.abstractmethod
    def MaxFirstIndex(self) -> int:
        ...

    @MaxFirstIndex.setter
    @abc.abstractmethod
    def MaxFirstIndex(self, value: int):
        ...

    @property
    @abc.abstractmethod
    def MaxSecndIndex(self) -> int:
        ...

    @MaxSecndIndex.setter
    @abc.abstractmethod
    def MaxSecndIndex(self, value: int):
        ...

    @property
    @abc.abstractmethod
    def MaxThirdIndex(self) -> int:
        ...

    @MaxThirdIndex.setter
    @abc.abstractmethod
    def MaxThirdIndex(self, value: int):
        ...


class IDataGroupAdmin(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def DataGroupTables(self) -> System.Collections.Generic.List[System.Collections.Generic.List[DNV.Sesam.SifApi.Core.IDataGroupTable]]:
        ...

    @property
    @abc.abstractmethod
    def DataGroupTableSorted(self) -> System.Collections.Generic.SortedDictionary[str, DNV.Sesam.SifApi.Core.IDataGroupTable]:
        ...


class IUserDataTypes(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def HasUserSpecifiedDataTypes(self) -> bool:
        ...

    def IsUserSpecifiedDataType(self, name: str) -> bool:
        ...


class IPointerTableArray(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def PointerTableRecordArray(self) -> System.Collections.Generic.List[int]:
        ...


class IDataGroupReader(DNV.Sesam.SifApi.Core.IDataGroupAdmin, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def Create(self, sinFileStream: System.IO.Stream, pointerTableArrays: System.Collections.Generic.List[DNV.Sesam.SifApi.Core.IPointerTableArray], nspi: int) -> None:
        ...

    def CreateOneSorted(self, sinFileStream: System.IO.Stream, pointerTableArrays: System.Collections.Generic.List[DNV.Sesam.SifApi.Core.IPointerTableArray], nspi: int) -> None:
        ...

    def CreateSetOfOneSorted(self, sinFileStream: System.IO.Stream, pointerTableArrays: System.Collections.Generic.List[DNV.Sesam.SifApi.Core.IPointerTableArray], nspi: int) -> None:
        ...

    def GetListOfUserSpecifiedDataOrAllData(self, sinFileStream: System.IO.Stream, pointerTableArrays: System.Collections.Generic.List[DNV.Sesam.SifApi.Core.IPointerTableArray], userDataTypes: DNV.Sesam.SifApi.Core.IUserDataTypes, nspi: int) -> DNV.Sesam.SifApi.Core.CachedKeyValueSortedDictionary[str, DNV.Sesam.SifApi.Core.IDataGroupTable]:
        ...

    def GetListOfUserSpecifiedDataOrAllDataForAllSuperElements(self, sinFileStream: System.IO.Stream, superElementReferenceId: System.Collections.Generic.List[int], pointerTableArrays: System.Collections.Generic.List[DNV.Sesam.SifApi.Core.IPointerTableArray], userDataTypes: DNV.Sesam.SifApi.Core.IUserDataTypes, nspi: int) -> System.Collections.Generic.SortedDictionary[int, System.Collections.Generic.SortedDictionary[str, DNV.Sesam.SifApi.Core.IDataGroupTable]]:
        ...


class IDataGroupTableArrayAdmin(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def FirstTime(self) -> bool:
        ...

    def ListOfDataGroups(self, sinFileStream: System.IO.Stream) -> System.Collections.Generic.List[DNV.Sesam.SifApi.Core.ISifData]:
        ...

    def SetDataGroupTable(self, dataGroupTable: DNV.Sesam.SifApi.Core.IDataGroupTable) -> None:
        ...


class IExtendHeader(DNV.Sesam.SifApi.Core.IBaseHeader, metaclass=abc.ABCMeta):
    """This class has no documentation."""


class IFileNameHeader(DNV.Sesam.SifApi.Core.IBaseHeader, metaclass=abc.ABCMeta):
    """This class has no documentation."""


class IResultsHeader(DNV.Sesam.SifApi.Core.IBaseHeader, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def PointerToPointerTableForThisSuperElement(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def SuperElementReferenceForThisSuperElement(self) -> int:
        ...


class IHeaderAdmin(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def Results(self) -> System.Collections.Generic.List[DNV.Sesam.SifApi.Core.IResultsHeader]:
        ...


class IHeaderReader(DNV.Sesam.SifApi.Core.IHeaderAdmin, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def ResultsFound(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def HeaderAreaBytes(self) -> typing.List[int]:
        ...

    @property
    @abc.abstractmethod
    def HeaderAreaString(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def NSPI(self) -> int:
        ...

    def DecodeSinHeader(self, sinFileStream: System.IO.Stream) -> int:
        ...


class IHeaderWriter(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def HeaderLength(self) -> int:
        ...

    def AddDataToHeader(self, listOfHeaderData: System.Collections.Generic.List[int]) -> None:
        ...

    def Write(self, stream: System.IO.Stream) -> None:
        ...


class IHeaderData(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def SizeOfWrittenData(self) -> int:
        """Size of written data in bytes."""
        ...

    @property
    @abc.abstractmethod
    def Address(self) -> int:
        """Address to data at sin."""
        ...

    def GetHeaderData(self) -> System.Collections.Generic.List[int]:
        ...


class IIendHeader(DNV.Sesam.SifApi.Core.IBaseHeader, metaclass=abc.ABCMeta):
    """This class has no documentation."""


class IIextHeader(DNV.Sesam.SifApi.Core.IBaseHeader, metaclass=abc.ABCMeta):
    """This class has no documentation."""


class INorsamHeader(DNV.Sesam.SifApi.Core.IBaseHeader, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def NSPI(self) -> int:
        ...


class IPointerTable(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def NGFILE(self) -> int:
        """Gets the number of data groups stored on the sin-file (ngfile)."""
        ...

    @property
    @abc.abstractmethod
    def PointerToArrayOfPointers(self) -> int:
        """Gets or sets the pointer to array of pointers."""
        ...

    @PointerToArrayOfPointers.setter
    @abc.abstractmethod
    def PointerToArrayOfPointers(self, value: int):
        """Gets or sets the pointer to array of pointers."""
        ...

    @property
    @abc.abstractmethod
    def IPTAB(self) -> int:
        """Gets or sets the pointer (iptab) to the current pointer table."""
        ...

    @IPTAB.setter
    @abc.abstractmethod
    def IPTAB(self, value: int):
        """Gets or sets the pointer (iptab) to the current pointer table."""
        ...

    def Create(self, sinFileStream: System.IO.Stream, result: DNV.Sesam.SifApi.Core.IResultsHeader, nspi: int, oldPtab: bool) -> None:
        """
        Creates the pointer table (PTAB) from a sin-file.
        
        :param sinFileStream: The sin file stream.
        :param result: The result header.
        :param nspi: The number of integers per real data - make precise.
        :param oldPtab: if set to true [old ptab].
        """
        ...

    def IncrementCounts(self) -> None:
        """Increments the counts."""
        ...


class IPointerTableAdmin(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def PointerTableArrays(self) -> System.Collections.Generic.List[DNV.Sesam.SifApi.Core.IPointerTableArray]:
        ...


class IPointerTableAndArray(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def PointerTableReference(self) -> int:
        """Gets and sets the super element reference value."""
        ...

    @PointerTableReference.setter
    @abc.abstractmethod
    def PointerTableReference(self, value: int):
        """Gets and sets the super element reference value."""
        ...

    @property
    @abc.abstractmethod
    def PointerTable(self) -> DNV.Sesam.SifApi.Core.IHeaderData:
        ...

    @PointerTable.setter
    @abc.abstractmethod
    def PointerTable(self, value: DNV.Sesam.SifApi.Core.IHeaderData):
        ...

    @property
    @abc.abstractmethod
    def PointerTableArray(self) -> System.Collections.Generic.SortedDictionary[str, int]:
        ...

    @PointerTableArray.setter
    @abc.abstractmethod
    def PointerTableArray(self, value: System.Collections.Generic.SortedDictionary[str, int]):
        ...

    @property
    @abc.abstractmethod
    def DataGroupTablesDictionary(self) -> DNV.Sesam.SifApi.Core.CachedKeyValueSortedDictionary[str, DNV.Sesam.SifApi.Core.IHeaderData]:
        ...

    @DataGroupTablesDictionary.setter
    @abc.abstractmethod
    def DataGroupTablesDictionary(self, value: DNV.Sesam.SifApi.Core.CachedKeyValueSortedDictionary[str, DNV.Sesam.SifApi.Core.IHeaderData]):
        ...

    def AddToPointerTableArray(self, name: str, address: int) -> None:
        ...

    def GetByteListPointerTableArray(self) -> System.Collections.Generic.List[int]:
        ...


class IPointerTableReader(DNV.Sesam.SifApi.Core.IPointerTableAdmin, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def Create(self, sinFileStream: System.IO.Stream, results: System.Collections.Generic.List[DNV.Sesam.SifApi.Core.IResultsHeader], nspi: int, oldPtab: bool = False) -> None:
        """
        Creates the specified sin file stream.
        
        :param sinFileStream: The sin file stream.
        :param results: The results.
        :param nspi: The nspi.
        :param oldPtab: if set to true [old ptab].
        """
        ...


class IResultFileAdapter(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def DataGroupHeadAddresses(self) -> DNV.Sesam.SifApi.Core.IDataGroupReader:
        ...

    def GetDataGroupSetOfHeadAddresses(self) -> None:
        ...


class ISifReader(metaclass=abc.ABCMeta):
    """Provides a mechanism to read SIF cards."""

    @property
    @abc.abstractmethod
    def EndOfStream(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def EndOfFile(self) -> bool:
        """Gets a value indicating whether the reader has reached the end of file."""
        ...

    @property
    @abc.abstractmethod
    def Format(self) -> str:
        """Double precision formats."""
        ...

    @Format.setter
    @abc.abstractmethod
    def Format(self, value: str):
        """Double precision formats."""
        ...

    def Close(self) -> None:
        ...

    def ReadAllCards(self) -> System.Collections.Generic.List[DNV.Sesam.SifApi.Core.ISifData]:
        """Read all cards at a SIF file."""
        ...

    def ReadCard(self) -> DNV.Sesam.SifApi.Core.ISifData:
        """
        Reads the next card from the SIF file.
        
        :returns: A SifData object.
        """
        ...

    def ReadCardExtended(self) -> DNV.Sesam.SifApi.Core.ISifData:
        """
        Read a single card from the SIF file. Handles double precision sif format.
        
        :returns: Returns the SIF card or null if there are no more cards.
        """
        ...


class IResultFileReader(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def Read(self, femOnSiu: bool = False, bResultReader: bool = False) -> System.Collections.Generic.List[System.Collections.Generic.List[DNV.Sesam.SifApi.Core.ISifData]]:
        ...

    def ReadSifBasic(self, reader: DNV.Sesam.SifApi.Core.ISifReader) -> System.Collections.Generic.List[System.Collections.Generic.List[DNV.Sesam.SifApi.Core.ISifData]]:
        ...


class IScratchHeader(DNV.Sesam.SifApi.Core.IBaseHeader, metaclass=abc.ABCMeta):
    """This class has no documentation."""


class ISesamCoreName(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def Name(self) -> str:
        """Gets the name of the Sesam data type."""
        ...


class ISesamCoreSerialize(DNV.Sesam.SifApi.Core.ISesamCoreName, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def Nfield(self) -> int:
        """Gets or sets length of the data type (including Nfield)."""
        ...

    def GetLfData(self) -> typing.List[float]:
        """
        Gets the data array which is the data serialized according to the specification of the data type in the Sif Manuals,
        except that the first item in the array is always "Nfield", i.e. the length of the array including "Nfield".
        For length first data types, this method and "GetSifDataArray()" return the same array. I.e. with Nfield as the first item.
        """
        ...

    def SetData(self, data: typing.List[float]) -> None:
        """
        Sets a data array which is not headed by its length.
        The array will be shifted one step to the right and then the length will be added as the first item.
        
        :param data: The data.
        """
        ...

    def SetLfData(self, data: typing.List[float]) -> None:
        """
        Sets the data array which is the data serialized according to the specification of the data type in the Sif Manuals,
        except that the first item in the array is always "Nfield", i.e. the length of the array including "Nfield".
        
        :param data: The data.
        """
        ...


class ISifBucketHandler(System.IDisposable, metaclass=abc.ABCMeta):
    """Supersedes cref="DNV.Sesam.SifApi.Core.ISifBucketFileAdministrator"."""

    def Add(self, dataTypeName: str, sifIndex: DNV.Sesam.SifApi.Core.ISifIndex) -> None:
        ...

    def Close(self) -> None:
        """Close/Dispose the resources used by the component."""
        ...


class ISifBucketHandlerData(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def SortedBucketData(self) -> System.Collections.Generic.SortedDictionary[DNV.Sesam.SifApi.Core.ISifIndex, DNV.Sesam.SifApi.Core.ISifBucketDefinition]:
        ...

    @property
    @abc.abstractmethod
    def PositionAtFile(self) -> int:
        ...

    @PositionAtFile.setter
    @abc.abstractmethod
    def PositionAtFile(self, value: int):
        ...


class ISifDataReader(System.IDisposable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def Close(self) -> None:
        """Closes this instance."""
        ...

    def CreateModel(self) -> int:
        """
        Create the direct access data model. This method must be called before data can be read from the model.
        
        :returns: = -3: IDENT data type is corrupt. = -2: Cannot start application. = -1: Input file not found. =  0: OK. =  1: Super element model. =  2: Error in the model creation process. =  3: The SIN file is empty or is not valid.
        """
        ...

    def GetCount(self, name: str) -> int:
        """
        Gets the number of occurrences of a data type.
        
        :param name: Name of the data type.
        :returns: The number of occurrences of the data type.
        """
        ...

    def GetTabDimensions(self, name: str) -> typing.List[int]:
        """
        Get the size of the established pointer table for a datatype
        
        :param name: The name of the data type.
        :returns: Array with elements holding the size of the pointer table in each pointer table dimension. The length of the array (number of dimensions) is equal to the number of SIF indices for the given datatype.
        """
        ...

    def GetToc(self) -> System.Collections.Generic.SortedDictionary[str, DNV.Sesam.SifApi.Core.ITableOfContents[int]]:
        """Gets the table of contents of the model."""
        ...

    @overload
    def ReadAll(self, name: str, blockSize: int, noMoreData: typing.Optional[bool]) -> typing.Union[System.Collections.Generic.List[DNV.Sesam.SifApi.Core.ISifData], bool]:
        """
        Reads all data of the specified data type.
        
        :param name: Name of the data type.
        :param blockSize: Number of data arrays to read.
        :param noMoreData: True if there is no more data to retrieve in a subsequent invocation.
        :returns: List of retrieved data.
        """
        ...

    @overload
    def ReadAll(self, name: str, blockSize: typing.Optional[int]=10000) -> System.Collections.Generic.List[DNV.Sesam.SifApi.Core.ISifData]:
        """
        Reads all data of the specified data type. Will also call SetFirstTimeReadAll.

        :param name: Name of the data type.
        :param blockSize: Number of data arrays to read. Default 10 000. May be changed manually for performance reasons
        :returns: List of retrieved data.
        """
        ...

    def ReadData(self, name: str, id: typing.List[int]) -> System.Collections.Generic.List[DNV.Sesam.SifApi.Core.ISifData]:
        """
        Reads all data for a given data type name and id.
        
        :param name: Name of the data type.
        :param id: The id of data to read.
        :returns: List of retrieved data.
        """
        ...

    def ReadExt(self, name: str, id: typing.List[int]) -> typing.List[float]:
        """
        Reads all data for a given data type name and id.
        
        :param name: Name of the data type.
        :param id: The data id.
        :returns: A double array containing the read data. If multiple data arrays are associated with the id all are returned according to the following schema:
        [ NumberOfDataArrays | LengtOfDataArray_1 | d_(1,1) | d_(1,2) | ... | ... | LengtOfDataArray_(2) | d_(2,1) | d_(2,2) | ... | ... | LengtOfDataArray_NumberOfDataArrays |d_(NumberOfDataArrays,1) | d_(NumberOfDataArrays,2) | ... | ... | ]
        where d_i is a single data array. This is similar to ReadData except that it returns a generic data type useful by C++ for instance.
        """
        ...

    @overload
    def ReadText(self, name: str, id: typing.List[int], text: typing.Optional[str]) -> typing.Union[bool, str]:
        """
        Reads text data.
        
        :param name: Name of the text data type.
        :param id: The data id.
        :param text: The read text data.
        :returns: A text string.
        """
        ...

    @overload
    def ReadText(self, name: str, id: typing.List[int]) -> System.Collections.Generic.List[DNV.Sesam.SifApi.Core.ISifData]:
        """
        Reads text data.
        
        :param name: Name of the the text data type.
        :param id: The data id.
        :returns: List of data. More than one dataset if multiple data arrays exist for the id.
        """
        ...

    def SetFirstTimeReadAll(self, name: str) -> None:
        """
        Must be called prior to a sequence of calls to ReadAll for a data type in order to reset internal pointers.
        
        :param name: Name of the data type.
        """
        ...

    def WriteToc(self, streamWriter: System.IO.StreamWriter) -> None:
        """
        Writes the table of contents to a StreamWriter.
        
        :param streamWriter: The StreamWriter on which to write the table of contents.
        """
        ...


class ISifDataWriter(System.IDisposable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def Close(self) -> None:
        """Close the writer."""
        ...

    def CreateTab(self, name: str, maxIds: typing.List[int], maxNumberOfArrays: int = ...) -> bool:
        """
        For indexed data types: Sets the maximum id for a data type in each dimension relevant for the data type. For non-indexed data types: allocates space for a specified number of data arrays.
        
        :param name: The name of the data type.
        :param maxIds: The maximum data id for each dimension. This is only used for indexed SIF data types.
        :param maxNumberOfArrays: Assumed number of entries to be added. This is used only for non-indexed SIF data types.
        :returns: true.
        """
        ...

    def GetTabDimensions(self, name: str) -> typing.List[int]:
        """
        Get the size of the established pointer table for a datatype
        
        :param name: The name of the data type.
        :returns: Array with elements holding the size of the pointer table in each pointer table dimension. The length of the array (number of dimensions) is equal to the number of SIF indices for the given datatype.
        """
        ...

    @overload
    def Write(self, name: str, data: typing.List[float], appendDataLength: bool) -> bool:
        """
        Write non-text data.
        
        :param name: The name of the data type.
        :param data: The numeric data.
        :param appendDataLength: Must be set to true iff sifVal[] does not hold the length of the data.
        :returns: true.
        """
        ...

    @overload
    def Write(self, name: str, data: typing.List[float]) -> bool:
        """
        Write non-text data.
        
        :param name: The name of the data type.
        :param data: The numeric data. sifVal[0] must equal the length of the data (including data[0]), also for data types not defined with the data length as the first element.
        :returns: true.
        """
        ...

    def WriteData(self, name: str, listOfData: System.Collections.Generic.List[DNV.Sesam.SifApi.Core.ISifData]) -> bool:
        """
        Writes a list of data. The data must be headed by the data length, also for data types not defined with the data length as the first element.
        
        :param name: The name of the data type.
        :param listOfData: The list of data to write.
        """
        ...

    def WriteDate(self, programName: str, programVersion: str, programReleaseDate: str) -> bool:
        """
        Write the data type DATE for an actual program, application or service.
        
        :param programName: The program, application or service name.
        :param programVersion: The program, application or service version.
        :param programReleaseDate: The program, application or service release date.
        :returns: true.
        """
        ...

    @overload
    def WriteSifFile(self, filename: str) -> bool:
        """
        Export data to a SIF file.
        
        :param filename: The name of the SIF file.
        :returns: true.
        """
        ...

    @overload
    def WriteSifFile(self, sifDataReader: ISifDataReader, filename: str, blockSize: int = 10000) -> bool:
        """
        Writes the sif file.

        :param sifDataReader: The sif data reader.
        :param filename: The full filename. I.e., includes the path.
        :param blockSize: The largest number of data sets read for a data type. Defaults to 10000.
        :returns: True if the file was successfully written without exceptions and model errors.
        """
        ...

    def WriteText(self, name: str, id: int, sifText: System.Collections.Generic.List[str]) -> bool:
        """
        Write text data.
        
        :param name: The name of the data type.
        :param id: The id of the data.
        :param sifText: List of text strings to write.
        :returns: true.
        """
        ...


class ISifModelReader(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def SinFileStream(self) -> System.IO.Stream:
        ...

    @property
    @abc.abstractmethod
    def EndOfFile(self) -> bool:
        ...

    def Close(self) -> None:
        ...

    def ReadCard(self) -> DNV.Sesam.SifApi.Core.ISifData:
        ...


class ISifModelBuilder(System.IDisposable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def Close(self) -> None:
        ...

    def CreateModel(self, reader: DNV.Sesam.SifApi.Core.ISifModelReader) -> int:
        """
        Create the direct access sif data model.
        
        :param reader: The stream that holds the sif data to be processed.
        :returns: = -3: IDENT data type is corrupt. = -2: Cannot start application. = -1: Input file not found. =  0: OK. =  1: Super element model. =  2: Some error in the model creation process. =  3: If the incoming sin file is empty or likely is not a valid input file.
        """
        ...


class ISifModelFileAdministrator(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def Close(self) -> None:
        ...

    def CreateModel(self, reader: DNV.Sesam.SifApi.Core.ISifModelReader, oldPtab: bool = False) -> int:
        """
        Create the direct access sif data model.
        
        :param reader: The stream that holds the sif data to be processed.
        :returns: = -3: IDENT data type is corrupt. = -2: Cannot start application. = -1: Input file not found. =  0: OK. =  1: Super element model. =  2: Some error in the model creation process. =  3: If the incoming sin file is empty or likely is not a valid input file.
        """
        ...

    def ReadAll(self, cardName: str, indexType: DNV.Sesam.SifApi.Core.SifIndexType, blockSize: int, noMoreData: typing.Optional[bool]) -> typing.Union[System.Collections.Generic.List[DNV.Sesam.SifApi.Core.ISifData], bool]:
        """"""
        ...

    def ReadCard(self, cardName: str, id: typing.List[int], indexType: DNV.Sesam.SifApi.Core.SifIndexType) -> System.Collections.Generic.List[DNV.Sesam.SifApi.Core.ISifData]:
        """"""
        ...

    def ReadExt(self, cardName: str, id: typing.List[int], indexType: DNV.Sesam.SifApi.Core.SifIndexType) -> typing.List[float]:
        """"""
        ...

    @overload
    def ReadText(self, cardName: str, id: typing.List[int], indexType: DNV.Sesam.SifApi.Core.SifIndexType, text: typing.Optional[str]) -> typing.Union[bool, str]:
        ...

    @overload
    def ReadText(self, cardName: str, id: typing.List[int]) -> System.Collections.Generic.List[DNV.Sesam.SifApi.Core.ISifData]:
        """"""
        ...

    def SetFirstTimeReadAll(self, cardName: str) -> None:
        ...


class ISifResultModelFileAdministrator(DNV.Sesam.SifApi.Core.ISifModelFileAdministrator, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def AddDataType(self, dataTypeName: str, hierarchyRef: int, id: DNV.Sesam.SifApi.Core.ISifIndex, data: typing.List[float]) -> None:
        """For data with one index where data types are ordered according to index at the SIF formatted input file."""
        ...

    def AddDataTypeForLinkedDataWithRepeatedIndex(self, dataTypeName: str, hierarchyRef: int, id: DNV.Sesam.SifApi.Core.ISifIndex, data: typing.List[float]) -> None:
        """"""
        ...

    def AddDataTypeForOneBucketOnly(self, dataTypeName: str, hierarchyRef: int, id: DNV.Sesam.SifApi.Core.ISifIndex, data: typing.List[float]) -> None:
        """
        For data where data types are NOT ordered according to index at the SIF formatted input file.
        Denne er ikke nødvendig når bucket-strukturen settes opp på forhånd - derfor ToDo: Refactor.
        """
        ...

    def Complete(self) -> None:
        """"""
        ...

    def GetBucketFileAdministrator(self, dataTypeName: str) -> DNV.Sesam.SifApi.Core.ISifBucketFileAdministrator:
        """"""
        ...


class ISifResultWriter(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def FlushAndClose(self) -> None:
        ...

    @overload
    def WriteCard(self, sifData: DNV.Sesam.SifApi.Core.ISifData) -> None:
        ...

    @overload
    def WriteCard(self, id: str, values: System.Collections.Generic.IEnumerable[float]) -> None:
        ...

    @overload
    def WriteCard(self, id: str, values: System.Collections.Generic.IEnumerable[float]) -> None:
        ...

    def WriteIend(self, continuation: int = 0) -> None:
        ...


class ISifWriter(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def Close(self) -> None:
        ...

    def Flush(self) -> None:
        ...

    @overload
    def WriteCard(self, card: DNV.Sesam.SifApi.Core.ISifData, skipFirstEntry: bool = False) -> None:
        ...

    @overload
    def WriteCard(self, id: str, values: System.Collections.Generic.IEnumerable[float], skipFirstEntry: bool = False) -> None:
        ...

    @overload
    def WriteCard(self, id: str, values: System.Collections.Generic.IEnumerable[float], skipFirstEntry: bool = False) -> None:
        ...

    @overload
    def WriteCard(self, id: str, values: typing.List[float], skipFirstEntry: bool = False) -> None:
        ...

    @overload
    def WriteCard(self, id: str, values: typing.List[float], skipFirstEntry: bool = False) -> None:
        ...

    def WriteIend(self, continuation: int = 0) -> None:
        ...

    def WriteMatrix(self, nRows: int, nCols: int, *values: float) -> None:
        ...

    @overload
    def WriteSinCard(self, id: str, textData: System.Collections.Generic.List[str], data: System.Collections.Generic.List[float], writeFirst: bool = True) -> None:
        ...

    @overload
    def WriteSinCard(self, id: str, data: System.Collections.Generic.List[float], writeFirst: bool = True) -> None:
        ...

    def WriteTextCard(self, id: str, text: System.Collections.Generic.List[str], values: typing.List[float], skipFirstEntry: bool = False) -> None:
        ...


class ISinDataTypeWriter(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @overload
    def Write(self, address: int, data: System.Collections.Generic.List[int]) -> None:
        ...

    @overload
    def Write(self, addressList: System.Collections.Generic.IEnumerable[System.ValueTuple[int, typing.List[int]]]) -> None:
        ...

    @overload
    def Write(self, address: int, listOfData: System.Collections.Generic.List[System.Collections.Generic.List[int]]) -> None:
        ...

    @overload
    def Write(self, address: int, listOfData: System.Collections.Generic.List[typing.List[int]]) -> None:
        ...

    @overload
    def Write(self, address: int, data: typing.List[int]) -> None:
        ...

    @overload
    def Write(self, address: int, data: typing.List[int], prevAddress: typing.Optional[typing.List[int]]) -> typing.Union[None, typing.List[int]]:
        ...


class ISinHeaderAccess(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def MRC(self) -> int:
        """Highest address in the Norsam addressable interface file containing valid data."""
        ...

    @MRC.setter
    @abc.abstractmethod
    def MRC(self, value: int):
        """Highest address in the Norsam addressable interface file containing valid data."""
        ...

    @property
    @abc.abstractmethod
    def HighestAddressInFileContainingValidData(self) -> int:
        """Highest address in the Norsam addressable interface file containing valid data -- the byte address."""
        ...

    @HighestAddressInFileContainingValidData.setter
    @abc.abstractmethod
    def HighestAddressInFileContainingValidData(self, value: int):
        """Highest address in the Norsam addressable interface file containing valid data -- the byte address."""
        ...

    def GetIpFile(self, iref: int) -> int:
        """
        Address to pointer table (PTAB) section for this super element.
        
        :param iref: This super element
        :returns: Address to pointer table (PTAB) section.
        """
        ...

    def SetIpFile(self, iref: int, ipfile: int) -> None:
        """
        Address to pointer table (PTAB) section for this super element.
        
        :param iref: This super element
        """
        ...


class ISinSuperElementModelAdministrator(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def SuperElementReferences(self) -> System.Collections.Generic.List[int]:
        ...

    @property
    @abc.abstractmethod
    def DataGroupTablesForAllSuperElements(self) -> System.Collections.Generic.SortedDictionary[int, System.Collections.Generic.SortedDictionary[str, DNV.Sesam.SifApi.Core.IDataGroupTable]]:
        ...

    def GetDataGroupTablesForASuperElement(self, superElementReference: int) -> System.Collections.Generic.SortedDictionary[str, DNV.Sesam.SifApi.Core.IDataGroupTable]:
        ...


class ISinWriter(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def FileStream(self) -> System.IO.Stream:
        ...

    @property
    @abc.abstractmethod
    def FileName(self) -> str:
        ...

    @FileName.setter
    @abc.abstractmethod
    def FileName(self, value: str):
        ...

    def AddDataTypeDimension(self, iref: int, name: str, count: int, firstDimension: int, secndDimension: int, thirdDimension: int, standardUsage: bool) -> None:
        ...

    @overload
    def BuildHeader(self) -> None:
        """Builds the header area of the sin-file."""
        ...

    @overload
    def BuildHeader(self, superElementReference: int) -> None:
        """
        Builds the header area of the sin-file.
        
        :param superElementReference: Reference to super element to create header space for.
        """
        ...

    def Close(self) -> None:
        ...

    def GetDataTypeDimension(self, iref: int, name: str) -> typing.List[int]:
        ...

    def WriteDataGroupTables(self) -> None:
        ...

    def WriteDataType(self, iref: int, name: str, sifVal: typing.List[float], shiftRight: bool) -> None:
        """
        Write a non-text data type.
        
        :param iref: Super element reference id.
        :param name: The name of the data type.
        :param sifVal: The data of the data type.
        :param shiftRight: The first entry of the data the data type must be the length of the data, if not shift right and add the entry.
        """
        ...

    def WriteDataTypes(self, model: DNV.Sesam.SifApi.Core.ISifDataReader) -> None:
        """Planned for use in Sestra, not yet used. Update text SinWriter and in ISinWriter.cs."""
        ...

    def WriteHeader(self) -> None:
        ...

    def WriteListOfDataTypes(self, iref: int, name: str, listOfData: System.Collections.Generic.List[DNV.Sesam.SifApi.Core.ISifData]) -> None:
        """
        Write a set of data types.
        
        :param iref: Super element reference id.
        :param name: The name of the data type.
        :param listOfData: The data on ISifData format.
        """
        ...

    def WritePointerTable(self) -> None:
        """Write pointer tables for ISifFileAdaptive."""
        ...

    def WritePointerTableAll(self) -> None:
        """Write pointer tables when files are converted to sin - files in one go."""
        ...

    def WriteSifFile(self, iref: int, filename: str) -> bool:
        """
        Writes the sif file.
        
        :param iref: Super element reference id.
        :param filename: The filename.
        """
        ...

    def WriteTdText(self, iref: int, name: str, dataTypeIndex: int, sifText: System.Collections.Generic.List[str]) -> None:
        """
        Write a TD-text data type.
        
        :param iref: Super element reference id.
        :param name: The name of the data type.
        :param dataTypeIndex: The index of the data type.
        :param sifText: The list of text-strings.
        """
        ...

    def WriteTextDate(self, iref: int, name: str, dataTypeIndex: int, sifText: System.Collections.Generic.List[str]) -> None:
        """
        Write a DATE or TEXT text data type.
        
        :param iref: Super element reference id.
        :param name: The name of the data type.
        :param dataTypeIndex: The index of the data type.
        :param sifText: The list of text-strings.
        """
        ...


class SifIndexRepeatCode(System.Enum):
    """This class has no documentation."""

    Unique = 0

    Repeated = 1

    Unknown = 2


class IWindExtensionCore(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def GetRvfatdam(self) -> System.Collections.Generic.Dictionary[DNV.Sesam.SifApi.Core.ComparablePair[int], typing.List[float]]:
        """
        Retrieve from the SIFTool data base all RVFATDAM entries on pair element number and load case.
        
        :returns: A dictionary where the key is an element number and load case pair and the value is the associated data hold as a double array.
        """
        ...

    def GetTdfatdam(self) -> System.Collections.Generic.Dictionary[int, System.Collections.Generic.List[str]]:
        """
        Retrieve from the SIFTool data base all TDFATDAM entries on element number.
        
        :returns: A dictionary where the key is an element number and the value is the associated data hold as a list of strings.
        """
        ...


class Matrix:
    """This class has no documentation."""

    @property
    def Id(self) -> int:
        ...

    @property
    def ColumnMajorOrder(self) -> bool:
        ...

    @property
    def T(self) -> typing.List[float]:
        ...

    def __init__(self, id: int, t: typing.List[float], columnMajorOrder: bool) -> None:
        ...


class MatrixData:
    """This class has no documentation."""

    @property
    def NumberOfEntries(self) -> int:
        ...

    @property
    def M11(self) -> float:
        ...

    @property
    def M21(self) -> float:
        ...

    @property
    def M31(self) -> float:
        ...

    @property
    def M12(self) -> float:
        ...

    @property
    def M22(self) -> float:
        ...

    @property
    def M32(self) -> float:
        ...

    @property
    def M13(self) -> float:
        ...

    @property
    def M23(self) -> float:
        ...

    @property
    def M33(self) -> float:
        ...

    def __init__(self, mat: typing.List[float], numberOfEntries: int = 9) -> None:
        ...


class VectorData:
    """This class has no documentation."""

    @property
    def NumberOfEntries(self) -> int:
        ...

    @property
    def V1(self) -> float:
        ...

    @property
    def V2(self) -> float:
        ...

    @property
    def V3(self) -> float:
        ...

    @overload
    def __init__(self, v1: float, v2: float, v3: float, numberOfEntries: int = 3) -> None:
        ...

    @overload
    def __init__(self, vec: typing.List[float], numberOfEntries: int = 3) -> None:
        ...


class MatVecOps(System.Object):
    """
    Library for small matrices and vector multiplications.
    In addition, some typical operations are added.
    Uses unrolled loops up to some matrix - vector order.
    """

    @staticmethod
    @overload
    def CrossProduct(vec1: typing.List[float], vec2: typing.List[float]) -> typing.List[float]:
        ...

    @staticmethod
    @overload
    def CrossProduct(vec1: typing.List[float], vec2: typing.List[float], result: typing.List[float]) -> None:
        ...

    @staticmethod
    @overload
    def CrossProduct(vec1Index: int, vec2Index: int, vec3Index: int, vec: typing.List[float]) -> None:
        ...

    @staticmethod
    def FillDirectionVectors(DirectionVectorsIn: System.Collections.Generic.List[typing.List[float]], DirectionVectorsOut: typing.List[float], numberOfPrincipalStresses: int) -> None:
        ...

    @staticmethod
    def FillPrincipalStresses(PrincipalStressesIn: System.Collections.Generic.List[float], PrincipalStressesOut: typing.List[float], numberOfPrincipalStresses: int) -> None:
        ...

    @staticmethod
    def Length(vec: typing.List[float]) -> float:
        ...

    @staticmethod
    @overload
    def LengthVec(vec: typing.List[float], vecLength: int) -> float:
        ...

    @staticmethod
    @overload
    def LengthVec(vec: typing.List[float], vecIndex: int, vecLength: int) -> float:
        ...

    @staticmethod
    def MatrixMultiply(N: int, A: typing.List[float], B: typing.List[float]) -> typing.List[float]:
        ...

    @staticmethod
    def MatrixMultiply_N5(A: typing.List[float], B: typing.List[float]) -> typing.List[float]:
        ...

    @staticmethod
    def MatrixMultiplyPrePostSpecial(A: typing.List[float], B: typing.List[float]) -> typing.List[float]:
        ...

    @staticmethod
    def MatrixMultiplyPrePostSpecial_BSym(A: typing.List[float], B: typing.List[float]) -> typing.List[float]:
        ...

    @staticmethod
    def MatrixMultiplyPrePostTrans(N: int, A: typing.List[float], B: typing.List[float]) -> typing.List[float]:
        ...

    @staticmethod
    def MatrixMultiplyPreTransPost(N: int, A: typing.List[float], B: typing.List[float]) -> typing.List[float]:
        ...

    @staticmethod
    def MatrixMultiplyTransA(N: int, A: typing.List[float], B: typing.List[float]) -> typing.List[float]:
        ...

    @staticmethod
    def MatrixMultiplyTransA_N5(A: typing.List[float], B: typing.List[float]) -> typing.List[float]:
        ...

    @staticmethod
    def MatrixMultiplyTransA_N5_BSym(A: typing.List[float], B: typing.List[float]) -> typing.List[float]:
        ...

    @staticmethod
    def MatrixMultiplyTransB(N: int, A: typing.List[float], B: typing.List[float]) -> typing.List[float]:
        ...

    @staticmethod
    def MatrixVectorMultiply(N: int, A: typing.List[float], b: typing.List[float]) -> typing.List[float]:
        ...

    @staticmethod
    @overload
    def MatrixVectorMultiplyTransA(N: int, A: typing.List[float], b: typing.List[float], c: typing.List[float]) -> None:
        ...

    @staticmethod
    @overload
    def MatrixVectorMultiplyTransA(N: int, A: typing.List[float], b: typing.List[float]) -> typing.List[float]:
        ...

    @staticmethod
    @overload
    def Normalize(vec: typing.List[float], result: typing.List[float]) -> None:
        ...

    @staticmethod
    @overload
    def Normalize(vec: typing.List[float]) -> typing.List[float]:
        ...

    @staticmethod
    def NormalizeVecData(vec: typing.List[float], vecLength: int) -> DNV.Sesam.SifApi.Core.VectorData:
        ...

    @staticmethod
    @overload
    def ScalarProduct(vec1: typing.List[float], vec1Index: int, vec2: typing.List[float], vec2Index: int, vectorLength: int) -> float:
        ...

    @staticmethod
    @overload
    def ScalarProduct(vectors: typing.List[float], vec1Index: int, vec2Index: int, vectorLength: int) -> float:
        ...

    @staticmethod
    @overload
    def ScalarProduct(vec1: typing.List[float], vec2: typing.List[float]) -> float:
        ...


class Pair(typing.Generic[DNV_Sesam_SifApi_Core_Pair_TU, DNV_Sesam_SifApi_Core_Pair_TV]):
    """This class has no documentation."""

    @property
    def A(self) -> DNV_Sesam_SifApi_Core_Pair_T:
        ...

    @property
    def B(self) -> DNV_Sesam_SifApi_Core_Pair_T:
        ...

    @overload
    def __init__(self, entryA: DNV_Sesam_SifApi_Core_Pair_T, entryB: DNV_Sesam_SifApi_Core_Pair_T) -> None:
        ...

    @overload
    def __init__(self, entryA: DNV_Sesam_SifApi_Core_Pair_TU, entryB: DNV_Sesam_SifApi_Core_Pair_TV) -> None:
        ...


class PairList(typing.Generic[DNV_Sesam_SifApi_Core_PairList_T]):
    """This class has no documentation."""

    @property
    def ListA(self) -> typing.List[DNV_Sesam_SifApi_Core_PairList_T]:
        ...

    @property
    def ListB(self) -> typing.List[DNV_Sesam_SifApi_Core_PairList_T]:
        ...

    @ListB.setter
    def ListB(self, value: typing.List[DNV_Sesam_SifApi_Core_PairList_T]):
        ...

    @property
    def IsListBSet(self) -> bool:
        ...

    @IsListBSet.setter
    def IsListBSet(self, value: bool):
        ...

    @overload
    def __init__(self, listA: typing.List[DNV_Sesam_SifApi_Core_PairList_T]) -> None:
        ...

    @overload
    def __init__(self, listA: typing.List[DNV_Sesam_SifApi_Core_PairList_T], listB: typing.List[DNV_Sesam_SifApi_Core_PairList_T]) -> None:
        ...

    def SetListB(self, list: typing.List[DNV_Sesam_SifApi_Core_PairList_T]) -> None:
        ...


class PairListHelper(System.Object):
    """This class has no documentation."""

    @staticmethod
    def Compare(expected: System.Collections.Generic.List[DNV.Sesam.SifApi.Core.PairList[float]], actual: System.Collections.Generic.List[DNV.Sesam.SifApi.Core.PairList[float]]) -> bool:
        """
        For unit tests - Compares two lists of pair lists.
        
        :param expected: The expected list of pair lists.
        :param actual: The actual list of pair lists.
        :returns: true if the lists of pair lists are equal.
        """
        ...


class PointAlgorithms(System.Object):
    """This class has no documentation."""

    @staticmethod
    def CheckForNaNAndInfinityOnPoint(point: DNV.Sesam.SifApi.Core.Point) -> None:
        ...

    @staticmethod
    def CompareTwoPoints(vec1: DNV.Sesam.SifApi.Core.Point, vec2: DNV.Sesam.SifApi.Core.Point, delta: float) -> bool:
        ...

    @staticmethod
    @overload
    def CrossProduct(vec1: DNV.Sesam.SifApi.Core.Point, vec2: DNV.Sesam.SifApi.Core.Point, result: DNV.Sesam.SifApi.Core.Point) -> None:
        ...

    @staticmethod
    @overload
    def CrossProduct(vec1: DNV.Sesam.SifApi.Core.Point, vec2: DNV.Sesam.SifApi.Core.Point) -> DNV.Sesam.SifApi.Core.Point:
        ...

    @staticmethod
    def DirectionCosines(startPoint: DNV.Sesam.SifApi.Core.Point, endPoint: DNV.Sesam.SifApi.Core.Point) -> typing.List[float]:
        ...

    @staticmethod
    def DirectionCosinesVec(startPoint: DNV.Sesam.SifApi.Core.Point, endPoint: DNV.Sesam.SifApi.Core.Point) -> DNV.Sesam.SifApi.Core.VectorData:
        ...

    @staticmethod
    @overload
    def DotProduct(vec1: DNV.Sesam.SifApi.Core.Point, vec2: DNV.Sesam.SifApi.Core.Point) -> float:
        ...

    @staticmethod
    @overload
    def DotProduct(vec1: DNV.Sesam.SifApi.Core.Point, vec2: typing.List[float]) -> float:
        ...

    @staticmethod
    def GetNormalizedVector(node1: DNV.Sesam.SifApi.Core.Point, node2: DNV.Sesam.SifApi.Core.Point) -> DNV.Sesam.SifApi.Core.Point:
        ...

    @staticmethod
    def GetVector(node1: DNV.Sesam.SifApi.Core.Point, node2: DNV.Sesam.SifApi.Core.Point) -> DNV.Sesam.SifApi.Core.Point:
        ...

    @staticmethod
    @overload
    def Length(vec: DNV.Sesam.SifApi.Core.Point) -> float:
        ...

    @staticmethod
    @overload
    def Length(startPoint: DNV.Sesam.SifApi.Core.Point, endPoint: DNV.Sesam.SifApi.Core.Point) -> float:
        ...

    @staticmethod
    def Normalize(vec: DNV.Sesam.SifApi.Core.Point) -> DNV.Sesam.SifApi.Core.Point:
        ...

    @staticmethod
    @overload
    def TransformPoint(point: DNV.Sesam.SifApi.Core.Point, T: typing.List[float], result: DNV.Sesam.SifApi.Core.Point, scratch1: typing.List[float], scratch2: typing.List[float]) -> None:
        ...

    @staticmethod
    @overload
    def TransformPoint(point: DNV.Sesam.SifApi.Core.Point, T: typing.List[float]) -> DNV.Sesam.SifApi.Core.Point:
        ...

    @staticmethod
    @overload
    def TransformPoint(pointCoordinates: typing.List[float], T: typing.List[float], result: typing.List[float]) -> None:
        ...

    @staticmethod
    @overload
    def TransformPoint(pointCoordinates: typing.List[float], T: typing.List[float]) -> typing.List[float]:
        ...

    @staticmethod
    def XDirection(startPoint: DNV.Sesam.SifApi.Core.Point, endPoint: DNV.Sesam.SifApi.Core.Point) -> float:
        ...

    @staticmethod
    def XLength(startPoint: DNV.Sesam.SifApi.Core.Point, endPoint: DNV.Sesam.SifApi.Core.Point) -> float:
        ...

    @staticmethod
    def YDirection(startPoint: DNV.Sesam.SifApi.Core.Point, endPoint: DNV.Sesam.SifApi.Core.Point) -> float:
        ...

    @staticmethod
    def YLength(startPoint: DNV.Sesam.SifApi.Core.Point, endPoint: DNV.Sesam.SifApi.Core.Point) -> float:
        ...

    @staticmethod
    def ZDirection(startPoint: DNV.Sesam.SifApi.Core.Point, endPoint: DNV.Sesam.SifApi.Core.Point) -> float:
        ...

    @staticmethod
    def ZLength(startPoint: DNV.Sesam.SifApi.Core.Point, endPoint: DNV.Sesam.SifApi.Core.Point) -> float:
        ...


class SesamCoreAggregatedDataException(System.Exception):
    """This class has no documentation."""

    def __init__(self, message: str, inner: System.Exception) -> None:
        ...


class SesamCoreDegeneratedDataException(System.Exception):
    """This class has no documentation."""

    def __init__(self, message: str) -> None:
        ...


class SetInsertionOrder(typing.Generic[DNV_Sesam_SifApi_Core_SetInsertionOrder_T], System.Object, System.Collections.Generic.ICollection[DNV_Sesam_SifApi_Core_SetInsertionOrder_T], typing.Iterable[DNV_Sesam_SifApi_Core_SetInsertionOrder_T]):
    """This class has no documentation."""

    @property
    def Count(self) -> int:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, comparer: System.Collections.Generic.IEqualityComparer[DNV_Sesam_SifApi_Core_SetInsertionOrder_T]) -> None:
        ...

    @overload
    def Add(self, item: DNV_Sesam_SifApi_Core_SetInsertionOrder_T) -> None:
        ...

    @overload
    def Add(self, item: DNV_Sesam_SifApi_Core_SetInsertionOrder_T) -> bool:
        ...

    def Clear(self) -> None:
        ...

    def Contains(self, item: DNV_Sesam_SifApi_Core_SetInsertionOrder_T) -> bool:
        ...

    def CopyTo(self, array: typing.List[DNV_Sesam_SifApi_Core_SetInsertionOrder_T], arrayIndex: int) -> None:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[DNV_Sesam_SifApi_Core_SetInsertionOrder_T]:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        ...

    def Remove(self, item: DNV_Sesam_SifApi_Core_SetInsertionOrder_T) -> bool:
        ...


class SifIndex(System.Object, DNV.Sesam.SifApi.Core.ISifIndex, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def FirstIndex(self) -> int:
        ...

    @FirstIndex.setter
    def FirstIndex(self, value: int):
        ...

    @property
    def SecndIndex(self) -> int:
        ...

    @SecndIndex.setter
    def SecndIndex(self, value: int):
        ...

    @property
    def ThirdIndex(self) -> int:
        ...

    @ThirdIndex.setter
    def ThirdIndex(self, value: int):
        ...

    def __init__(self, first: int = ..., secnd: int = ..., third: int = ...) -> None:
        """This method is protected."""
        ...

    def CompareIndexAndReturnTrueIfOtherIsBigger(self, other: DNV.Sesam.SifApi.Core.ISifIndex, swapFirstAndSecondIndex: bool = False) -> bool:
        ...

    def CompareIndicesAndUpdateThisIfOtherIsBigger(self, other: DNV.Sesam.SifApi.Core.ISifIndex, swapFirstAndSecondIndex: bool = False) -> None:
        ...

    @overload
    def CompareTo(self, other: DNV.Sesam.SifApi.Core.ISifIndex) -> int:
        ...

    @staticmethod
    @overload
    def CompareTo(firstIndex: int, otherFirstIndex: int) -> int:
        """This method is protected."""
        ...

    def CompareTwoIndices(self, other: DNV.Sesam.SifApi.Core.ISifIndex) -> int:
        ...

    def Equals(self, other: DNV.Sesam.SifApi.Core.ISifIndex) -> bool:
        ...

    def GetAsBytes(self) -> typing.List[int]:
        ...

    def GetHashCode(self) -> int:
        ...

    def GetNextIndex(self, binaryBucketReader: System.IO.BinaryReader) -> DNV.Sesam.SifApi.Core.ISifIndex:
        ...

    def NoIndex(self) -> bool:
        ...

    def ReadIndexAndCompare(self, binaryBucketReader: System.IO.BinaryReader) -> bool:
        ...

    def SetNoIndex(self) -> DNV.Sesam.SifApi.Core.ISifIndex:
        ...

    def SizeOfIndexPackage(self) -> int:
        ...

    def SizeOfIndices(self) -> int:
        ...

    def ToString(self) -> str:
        ...

    def WriteIndex(self, binaryBucketWriter: System.IO.BinaryWriter) -> None:
        ...


class SifIndexOne(DNV.Sesam.SifApi.Core.SifIndex, System.IComparable):
    """This class has no documentation."""

    def __init__(self, first: int) -> None:
        ...

    @overload
    def CompareTo(self, other: DNV.Sesam.SifApi.Core.SifIndexOne) -> int:
        ...

    @overload
    def CompareTo(self, obj: typing.Any) -> int:
        ...

    def CompareTwoIndices(self, other: DNV.Sesam.SifApi.Core.ISifIndex) -> int:
        ...

    def GetAsBytes(self) -> typing.List[int]:
        ...

    def GetNextIndex(self, binaryBucketReader: System.IO.BinaryReader) -> DNV.Sesam.SifApi.Core.ISifIndex:
        ...

    def NoIndex(self) -> bool:
        ...

    def ReadIndexAndCompare(self, binaryBucketReader: System.IO.BinaryReader) -> bool:
        ...

    def SetNoIndex(self) -> DNV.Sesam.SifApi.Core.ISifIndex:
        ...

    def SizeOfIndexPackage(self) -> int:
        ...

    def SizeOfIndices(self) -> int:
        ...

    def ToString(self) -> str:
        ...

    def WriteIndex(self, binaryBucketWriter: System.IO.BinaryWriter) -> None:
        ...


class SifIndexTwo(DNV.Sesam.SifApi.Core.SifIndex, System.IComparable):
    """This class has no documentation."""

    def __init__(self, first: int, secnd: int) -> None:
        ...

    @overload
    def CompareTo(self, other: DNV.Sesam.SifApi.Core.ISifIndex) -> int:
        ...

    @overload
    def CompareTo(self, obj: typing.Any) -> int:
        ...

    def CompareTwoIndices(self, other: DNV.Sesam.SifApi.Core.ISifIndex) -> int:
        ...

    def Equals(self, other: DNV.Sesam.SifApi.Core.ISifIndex) -> bool:
        ...

    def GetAsBytes(self) -> typing.List[int]:
        ...

    def GetNextIndex(self, binaryBucketReader: System.IO.BinaryReader) -> DNV.Sesam.SifApi.Core.ISifIndex:
        ...

    def NoIndex(self) -> bool:
        ...

    def ReadIndexAndCompare(self, binaryBucketReader: System.IO.BinaryReader) -> bool:
        ...

    def SetNoIndex(self) -> DNV.Sesam.SifApi.Core.ISifIndex:
        ...

    def SizeOfIndexPackage(self) -> int:
        ...

    def SizeOfIndices(self) -> int:
        ...

    def ToString(self) -> str:
        ...

    def WriteIndex(self, binaryBucketWriter: System.IO.BinaryWriter) -> None:
        ...


class SifIndexThree(DNV.Sesam.SifApi.Core.SifIndex, System.IComparable):
    """This class has no documentation."""

    def __init__(self, first: int, secnd: int, third: int) -> None:
        ...

    def CompareIndexAndReturnTrueIfOtherIsBigger(self, other: DNV.Sesam.SifApi.Core.ISifIndex, swapFirstAndSecondIndex: bool = False) -> bool:
        ...

    def CompareIndicesAndUpdateThisIfOtherIsBigger(self, other: DNV.Sesam.SifApi.Core.ISifIndex, swapFirstAndSecondIndex: bool = False) -> None:
        ...

    def CompareTo(self, obj: typing.Any) -> int:
        ...

    def CompareTwoIndices(self, other: DNV.Sesam.SifApi.Core.ISifIndex) -> int:
        ...

    def GetAsBytes(self) -> typing.List[int]:
        ...

    def GetNextIndex(self, binaryBucketReader: System.IO.BinaryReader) -> DNV.Sesam.SifApi.Core.ISifIndex:
        ...

    def NoIndex(self) -> bool:
        ...

    def ReadIndexAndCompare(self, binaryBucketReader: System.IO.BinaryReader) -> bool:
        ...

    def SetNoIndex(self) -> DNV.Sesam.SifApi.Core.ISifIndex:
        ...

    def SizeOfIndexPackage(self) -> int:
        ...

    def SizeOfIndices(self) -> int:
        ...

    def ToString(self) -> str:
        ...

    def WriteIndex(self, binaryBucketWriter: System.IO.BinaryWriter) -> None:
        ...


class SifIndexCode(System.Object):
    """This class has no documentation."""

    @staticmethod
    def GetIndexCode(sifIndex: DNV.Sesam.SifApi.Core.ISifIndex, indexCodeDivisor: int = 128) -> DNV.Sesam.SifApi.Core.ISifIndex:
        ...

    @staticmethod
    def GetIndexCodeForBuckets(sifIndex: DNV.Sesam.SifApi.Core.ISifIndex, indexCodeDivisor: int = 128) -> DNV.Sesam.SifApi.Core.ISifIndex:
        ...

    @staticmethod
    def GetIndexNumber(sifIndex: DNV.Sesam.SifApi.Core.ISifIndex, indexCodeDivisor: int = 128) -> int:
        ...


class SifIndexFactory(System.Object):
    """This class has no documentation."""

    @staticmethod
    @overload
    def Create(validIndices: typing.List[int]) -> DNV.Sesam.SifApi.Core.ISifIndex:
        ...

    @staticmethod
    @overload
    def Create(i: int) -> DNV.Sesam.SifApi.Core.ISifIndex:
        ...

    @staticmethod
    @overload
    def Create(i: int, j: int) -> DNV.Sesam.SifApi.Core.ISifIndex:
        ...

    @staticmethod
    @overload
    def Create(i: int, j: int, k: int) -> DNV.Sesam.SifApi.Core.ISifIndex:
        ...

    @staticmethod
    def CreateMinimalType(i: int, j: int, k: int) -> DNV.Sesam.SifApi.Core.ISifIndex:
        ...


class TransformationMatrix:
    """This class has no documentation."""

    @property
    def Transpose(self) -> typing.List[float]:
        ...

    @property
    def Id(self) -> int:
        ...

    @property
    def ColumnMajorOrder(self) -> bool:
        ...

    @property
    def T(self) -> typing.List[float]:
        ...

    def __init__(self, id: int, t: typing.List[float], columnMajorOrder: bool = True) -> None:
        ...