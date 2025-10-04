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

class IOutputFile:
    '''Represents an output file.'''
    def write(self, stream: io.RawIOBase) -> None:
        '''Writes the file content to the stream.
        :param stream: Destination stream.'''
        ...

    ...

class IOutputSaver:
    '''Represents an output saving service.'''
    def save(self, path: str, output_file: IOutputFile) -> None:
        '''Saves the output file to the given path.
        :param path: Path to save the file to.
        :param output_file: Output file.'''
        ...

    ...

class ITemplateEngine:
    '''Represents a template engine that transforms template and data pair into resulting output (usually HTML).'''
    def add_template(self, key: str, template: str, model_type: Type) -> None:
        ...

    def compile(self, key: str, model: any) -> str:
        '''Transforms the template with the given key and model object to output.
        :param key: Key for the template in the template collection.
        :param model: Model object with data for transformation.
        :returns: Resulting output as a :py:class:`str`.'''
        ...

    ...

class Input:
    '''Represents a collection of input elements (templates).'''
    ...

class Output:
    '''Represents a collection of output elements for :py:class:`IWebDocument`.'''
    @overload
    def add(self, path: str, image: IPPImage) -> IOutputFile:
        '''Adds an output element for the image.
        :param path: Output path.
        :param image: Image to output.
        :returns: :py:class:`aspose.slides.export.web.IOutputFile` object for the image.'''
        ...

    @overload
    def add(self, path: str, image: aspose.pydrawing.Image) -> IOutputFile:
        '''Adds an output element for the image.
        :param path: Output path.
        :param image: Image to output.
        :returns: :py:class:`aspose.slides.export.web.IOutputFile` object for the image.'''
        ...

    @overload
    def add(self, path: str, image: IImage) -> IOutputFile:
        '''Adds an output element for the image.
        :param path: Output path.
        :param image: Image to output.
        :returns: :py:class:`aspose.slides.export.web.IOutputFile` object for the image.'''
        ...

    @overload
    def add(self, path: str, video: IVideo) -> IOutputFile:
        '''Adds an output element for the video.
        :param path: Output path.
        :param video: Video to output.
        :returns: :py:class:`aspose.slides.export.web.IOutputFile` object for the video.'''
        ...

    @overload
    def add(self, path: str, font_data: IFontData, font_style: aspose.pydrawing.FontStyle) -> IOutputFile:
        '''Adds an output element for the font.
        :param path: Output path.
        :param font_data: Font to output.
        :param font_style: Font style.
        :returns: :py:class:`aspose.slides.export.web.IOutputFile` object for the font.'''
        ...

    @overload
    def add(self, path: str, text_content: str) -> IOutputFile:
        '''Adds an output element for the text content.
        :param path: Output path.
        :param text_content: Content to output.
        :returns: :py:class:`aspose.slides.export.web.IOutputFile` object for the text content.'''
        ...

    def bind_resource(self, output_file: IOutputFile, obj: any) -> None:
        '''Binds resource to output file.
        :param output_file: Output file.
        :param obj: Resource object.'''
        ...

    def get_resource_path(self, obj: any) -> str:
        '''Returns the path for a given resource.
        :param obj: Resource object.
        :returns: Resource path.'''
        ...

    ...

class OutputFile:
    '''Represents an output file.'''
    def write(self, stream: io.RawIOBase) -> None:
        '''Writes the file content to the stream.
        :param stream: Destination stream.'''
        ...

    ...

class Storage:
    '''Represents a temporary data storage for :py:class:`aspose.slides.export.web.WebDocument`.'''
    def __init__(self):
        ...

    def contains_key(self, key: str) -> bool:
        '''Determines whether the storage contains an element with the specified key.
        :param key: Key of the value.
        :returns: True if the storage contains an element with the specified key, false otherwise.'''
        ...

    ...

class WebDocument:
    '''Represents a transition form of the presentation for saving into a web format.'''
    def __init__(self, options: WebDocumentOptions):
        ''':py:class:`aspose.slides.export.web.WebDocument` constructor.
        :param options: Options set for the document.
        :returns: A new instance of :py:class:`aspose.slides.export.web.WebDocument`.'''
        ...

    def save(self) -> None:
        '''Saves the document output.'''
        ...

    @property
    def input(self) -> Input:
        ...

    @property
    def output(self) -> Output:
        '''Returns collection of output elements of the document.
                     Read-only :py:attr:`aspose.slides.export.web.WebDocument.output`.'''
        ...

    ...

class WebDocumentOptions:
    '''Represents an options set for :py:class:`aspose.slides.export.web.WebDocument` saving.'''
    def __init__(self):
        ...

    @property
    def template_engine(self) -> ITemplateEngine:
        ...

    @template_engine.setter
    def template_engine(self, value: ITemplateEngine):
        ...

    @property
    def output_saver(self) -> IOutputSaver:
        ...

    @output_saver.setter
    def output_saver(self, value: IOutputSaver):
        ...

    @property
    def embed_images(self) -> bool:
        ...

    @embed_images.setter
    def embed_images(self, value: bool):
        ...

    @property
    def animate_transitions(self) -> bool:
        ...

    @animate_transitions.setter
    def animate_transitions(self, value: bool):
        ...

    @property
    def animate_shapes(self) -> bool:
        ...

    @animate_shapes.setter
    def animate_shapes(self, value: bool):
        ...

    ...

