from typing import List, Optional, Dict, Iterable
import aspose.pycore
import aspose.pydrawing
import aspose.slides
import aspose.slides.animation
import aspose.slides.charts
import aspose.slides.dom.ole
import aspose.slides.effects
import aspose.slides.export
import aspose.slides.export.web
import aspose.slides.export.xaml
import aspose.slides.importing
import aspose.slides.ink
import aspose.slides.lowcode
import aspose.slides.mathtext
import aspose.slides.slideshow
import aspose.slides.smartart
import aspose.slides.spreadsheet
import aspose.slides.theme
import aspose.slides.util
import aspose.slides.vba
import aspose.slides.warnings

class IVbaModule:
    '''Represents module that is contained in VBA project.'''
    @property
    def name(self) -> str:
        '''Name of the module.
                    Read-only :py:class:`str`.'''
        ...

    @property
    def source_code(self) -> str:
        ...

    @source_code.setter
    def source_code(self, value: str):
        ...

    ...

class IVbaModuleCollection:
    '''Represents a collection of a VBA Project modules.'''
    def add_empty_module(self, name: str) -> IVbaModule:
        '''Adds a new empty module to the VBA Project.
        :param name: Name of the module
        :returns: Added module.'''
        ...

    def remove(self, value: IVbaModule) -> None:
        '''Removes the first occurrence of a specific object from the collection.
        :param value: The module to remove from the collection.'''
        ...

    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IVbaModule
        ...

    ...

class IVbaProject:
    '''Represents VBA project with presentation macros.'''
    def to_binary(self) -> bytes:
        '''Returns the binary representation of the VBA project as OLE container.
                    Read-only :py:class:`int`[].
        :returns: Binary representation of the VBA project as OLE container'''
        ...

    @property
    def name(self) -> str:
        '''Returns the name of the VBA project.
                    Read-only :py:class:`str`.'''
        ...

    @property
    def modules(self) -> IVbaModuleCollection:
        '''Returns the list of all modules that are contained in the VBA project.
                    Read-only :py:class:`aspose.slides.vba.IVbaModuleCollection`.'''
        ...

    @property
    def references(self) -> IVbaReferenceCollection:
        '''Returns the list of all references that are contained in the VBA project.
                    Read-only :py:class:`aspose.slides.vba.IVbaReferenceCollection`.'''
        ...

    @property
    def is_password_protected(self) -> bool:
        ...

    ...

class IVbaProjectFactory:
    '''Allows to create VBA project via COM interface'''
    def create_vba_project(self) -> IVbaProject:
        '''Creates new VBA project.
        :returns: New VBA project'''
        ...

    def read_vba_project(self, data: bytes) -> IVbaProject:
        '''Reads VBA project from OLE container.
        :param data: Ole data :py:class:`int`[]
        :returns: Read VBA project'''
        ...

    ...

class IVbaReference:
    '''Represents the name of the VBA project reference.'''
    @property
    def name(self) -> str:
        '''Represents the name of the VBA project reference.
                    Read/write :py:class:`str`.'''
        ...

    @name.setter
    def name(self, value: str):
        '''Represents the name of the VBA project reference.
                    Read/write :py:class:`str`.'''
        ...

    ...

class IVbaReferenceCollection:
    '''Represents a collection of a VBA Project references.'''
    def add(self, value: IVbaReference) -> None:
        '''Adds the new reference to references collection
        :param value: VBA project reference :py:class:`aspose.slides.vba.IVbaReference`'''
        ...

    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IVbaReference
        ...

    ...

class IVbaReferenceFactory:
    '''Allows to create VBA project references via COM interface'''
    def create_ole_type_lib_reference(self, name: str, libid: str) -> IVbaReferenceOleTypeLib:
        '''Creates new OLE Automation type library reference.
        :param name: Name of the VBA project reference :py:class:`str`
        :param libid: Identifier of an Automation type library :py:class:`str`
        :returns: New OLE Automation type library reference :py:class:`aspose.slides.vba.IVbaReferenceOleTypeLib`'''
        ...

    ...

class IVbaReferenceOleTwiddledTypeLib:
    '''Represents modified OLE Automation type library reference in which 
                all controls are marked as extensible.'''
    @property
    def as_i_vba_reference(self) -> IVbaReference:
        ...

    @property
    def name(self) -> str:
        ...

    @name.setter
    def name(self, value: str):
        ...

    ...

class IVbaReferenceOleTypeLib:
    '''Represents OLE Automation type library reference.'''
    @property
    def libid(self) -> str:
        '''Represents the identifier of an Automation type library.
                    Read/write :py:class:`str`.'''
        ...

    @libid.setter
    def libid(self, value: str):
        '''Represents the identifier of an Automation type library.
                    Read/write :py:class:`str`.'''
        ...

    @property
    def as_i_vba_reference(self) -> IVbaReference:
        ...

    @property
    def name(self) -> str:
        ...

    @name.setter
    def name(self, value: str):
        ...

    ...

class IVbaReferenceProject:
    '''Represents reference to an external VBA project.'''
    @property
    def as_i_vba_reference(self) -> IVbaReference:
        ...

    @property
    def name(self) -> str:
        ...

    @name.setter
    def name(self, value: str):
        ...

    ...

class VbaModule:
    '''Represents module that is contained in VBA project.'''
    @property
    def name(self) -> str:
        '''Gets the name of the module.
                    Read-only :py:class:`str`.'''
        ...

    @property
    def source_code(self) -> str:
        ...

    @source_code.setter
    def source_code(self, value: str):
        ...

    ...

class VbaModuleCollection:
    '''Represents a collection of a VBA Project modules.'''
    def remove(self, value: IVbaModule) -> None:
        '''Removes the first occurrence of a specific object from the collection.
        :param value: The module to remove from the collection.'''
        ...

    def add_empty_module(self, name: str) -> IVbaModule:
        '''Adds a new empty module to the VBA Project.
        :param name: Name of the module
        :returns: Added module.'''
        ...

    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IVbaModule
        ...

    ...

class VbaProject:
    '''Represents VBA project with presentation macros.'''
    def __init__(self):
        '''This constructor creates new VBA project from scratch.
                    Project will be created in 1252 Windows Latin 1 (ANSI) codepage'''
        ...

    def __init__(self, data: bytes):
        '''This constructor loads VBA project from binary representation of OLE container.'''
        ...

    def to_binary(self) -> bytes:
        '''Returns the binary representation of the VBA project as OLE container
        :returns: Binary representation of the VBA project as OLE container'''
        ...

    @property
    def name(self) -> str:
        '''Returns the name of the VBA project.
                    Read-only :py:class:`str`.'''
        ...

    @property
    def modules(self) -> IVbaModuleCollection:
        '''Returns the list of all modules that are contained in the VBA project.
                    Read-only :py:class:`aspose.slides.vba.IVbaModuleCollection`.'''
        ...

    @property
    def references(self) -> IVbaReferenceCollection:
        '''Returns the list of all references that are contained in the VBA project.
                    Read-only :py:class:`aspose.slides.vba.IVbaReferenceCollection`.'''
        ...

    @property
    def is_password_protected(self) -> bool:
        ...

    ...

class VbaProjectFactory:
    '''Allows to create VBA project via COM interface'''
    def __init__(self):
        ...

    def create_vba_project(self) -> IVbaProject:
        '''Creates new VBA project.
        :returns: New VBA project'''
        ...

    def read_vba_project(self, data: bytes) -> IVbaProject:
        '''Reads VBA project from OLE container.
        :returns: Read VBA project'''
        ...

    @classmethod
    @property
    def instance(cls) -> VbaProjectFactory:
        '''VBA project factory static instance.
                    Read-only :py:class:`aspose.slides.vba.VbaProjectFactory`.'''
        ...

    ...

class VbaReferenceCollection:
    '''Represents a collection of a VBA Project references.'''
    def add(self, value: IVbaReference) -> None:
        '''Adds the new reference to references collection'''
        ...

    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IVbaReference
        ...

    ...

class VbaReferenceFactory:
    '''Allows to create VBA project references via COM interface'''
    def __init__(self):
        ...

    def create_ole_type_lib_reference(self, name: str, libid: str) -> IVbaReferenceOleTypeLib:
        '''Creates new OLE Automation type library reference.
        :returns: New OLE Automation type library reference'''
        ...

    @classmethod
    @property
    def instance(cls) -> VbaReferenceFactory:
        '''VBA project references factory static instance.
                    Read-only :py:class:`aspose.slides.vba.VbaReferenceFactory`.'''
        ...

    ...

class VbaReferenceOleTypeLib:
    '''Represents OLE Automation type library reference.'''
    def __init__(self, name: str, libid: str):
        '''This constructor creates new OLE Automation type library reference.'''
        ...

    @property
    def name(self) -> str:
        '''Represents the name of the VBA project reference.
                    Read/write :py:class:`str`.'''
        ...

    @name.setter
    def name(self, value: str):
        '''Represents the name of the VBA project reference.
                    Read/write :py:class:`str`.'''
        ...

    @property
    def libid(self) -> str:
        '''Represents the identifier of an Automation type library.
                    Read/write :py:class:`str`.'''
        ...

    @libid.setter
    def libid(self, value: str):
        '''Represents the identifier of an Automation type library.
                    Read/write :py:class:`str`.'''
        ...

    @property
    def as_i_vba_reference(self) -> IVbaReference:
        ...

    ...

