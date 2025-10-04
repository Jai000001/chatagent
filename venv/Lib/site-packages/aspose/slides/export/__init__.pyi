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

class EmbedAllFontsHtmlController:
    '''The formatting controller class to use for embedding all presentation fonts in WOFF format.'''
    def __init__(self):
        '''Creates new instance'''
        ...

    def __init__(self, font_name_exclude_list: List[str]):
        '''Creates new instance
        :param font_name_exclude_list: Fonts to be excluded from embedding'''
        ...

    def write_document_start(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        '''Called to write html document header. Called once per presentation conversion.
        :param generator: Output object.
        :param presentation: Presentation which being currently rendered.'''
        ...

    def write_document_end(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        '''Called to write html document footer. Called once per presentation conversion.
        :param generator: Output object.
        :param presentation: Presentation which being currently rendered.'''
        ...

    def write_slide_start(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        '''Called to write html slide header. Called once per each of slides.
        :param generator: Output object.
        :param slide: Slide which being currently rendered.'''
        ...

    def write_slide_end(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        '''Called to write html slide footer. Called once per each of slides.
        :param generator: Output object.
        :param slide: Slide which being currently rendered.'''
        ...

    def write_shape_start(self, generator: IHtmlGenerator, shape: IShape) -> None:
        '''Called before shape's rendering. Called once per each of shape. If this function writes anything to generator, current slide image generation will be finished, added html fragment inserted and new image will be started atop of the previous.
        :param generator: Output object.
        :param shape: Shape which is about to render.'''
        ...

    def write_shape_end(self, generator: IHtmlGenerator, shape: IShape) -> None:
        '''Called before shape's rendering. Called once per each of shape. If this function writes anything to generator, current slide image generation will be finished, added html fragment inserted and new image will be started atop of the previous.
        :param generator: Output object.
        :param shape: Shape which is rendered last.'''
        ...

    def write_all_fonts(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        '''Write all fonts contained in :py:class:`aspose.slides.Presentation`.
        :param generator: Output object.
        :param presentation: Presentation which being currently rendered.'''
        ...

    def write_font(self, generator: IHtmlGenerator, original_font: IFontData, substituted_font: IFontData, font_style: str, font_weight: str, font_data: bytes) -> None:
        '''Writes data as base64 into HTML document itself
        :param generator: HTML generator
        :param original_font: Font to be serialized
        :param substituted_font: Substituted font (if font substitution occured), null otherwise
        :param font_style: Font style
        :param font_weight: Font weight
        :param font_data: Font data'''
        ...

    ...

class EmbeddedEotFontsHtmlController:
    '''The formatting controller class to use for fonts embedding in EOT format'''
    def __init__(self):
        '''Creates new instance.'''
        ...

    def __init__(self, controller: IHtmlFormattingController):
        '''Creates new instance.
        :param controller: HTML formatting controller.'''
        ...

    def write_document_start(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_document_end(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_slide_start(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_slide_end(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_shape_start(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    def write_shape_end(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    @property
    def as_i_html_formatting_controller(self) -> IHtmlFormattingController:
        ...

    ...

class EmbeddedWoffFontsHtmlController:
    '''The formatting controller class to use for fonts embedding in WOFF format'''
    def __init__(self):
        '''Creates new instance.'''
        ...

    def __init__(self, controller: IHtmlFormattingController):
        '''Creates new instance.
        :param controller: HTML formatting controller.'''
        ...

    def write_document_start(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_document_end(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_slide_start(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_slide_end(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_shape_start(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    def write_shape_end(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    @property
    def as_i_html_formatting_controller(self) -> IHtmlFormattingController:
        ...

    ...

class EnumerableFrameArgs:
    '''Represents return values of :py:func:`Aspose.Slides.Export.PresentationEnumerableFramesGenerator.EnumerateFrames(System.Collections.Generic.IEnumerable{Aspose.Slide.` method.'''
    def get_frame(self) -> IImage:
        '''Get the current :py:class:`aspose.slides.export.PresentationEnumerableFramesGenerator` frame.'''
        ...

    @property
    def frames_generator(self) -> PresentationEnumerableFramesGenerator:
        ...

    ...

class FrameTickEventArgs:
    '''Represents arguments of the  event.'''
    def get_frame(self) -> IImage:
        '''Get the current :py:class:`aspose.slides.export.PresentationPlayer` frame.'''
        ...

    @property
    def player(self) -> PresentationPlayer:
        '''Get the presentation player'''
        ...

    ...

class GifOptions(SaveOptions):
    '''Represents GIF exporting options.'''
    def __init__(self):
        '''Initializes a new instance of the GifOptions class.'''
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> str:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: str):
        ...

    @property
    def gradient_style(self) -> GradientStyle:
        ...

    @gradient_style.setter
    def gradient_style(self, value: GradientStyle):
        ...

    @property
    def frame_size(self) -> aspose.pydrawing.Size:
        ...

    @frame_size.setter
    def frame_size(self, value: aspose.pydrawing.Size):
        ...

    @property
    def export_hidden_slides(self) -> bool:
        ...

    @export_hidden_slides.setter
    def export_hidden_slides(self, value: bool):
        ...

    @property
    def transition_fps(self) -> int:
        ...

    @transition_fps.setter
    def transition_fps(self, value: int):
        ...

    @property
    def default_delay(self) -> int:
        ...

    @default_delay.setter
    def default_delay(self, value: int):
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    ...

class HandoutLayoutingOptions:
    '''Represents the handout presentation layout mode for export.'''
    def __init__(self):
        '''Initializes the default values.'''
        ...

    @property
    def handout(self) -> HandoutType:
        '''Specifies how many slides and in what sequence will be placed on the page :py:enum:`aspose.slides.export.HandoutType`.'''
        ...

    @handout.setter
    def handout(self, value: HandoutType):
        '''Specifies how many slides and in what sequence will be placed on the page :py:enum:`aspose.slides.export.HandoutType`.'''
        ...

    @property
    def print_slide_numbers(self) -> bool:
        ...

    @print_slide_numbers.setter
    def print_slide_numbers(self, value: bool):
        ...

    @property
    def print_frame_slide(self) -> bool:
        ...

    @print_frame_slide.setter
    def print_frame_slide(self, value: bool):
        ...

    @property
    def print_comments(self) -> bool:
        ...

    @print_comments.setter
    def print_comments(self, value: bool):
        ...

    ...

class Html5Options(SaveOptions):
    '''Represents a HTML5 exporting options.'''
    def __init__(self):
        '''Default constructor.'''
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> str:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: str):
        ...

    @property
    def gradient_style(self) -> GradientStyle:
        ...

    @gradient_style.setter
    def gradient_style(self, value: GradientStyle):
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

    @property
    def embed_images(self) -> bool:
        ...

    @embed_images.setter
    def embed_images(self, value: bool):
        ...

    @property
    def output_path(self) -> str:
        ...

    @output_path.setter
    def output_path(self, value: str):
        ...

    @property
    def notes_comments_layouting(self) -> INotesCommentsLayoutingOptions:
        ...

    @notes_comments_layouting.setter
    def notes_comments_layouting(self, value: INotesCommentsLayoutingOptions):
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    ...

class HtmlFormatter:
    '''Represents HTML file template.'''
    @staticmethod
    def create_document_formatter(css: str, show_slide_title: bool) -> HtmlFormatter:
        '''Creates and returns HTML formatter for a simple document view which consists of sequences of slides one below another.
        :param css: Specifies CSS for this file.
        :param show_slide_title: Add slide title if there is one above slide image.'''
        ...

    @staticmethod
    def create_slide_show_formatter(css: str, show_slide_title: bool) -> HtmlFormatter:
        '''Creates and returns HTML formatter for a simple slide show html which shows slides one after another.
        :param css: Specifies URL of CCS file used.
        :param show_slide_title: Add slide title if there is one above slide image.'''
        ...

    @staticmethod
    def create_custom_formatter(formatting_controller: IHtmlFormattingController) -> HtmlFormatter:
        '''Creates and returns HTML formatter for custom callback-driven html generation.
        :param formatting_controller: Callback interface which controls html file generation.'''
        ...

    ...

class HtmlGenerator:
    '''Html generator.'''
    @overload
    def add_html(self, html: str) -> None:
        '''Adds formatted HTML text.
        :param html: Text to add.'''
        ...

    @overload
    def add_html(self, html: List[char]) -> None:
        '''Adds formatted HTML text.
        :param html: Text to add.'''
        ...

    @overload
    def add_html(self, html: List[char], start_index: int, length: int) -> None:
        '''Adds formatted HTML text.
        :param html: Text to add.
        :param start_index: Start index of the portion to add.
        :param length: Length of the portion to add.'''
        ...

    @overload
    def add_text(self, text: str) -> None:
        '''Adds plain text to the html files, replacing special characters with html entities.
                    Linebreaks and whitespaces aren't replaced.
        :param text: Text to add.'''
        ...

    @overload
    def add_text(self, text: List[char]) -> None:
        '''Adds plain text to the html files, replacing special characters with html entities.
                    Linebreaks and whitespaces aren't replaced.
        :param text: Text to add.'''
        ...

    @overload
    def add_text(self, text: List[char], start_index: int, length: int) -> None:
        '''Adds plain text to the html files, replacing special characters with html entities.
                    Linebreaks and whitespaces aren't replaced.
        :param text: Text to add.
        :param start_index: Start index of the portion to add.
        :param length: Length of the portion to add.'''
        ...

    @overload
    def add_attribute_value(self, value: str) -> None:
        '''Quotes attribute value and adds it to the html file.
        :param value: Attribute value string.'''
        ...

    @overload
    def add_attribute_value(self, value: List[char]) -> None:
        '''Quotes attribute value and adds it to the html file.
        :param value: Attribute value string.'''
        ...

    @overload
    def add_attribute_value(self, value: List[char], start_index: int, length: int) -> None:
        '''Quotes attribute value and adds it to the html file.
        :param value: Attribute value string.
        :param start_index: Start index of the portion to add.
        :param length: Length of the portion to add.'''
        ...

    @property
    def slide_image_size(self) -> aspose.pydrawing.SizeF:
        ...

    @property
    def slide_image_size_unit(self) -> SvgCoordinateUnit:
        ...

    @property
    def slide_image_size_unit_code(self) -> str:
        ...

    @property
    def previous_slide_index(self) -> int:
        ...

    @property
    def slide_index(self) -> int:
        ...

    @property
    def next_slide_index(self) -> int:
        ...

    ...

class HtmlOptions(SaveOptions):
    '''Represents a HTML exporting options.'''
    def __init__(self, link_embed_controller: ILinkEmbedController):
        '''Creates a new HtmlOptions object specifiing callback.
        :param link_embed_controller: Callback object which controls saving project.'''
        ...

    def __init__(self):
        '''Creates a new HtmlOptions object for saving into single HTML file.'''
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> str:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: str):
        ...

    @property
    def gradient_style(self) -> GradientStyle:
        ...

    @gradient_style.setter
    def gradient_style(self, value: GradientStyle):
        ...

    @property
    def slides_layout_options(self) -> ISlidesLayoutOptions:
        ...

    @slides_layout_options.setter
    def slides_layout_options(self, value: ISlidesLayoutOptions):
        ...

    @property
    def ink_options(self) -> IInkOptions:
        ...

    @property
    def notes_comments_layouting(self) -> INotesCommentsLayoutingOptions:
        ...

    @property
    def show_hidden_slides(self) -> bool:
        ...

    @show_hidden_slides.setter
    def show_hidden_slides(self, value: bool):
        ...

    @property
    def html_formatter(self) -> IHtmlFormatter:
        ...

    @html_formatter.setter
    def html_formatter(self, value: IHtmlFormatter):
        ...

    @property
    def slide_image_format(self) -> ISlideImageFormat:
        ...

    @slide_image_format.setter
    def slide_image_format(self, value: ISlideImageFormat):
        ...

    @property
    def jpeg_quality(self) -> int:
        ...

    @jpeg_quality.setter
    def jpeg_quality(self, value: int):
        ...

    @property
    def pictures_compression(self) -> PicturesCompression:
        ...

    @pictures_compression.setter
    def pictures_compression(self, value: PicturesCompression):
        ...

    @property
    def delete_pictures_cropped_areas(self) -> bool:
        ...

    @delete_pictures_cropped_areas.setter
    def delete_pictures_cropped_areas(self, value: bool):
        ...

    @property
    def svg_responsive_layout(self) -> bool:
        ...

    @svg_responsive_layout.setter
    def svg_responsive_layout(self, value: bool):
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    ...

class IEmbeddedEotFontsHtmlController:
    '''Embedded Eot fonts HTML controller.'''
    def write_document_start(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_document_end(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_slide_start(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_slide_end(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_shape_start(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    def write_shape_end(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    @property
    def as_i_html_formatting_controller(self) -> IHtmlFormattingController:
        ...

    ...

class IEmbeddedWoffFontsHtmlController:
    '''Embedded woff fonts html controller.'''
    def write_document_start(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_document_end(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_slide_start(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_slide_end(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_shape_start(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    def write_shape_end(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    @property
    def as_i_html_formatting_controller(self) -> IHtmlFormattingController:
        ...

    ...

class IGifOptions:
    '''Represents GIF exporting options.'''
    @property
    def frame_size(self) -> aspose.pydrawing.Size:
        ...

    @frame_size.setter
    def frame_size(self, value: aspose.pydrawing.Size):
        ...

    @property
    def export_hidden_slides(self) -> bool:
        ...

    @export_hidden_slides.setter
    def export_hidden_slides(self, value: bool):
        ...

    @property
    def transition_fps(self) -> int:
        ...

    @transition_fps.setter
    def transition_fps(self, value: int):
        ...

    @property
    def default_delay(self) -> int:
        ...

    @default_delay.setter
    def default_delay(self, value: int):
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> str:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: str):
        ...

    @property
    def gradient_style(self) -> GradientStyle:
        ...

    @gradient_style.setter
    def gradient_style(self, value: GradientStyle):
        ...

    ...

class IHtml5Options:
    '''Represents a HTML5 exporting options.'''
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

    @property
    def embed_images(self) -> bool:
        ...

    @embed_images.setter
    def embed_images(self, value: bool):
        ...

    @property
    def output_path(self) -> str:
        ...

    @output_path.setter
    def output_path(self, value: str):
        ...

    @property
    def notes_comments_layouting(self) -> INotesCommentsLayoutingOptions:
        ...

    @notes_comments_layouting.setter
    def notes_comments_layouting(self, value: INotesCommentsLayoutingOptions):
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> str:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: str):
        ...

    @property
    def gradient_style(self) -> GradientStyle:
        ...

    @gradient_style.setter
    def gradient_style(self, value: GradientStyle):
        ...

    ...

class IHtmlFormatter:
    '''Represents HTML file template.'''
    ...

class IHtmlFormattingController:
    '''Controls a html file generation.'''
    def write_document_start(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        '''Called to write html document header. Called once per presentation conversion.
        :param generator: Output object.
        :param presentation: Presentation which being currently rendered.'''
        ...

    def write_document_end(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        '''Called to write html document footer. Called once per presentation conversion.
        :param generator: Output object.
        :param presentation: Presentation which being currently rendered.'''
        ...

    def write_slide_start(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        '''Called to write html slide header. Called once per each of slides.
        :param generator: Output object.
        :param slide: Slide which being currently rendered.'''
        ...

    def write_slide_end(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        '''Called to write html slide footer. Called once per each of slides.
        :param generator: Output object.
        :param slide: Slide which being currently rendered.'''
        ...

    def write_shape_start(self, generator: IHtmlGenerator, shape: IShape) -> None:
        '''Called before shape's rendering. Called once per each of shape. If this function writes anything to generator, current slide image generation will be finished, added html fragment inserted and new image will be started atop of the previous.
        :param generator: Output object.
        :param shape: Shape which is about to render.'''
        ...

    def write_shape_end(self, generator: IHtmlGenerator, shape: IShape) -> None:
        '''Called before shape's rendering. Called once per each of shape. If this function writes anything to generator, current slide image generation will be finished, added html fragment inserted and new image will be started atop of the previous.
        :param generator: Output object.
        :param shape: Shape which is rendered last.'''
        ...

    ...

class IHtmlGenerator:
    '''Html generator.'''
    @overload
    def add_html(self, html: str) -> None:
        '''Adds formatted HTML text.
        :param html: Text to add.'''
        ...

    @overload
    def add_html(self, html: List[char]) -> None:
        '''Adds formatted HTML text.
        :param html: Text to add.'''
        ...

    @overload
    def add_html(self, html: List[char], start_index: int, length: int) -> None:
        '''Adds formatted HTML text.
        :param html: Text to add.
        :param start_index: Start index of the portion to add.
        :param length: Length of the portion to add.'''
        ...

    @overload
    def add_text(self, text: str) -> None:
        '''Adds plain text to the html files, replacing special characters with html entities.
                    Linebreaks and whitespaces aren't replaced.
        :param text: Text to add.'''
        ...

    @overload
    def add_text(self, text: List[char]) -> None:
        '''Adds plain text to the html files, replacing special characters with html entities.
                    Linebreaks and whitespaces aren't replaced.
        :param text: Text to add.'''
        ...

    @overload
    def add_text(self, text: List[char], start_index: int, length: int) -> None:
        '''Adds plain text to the html files, replacing special characters with html entities.
                    Linebreaks and whitespaces aren't replaced.
        :param text: Text to add.
        :param start_index: Start index of the portion to add.
        :param length: Length of the portion to add.'''
        ...

    @overload
    def add_attribute_value(self, value: str) -> None:
        '''Quotes attribute value and adds it to the html file.
        :param value: Attribute value string.'''
        ...

    @overload
    def add_attribute_value(self, value: List[char]) -> None:
        '''Quotes attribute value and adds it to the html file.
        :param value: Attribute value string.'''
        ...

    @overload
    def add_attribute_value(self, value: List[char], start_index: int, length: int) -> None:
        '''Quotes attribute value and adds it to the html file.
        :param value: Attribute value string.
        :param start_index: Start index of the portion to add.
        :param length: Length of the portion to add.'''
        ...

    @property
    def slide_image_size(self) -> aspose.pydrawing.SizeF:
        ...

    @property
    def slide_image_size_unit(self) -> SvgCoordinateUnit:
        ...

    @property
    def slide_image_size_unit_code(self) -> str:
        ...

    @property
    def previous_slide_index(self) -> int:
        ...

    @property
    def slide_index(self) -> int:
        ...

    @property
    def next_slide_index(self) -> int:
        ...

    ...

class IHtmlOptions:
    '''Represents a HTML exporting options.'''
    @property
    def html_formatter(self) -> IHtmlFormatter:
        ...

    @html_formatter.setter
    def html_formatter(self, value: IHtmlFormatter):
        ...

    @property
    def slide_image_format(self) -> ISlideImageFormat:
        ...

    @slide_image_format.setter
    def slide_image_format(self, value: ISlideImageFormat):
        ...

    @property
    def show_hidden_slides(self) -> bool:
        ...

    @show_hidden_slides.setter
    def show_hidden_slides(self, value: bool):
        ...

    @property
    def jpeg_quality(self) -> int:
        ...

    @jpeg_quality.setter
    def jpeg_quality(self, value: int):
        ...

    @property
    def pictures_compression(self) -> PicturesCompression:
        ...

    @pictures_compression.setter
    def pictures_compression(self, value: PicturesCompression):
        ...

    @property
    def delete_pictures_cropped_areas(self) -> bool:
        ...

    @delete_pictures_cropped_areas.setter
    def delete_pictures_cropped_areas(self, value: bool):
        ...

    @property
    def svg_responsive_layout(self) -> bool:
        ...

    @svg_responsive_layout.setter
    def svg_responsive_layout(self, value: bool):
        ...

    @property
    def notes_comments_layouting(self) -> INotesCommentsLayoutingOptions:
        ...

    @property
    def slides_layout_options(self) -> ISlidesLayoutOptions:
        ...

    @slides_layout_options.setter
    def slides_layout_options(self, value: ISlidesLayoutOptions):
        ...

    @property
    def ink_options(self) -> IInkOptions:
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> str:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: str):
        ...

    @property
    def gradient_style(self) -> GradientStyle:
        ...

    @gradient_style.setter
    def gradient_style(self, value: GradientStyle):
        ...

    ...

class IInkOptions:
    '''Provides options that control the look of Ink objects in exported document.'''
    @property
    def hide_ink(self) -> bool:
        ...

    @hide_ink.setter
    def hide_ink(self, value: bool):
        ...

    @property
    def interpret_mask_op_as_opacity(self) -> bool:
        ...

    @interpret_mask_op_as_opacity.setter
    def interpret_mask_op_as_opacity(self, value: bool):
        ...

    ...

class ILinkEmbedController:
    '''Callback interface used to determine how object should be processed during saving.'''
    def get_object_storing_location(self, id: int, entity_data: bytes, semantic_name: str, content_type: str, recomended_extension: str) -> LinkEmbedDecision:
        '''Determines where object should be stored.
                    This method is called once for each object id.
                    It is not guaranteed that there won't be two objects with same data, semanticName and contentType but with different id.
        :param id: Object id. This id is saving operation-wide unique.
        :param entity_data: Object binary data. This parameter can be null, if object binary data is not generated yet.
        :param semantic_name: Some short text, describing meaning of object. Controller may use this as a part of external object name, but it is up to dispatcher to ensure that names will be unique and contain only allowed characters.
        :param content_type: MIME type of object.
        :param recomended_extension: File name extension, recommended for this MIME type.
        :returns: Decision'''
        ...

    def get_url(self, id: int, referrer: int) -> str:
        '''Returns an URL to an external object.
                    This method always called if :py:func:`Aspose.Slides.Export.ILinkEmbedController.GetObjectStoringLocation(System.Int32,System.Byte[],System.String,System.String,Syste.` returned :py:attr:`aspose.slides.export.LinkEmbedDecision.LINK` and may be called if :py:func:`Aspose.Slides.Export.ILinkEmbedController.GetObjectStoringLocation(System.Int32,System.Byte[],System.String,System.String,Syste.` returned :py:attr:`aspose.slides.export.LinkEmbedDecision.EMBED` but embedding is impossible.
                    Can be called multiple time for same object id.
        :param id: Object id. This id is saving operation-wide unique.
        :param referrer: id of referrencing object or 0, if object is referrenced by the root document. May be used to generate relative link.
        :returns: Url of external object or null if this object should be ignored.'''
        ...

    def save_external(self, id: int, entity_data: bytes) -> None:
        '''Saves external object.
        :param id: Object id. This id is saving operation-wide unique.
        :param entity_data: Object binary data. This parameter cannot be null.'''
        ...

    ...

class INotesCommentsLayoutingOptions:
    '''Provides options that control the look of layouting of notes and comments in exported document.'''
    @property
    def notes_position(self) -> NotesPositions:
        ...

    @notes_position.setter
    def notes_position(self, value: NotesPositions):
        ...

    @property
    def comments_position(self) -> CommentsPositions:
        ...

    @comments_position.setter
    def comments_position(self, value: CommentsPositions):
        ...

    @property
    def comments_area_color(self) -> aspose.pydrawing.Color:
        ...

    @comments_area_color.setter
    def comments_area_color(self, value: aspose.pydrawing.Color):
        ...

    @property
    def comments_area_width(self) -> int:
        ...

    @comments_area_width.setter
    def comments_area_width(self, value: int):
        ...

    @property
    def show_comments_by_no_author(self) -> bool:
        ...

    @show_comments_by_no_author.setter
    def show_comments_by_no_author(self, value: bool):
        ...

    ...

class IPdfOptions:
    '''Provides options that control how a presentation is saved in Pdf format.'''
    @property
    def text_compression(self) -> PdfTextCompression:
        ...

    @text_compression.setter
    def text_compression(self, value: PdfTextCompression):
        ...

    @property
    def best_images_compression_ratio(self) -> bool:
        ...

    @best_images_compression_ratio.setter
    def best_images_compression_ratio(self, value: bool):
        ...

    @property
    def embed_true_type_fonts_for_ascii(self) -> bool:
        ...

    @embed_true_type_fonts_for_ascii.setter
    def embed_true_type_fonts_for_ascii(self, value: bool):
        ...

    @property
    def show_hidden_slides(self) -> bool:
        ...

    @show_hidden_slides.setter
    def show_hidden_slides(self, value: bool):
        ...

    @property
    def additional_common_font_families(self) -> List[str]:
        ...

    @additional_common_font_families.setter
    def additional_common_font_families(self, value: List[str]):
        ...

    @property
    def embed_full_fonts(self) -> bool:
        ...

    @embed_full_fonts.setter
    def embed_full_fonts(self, value: bool):
        ...

    @property
    def rasterize_unsupported_font_styles(self) -> bool:
        ...

    @rasterize_unsupported_font_styles.setter
    def rasterize_unsupported_font_styles(self, value: bool):
        ...

    @property
    def jpeg_quality(self) -> int:
        ...

    @jpeg_quality.setter
    def jpeg_quality(self, value: int):
        ...

    @property
    def compliance(self) -> PdfCompliance:
        '''Desired conformance level for generated PDF document.
                    Read/write :py:enum:`aspose.slides.export.PdfCompliance`.'''
        ...

    @compliance.setter
    def compliance(self, value: PdfCompliance):
        '''Desired conformance level for generated PDF document.
                    Read/write :py:enum:`aspose.slides.export.PdfCompliance`.'''
        ...

    @property
    def password(self) -> str:
        '''Setting user password to protect the PDF document. 
                    Read/write :py:class:`str`.'''
        ...

    @password.setter
    def password(self, value: str):
        '''Setting user password to protect the PDF document. 
                    Read/write :py:class:`str`.'''
        ...

    @property
    def access_permissions(self) -> PdfAccessPermissions:
        ...

    @access_permissions.setter
    def access_permissions(self, value: PdfAccessPermissions):
        ...

    @property
    def save_metafiles_as_png(self) -> bool:
        ...

    @save_metafiles_as_png.setter
    def save_metafiles_as_png(self, value: bool):
        ...

    @property
    def sufficient_resolution(self) -> float:
        ...

    @sufficient_resolution.setter
    def sufficient_resolution(self, value: float):
        ...

    @property
    def draw_slides_frame(self) -> bool:
        ...

    @draw_slides_frame.setter
    def draw_slides_frame(self, value: bool):
        ...

    @property
    def notes_comments_layouting(self) -> INotesCommentsLayoutingOptions:
        ...

    @property
    def slides_layout_options(self) -> ISlidesLayoutOptions:
        ...

    @slides_layout_options.setter
    def slides_layout_options(self, value: ISlidesLayoutOptions):
        ...

    @property
    def image_transparent_color(self) -> aspose.pydrawing.Color:
        ...

    @image_transparent_color.setter
    def image_transparent_color(self, value: aspose.pydrawing.Color):
        ...

    @property
    def apply_image_transparent(self) -> bool:
        ...

    @apply_image_transparent.setter
    def apply_image_transparent(self, value: bool):
        ...

    @property
    def ink_options(self) -> IInkOptions:
        ...

    @property
    def include_ole_data(self) -> bool:
        ...

    @include_ole_data.setter
    def include_ole_data(self, value: bool):
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> str:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: str):
        ...

    @property
    def gradient_style(self) -> GradientStyle:
        ...

    @gradient_style.setter
    def gradient_style(self, value: GradientStyle):
        ...

    ...

class IPptOptions:
    '''Provides options that control how a presentation is saved in PPT format.'''
    @property
    def root_directory_clsid(self) -> Guid:
        ...

    @root_directory_clsid.setter
    def root_directory_clsid(self, value: Guid):
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> str:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: str):
        ...

    @property
    def gradient_style(self) -> GradientStyle:
        ...

    @gradient_style.setter
    def gradient_style(self, value: GradientStyle):
        ...

    ...

class IPptxOptions:
    '''Represents options for saving OpenXml presentations (PPTX, PPSX, POTX, PPTM, PPSM, POTM).'''
    @property
    def conformance(self) -> Conformance:
        '''Specifies the conformance class to which the Presentation document conforms.
                    Default value is :py:attr:`aspose.slides.export.Conformance.ECMA_376_2006`'''
        ...

    @conformance.setter
    def conformance(self, value: Conformance):
        '''Specifies the conformance class to which the Presentation document conforms.
                    Default value is :py:attr:`aspose.slides.export.Conformance.ECMA_376_2006`'''
        ...

    @property
    def zip_64_mode(self) -> Zip64Mode:
        ...

    @zip_64_mode.setter
    def zip_64_mode(self, value: Zip64Mode):
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> str:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: str):
        ...

    @property
    def gradient_style(self) -> GradientStyle:
        ...

    @gradient_style.setter
    def gradient_style(self, value: GradientStyle):
        ...

    ...

class IPresentationAnimationPlayer:
    '''Represents a player of the animation.'''
    def set_time_position(self, time: float) -> None:
        '''Set the animation time position within the :py:attr:`aspose.slides.export.IPresentationAnimationPlayer.duration`.'''
        ...

    def get_frame(self) -> IImage:
        '''Get the frame for the current time position previously set with the :py:func:`Aspose.Slides.Export.IPresentationAnimationPlayer.SetTimePosition(Syste.` method.'''
        ...

    @property
    def duration(self) -> float:
        '''Get animation duration [ms]'''
        ...

    ...

class IRenderingOptions:
    '''Provides options that control how a presentation/slide is rendered.'''
    @property
    def notes_comments_layouting(self) -> INotesCommentsLayoutingOptions:
        ...

    @property
    def slides_layout_options(self) -> ISlidesLayoutOptions:
        ...

    @slides_layout_options.setter
    def slides_layout_options(self, value: ISlidesLayoutOptions):
        ...

    @property
    def ink_options(self) -> IInkOptions:
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> str:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: str):
        ...

    @property
    def gradient_style(self) -> GradientStyle:
        ...

    @gradient_style.setter
    def gradient_style(self, value: GradientStyle):
        ...

    ...

class IResponsiveHtmlController:
    '''Responsive HTML Controller'''
    def write_document_start(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_document_end(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_slide_start(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_slide_end(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_shape_start(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    def write_shape_end(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    @property
    def as_i_html_formatting_controller(self) -> IHtmlFormattingController:
        ...

    ...

class ISVGOptions:
    '''Represents an SVG options.'''
    @property
    def vectorize_text(self) -> bool:
        ...

    @vectorize_text.setter
    def vectorize_text(self, value: bool):
        ...

    @property
    def metafile_rasterization_dpi(self) -> int:
        ...

    @metafile_rasterization_dpi.setter
    def metafile_rasterization_dpi(self, value: int):
        ...

    @property
    def disable_3d_text(self) -> bool:
        ...

    @disable_3d_text.setter
    def disable_3d_text(self, value: bool):
        ...

    @property
    def disable_gradient_split(self) -> bool:
        ...

    @disable_gradient_split.setter
    def disable_gradient_split(self, value: bool):
        ...

    @property
    def disable_line_end_cropping(self) -> bool:
        ...

    @disable_line_end_cropping.setter
    def disable_line_end_cropping(self, value: bool):
        ...

    @property
    def jpeg_quality(self) -> int:
        ...

    @jpeg_quality.setter
    def jpeg_quality(self, value: int):
        ...

    @property
    def shape_formatting_controller(self) -> ISvgShapeFormattingController:
        ...

    @shape_formatting_controller.setter
    def shape_formatting_controller(self, value: ISvgShapeFormattingController):
        ...

    @property
    def pictures_compression(self) -> PicturesCompression:
        ...

    @pictures_compression.setter
    def pictures_compression(self, value: PicturesCompression):
        ...

    @property
    def delete_pictures_cropped_areas(self) -> bool:
        ...

    @delete_pictures_cropped_areas.setter
    def delete_pictures_cropped_areas(self, value: bool):
        ...

    @property
    def use_frame_size(self) -> bool:
        ...

    @use_frame_size.setter
    def use_frame_size(self, value: bool):
        ...

    @property
    def use_frame_rotation(self) -> bool:
        ...

    @use_frame_rotation.setter
    def use_frame_rotation(self, value: bool):
        ...

    @property
    def external_fonts_handling(self) -> SvgExternalFontsHandling:
        ...

    @external_fonts_handling.setter
    def external_fonts_handling(self, value: SvgExternalFontsHandling):
        ...

    @property
    def ink_options(self) -> IInkOptions:
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> str:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: str):
        ...

    @property
    def gradient_style(self) -> GradientStyle:
        ...

    @gradient_style.setter
    def gradient_style(self, value: GradientStyle):
        ...

    ...

class ISaveOptions:
    '''Options that control how a presentation is saved.'''
    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> str:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: str):
        ...

    @property
    def gradient_style(self) -> GradientStyle:
        ...

    @gradient_style.setter
    def gradient_style(self, value: GradientStyle):
        ...

    ...

class ISaveOptionsFactory:
    '''Allows to create save options' instances'''
    def create_pptx_options(self) -> IPptxOptions:
        '''Creates PPTX save options.
        :returns: Save options.'''
        ...

    ...

class ISlideImageFormat:
    '''Determines format in which slide image will be saved for presentation to HTML export.'''
    ...

class ISlidesLayoutOptions:
    '''Represents the presentation layout mode for export.'''
    ...

class ISvgShape:
    '''Represents options for SVG shape.'''
    def set_event_handler(self, event_type: SvgEvent, handler: str) -> None:
        '''Sets event handler for the shape
        :param event_type: Type of event.
        :param handler: Javascript function to handle event. Null value removes handler.'''
        ...

    @property
    def id(self) -> str:
        '''Sets or gets id for the shape'''
        ...

    @id.setter
    def id(self, value: str):
        '''Sets or gets id for the shape'''
        ...

    ...

class ISvgShapeAndTextFormattingController:
    '''Controls SVG shape and text generation.'''
    def format_text(self, svg_t_span: ISvgTSpan, portion: IPortion, text_frame: ITextFrame) -> None:
        '''This function is called before rendering of text portion to SVG to allow user to control resulting SVG.
        :param svg_t_span: Object to control SVG tspan generation.
        :param portion: Source portion.
        :param text_frame: Source portion text frame.'''
        ...

    def format_shape(self, svg_shape: ISvgShape, shape: IShape) -> None:
        ...

    @property
    def as_i_svg_shape_formatting_controller(self) -> ISvgShapeFormattingController:
        ...

    ...

class ISvgShapeFormattingController:
    '''Controls SVG shape generation.'''
    def format_shape(self, svg_shape: ISvgShape, shape: IShape) -> None:
        '''This function is called before rendering of shape to SVG to allow user to control resulting SVG.
        :param svg_shape: Object to control SVG shape generation.
        :param shape: Source shape.'''
        ...

    ...

class ISvgTSpan:
    '''Represents options for SVG text portion ("tspan").'''
    @property
    def id(self) -> str:
        '''Gets or sets id for the "tspan" element'''
        ...

    @id.setter
    def id(self, value: str):
        '''Gets or sets id for the "tspan" element'''
        ...

    ...

class ISwfOptions:
    '''Provides options that control how a presentation is saved in SWF format.'''
    @property
    def compressed(self) -> bool:
        '''Specifies whether the generated SWF document should be compressed or not.
                    Default is ``true``.'''
        ...

    @compressed.setter
    def compressed(self, value: bool):
        '''Specifies whether the generated SWF document should be compressed or not.
                    Default is ``true``.'''
        ...

    @property
    def viewer_included(self) -> bool:
        ...

    @viewer_included.setter
    def viewer_included(self, value: bool):
        ...

    @property
    def show_page_border(self) -> bool:
        ...

    @show_page_border.setter
    def show_page_border(self, value: bool):
        ...

    @property
    def show_hidden_slides(self) -> bool:
        ...

    @show_hidden_slides.setter
    def show_hidden_slides(self, value: bool):
        ...

    @property
    def show_full_screen(self) -> bool:
        ...

    @show_full_screen.setter
    def show_full_screen(self, value: bool):
        ...

    @property
    def show_page_stepper(self) -> bool:
        ...

    @show_page_stepper.setter
    def show_page_stepper(self, value: bool):
        ...

    @property
    def show_search(self) -> bool:
        ...

    @show_search.setter
    def show_search(self, value: bool):
        ...

    @property
    def show_top_pane(self) -> bool:
        ...

    @show_top_pane.setter
    def show_top_pane(self, value: bool):
        ...

    @property
    def show_bottom_pane(self) -> bool:
        ...

    @show_bottom_pane.setter
    def show_bottom_pane(self, value: bool):
        ...

    @property
    def show_left_pane(self) -> bool:
        ...

    @show_left_pane.setter
    def show_left_pane(self, value: bool):
        ...

    @property
    def start_open_left_pane(self) -> bool:
        ...

    @start_open_left_pane.setter
    def start_open_left_pane(self, value: bool):
        ...

    @property
    def enable_context_menu(self) -> bool:
        ...

    @enable_context_menu.setter
    def enable_context_menu(self, value: bool):
        ...

    @property
    def logo_image_bytes(self) -> bytes:
        ...

    @logo_image_bytes.setter
    def logo_image_bytes(self, value: bytes):
        ...

    @property
    def logo_link(self) -> str:
        ...

    @logo_link.setter
    def logo_link(self, value: str):
        ...

    @property
    def jpeg_quality(self) -> int:
        ...

    @jpeg_quality.setter
    def jpeg_quality(self, value: int):
        ...

    @property
    def notes_comments_layouting(self) -> INotesCommentsLayoutingOptions:
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> str:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: str):
        ...

    @property
    def gradient_style(self) -> GradientStyle:
        ...

    @gradient_style.setter
    def gradient_style(self, value: GradientStyle):
        ...

    ...

class ITextToHtmlConversionOptions:
    '''Options for extracting HTML from the Pptx text.'''
    @property
    def add_clipboard_fragment_header(self) -> bool:
        ...

    @add_clipboard_fragment_header.setter
    def add_clipboard_fragment_header(self, value: bool):
        ...

    @property
    def text_inheritance_limit(self) -> TextInheritanceLimit:
        ...

    @text_inheritance_limit.setter
    def text_inheritance_limit(self, value: TextInheritanceLimit):
        ...

    @property
    def link_embed_controller(self) -> ILinkEmbedController:
        ...

    @link_embed_controller.setter
    def link_embed_controller(self, value: ILinkEmbedController):
        ...

    @property
    def encoding_name(self) -> str:
        ...

    @encoding_name.setter
    def encoding_name(self, value: str):
        ...

    ...

class ITiffOptions:
    '''Provides options that control how a presentation is saved in TIFF format.'''
    @property
    def image_size(self) -> aspose.pydrawing.Size:
        ...

    @image_size.setter
    def image_size(self, value: aspose.pydrawing.Size):
        ...

    @property
    def dpi_x(self) -> int:
        ...

    @dpi_x.setter
    def dpi_x(self, value: int):
        ...

    @property
    def dpi_y(self) -> int:
        ...

    @dpi_y.setter
    def dpi_y(self, value: int):
        ...

    @property
    def show_hidden_slides(self) -> bool:
        ...

    @show_hidden_slides.setter
    def show_hidden_slides(self, value: bool):
        ...

    @property
    def compression_type(self) -> TiffCompressionTypes:
        ...

    @compression_type.setter
    def compression_type(self, value: TiffCompressionTypes):
        ...

    @property
    def pixel_format(self) -> ImagePixelFormat:
        ...

    @pixel_format.setter
    def pixel_format(self, value: ImagePixelFormat):
        ...

    @property
    def notes_comments_layouting(self) -> INotesCommentsLayoutingOptions:
        ...

    @property
    def slides_layout_options(self) -> ISlidesLayoutOptions:
        ...

    @slides_layout_options.setter
    def slides_layout_options(self, value: ISlidesLayoutOptions):
        ...

    @property
    def bw_conversion_mode(self) -> BlackWhiteConversionMode:
        ...

    @bw_conversion_mode.setter
    def bw_conversion_mode(self, value: BlackWhiteConversionMode):
        ...

    @property
    def ink_options(self) -> IInkOptions:
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> str:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: str):
        ...

    @property
    def gradient_style(self) -> GradientStyle:
        ...

    @gradient_style.setter
    def gradient_style(self, value: GradientStyle):
        ...

    ...

class IVideoPlayerHtmlController:
    '''This class allows export of video and audio files into a HTML'''
    def write_document_start(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_document_end(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_slide_start(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_slide_end(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_shape_start(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    def write_shape_end(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    def format_shape(self, svg_shape: ISvgShape, shape: IShape) -> None:
        ...

    def get_object_storing_location(self, id: int, entity_data: bytes, semantic_name: str, content_type: str, recomended_extension: str) -> LinkEmbedDecision:
        ...

    def get_url(self, id: int, referrer: int) -> str:
        ...

    def save_external(self, id: int, entity_data: bytes) -> None:
        ...

    @property
    def as_i_html_formatting_controller(self) -> IHtmlFormattingController:
        ...

    @property
    def as_i_svg_shape_formatting_controller(self) -> ISvgShapeFormattingController:
        ...

    @property
    def as_i_link_embed_controller(self) -> ILinkEmbedController:
        ...

    ...

class IVideoPlayerHtmlControllerFactory:
    '''Allows to create VideoPlayerHtmlController.'''
    def create_video_player_html_controller(self, path: str, file_name: str, base_uri: str) -> IVideoPlayerHtmlController:
        '''Create video player HTML controller.
        :param path: Path.
        :param file_name: File Name.
        :param base_uri: Base URI.
        :returns: Video player HTML controller :py:class:`aspose.slides.export.IVideoPlayerHtmlController`'''
        ...

    ...

class IXpsOptions:
    '''Provides options that control how a presentation is saved in XPS format.'''
    @property
    def save_metafiles_as_png(self) -> bool:
        ...

    @save_metafiles_as_png.setter
    def save_metafiles_as_png(self, value: bool):
        ...

    @property
    def draw_slides_frame(self) -> bool:
        ...

    @draw_slides_frame.setter
    def draw_slides_frame(self, value: bool):
        ...

    @property
    def show_hidden_slides(self) -> bool:
        ...

    @show_hidden_slides.setter
    def show_hidden_slides(self, value: bool):
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> str:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: str):
        ...

    @property
    def gradient_style(self) -> GradientStyle:
        ...

    @gradient_style.setter
    def gradient_style(self, value: GradientStyle):
        ...

    ...

class InkOptions:
    '''Provides options that control the look of Ink objects in exported document.'''
    @property
    def hide_ink(self) -> bool:
        ...

    @hide_ink.setter
    def hide_ink(self, value: bool):
        ...

    @property
    def interpret_mask_op_as_opacity(self) -> bool:
        ...

    @interpret_mask_op_as_opacity.setter
    def interpret_mask_op_as_opacity(self, value: bool):
        ...

    ...

class MarkdownSaveOptions(SaveOptions):
    '''Represents options that control how presentation should be saved to markdown.'''
    def __init__(self):
        '''Ctor.'''
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> str:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: str):
        ...

    @property
    def gradient_style(self) -> GradientStyle:
        ...

    @gradient_style.setter
    def gradient_style(self, value: GradientStyle):
        ...

    @property
    def export_type(self) -> MarkdownExportType:
        ...

    @export_type.setter
    def export_type(self, value: MarkdownExportType):
        ...

    @property
    def base_path(self) -> str:
        ...

    @base_path.setter
    def base_path(self, value: str):
        ...

    @property
    def images_save_folder_name(self) -> str:
        ...

    @images_save_folder_name.setter
    def images_save_folder_name(self, value: str):
        ...

    @property
    def new_line_type(self) -> NewLineType:
        ...

    @new_line_type.setter
    def new_line_type(self, value: NewLineType):
        ...

    @property
    def show_comments(self) -> bool:
        ...

    @show_comments.setter
    def show_comments(self, value: bool):
        ...

    @property
    def show_hidden_slides(self) -> bool:
        ...

    @show_hidden_slides.setter
    def show_hidden_slides(self, value: bool):
        ...

    @property
    def show_slide_number(self) -> bool:
        ...

    @show_slide_number.setter
    def show_slide_number(self, value: bool):
        ...

    @property
    def flavor(self) -> Flavor:
        '''Specifies markdown specification to convert presentation.
                    Default is ``Multi-markdown``.'''
        ...

    @flavor.setter
    def flavor(self, value: Flavor):
        '''Specifies markdown specification to convert presentation.
                    Default is ``Multi-markdown``.'''
        ...

    ...

class NotesCommentsLayoutingOptions:
    '''Provides options that control the look of layouting of notes and comments in exported document.'''
    def __init__(self):
        '''Default constructor.'''
        ...

    @property
    def show_comments_by_no_author(self) -> bool:
        ...

    @show_comments_by_no_author.setter
    def show_comments_by_no_author(self, value: bool):
        ...

    @property
    def notes_position(self) -> NotesPositions:
        ...

    @notes_position.setter
    def notes_position(self, value: NotesPositions):
        ...

    @property
    def comments_position(self) -> CommentsPositions:
        ...

    @comments_position.setter
    def comments_position(self, value: CommentsPositions):
        ...

    @property
    def comments_area_color(self) -> aspose.pydrawing.Color:
        ...

    @comments_area_color.setter
    def comments_area_color(self, value: aspose.pydrawing.Color):
        ...

    @property
    def comments_area_width(self) -> int:
        ...

    @comments_area_width.setter
    def comments_area_width(self, value: int):
        ...

    ...

class PdfOptions(SaveOptions):
    '''Provides options that control how a presentation is saved in Pdf format.'''
    def __init__(self):
        '''Default constructor.'''
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> str:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: str):
        ...

    @property
    def gradient_style(self) -> GradientStyle:
        ...

    @gradient_style.setter
    def gradient_style(self, value: GradientStyle):
        ...

    @property
    def slides_layout_options(self) -> ISlidesLayoutOptions:
        ...

    @slides_layout_options.setter
    def slides_layout_options(self, value: ISlidesLayoutOptions):
        ...

    @property
    def ink_options(self) -> IInkOptions:
        ...

    @property
    def notes_comments_layouting(self) -> INotesCommentsLayoutingOptions:
        ...

    @property
    def show_hidden_slides(self) -> bool:
        ...

    @show_hidden_slides.setter
    def show_hidden_slides(self, value: bool):
        ...

    @property
    def text_compression(self) -> PdfTextCompression:
        ...

    @text_compression.setter
    def text_compression(self, value: PdfTextCompression):
        ...

    @property
    def best_images_compression_ratio(self) -> bool:
        ...

    @best_images_compression_ratio.setter
    def best_images_compression_ratio(self, value: bool):
        ...

    @property
    def embed_true_type_fonts_for_ascii(self) -> bool:
        ...

    @embed_true_type_fonts_for_ascii.setter
    def embed_true_type_fonts_for_ascii(self, value: bool):
        ...

    @property
    def additional_common_font_families(self) -> List[str]:
        ...

    @additional_common_font_families.setter
    def additional_common_font_families(self, value: List[str]):
        ...

    @property
    def embed_full_fonts(self) -> bool:
        ...

    @embed_full_fonts.setter
    def embed_full_fonts(self, value: bool):
        ...

    @property
    def rasterize_unsupported_font_styles(self) -> bool:
        ...

    @rasterize_unsupported_font_styles.setter
    def rasterize_unsupported_font_styles(self, value: bool):
        ...

    @property
    def jpeg_quality(self) -> int:
        ...

    @jpeg_quality.setter
    def jpeg_quality(self, value: int):
        ...

    @property
    def compliance(self) -> PdfCompliance:
        '''Desired conformance level for generated PDF document.
                    Read/write :py:enum:`aspose.slides.export.PdfCompliance`.'''
        ...

    @compliance.setter
    def compliance(self, value: PdfCompliance):
        '''Desired conformance level for generated PDF document.
                    Read/write :py:enum:`aspose.slides.export.PdfCompliance`.'''
        ...

    @property
    def password(self) -> str:
        '''Setting user password to protect the PDF document. 
                    Read/write :py:class:`str`.'''
        ...

    @password.setter
    def password(self, value: str):
        '''Setting user password to protect the PDF document. 
                    Read/write :py:class:`str`.'''
        ...

    @property
    def access_permissions(self) -> PdfAccessPermissions:
        ...

    @access_permissions.setter
    def access_permissions(self, value: PdfAccessPermissions):
        ...

    @property
    def save_metafiles_as_png(self) -> bool:
        ...

    @save_metafiles_as_png.setter
    def save_metafiles_as_png(self, value: bool):
        ...

    @property
    def sufficient_resolution(self) -> float:
        ...

    @sufficient_resolution.setter
    def sufficient_resolution(self, value: float):
        ...

    @property
    def draw_slides_frame(self) -> bool:
        ...

    @draw_slides_frame.setter
    def draw_slides_frame(self, value: bool):
        ...

    @property
    def image_transparent_color(self) -> aspose.pydrawing.Color:
        ...

    @image_transparent_color.setter
    def image_transparent_color(self, value: aspose.pydrawing.Color):
        ...

    @property
    def apply_image_transparent(self) -> bool:
        ...

    @apply_image_transparent.setter
    def apply_image_transparent(self, value: bool):
        ...

    @property
    def include_ole_data(self) -> bool:
        ...

    @include_ole_data.setter
    def include_ole_data(self, value: bool):
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    ...

class PptOptions(SaveOptions):
    '''Provides options that control how a presentation is saved in PPT format.'''
    def __init__(self):
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> str:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: str):
        ...

    @property
    def gradient_style(self) -> GradientStyle:
        ...

    @gradient_style.setter
    def gradient_style(self, value: GradientStyle):
        ...

    @property
    def root_directory_clsid(self) -> Guid:
        ...

    @root_directory_clsid.setter
    def root_directory_clsid(self, value: Guid):
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    ...

class PptxOptions(SaveOptions):
    '''Represents options for saving OpenXml presentations (PPTX, PPSX, POTX, PPTM, PPSM, POTM).'''
    def __init__(self):
        '''Creates new instance of PptxOptions'''
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> str:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: str):
        ...

    @property
    def gradient_style(self) -> GradientStyle:
        ...

    @gradient_style.setter
    def gradient_style(self, value: GradientStyle):
        ...

    @property
    def conformance(self) -> Conformance:
        '''Specifies the conformance class to which the Presentation document conforms.
                    Default value is :py:attr:`aspose.slides.export.Conformance.ECMA_376_2006`'''
        ...

    @conformance.setter
    def conformance(self, value: Conformance):
        '''Specifies the conformance class to which the Presentation document conforms.
                    Default value is :py:attr:`aspose.slides.export.Conformance.ECMA_376_2006`'''
        ...

    @property
    def zip_64_mode(self) -> Zip64Mode:
        ...

    @zip_64_mode.setter
    def zip_64_mode(self, value: Zip64Mode):
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    ...

class PresentationAnimationsGenerator:
    '''Represents a generator of the animations in the :py:class:`aspose.slides.Presentation`.'''
    def __init__(self, presentation: Presentation):
        '''Creates a new instance of the :py:class:`aspose.slides.export.PresentationAnimationsGenerator`.
        :param presentation: The frame size will be set with accordance to the :py:attr:`aspose.slides.Presentation.slide_size`'''
        ...

    def __init__(self, frame_size: aspose.pydrawing.Size):
        '''Creates a new instance of the :py:class:`aspose.slides.export.PresentationAnimationsGenerator`.
        :param frame_size: The frame size.'''
        ...

    def run(self, slides: Iterable[ISlide]) -> None:
        ...

    @property
    def default_delay(self) -> int:
        ...

    @default_delay.setter
    def default_delay(self, value: int):
        ...

    @property
    def include_hidden_slides(self) -> bool:
        ...

    @include_hidden_slides.setter
    def include_hidden_slides(self, value: bool):
        ...

    @property
    def exported_slides(self) -> int:
        ...

    @property
    def FRAME_SIZE(self) -> aspose.pydrawing.Size:
        ...

    ...

class PresentationEnumerableFramesGenerator:
    '''Represents a generator of the animations in the :py:class:`aspose.slides.Presentation`.'''
    def __init__(self, presentation: Presentation, fps: float):
        '''Creates new instance of the :py:class:`aspose.slides.export.PresentationPlayer`.
        :param presentation: Presentation
        :param fps: Frames per second (FPS)'''
        ...

    def __init__(self, frame_size: aspose.pydrawing.Size, fps: float):
        '''Creates new instance of the :py:class:`aspose.slides.export.PresentationPlayer`.
        :param frame_size: The frame size
        :param fps: Frames per second (FPS)'''
        ...

    def enumerate_frames(self, slides: Iterable[ISlide]) -> Iterable[EnumerableFrameArgs]:
        ...

    @property
    def frame_index(self) -> int:
        ...

    @property
    def default_delay(self) -> int:
        ...

    @default_delay.setter
    def default_delay(self, value: int):
        ...

    @property
    def include_hidden_slides(self) -> bool:
        ...

    @include_hidden_slides.setter
    def include_hidden_slides(self, value: bool):
        ...

    @property
    def exported_slides(self) -> int:
        ...

    ...

class PresentationPlayer:
    '''Represents the player of animations associated with the :py:class:`aspose.slides.Presentation`.'''
    def __init__(self, generator: PresentationAnimationsGenerator, fps: float):
        '''Creates new instance of the :py:class:`aspose.slides.export.PresentationPlayer`.
        :param fps: Frames per second (FPS)'''
        ...

    @property
    def frame_index(self) -> int:
        ...

    ...

class RenderingOptions(SaveOptions):
    '''Provides options that control how a presentation/slide is rendered.'''
    def __init__(self):
        '''Default constructor.'''
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> str:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: str):
        ...

    @property
    def gradient_style(self) -> GradientStyle:
        ...

    @gradient_style.setter
    def gradient_style(self, value: GradientStyle):
        ...

    @property
    def notes_comments_layouting(self) -> INotesCommentsLayoutingOptions:
        ...

    @property
    def slides_layout_options(self) -> ISlidesLayoutOptions:
        ...

    @slides_layout_options.setter
    def slides_layout_options(self, value: ISlidesLayoutOptions):
        ...

    @property
    def ink_options(self) -> IInkOptions:
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    ...

class ResponsiveHtmlController:
    '''Responsive HTML Controller'''
    def __init__(self):
        '''Creates new instance'''
        ...

    def __init__(self, controller: IHtmlFormattingController):
        '''Creates new instance
        :param controller: HTML formatting controller'''
        ...

    def write_document_start(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_document_end(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_slide_start(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_slide_end(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_shape_start(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    def write_shape_end(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    @property
    def as_i_html_formatting_controller(self) -> IHtmlFormattingController:
        ...

    ...

class SVGOptions(SaveOptions):
    '''Represents an SVG options.'''
    def __init__(self):
        '''Initializes a new instance of the SVGOptions class.'''
        ...

    def __init__(self, link_embed_controller: ILinkEmbedController):
        '''Initializes a new instance of the SVGOptions class specifying the link embedding controller object.
        :param link_embed_controller: The link embedding controller reference.'''
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> str:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: str):
        ...

    @property
    def gradient_style(self) -> GradientStyle:
        ...

    @gradient_style.setter
    def gradient_style(self, value: GradientStyle):
        ...

    @property
    def ink_options(self) -> IInkOptions:
        ...

    @property
    def use_frame_size(self) -> bool:
        ...

    @use_frame_size.setter
    def use_frame_size(self, value: bool):
        ...

    @property
    def use_frame_rotation(self) -> bool:
        ...

    @use_frame_rotation.setter
    def use_frame_rotation(self, value: bool):
        ...

    @property
    def vectorize_text(self) -> bool:
        ...

    @vectorize_text.setter
    def vectorize_text(self, value: bool):
        ...

    @property
    def metafile_rasterization_dpi(self) -> int:
        ...

    @metafile_rasterization_dpi.setter
    def metafile_rasterization_dpi(self, value: int):
        ...

    @property
    def disable_3d_text(self) -> bool:
        ...

    @disable_3d_text.setter
    def disable_3d_text(self, value: bool):
        ...

    @property
    def disable_gradient_split(self) -> bool:
        ...

    @disable_gradient_split.setter
    def disable_gradient_split(self, value: bool):
        ...

    @property
    def disable_line_end_cropping(self) -> bool:
        ...

    @disable_line_end_cropping.setter
    def disable_line_end_cropping(self, value: bool):
        ...

    @classmethod
    @property
    def default(cls) -> SVGOptions:
        '''Returns default settings.
                    Read-only :py:class:`aspose.slides.export.SVGOptions`.'''
        ...

    @classmethod
    @property
    def simple(cls) -> SVGOptions:
        '''Returns settings for simpliest and smallest SVG file generation.
                    Read-only :py:class:`aspose.slides.export.SVGOptions`.'''
        ...

    @classmethod
    @property
    def wysiwyg(cls) -> SVGOptions:
        '''Returns settings for most accurate SVG file generation.
                    Read-only :py:class:`aspose.slides.export.SVGOptions`.'''
        ...

    @property
    def jpeg_quality(self) -> int:
        ...

    @jpeg_quality.setter
    def jpeg_quality(self, value: int):
        ...

    @property
    def shape_formatting_controller(self) -> ISvgShapeFormattingController:
        ...

    @shape_formatting_controller.setter
    def shape_formatting_controller(self, value: ISvgShapeFormattingController):
        ...

    @property
    def pictures_compression(self) -> PicturesCompression:
        ...

    @pictures_compression.setter
    def pictures_compression(self, value: PicturesCompression):
        ...

    @property
    def delete_pictures_cropped_areas(self) -> bool:
        ...

    @delete_pictures_cropped_areas.setter
    def delete_pictures_cropped_areas(self, value: bool):
        ...

    @property
    def external_fonts_handling(self) -> SvgExternalFontsHandling:
        ...

    @external_fonts_handling.setter
    def external_fonts_handling(self, value: SvgExternalFontsHandling):
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    ...

class SaveOptions:
    '''Abstract class with options that control how a presentation is saved.'''
    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> str:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: str):
        ...

    @property
    def gradient_style(self) -> GradientStyle:
        ...

    @gradient_style.setter
    def gradient_style(self, value: GradientStyle):
        ...

    ...

class SaveOptionsFactory:
    '''Allows to create save options' instances'''
    def __init__(self):
        ...

    def create_pptx_options(self) -> IPptxOptions:
        '''Creates PPTX save options.
        :returns: Save options.'''
        ...

    ...

class SlideImageFormat:
    '''Determines format in which slide image will be saved for presentation to HTML export.'''
    def __init__(self):
        ...

    @staticmethod
    def svg(options: SVGOptions) -> SlideImageFormat:
        '''Slides should converted to a SVG format.
        :param options: Options for SVG export.'''
        ...

    @staticmethod
    def bitmap(scale: float, img_format: aspose.pydrawing.Imaging.ImageFormat) -> SlideImageFormat:
        '''Slides should be converted to a raster image.
        :param scale: Image scale factor.
        :param img_format: Image format.'''
        ...

    ...

class SvgShape:
    '''Represents options for SVG shape.'''
    def set_event_handler(self, event_type: SvgEvent, handler: str) -> None:
        '''Sets event handler for the shape
        :param event_type: Type of event.
        :param handler: Javascript function to handle event. Null value removes handler.'''
        ...

    @property
    def id(self) -> str:
        '''Gets shape id'''
        ...

    @id.setter
    def id(self, value: str):
        '''Gets shape id'''
        ...

    ...

class SvgTSpan:
    '''Represents options for SVG text portion ("tspan").'''
    @property
    def id(self) -> str:
        '''Gets "tspan" element id'''
        ...

    @id.setter
    def id(self, value: str):
        '''Gets "tspan" element id'''
        ...

    ...

class SwfOptions(SaveOptions):
    '''Provides options that control how a presentation is saved in Swf format.'''
    def __init__(self):
        '''Default constructor.'''
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> str:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: str):
        ...

    @property
    def gradient_style(self) -> GradientStyle:
        ...

    @gradient_style.setter
    def gradient_style(self, value: GradientStyle):
        ...

    @property
    def show_hidden_slides(self) -> bool:
        ...

    @show_hidden_slides.setter
    def show_hidden_slides(self, value: bool):
        ...

    @property
    def compressed(self) -> bool:
        '''Specifies whether the generated SWF document should be compressed or not.
                    Default is ``true``.'''
        ...

    @compressed.setter
    def compressed(self, value: bool):
        '''Specifies whether the generated SWF document should be compressed or not.
                    Default is ``true``.'''
        ...

    @property
    def viewer_included(self) -> bool:
        ...

    @viewer_included.setter
    def viewer_included(self, value: bool):
        ...

    @property
    def show_page_border(self) -> bool:
        ...

    @show_page_border.setter
    def show_page_border(self, value: bool):
        ...

    @property
    def show_full_screen(self) -> bool:
        ...

    @show_full_screen.setter
    def show_full_screen(self, value: bool):
        ...

    @property
    def show_page_stepper(self) -> bool:
        ...

    @show_page_stepper.setter
    def show_page_stepper(self, value: bool):
        ...

    @property
    def show_search(self) -> bool:
        ...

    @show_search.setter
    def show_search(self, value: bool):
        ...

    @property
    def show_top_pane(self) -> bool:
        ...

    @show_top_pane.setter
    def show_top_pane(self, value: bool):
        ...

    @property
    def show_bottom_pane(self) -> bool:
        ...

    @show_bottom_pane.setter
    def show_bottom_pane(self, value: bool):
        ...

    @property
    def show_left_pane(self) -> bool:
        ...

    @show_left_pane.setter
    def show_left_pane(self, value: bool):
        ...

    @property
    def start_open_left_pane(self) -> bool:
        ...

    @start_open_left_pane.setter
    def start_open_left_pane(self, value: bool):
        ...

    @property
    def enable_context_menu(self) -> bool:
        ...

    @enable_context_menu.setter
    def enable_context_menu(self, value: bool):
        ...

    @property
    def logo_image_bytes(self) -> bytes:
        ...

    @logo_image_bytes.setter
    def logo_image_bytes(self, value: bytes):
        ...

    @property
    def logo_link(self) -> str:
        ...

    @logo_link.setter
    def logo_link(self, value: str):
        ...

    @property
    def jpeg_quality(self) -> int:
        ...

    @jpeg_quality.setter
    def jpeg_quality(self, value: int):
        ...

    @property
    def notes_comments_layouting(self) -> INotesCommentsLayoutingOptions:
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    ...

class TextToHtmlConversionOptions:
    '''Options for extracting HTML from the Pptx text.'''
    def __init__(self):
        ...

    @property
    def add_clipboard_fragment_header(self) -> bool:
        ...

    @add_clipboard_fragment_header.setter
    def add_clipboard_fragment_header(self, value: bool):
        ...

    @property
    def text_inheritance_limit(self) -> TextInheritanceLimit:
        ...

    @text_inheritance_limit.setter
    def text_inheritance_limit(self, value: TextInheritanceLimit):
        ...

    @property
    def link_embed_controller(self) -> ILinkEmbedController:
        ...

    @link_embed_controller.setter
    def link_embed_controller(self, value: ILinkEmbedController):
        ...

    @property
    def encoding_name(self) -> str:
        ...

    @encoding_name.setter
    def encoding_name(self, value: str):
        ...

    ...

class TiffOptions(SaveOptions):
    '''Provides options that control how a presentation is saved in TIFF format.'''
    def __init__(self):
        '''Default constructor.'''
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> str:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: str):
        ...

    @property
    def gradient_style(self) -> GradientStyle:
        ...

    @gradient_style.setter
    def gradient_style(self, value: GradientStyle):
        ...

    @property
    def ink_options(self) -> IInkOptions:
        ...

    @property
    def notes_comments_layouting(self) -> INotesCommentsLayoutingOptions:
        ...

    @property
    def show_hidden_slides(self) -> bool:
        ...

    @show_hidden_slides.setter
    def show_hidden_slides(self, value: bool):
        ...

    @property
    def image_size(self) -> aspose.pydrawing.Size:
        ...

    @image_size.setter
    def image_size(self, value: aspose.pydrawing.Size):
        ...

    @property
    def dpi_x(self) -> int:
        ...

    @dpi_x.setter
    def dpi_x(self, value: int):
        ...

    @property
    def dpi_y(self) -> int:
        ...

    @dpi_y.setter
    def dpi_y(self, value: int):
        ...

    @property
    def compression_type(self) -> TiffCompressionTypes:
        ...

    @compression_type.setter
    def compression_type(self, value: TiffCompressionTypes):
        ...

    @property
    def pixel_format(self) -> ImagePixelFormat:
        ...

    @pixel_format.setter
    def pixel_format(self, value: ImagePixelFormat):
        ...

    @property
    def slides_layout_options(self) -> ISlidesLayoutOptions:
        ...

    @slides_layout_options.setter
    def slides_layout_options(self, value: ISlidesLayoutOptions):
        ...

    @property
    def bw_conversion_mode(self) -> BlackWhiteConversionMode:
        ...

    @bw_conversion_mode.setter
    def bw_conversion_mode(self, value: BlackWhiteConversionMode):
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    ...

class VideoPlayerHtmlController:
    '''This class allows export of video and audio files into a HTML'''
    def __init__(self, path: str, file_name: str, base_uri: str):
        '''Creates a new instance of controller
        :param path: The path where video and audio files will be generated
        :param file_name: The name of the HTML file
        :param base_uri: The base URI which will be used for links generating'''
        ...

    def write_document_start(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_document_end(self, generator: IHtmlGenerator, presentation: IPresentation) -> None:
        ...

    def write_slide_start(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_slide_end(self, generator: IHtmlGenerator, slide: ISlide) -> None:
        ...

    def write_shape_start(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    def write_shape_end(self, generator: IHtmlGenerator, shape: IShape) -> None:
        ...

    def format_shape(self, svg_shape: ISvgShape, shape: IShape) -> None:
        ...

    def get_object_storing_location(self, id: int, entity_data: bytes, semantic_name: str, content_type: str, recomended_extension: str) -> LinkEmbedDecision:
        ...

    def get_url(self, id: int, referrer: int) -> str:
        ...

    def save_external(self, id: int, entity_data: bytes) -> None:
        ...

    @property
    def as_i_html_formatting_controller(self) -> IHtmlFormattingController:
        ...

    @property
    def as_i_svg_shape_formatting_controller(self) -> ISvgShapeFormattingController:
        ...

    @property
    def as_i_link_embed_controller(self) -> ILinkEmbedController:
        ...

    ...

class VideoPlayerHtmlControllerFactory:
    '''Allows to create VideoPlayerHtmlController.'''
    def __init__(self):
        ...

    def create_video_player_html_controller(self, path: str, file_name: str, base_uri: str) -> IVideoPlayerHtmlController:
        '''Creates new ``VideoPlayerHtmlController``.
        :param path: Path.
        :param file_name: File name.
        :param base_uri: Base URI.'''
        ...

    ...

class XpsOptions(SaveOptions):
    '''Provides options that control how a presentation is saved in XPS format.'''
    def __init__(self):
        '''Default constructor.'''
        ...

    @property
    def warning_callback(self) -> aspose.slides.warnings.IWarningCallback:
        ...

    @warning_callback.setter
    def warning_callback(self, value: aspose.slides.warnings.IWarningCallback):
        ...

    @property
    def progress_callback(self) -> IProgressCallback:
        ...

    @progress_callback.setter
    def progress_callback(self, value: IProgressCallback):
        ...

    @property
    def default_regular_font(self) -> str:
        ...

    @default_regular_font.setter
    def default_regular_font(self, value: str):
        ...

    @property
    def gradient_style(self) -> GradientStyle:
        ...

    @gradient_style.setter
    def gradient_style(self, value: GradientStyle):
        ...

    @property
    def show_hidden_slides(self) -> bool:
        ...

    @show_hidden_slides.setter
    def show_hidden_slides(self, value: bool):
        ...

    @property
    def save_metafiles_as_png(self) -> bool:
        ...

    @save_metafiles_as_png.setter
    def save_metafiles_as_png(self, value: bool):
        ...

    @property
    def draw_slides_frame(self) -> bool:
        ...

    @draw_slides_frame.setter
    def draw_slides_frame(self, value: bool):
        ...

    @property
    def as_i_save_options(self) -> ISaveOptions:
        ...

    ...

class BlackWhiteConversionMode:
    '''Provides options that control how slides' images will be converted to bitonal images.'''
    @classmethod
    @property
    def DEFAULT(cls) -> BlackWhiteConversionMode:
        '''Specifies no conversion algorithm. The algorithm implemented in the TIFF codec will be used. (Default)'''
        ...

    @classmethod
    @property
    def DITHERING(cls) -> BlackWhiteConversionMode:
        '''Specifies the dithering algorithm (Floyd-Steinberg).'''
        ...

    @classmethod
    @property
    def DITHERING_FLOYD_STEINBERG(cls) -> BlackWhiteConversionMode:
        '''Specifies the Floyd-Steinberg dithering algorithm.'''
        ...

    @classmethod
    @property
    def AUTO(cls) -> BlackWhiteConversionMode:
        '''Specifies the automatically calculated threshold algorithm (Otsu).'''
        ...

    @classmethod
    @property
    def AUTO_OTSU(cls) -> BlackWhiteConversionMode:
        '''Specifies the automatically calculated Otsu's threshold algorithm.'''
        ...

    @classmethod
    @property
    def THRESHOLD25(cls) -> BlackWhiteConversionMode:
        '''Specifies the static threshold algorithm (25%).'''
        ...

    @classmethod
    @property
    def THRESHOLD50(cls) -> BlackWhiteConversionMode:
        '''Specifies the static threshold algorithm (50%).'''
        ...

    @classmethod
    @property
    def THRESHOLD75(cls) -> BlackWhiteConversionMode:
        '''Specifies the static threshold algorithm (75%).'''
        ...

    ...

class CommentsPositions:
    '''Represents the rule to render comments into exported document'''
    @classmethod
    @property
    def NONE(cls) -> CommentsPositions:
        '''Specifies that comments should not be displayed at all.'''
        ...

    @classmethod
    @property
    def BOTTOM(cls) -> CommentsPositions:
        '''Specifies that comments should be displayed at the bottom of the page.'''
        ...

    @classmethod
    @property
    def RIGHT(cls) -> CommentsPositions:
        '''Specifies that comments should be displayed to the right of the page.'''
        ...

    ...

class Conformance:
    '''Specifies the conformance class to which the PresentationML document conforms.'''
    @classmethod
    @property
    def ECMA_376_2006(cls) -> Conformance:
        '''Specifies that the document conforms to the ECMA376:2006.'''
        ...

    @classmethod
    @property
    def ISO_29500_2008_TRANSITIONAL(cls) -> Conformance:
        '''Specifies that the document conforms to the ISO/IEC 29500:2008 Transitional conformance class.'''
        ...

    @classmethod
    @property
    def ISO_29500_2008_STRICT(cls) -> Conformance:
        '''Specifies that the document conforms to the ISO/IEC 29500:2008 Strict conformance class.'''
        ...

    ...

class EmbedFontCharacters:
    '''Represents the rule to use for adding new embedding font into :py:class:`aspose.slides.IPresentation`'''
    @classmethod
    @property
    def ONLY_USED(cls) -> EmbedFontCharacters:
        '''Embed only the characters used in the presentation (best for reducing file size).'''
        ...

    @classmethod
    @property
    def ALL(cls) -> EmbedFontCharacters:
        '''Embed all characters (best for editing by other people).'''
        ...

    ...

class Flavor:
    '''All markdown specifications used in program.'''
    @classmethod
    @property
    def GITHUB(cls) -> Flavor:
        '''Github flavor.'''
        ...

    @classmethod
    @property
    def GRUBER(cls) -> Flavor:
        '''Gruber flavor.'''
        ...

    @classmethod
    @property
    def MULTI_MARKDOWN(cls) -> Flavor:
        '''Multi markdown flavor.'''
        ...

    @classmethod
    @property
    def COMMON_MARK(cls) -> Flavor:
        '''Common mark flavor.'''
        ...

    @classmethod
    @property
    def MARKDOWN_EXTRA(cls) -> Flavor:
        '''Markdown extra flavor.'''
        ...

    @classmethod
    @property
    def PANDOC(cls) -> Flavor:
        '''Pandoc flavor.'''
        ...

    @classmethod
    @property
    def KRAMDOWN(cls) -> Flavor:
        '''Kramdown flavor.'''
        ...

    @classmethod
    @property
    def MARKUA(cls) -> Flavor:
        '''Markua flavor.'''
        ...

    @classmethod
    @property
    def MARUKU(cls) -> Flavor:
        '''Maruku flavor.'''
        ...

    @classmethod
    @property
    def MARKDOWN2(cls) -> Flavor:
        '''Markdown2 flavor.'''
        ...

    @classmethod
    @property
    def REMARKABLE(cls) -> Flavor:
        '''Remarkable flavor'''
        ...

    @classmethod
    @property
    def SHOWDOWN(cls) -> Flavor:
        '''Showdown flavor.'''
        ...

    @classmethod
    @property
    def GHOST(cls) -> Flavor:
        '''Ghost flavor.'''
        ...

    @classmethod
    @property
    def GIT_LAB(cls) -> Flavor:
        '''Gitlab flavor.'''
        ...

    @classmethod
    @property
    def HAROOPAD(cls) -> Flavor:
        '''Haroopad flavor.'''
        ...

    @classmethod
    @property
    def IA_WRITER(cls) -> Flavor:
        '''IAWriter flavor.'''
        ...

    @classmethod
    @property
    def REDCARPET(cls) -> Flavor:
        '''Redcarpet flavor.'''
        ...

    @classmethod
    @property
    def SCHOLARLY_MARKDOWN(cls) -> Flavor:
        '''Scholarly markdown flavor.'''
        ...

    @classmethod
    @property
    def TAIGA(cls) -> Flavor:
        '''Taiga flavor.'''
        ...

    @classmethod
    @property
    def TRELLO(cls) -> Flavor:
        '''Trello flavor.'''
        ...

    @classmethod
    @property
    def S9E_TEXT_FORMATTER(cls) -> Flavor:
        '''S9E text formatter flavor.'''
        ...

    @classmethod
    @property
    def X_WIKI(cls) -> Flavor:
        '''XWiki flavor.'''
        ...

    @classmethod
    @property
    def STACK_OVERFLOW(cls) -> Flavor:
        '''Stack overflow flavor.'''
        ...

    @classmethod
    @property
    def DEFAULT(cls) -> Flavor:
        '''Default markdown flavor.'''
        ...

    ...

class HandoutType:
    '''Specifies how many slides and in what sequence will be placed on the page.'''
    @classmethod
    @property
    def HANDOUTS1(cls) -> HandoutType:
        '''One slide per page.'''
        ...

    @classmethod
    @property
    def HANDOUTS2(cls) -> HandoutType:
        '''Two slides per page.'''
        ...

    @classmethod
    @property
    def HANDOUTS3(cls) -> HandoutType:
        '''Three slides per page.'''
        ...

    @classmethod
    @property
    def HANDOUTS_4_HORIZONTAL(cls) -> HandoutType:
        '''Four slides per page in a horizontal sequence.'''
        ...

    @classmethod
    @property
    def HANDOUTS_4_VERTICAL(cls) -> HandoutType:
        '''Four slides per page in a vertical sequence.'''
        ...

    @classmethod
    @property
    def HANDOUTS_6_HORIZONTAL(cls) -> HandoutType:
        '''Six slides per page in a horizontal sequence.'''
        ...

    @classmethod
    @property
    def HANDOUTS_6_VERTICAL(cls) -> HandoutType:
        '''Six slides per page in a vertical sequence.'''
        ...

    @classmethod
    @property
    def HANDOUTS_9_HORIZONTAL(cls) -> HandoutType:
        '''Nine slides per page in a horizontal sequence.'''
        ...

    @classmethod
    @property
    def HANDOUTS_9_VERTICAL(cls) -> HandoutType:
        '''Nine slides per page in a vertical sequence.'''
        ...

    ...

class ImagePixelFormat:
    '''Specifies the pixel format for the generated images.'''
    @classmethod
    @property
    def FORMAT_1BPP_INDEXED(cls) -> ImagePixelFormat:
        '''1 bits per pixel, indexed.'''
        ...

    @classmethod
    @property
    def FORMAT_4BPP_INDEXED(cls) -> ImagePixelFormat:
        '''4 bits per pixel, indexed.'''
        ...

    @classmethod
    @property
    def FORMAT_8BPP_INDEXED(cls) -> ImagePixelFormat:
        '''8 bits per pixel, indexed.'''
        ...

    @classmethod
    @property
    def FORMAT_24BPP_RGB(cls) -> ImagePixelFormat:
        '''24 bits per pixel, RGB.'''
        ...

    @classmethod
    @property
    def FORMAT_32BPP_ARGB(cls) -> ImagePixelFormat:
        '''32 bits per pixel, ARGB.'''
        ...

    ...

class LinkEmbedDecision:
    '''Determines how object will be processed during saving.'''
    @classmethod
    @property
    def LINK(cls) -> LinkEmbedDecision:
        '''Object will be stored externally, referrenced by URL'''
        ...

    @classmethod
    @property
    def EMBED(cls) -> LinkEmbedDecision:
        '''Object should be embedded to a generated file if possible. If embedding is imposible, GetUrl will be called and, depending on result, object will be referrenced by URL or ignored.'''
        ...

    @classmethod
    @property
    def IGNORE(cls) -> LinkEmbedDecision:
        '''Object will be ignored.'''
        ...

    ...

class MarkdownExportType:
    '''Type of rendering document.'''
    @classmethod
    @property
    def SEQUENTIAL(cls) -> MarkdownExportType:
        '''Render all items separately. One by one.'''
        ...

    @classmethod
    @property
    def TEXT_ONLY(cls) -> MarkdownExportType:
        '''Render only text.'''
        ...

    @classmethod
    @property
    def VISUAL(cls) -> MarkdownExportType:
        '''Render all items, items that are grouped - render together.'''
        ...

    ...

class NewLineType:
    '''Type of new line that will be used in generated document.'''
    @classmethod
    @property
    def WINDOWS(cls) -> NewLineType:
        ...

    @classmethod
    @property
    def UNIX(cls) -> NewLineType:
        ...

    @classmethod
    @property
    def MAC(cls) -> NewLineType:
        '''Mac (OS 9) new line - \\r'''
        ...

    ...

class NotesPositions:
    '''Represents the rule to render notes into exported document'''
    @classmethod
    @property
    def NONE(cls) -> NotesPositions:
        '''Specifies that notes should not be displayed at all.'''
        ...

    @classmethod
    @property
    def BOTTOM_FULL(cls) -> NotesPositions:
        '''Specifies that notes should be full displayed using additional pages as it is needed.'''
        ...

    @classmethod
    @property
    def BOTTOM_TRUNCATED(cls) -> NotesPositions:
        '''Specifies that notes should be displayed in only one page.'''
        ...

    ...

class PdfAccessPermissions:
    '''Contains a set of flags specifying which access permissions should be granted when the document is opened with 
                user access.'''
    @classmethod
    @property
    def NONE(cls) -> PdfAccessPermissions:
        '''Specifies that a user does not have access permissions.'''
        ...

    @classmethod
    @property
    def PRINT_DOCUMENT(cls) -> PdfAccessPermissions:
        '''Specifies whether a user may print the document (possibly not at the highest quality level, depending on 
                    whether bit :py:attr:`aspose.slides.export.PdfAccessPermissions.HIGH_QUALITY_PRINT` is also set).'''
        ...

    @classmethod
    @property
    def MODIFY_CONTENT(cls) -> PdfAccessPermissions:
        '''Specifies whether a user may modify the contents of the document by operations other than those controlled
                    by bits :py:attr:`aspose.slides.export.PdfAccessPermissions.ADD_OR_MODIFY_FIELDS`, :py:attr:`aspose.slides.export.PdfAccessPermissions.FILL_EXISTING_FIELDS`, :py:attr:`aspose.slides.export.PdfAccessPermissions.ASSEMBLE_DOCUMENT`.'''
        ...

    @classmethod
    @property
    def COPY_TEXT_AND_GRAPHICS(cls) -> PdfAccessPermissions:
        '''Specifies whether a user may copy or otherwise extract text and graphics from the document by operations 
                    other than that controlled by bit :py:attr:`aspose.slides.export.PdfAccessPermissions.EXTRACT_TEXT_AND_GRAPHICS`.'''
        ...

    @classmethod
    @property
    def ADD_OR_MODIFY_FIELDS(cls) -> PdfAccessPermissions:
        '''Specifies whether a user may add or modify text annotations, fill in interactive form fields, and, if bit
                    :py:attr:`aspose.slides.export.PdfAccessPermissions.MODIFY_CONTENT` is also set, create or modify interactive form fields (including signature 
                    fields).'''
        ...

    @classmethod
    @property
    def FILL_EXISTING_FIELDS(cls) -> PdfAccessPermissions:
        '''Specifies whether a user may fill in existing interactive form fields (including signature fields), even if
                    bit :py:attr:`aspose.slides.export.PdfAccessPermissions.ADD_OR_MODIFY_FIELDS` is clear.'''
        ...

    @classmethod
    @property
    def EXTRACT_TEXT_AND_GRAPHICS(cls) -> PdfAccessPermissions:
        '''Specifies whether a user may extract text and graphics in support of accessibility to users with disabilities
                    or for other purposes.'''
        ...

    @classmethod
    @property
    def ASSEMBLE_DOCUMENT(cls) -> PdfAccessPermissions:
        '''Specifies whether a user may assemble the document (insert, rotate, or delete pages and create bookmarks or
                    thumbnail images), even if bit :py:attr:`aspose.slides.export.PdfAccessPermissions.MODIFY_CONTENT` is clear.'''
        ...

    @classmethod
    @property
    def HIGH_QUALITY_PRINT(cls) -> PdfAccessPermissions:
        '''Specifies whether a user may print the document to a representation from which a faithful digital copy of
                    the PDF content could be generated. When this bit is clear (and bit :py:attr:`aspose.slides.export.PdfAccessPermissions.PRINT_DOCUMENT` is set),
                    printing is limited to a low-level representation of the appearance, possibly of degraded quality.'''
        ...

    ...

class PdfCompliance:
    '''Constants which define the PDF standards compliance level.'''
    @classmethod
    @property
    def PDF15(cls) -> PdfCompliance:
        '''The output file will comply with the PDF 1.5 standard.'''
        ...

    @classmethod
    @property
    def PDF16(cls) -> PdfCompliance:
        '''The output file will comply with the PDF 1.6 standard.'''
        ...

    @classmethod
    @property
    def PDF17(cls) -> PdfCompliance:
        '''The output file will comply with the PDF 1.7 standard.'''
        ...

    @classmethod
    @property
    def PDF_A1B(cls) -> PdfCompliance:
        '''The output file will comply with the PDF/A-1b standard.'''
        ...

    @classmethod
    @property
    def PDF_A1A(cls) -> PdfCompliance:
        '''The output file will comply with the PDF/A-1a standard.'''
        ...

    @classmethod
    @property
    def PDF_A2B(cls) -> PdfCompliance:
        '''The output file will comply with the PDF/A-2b standard.'''
        ...

    @classmethod
    @property
    def PDF_A2A(cls) -> PdfCompliance:
        '''The output file will comply with the PDF/A-2a standard.'''
        ...

    @classmethod
    @property
    def PDF_A3B(cls) -> PdfCompliance:
        '''The output file will comply with the PDF/A-3b standard.'''
        ...

    @classmethod
    @property
    def PDF_A3A(cls) -> PdfCompliance:
        '''The output file will comply with the PDF/A-3a standard.'''
        ...

    @classmethod
    @property
    def PDF_UA(cls) -> PdfCompliance:
        '''The output file will comply with the PDF/UA standard.'''
        ...

    @classmethod
    @property
    def PDF_A2U(cls) -> PdfCompliance:
        '''The output file will comply with the PDF/A-2u standard.'''
        ...

    ...

class PdfTextCompression:
    '''Constants which define the type of a compression applied to all content in the PDF file except images.'''
    @classmethod
    @property
    def NONE(cls) -> PdfTextCompression:
        '''No compression.'''
        ...

    @classmethod
    @property
    def FLATE(cls) -> PdfTextCompression:
        '''Flate (ZIP) compression.'''
        ...

    ...

class PicturesCompression:
    '''Represents the pictures compression level'''
    @classmethod
    @property
    def DPI330(cls) -> PicturesCompression:
        '''Good quality for high-definition (HD) displays'''
        ...

    @classmethod
    @property
    def DPI220(cls) -> PicturesCompression:
        '''Excellent quality on most printers and screens'''
        ...

    @classmethod
    @property
    def DPI150(cls) -> PicturesCompression:
        '''Good for web pages and projectors'''
        ...

    @classmethod
    @property
    def DPI96(cls) -> PicturesCompression:
        '''Minimize document size for sharing'''
        ...

    @classmethod
    @property
    def DPI72(cls) -> PicturesCompression:
        '''Default compression level'''
        ...

    @classmethod
    @property
    def DOCUMENT_RESOLUTION(cls) -> PicturesCompression:
        '''Use document resolution - the picture will not be compressed and used in document as-is'''
        ...

    ...

class SaveFormat:
    '''Constants which define the format of a saved presentation.'''
    @classmethod
    @property
    def PPT(cls) -> SaveFormat:
        '''Save presentation in PPT format.'''
        ...

    @classmethod
    @property
    def PDF(cls) -> SaveFormat:
        '''Save presentation in PDF format.'''
        ...

    @classmethod
    @property
    def XPS(cls) -> SaveFormat:
        '''Save presentation in XPS format.'''
        ...

    @classmethod
    @property
    def PPTX(cls) -> SaveFormat:
        '''Save presentation in PPTX format.'''
        ...

    @classmethod
    @property
    def PPSX(cls) -> SaveFormat:
        '''Save presentation in PPSX (slideshow) format.'''
        ...

    @classmethod
    @property
    def TIFF(cls) -> SaveFormat:
        '''Save presentation as multi-page TIFF image.'''
        ...

    @classmethod
    @property
    def ODP(cls) -> SaveFormat:
        '''Save presentation in ODP format.'''
        ...

    @classmethod
    @property
    def PPTM(cls) -> SaveFormat:
        '''Save presentation in PPTM (macro-enabled presentation) format.'''
        ...

    @classmethod
    @property
    def PPSM(cls) -> SaveFormat:
        '''Save presentation in PPSM (macro-enabled slideshow) format.'''
        ...

    @classmethod
    @property
    def POTX(cls) -> SaveFormat:
        '''Save presentation in POTX (template) format.'''
        ...

    @classmethod
    @property
    def POTM(cls) -> SaveFormat:
        '''Save presentation in POTM (macro-enabled template) format.'''
        ...

    @classmethod
    @property
    def HTML(cls) -> SaveFormat:
        '''Save presentation in HTML format.'''
        ...

    @classmethod
    @property
    def SWF(cls) -> SaveFormat:
        '''Save presentation in SWF format.'''
        ...

    @classmethod
    @property
    def OTP(cls) -> SaveFormat:
        '''Save presentation in OTP (presentation template) format.'''
        ...

    @classmethod
    @property
    def PPS(cls) -> SaveFormat:
        '''Save presentation in PPS format.'''
        ...

    @classmethod
    @property
    def POT(cls) -> SaveFormat:
        '''Save presentation in POT format.'''
        ...

    @classmethod
    @property
    def FODP(cls) -> SaveFormat:
        '''Save presentation in FODP format.'''
        ...

    @classmethod
    @property
    def GIF(cls) -> SaveFormat:
        '''Save presentation in GIF format.'''
        ...

    @classmethod
    @property
    def HTML5(cls) -> SaveFormat:
        '''Save presentation in HTML format using new HTML5 templating system.'''
        ...

    @classmethod
    @property
    def MD(cls) -> SaveFormat:
        '''Save presentation in Markdown format'''
        ...

    @classmethod
    @property
    def XML(cls) -> SaveFormat:
        '''Save presentation in PowerPoint XML Presentation format.'''
        ...

    ...

class SvgCoordinateUnit:
    '''Represents CSS2 coordinate units used to define SVG coordinates.'''
    @classmethod
    @property
    def INCH(cls) -> SvgCoordinateUnit:
        '''Inch'''
        ...

    @classmethod
    @property
    def CENTIMETER(cls) -> SvgCoordinateUnit:
        '''Centimeter.'''
        ...

    @classmethod
    @property
    def MILLIMETER(cls) -> SvgCoordinateUnit:
        '''Millimeter.'''
        ...

    @classmethod
    @property
    def POINT(cls) -> SvgCoordinateUnit:
        '''Point (1/72 of inch),'''
        ...

    @classmethod
    @property
    def PICA(cls) -> SvgCoordinateUnit:
        '''Pica (1/6 of inch).'''
        ...

    @classmethod
    @property
    def EM(cls) -> SvgCoordinateUnit:
        '''Em size of a font of containing element.'''
        ...

    @classmethod
    @property
    def EX(cls) -> SvgCoordinateUnit:
        '''Ex size (size of lowercase letter, usualy "x") of font of containing element.'''
        ...

    @classmethod
    @property
    def PIXEL(cls) -> SvgCoordinateUnit:
        '''Pixel size.'''
        ...

    @classmethod
    @property
    def PERCENT(cls) -> SvgCoordinateUnit:
        '''Percent.'''
        ...

    ...

class SvgEvent:
    '''Represents options for SVG shape.'''
    @classmethod
    @property
    def ON_FOCUS_IN(cls) -> SvgEvent:
        '''Occurs when an element receives focus, such as when a text becomes selected.'''
        ...

    @classmethod
    @property
    def ON_FOCUS_OUT(cls) -> SvgEvent:
        '''Occurs when an element loses focus, such as when a text becomes unselected.'''
        ...

    @classmethod
    @property
    def ON_ACTIVATE(cls) -> SvgEvent:
        '''Occurs when an element is activated, for instance, through a mouse click or a keypress.'''
        ...

    @classmethod
    @property
    def ON_CLICK(cls) -> SvgEvent:
        '''Occurs when the pointing device button is clicked over an element.'''
        ...

    @classmethod
    @property
    def ON_MOUSE_DOWN(cls) -> SvgEvent:
        '''Occurs when the pointing device button is pressed over an element.'''
        ...

    @classmethod
    @property
    def ON_MOUSE_UP(cls) -> SvgEvent:
        '''Occurs when the pointing device button is released over an element.'''
        ...

    @classmethod
    @property
    def ON_MOUSE_OVER(cls) -> SvgEvent:
        '''Occurs when the pointing device is moved onto an element.'''
        ...

    @classmethod
    @property
    def ON_MOUSE_MOVE(cls) -> SvgEvent:
        '''Occurs when the pointing device is moved while it is over an element.'''
        ...

    @classmethod
    @property
    def ON_MOUSE_OUT(cls) -> SvgEvent:
        '''Occurs when the pointing device is moved away from an element.'''
        ...

    @classmethod
    @property
    def ON_LOAD(cls) -> SvgEvent:
        '''Occurs when the user agent has fully parsed the element and its descendants and all referrenced resurces, required to render it.'''
        ...

    @classmethod
    @property
    def ON_UNLOAD(cls) -> SvgEvent:
        '''Occurs when the DOM implementation removes a document from a window or frame. Only applicable to outermost svg elements.'''
        ...

    @classmethod
    @property
    def ON_ABORT(cls) -> SvgEvent:
        '''Occurs when page loading is stopped before an element has been allowed to load completely.'''
        ...

    @classmethod
    @property
    def ON_ERROR(cls) -> SvgEvent:
        '''Occurs when an element does not load properly or when an error occurs during script execution.'''
        ...

    @classmethod
    @property
    def ON_RESIZE(cls) -> SvgEvent:
        '''Occurs when a document view is being resized. Only applicable to outermost svg elements.'''
        ...

    @classmethod
    @property
    def ON_SCROLL(cls) -> SvgEvent:
        '''Occurs when a document view is being shifted along the X or Y or both axis. Only applicable to outermost svg elements.'''
        ...

    @classmethod
    @property
    def ON_ZOOM(cls) -> SvgEvent:
        '''Occurs when the zoom level of a document view is being changed. Only applicable to outermost svg elements.'''
        ...

    @classmethod
    @property
    def ON_BEGIN(cls) -> SvgEvent:
        '''Occurs when an animation element begins.'''
        ...

    @classmethod
    @property
    def ON_END(cls) -> SvgEvent:
        '''Occurs when an animation element ends.'''
        ...

    @classmethod
    @property
    def ON_REPEAT(cls) -> SvgEvent:
        '''Occurs when an animation element repeats.'''
        ...

    ...

class SvgExternalFontsHandling:
    '''Represents a way to handle external fonts used for text drawing.'''
    @classmethod
    @property
    def ADD_LINKS_TO_FONT_FILES(cls) -> SvgExternalFontsHandling:
        '''Add links to separate font files to style section of SVG file.'''
        ...

    @classmethod
    @property
    def EMBED(cls) -> SvgExternalFontsHandling:
        '''Save fonts data directly to SVG file. Please check all external fonts license agreements before using this option.'''
        ...

    @classmethod
    @property
    def VECTORIZE(cls) -> SvgExternalFontsHandling:
        '''Save all text using external fonts as graphics.'''
        ...

    ...

class TextInheritanceLimit:
    '''Controls the depth of the text properties inheritance.'''
    @classmethod
    @property
    def ALL(cls) -> TextInheritanceLimit:
        '''Inherit all text properties.'''
        ...

    @classmethod
    @property
    def TEXT_BOX(cls) -> TextInheritanceLimit:
        '''Inherit only from TextFrameEx's style.'''
        ...

    @classmethod
    @property
    def PARAGRAPH_ONLY(cls) -> TextInheritanceLimit:
        '''Use only properties defined for paragraph.'''
        ...

    ...

class TiffCompressionTypes:
    '''Provides options that control how a presentation is compressed in TIFF format.'''
    @classmethod
    @property
    def DEFAULT(cls) -> TiffCompressionTypes:
        '''Specifies the default compression scheme (LZW).'''
        ...

    @classmethod
    @property
    def NONE(cls) -> TiffCompressionTypes:
        '''Specifies no compression.'''
        ...

    @classmethod
    @property
    def CCITT3(cls) -> TiffCompressionTypes:
        '''Specifies the CCITT3 compression scheme.'''
        ...

    @classmethod
    @property
    def CCITT4(cls) -> TiffCompressionTypes:
        '''Specifies the CCITT4 compression scheme.'''
        ...

    @classmethod
    @property
    def LZW(cls) -> TiffCompressionTypes:
        '''Specifies the LZW compression scheme (Default).'''
        ...

    @classmethod
    @property
    def RLE(cls) -> TiffCompressionTypes:
        '''Specifies the RLE compression scheme.'''
        ...

    ...

class Zip64Mode:
    '''Specifies when to use ZIP64 format extensions for OpenXML file.'''
    @classmethod
    @property
    def NEVER(cls) -> Zip64Mode:
        '''Do not use ZIP64 format extensions.'''
        ...

    @classmethod
    @property
    def IF_NECESSARY(cls) -> Zip64Mode:
        '''Use ZIP64 format extensions if necessary.'''
        ...

    @classmethod
    @property
    def ALWAYS(cls) -> Zip64Mode:
        '''Always use ZIP64 format extensions.'''
        ...

    ...

