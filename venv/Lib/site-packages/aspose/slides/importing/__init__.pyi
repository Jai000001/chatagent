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

class ExternalResourceResolver:
    '''Callback class used to resolve external resources during Html, Svg documents import.'''
    def __init__(self):
        ...

    def resolve_uri(self, base_uri: str, relative_uri: str) -> str:
        '''Resolves the absolute URI from the base and relative URIs.
        :param base_uri: Base URI of linking objects
        :param relative_uri: Relative URI to the linked object.
        :returns: Absolute URI or null if the relative URI cannot be resolved.'''
        ...

    def get_entity(self, absolute_uri: str) -> io.RawIOBase:
        '''Maps a URI to an object containing the actual resource.
        :param absolute_uri: Absolute URI to the object.
        :returns: A :py:class:`io.RawIOBase` object or null if resource cannot be streamed.'''
        ...

    ...

class HtmlExternalResolver:
    '''Callback object used by HTML import routine to obtain referrenced objects such as images.'''
    def __init__(self):
        ...

    def resolve_uri(self, base_uri: str, relative_uri: str) -> str:
        '''Resolves the absolute URI from the base and relative URIs.
        :param base_uri: Base URI of linking objects
        :param relative_uri: Relative URI to the linked object.
        :returns: Absolute URI or null if the relative URI cannot be resolved.'''
        ...

    def get_entity(self, absolute_uri: str) -> io.RawIOBase:
        '''Maps a URI to an object containing the actual resource.
        :param absolute_uri: Absolute URI to the object.
        :returns: A :py:class:`io.RawIOBase` object or null if resource cannot be streamed.'''
        ...

    @property
    def as_i_external_resource_resolver(self) -> IExternalResourceResolver:
        ...

    ...

class IExternalResourceResolver:
    '''Callback interface used to resolve external resources during Html, Svg documents import.'''
    def resolve_uri(self, base_uri: str, relative_uri: str) -> str:
        '''Resolves the absolute URI from the base and relative URIs.
        :param base_uri: Base URI of linking objects
        :param relative_uri: Relative URI to the linked object.
        :returns: Absolute URI or null if the relative URI cannot be resolved.'''
        ...

    def get_entity(self, absolute_uri: str) -> io.RawIOBase:
        '''Maps a URI to an object containing the actual resource.
        :param absolute_uri: Absolute URI to the object.
        :returns: A :py:class:`io.RawIOBase` object or null if resource cannot be streamed.'''
        ...

    ...

class IHtmlExternalResolver:
    '''Callback interface used by HTML import routine to obtain referrenced objects such as images.'''
    def resolve_uri(self, base_uri: str, relative_uri: str) -> str:
        ...

    def get_entity(self, absolute_uri: str) -> io.RawIOBase:
        ...

    @property
    def as_i_external_resource_resolver(self) -> IExternalResourceResolver:
        ...

    ...

class PdfImportOptions:
    '''Represents the PDF import options'''
    def __init__(self):
        ...

    @property
    def detect_tables(self) -> bool:
        ...

    @detect_tables.setter
    def detect_tables(self, value: bool):
        ...

    ...

