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

class IKnownIssueWarningInfo:
    '''Represents a warning about known issue which won't be fixed in the near future.'''
    def send_warning(self, receiver: IWarningCallback) -> None:
        ...

    @property
    def as_i_warning_info(self) -> IWarningInfo:
        ...

    @property
    def warning_type(self) -> WarningType:
        ...

    @property
    def description(self) -> str:
        ...

    ...

class INotImplementedWarningInfo:
    '''Represents a warning about known not implemented feature which won't be implemented in the near future.'''
    def send_warning(self, receiver: IWarningCallback) -> None:
        ...

    @property
    def as_i_warning_info(self) -> IWarningInfo:
        ...

    @property
    def warning_type(self) -> WarningType:
        ...

    @property
    def description(self) -> str:
        ...

    ...

class IObsoletePresLockingBehaviorWarningInfo:
    '''This warning indicates that an obsolete presentation locking behavior is used.'''
    def send_warning(self, receiver: IWarningCallback) -> None:
        ...

    @property
    def as_i_warning_info(self) -> IWarningInfo:
        ...

    @property
    def warning_type(self) -> WarningType:
        ...

    @property
    def description(self) -> str:
        ...

    ...

class IPresentationSignedWarningInfo:
    '''This warning indicates that the presentation being read has the signature 
                and this signature will be removed during processing.'''
    def send_warning(self, receiver: IWarningCallback) -> None:
        ...

    @property
    def as_i_warning_info(self) -> IWarningInfo:
        ...

    @property
    def warning_type(self) -> WarningType:
        ...

    @property
    def description(self) -> str:
        ...

    ...

class IWarningCallback:
    '''Interface for classes which receive warning'''
    def warning(self, warning: IWarningInfo) -> ReturnAction:
        '''Callback method which receives warning and decides whether operation should be aborted.
        :param warning: Warning to process.
        :returns: Abortion decision :py:enum:`aspose.slides.warnings.ReturnAction`.'''
        ...

    ...

class IWarningInfo:
    '''Represents a base interface for all warnings.'''
    def send_warning(self, receiver: IWarningCallback) -> None:
        '''If receiver is not null ends warning to a specified receiver and throws the 
                    AbortRequestedException if receiver decided to abort a operation.
        :param receiver: Receiver object :py:class:`aspose.slides.warnings.IWarningCallback`'''
        ...

    @property
    def warning_type(self) -> WarningType:
        ...

    @property
    def description(self) -> str:
        '''Returns a human readable description of this warning.
                    Read-only :py:class:`str`.'''
        ...

    ...

class ReturnAction:
    '''Represents warning callback decision options.'''
    @classmethod
    @property
    def CONTINUE(cls) -> ReturnAction:
        '''Operation should be continued.'''
        ...

    @classmethod
    @property
    def ABORT(cls) -> ReturnAction:
        '''Operation should be aborted.'''
        ...

    ...

class WarningType:
    '''Represents a type of warning.'''
    @classmethod
    @property
    def SOURCE_FILE_CORRUPTION(cls) -> WarningType:
        '''An issue has been detected in the source document which makes it very likely the document will be not be able to be opened if saved in it's original format.'''
        ...

    @classmethod
    @property
    def DATA_LOSS(cls) -> WarningType:
        '''Text/chart/image or other data will be completely missing from either the documet tree following load, or the created document following save.'''
        ...

    @classmethod
    @property
    def MAJOR_FORMATTING_LOSS(cls) -> WarningType:
        '''Major formatting loss.'''
        ...

    @classmethod
    @property
    def MINOR_FORMATTING_LOSS(cls) -> WarningType:
        '''Minor formatting loss.'''
        ...

    @classmethod
    @property
    def COMPATIBILITY_ISSUE(cls) -> WarningType:
        '''This is known issue that will prevent the document being opened by certain user agents, or previous versions of user agents.'''
        ...

    @classmethod
    @property
    def UNEXPECTED_CONTENT(cls) -> WarningType:
        '''Some content in the source document could not be recognised (i.e. is unsupported), this may or may not cause issues or result in data/formatting loss.'''
        ...

    ...

