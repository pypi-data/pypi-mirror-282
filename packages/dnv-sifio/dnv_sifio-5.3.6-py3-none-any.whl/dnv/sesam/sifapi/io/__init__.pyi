from typing import overload
import abc
import typing

import DNV.Sesam.SifApi.Core
import DNV.Sesam.SifApi.IO
import System

DNV_Sesam_SifApi_IO_MemoryManager_T = typing.TypeVar("DNV_Sesam_SifApi_IO_MemoryManager_T")


class IHiddenInformation(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def GetMessage(self) -> str:
        ...


class MemoryManager(typing.Generic[DNV_Sesam_SifApi_IO_MemoryManager_T], System.Object):
    """This class has no documentation."""

    @property
    def Buffer(self) -> typing.List[DNV_Sesam_SifApi_IO_MemoryManager_T]:
        ...

    @Buffer.setter
    def Buffer(self, value: typing.List[DNV_Sesam_SifApi_IO_MemoryManager_T]):
        ...

    def Create(self, lengthOfBuffer: int) -> None:
        ...


class CreateNewWriterArgs:
    """This class has no documentation."""

    @property
    def fileName(self) -> System.IntPtr:
        ...

    @fileName.setter
    def fileName(self, value: System.IntPtr):
        ...


class CreateNewArgs:
    """This class has no documentation."""

    @property
    def userFolder(self) -> System.IntPtr:
        ...

    @userFolder.setter
    def userFolder(self, value: System.IntPtr):
        ...

    @property
    def modelName(self) -> System.IntPtr:
        ...

    @modelName.setter
    def modelName(self, value: System.IntPtr):
        ...


class GetTabDimensionArgs:
    """This class has no documentation."""

    @property
    def id(self) -> int:
        ...

    @id.setter
    def id(self, value: int):
        ...

    @property
    def cardName(self) -> System.IntPtr:
        ...

    @cardName.setter
    def cardName(self, value: System.IntPtr):
        ...

    @property
    def tabDim(self) -> System.IntPtr:
        ...

    @tabDim.setter
    def tabDim(self, value: System.IntPtr):
        ...


class CreateTabArgs:
    """This class has no documentation."""

    @property
    def id(self) -> int:
        ...

    @id.setter
    def id(self, value: int):
        ...

    @property
    def cardName(self) -> System.IntPtr:
        ...

    @cardName.setter
    def cardName(self, value: System.IntPtr):
        ...

    @property
    def tabDim(self) -> System.IntPtr:
        ...

    @tabDim.setter
    def tabDim(self, value: System.IntPtr):
        ...

    @property
    def lengthOfTabDim(self) -> int:
        ...

    @lengthOfTabDim.setter
    def lengthOfTabDim(self, value: int):
        ...


class GetCountArgs:
    """This class has no documentation."""

    @property
    def id(self) -> int:
        ...

    @id.setter
    def id(self, value: int):
        ...

    @property
    def cardName(self) -> System.IntPtr:
        ...

    @cardName.setter
    def cardName(self, value: System.IntPtr):
        ...


class ReadTextVectorArgs:
    """This class has no documentation."""

    @property
    def id(self) -> int:
        ...

    @id.setter
    def id(self, value: int):
        ...

    @property
    def cardName(self) -> System.IntPtr:
        ...

    @cardName.setter
    def cardName(self, value: System.IntPtr):
        ...

    @property
    def sifRef(self) -> int:
        ...

    @sifRef.setter
    def sifRef(self, value: int):
        ...

    @property
    def numberOfLinesInEachCard(self) -> System.IntPtr:
        ...

    @numberOfLinesInEachCard.setter
    def numberOfLinesInEachCard(self, value: System.IntPtr):
        ...


class ReadExtArgs:
    """This class has no documentation."""

    @property
    def id(self) -> int:
        ...

    @id.setter
    def id(self, value: int):
        ...

    @property
    def cardName(self) -> System.IntPtr:
        ...

    @cardName.setter
    def cardName(self, value: System.IntPtr):
        ...

    @property
    def sifRef(self) -> System.IntPtr:
        ...

    @sifRef.setter
    def sifRef(self, value: System.IntPtr):
        ...

    @property
    def lengthOfSifRef(self) -> int:
        ...

    @lengthOfSifRef.setter
    def lengthOfSifRef(self, value: int):
        ...


class ReadAllArgs:
    """This class has no documentation."""

    @property
    def id(self) -> int:
        ...

    @id.setter
    def id(self, value: int):
        ...

    @property
    def cardName(self) -> System.IntPtr:
        ...

    @cardName.setter
    def cardName(self, value: System.IntPtr):
        ...

    @property
    def blocksize(self) -> int:
        ...

    @blocksize.setter
    def blocksize(self, value: int):
        ...

    @property
    def noMoreData(self) -> System.IntPtr:
        ...

    @noMoreData.setter
    def noMoreData(self, value: System.IntPtr):
        ...


class WriteArgs:
    """This class has no documentation."""

    @property
    def id(self) -> int:
        ...

    @id.setter
    def id(self, value: int):
        ...

    @property
    def cardName(self) -> System.IntPtr:
        ...

    @cardName.setter
    def cardName(self, value: System.IntPtr):
        ...

    @property
    def data(self) -> System.IntPtr:
        ...

    @data.setter
    def data(self, value: System.IntPtr):
        ...

    @property
    def lengthOfData(self) -> int:
        ...

    @lengthOfData.setter
    def lengthOfData(self, value: int):
        ...


class WriteTextArgs:
    """This class has no documentation."""

    @property
    def id(self) -> int:
        ...

    @id.setter
    def id(self, value: int):
        ...

    @property
    def cardName(self) -> System.IntPtr:
        ...

    @cardName.setter
    def cardName(self, value: System.IntPtr):
        ...

    @property
    def sifRef(self) -> int:
        ...

    @sifRef.setter
    def sifRef(self, value: int):
        ...

    @property
    def textData(self) -> System.IntPtr:
        ...

    @textData.setter
    def textData(self, value: System.IntPtr):
        ...


class WriteDateArgs:
    """This class has no documentation."""

    @property
    def id(self) -> int:
        ...

    @id.setter
    def id(self, value: int):
        ...

    @property
    def programName(self) -> System.IntPtr:
        ...

    @programName.setter
    def programName(self, value: System.IntPtr):
        ...

    @property
    def programVersion(self) -> System.IntPtr:
        ...

    @programVersion.setter
    def programVersion(self, value: System.IntPtr):
        ...

    @property
    def programReleaseDate(self) -> System.IntPtr:
        ...

    @programReleaseDate.setter
    def programReleaseDate(self, value: System.IntPtr):
        ...


class SesamDataAdminCommon(System.Object):
    """This class has no documentation."""

    @staticmethod
    def HandleError(message: str, errFun: System.IntPtr) -> None:
        ...

    @staticmethod
    def InvokeFunctionA(func: System.IntPtr, param1: int) -> System.IntPtr:
        ...

    @staticmethod
    def InvokeFunctionB(func: System.IntPtr, param1: int, param2: int) -> System.IntPtr:
        ...

    @staticmethod
    def InvokeFunctionC(func: System.IntPtr, param1: int, param2: int, param3: int, param4: int) -> System.IntPtr:
        ...


class SesamDataAdminInput(System.Object):
    """This class has no documentation."""

    @staticmethod
    def CloseEntryPoint(args: int, errorFun: System.IntPtr) -> int:
        ...

    def CloseEntryPointDelegate(self, args: int, errorFun: System.IntPtr) -> int:
        ...

    @staticmethod
    def CreateModelEntryPoint(args: int, errorFun: System.IntPtr) -> int:
        ...

    def CreateModelEntryPointDelegate(self, args: int, errorFun: System.IntPtr) -> int:
        ...

    @staticmethod
    def CreateNewEntryPoint(args: DNV.Sesam.SifApi.IO.CreateNewArgs, errorFun: System.IntPtr) -> int:
        ...

    def CreateNewEntryPointDelegate(self, args: DNV.Sesam.SifApi.IO.CreateNewArgs, errorFun: System.IntPtr) -> int:
        ...

    @staticmethod
    def DestroyEntryPoint(id: int) -> bool:
        ...

    def DestroyEntryPointDelegate(self, id: int) -> bool:
        ...

    @staticmethod
    def GetCountEntryPoint(args: DNV.Sesam.SifApi.IO.GetCountArgs, errorFun: System.IntPtr) -> int:
        ...

    def GetCountEntryPointDelegate(self, args: DNV.Sesam.SifApi.IO.GetCountArgs, errorFun: System.IntPtr) -> int:
        ...

    @staticmethod
    def GetTabDimensionEntryPoint(args: DNV.Sesam.SifApi.IO.GetTabDimensionArgs, errorFun: System.IntPtr) -> int:
        ...

    def GetTabDimensionEntryPointDelegate(self, args: DNV.Sesam.SifApi.IO.GetTabDimensionArgs, errorFun: System.IntPtr) -> int:
        ...

    @staticmethod
    def GetTocEntryPoint(id: int, tocFun: System.IntPtr, errorFun: System.IntPtr) -> int:
        ...

    def GetTocEntryPointDelegate(self, id: int, tocFun: System.IntPtr, errorFun: System.IntPtr) -> int:
        ...

    @staticmethod
    def ReadAllEntryPoint(args: DNV.Sesam.SifApi.IO.ReadAllArgs, allocationFun: System.IntPtr, errorFun: System.IntPtr) -> None:
        ...

    def ReadAllEntryPointDelegate(self, args: DNV.Sesam.SifApi.IO.ReadAllArgs, allocationFun: System.IntPtr, errorFun: System.IntPtr) -> None:
        ...

    @staticmethod
    def ReadExtEntryPoint(args: DNV.Sesam.SifApi.IO.ReadExtArgs, allocationFun: System.IntPtr, errorFun: System.IntPtr) -> int:
        ...

    def ReadExtEntryPointDelegate(self, args: DNV.Sesam.SifApi.IO.ReadExtArgs, allocationFun: System.IntPtr, errorFun: System.IntPtr) -> int:
        ...

    @staticmethod
    def ReadTextEntryPoint(args: DNV.Sesam.SifApi.IO.ReadExtArgs, allocationFun: System.IntPtr, errorFun: System.IntPtr) -> bool:
        ...

    def ReadTextEntryPointDelegate(self, args: DNV.Sesam.SifApi.IO.ReadExtArgs, allocationFun: System.IntPtr, errorFun: System.IntPtr) -> bool:
        ...

    @staticmethod
    def ReadTextVectorEntryPoint(args: DNV.Sesam.SifApi.IO.ReadTextVectorArgs, allocationFun: System.IntPtr, allocationFun2: System.IntPtr, errorFun: System.IntPtr) -> bool:
        ...

    def ReadTextVectorEntryPointDelegate(self, args: DNV.Sesam.SifApi.IO.ReadTextVectorArgs, allocationFun: System.IntPtr, allocationFun2: System.IntPtr, errorFun: System.IntPtr) -> bool:
        ...

    @staticmethod
    def SetFirstTimeReadAllEntryPoint(args: DNV.Sesam.SifApi.IO.GetCountArgs, errorFun: System.IntPtr) -> None:
        ...

    def SetFirstTimeReadAllEntryPointDelegate(self, args: DNV.Sesam.SifApi.IO.GetCountArgs, errorFun: System.IntPtr) -> None:
        ...


class SesamDataAdminOutput(System.Object):
    """This class has no documentation."""

    @staticmethod
    def CloseEntryPoint(args: int, errFun: System.IntPtr) -> int:
        ...

    def CloseEntryPointDelegate(self, args: int, errFun: System.IntPtr) -> int:
        ...

    @staticmethod
    def CreateNewEntryPoint(args: DNV.Sesam.SifApi.IO.CreateNewWriterArgs, errFun: System.IntPtr) -> int:
        ...

    def CreateNewEntryPointDelegate(self, args: DNV.Sesam.SifApi.IO.CreateNewWriterArgs, errFun: System.IntPtr) -> int:
        ...

    @staticmethod
    def CreateTabEntryPoint(args: DNV.Sesam.SifApi.IO.CreateTabArgs, errFun: System.IntPtr) -> int:
        ...

    def CreateTabEntryPointDelegate(self, args: DNV.Sesam.SifApi.IO.CreateTabArgs, errFun: System.IntPtr) -> int:
        ...

    @staticmethod
    def DestroyEntryPoint(id: int) -> bool:
        ...

    def DestroyEntryPointDelegate(self, id: int) -> bool:
        ...

    @staticmethod
    def GetTabDimensionEntryPoint(args: DNV.Sesam.SifApi.IO.GetTabDimensionArgs, errFun: System.IntPtr) -> int:
        ...

    def GetTabDimensionEntryPointDelegate(self, args: DNV.Sesam.SifApi.IO.GetTabDimensionArgs, errFun: System.IntPtr) -> int:
        ...

    @staticmethod
    def WriteDateEntryPoint(args: DNV.Sesam.SifApi.IO.WriteDateArgs, errFun: System.IntPtr) -> int:
        ...

    def WriteDateEntryPointDelegate(self, args: DNV.Sesam.SifApi.IO.WriteDateArgs, errFun: System.IntPtr) -> int:
        ...

    @staticmethod
    def WriteDateOrTextEntryPoint(args: DNV.Sesam.SifApi.IO.WriteTextArgs, charFun: System.IntPtr, errFun: System.IntPtr) -> int:
        ...

    def WriteDateOrTextEntryPointDelegate(self, args: DNV.Sesam.SifApi.IO.WriteTextArgs, charFun: System.IntPtr, errFun: System.IntPtr) -> int:
        ...

    @staticmethod
    def WriteEntryPoint(args: DNV.Sesam.SifApi.IO.WriteArgs, errFun: System.IntPtr) -> int:
        ...

    def WriteEntryPointDelegate(self, args: DNV.Sesam.SifApi.IO.WriteArgs, errFun: System.IntPtr) -> int:
        ...

    @staticmethod
    def WriteSIFFileEntryPoint(args: DNV.Sesam.SifApi.IO.GetCountArgs, errFun: System.IntPtr) -> int:
        ...

    def WriteSIFFileEntryPointDelegate(self, args: DNV.Sesam.SifApi.IO.GetCountArgs, errFun: System.IntPtr) -> int:
        ...

    @staticmethod
    def WriteTextEntryPoint(args: DNV.Sesam.SifApi.IO.WriteTextArgs, errFun: System.IntPtr) -> int:
        ...

    def WriteTextEntryPointDelegate(self, args: DNV.Sesam.SifApi.IO.WriteTextArgs, errFun: System.IntPtr) -> int:
        ...


class SesamDataFactory(System.Object):
    """This class has no documentation."""

    @overload
    @staticmethod
    def CreateReader(modelName: str) -> DNV.Sesam.SifApi.Core.ISifDataReader:
        """
        Creates a new instance of an ISifDataReader, used to read data from SIN, SIF, or FEM-files.
        
        :param modelName: Filename of the SIN, SIF or FEM-file to be imported. Relative or absolute path is accepted.
        :returns: A new instance of ISifDataReader.
        """
        ...

    @overload
    @staticmethod
    def CreateReader(userTempFolder: str, modelName: str) -> DNV.Sesam.SifApi.Core.ISifDataReader:
        """
        Creates a new instance of an ISifDataReader, used to read data from SIN, SIF, or FEM-files.
        
        :param userTempFolder: User-defined folder for temporary data
        :param modelName: Filename of the SIN, SIF or FEM-file to be imported. Relative or absolute path is accepted.
        :returns: A new instance of ISifDataReader.
        """
        ...

    @staticmethod
    def CreateWriter(sinFileName: str) -> DNV.Sesam.SifApi.Core.ISifDataWriter:
        """
        Creates a new instance of an ISifDataWriter, used to write SIN or SIF files.
        
        :param sinFileName: Filename of the SIN file to be created. Relative or absolute path is accepted.
        :returns: A new instance of ISifDataWriter.
        """
        ...
