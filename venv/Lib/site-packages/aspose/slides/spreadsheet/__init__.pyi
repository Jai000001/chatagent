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

class CellCircularReferenceException(aspose.slides.PptxEditException):
    '''The exception that is thrown when one or more circular references are detected where a formula refers to its
                own cell either directly or indirectly.'''
    def __init__(self):
        '''Initializes a new instance of the :py:class:`aspose.slides.spreadsheet.CellCircularReferenceException` class.'''
        ...

    def __init__(self, message: str):
        '''Initializes a new instance of the :py:class:`aspose.slides.spreadsheet.CellCircularReferenceException` class with a specified error message.
        :param message: A string that describes the error.'''
        ...

    def __init__(self, message: str, reference: str):
        '''Initializes a new instance of the :py:class:`aspose.slides.spreadsheet.CellCircularReferenceException` class with a specified error message
                    and circular cell reference.
        :param message: A string that describes the error.
        :param reference: A circular cell reference.'''
        ...

    @property
    def reference(self) -> str:
        '''Gets a circular cell reference.'''
        ...

    ...

class CellInvalidFormulaException(aspose.slides.PptxEditException):
    '''The exception that is thrown when a calculated formula is not correct or was not parsed.'''
    def __init__(self):
        '''Initializes a new instance of the :py:class:`aspose.slides.spreadsheet.CellInvalidFormulaException` class.'''
        ...

    def __init__(self, message: str):
        '''Initializes a new instance of the :py:class:`aspose.slides.spreadsheet.CellInvalidFormulaException` class with a specified error message.
        :param message: A string that describes the error.'''
        ...

    def __init__(self, message: str, reference: str):
        '''Initializes a new instance of the :py:class:`aspose.slides.spreadsheet.CellInvalidFormulaException` class with a specified error message
                    and a cell reference that contains the invalid formula.'''
        ...

    @property
    def reference(self) -> str:
        '''Gets a cell reference that contains the invalid formula.'''
        ...

    ...

class CellInvalidReferenceException(aspose.slides.PptxEditException):
    '''The exception that is thrown when an invalid cell reference is encountered.'''
    def __init__(self):
        '''Initializes a new instance of the :py:class:`aspose.slides.spreadsheet.CellInvalidReferenceException` class.'''
        ...

    def __init__(self, message: str):
        '''Initializes a new instance of the :py:class:`aspose.slides.spreadsheet.CellInvalidReferenceException` class with a specified error message.
        :param message: A string that describes the error.'''
        ...

    def __init__(self, message: str, reference: str):
        '''Initializes a new instance of the :py:class:`aspose.slides.spreadsheet.CellCircularReferenceException` class with a specified error message
                    and an invalid cell reference.
        :param message: A string that describes the error.
        :param reference: An invalid cell reference.'''
        ...

    @property
    def reference(self) -> str:
        '''Gets an invalid cell reference.'''
        ...

    ...

class CellUnsupportedDataException(aspose.slides.PptxEditException):
    '''The exception that is thrown when an unsupported data is encountered in a spreadsheet cell.'''
    def __init__(self):
        '''Initializes a new instance of the :py:class:`aspose.slides.spreadsheet.CellUnsupportedDataException` class.'''
        ...

    def __init__(self, message: str):
        '''Initializes a new instance of the :py:class:`aspose.slides.spreadsheet.CellUnsupportedDataException` class with a specified error
                    message.
        :param message: A string that describes the error.'''
        ...

    ...

