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

class IInk:
    '''Represents an ink object on a slide.'''
    @overload
    def get_thumbnail(self) -> aspose.pydrawing.Bitmap:
        ...

    @overload
    def get_thumbnail(self, bounds: ShapeThumbnailBounds, scale_x: float, scale_y: float) -> aspose.pydrawing.Bitmap:
        ...

    @overload
    def get_image(self) -> IImage:
        ...

    @overload
    def get_image(self, bounds: ShapeThumbnailBounds, scale_x: float, scale_y: float) -> IImage:
        ...

    @overload
    def write_as_svg(self, stream: io.RawIOBase) -> None:
        ...

    @overload
    def write_as_svg(self, stream: io.RawIOBase, svg_options: aspose.slides.export.ISVGOptions) -> None:
        ...

    def add_placeholder(self, placeholder_to_copy_from: IPlaceholder) -> IPlaceholder:
        ...

    def remove_placeholder(self) -> None:
        ...

    def get_base_placeholder(self) -> IShape:
        ...

    @property
    def traces(self) -> List[IInkTrace]:
        '''Gets all traces containing in the IInk element :py:class:`aspose.slides.ink.IInkTrace`.
                    Read-only.'''
        ...

    @property
    def as_i_graphical_object(self) -> IGraphicalObject:
        ...

    @property
    def shape_lock(self) -> IGraphicalObjectLock:
        ...

    @property
    def graphical_object_lock(self) -> IGraphicalObjectLock:
        ...

    @property
    def as_i_shape(self) -> IShape:
        ...

    @property
    def is_text_holder(self) -> bool:
        ...

    @property
    def placeholder(self) -> IPlaceholder:
        ...

    @property
    def custom_data(self) -> ICustomData:
        ...

    @property
    def raw_frame(self) -> IShapeFrame:
        ...

    @raw_frame.setter
    def raw_frame(self, value: IShapeFrame):
        ...

    @property
    def frame(self) -> IShapeFrame:
        ...

    @frame.setter
    def frame(self, value: IShapeFrame):
        ...

    @property
    def line_format(self) -> ILineFormat:
        ...

    @property
    def three_d_format(self) -> IThreeDFormat:
        ...

    @property
    def effect_format(self) -> IEffectFormat:
        ...

    @property
    def fill_format(self) -> IFillFormat:
        ...

    @property
    def hidden(self) -> bool:
        ...

    @hidden.setter
    def hidden(self, value: bool):
        ...

    @property
    def z_order_position(self) -> int:
        ...

    @property
    def connection_site_count(self) -> int:
        ...

    @property
    def rotation(self) -> float:
        ...

    @rotation.setter
    def rotation(self, value: float):
        ...

    @property
    def x(self) -> float:
        ...

    @x.setter
    def x(self, value: float):
        ...

    @property
    def y(self) -> float:
        ...

    @y.setter
    def y(self, value: float):
        ...

    @property
    def width(self) -> float:
        ...

    @width.setter
    def width(self, value: float):
        ...

    @property
    def height(self) -> float:
        ...

    @height.setter
    def height(self, value: float):
        ...

    @property
    def alternative_text(self) -> str:
        ...

    @alternative_text.setter
    def alternative_text(self, value: str):
        ...

    @property
    def alternative_text_title(self) -> str:
        ...

    @alternative_text_title.setter
    def alternative_text_title(self, value: str):
        ...

    @property
    def name(self) -> str:
        ...

    @name.setter
    def name(self, value: str):
        ...

    @property
    def is_decorative(self) -> bool:
        ...

    @is_decorative.setter
    def is_decorative(self, value: bool):
        ...

    @property
    def unique_id(self) -> int:
        ...

    @property
    def office_interop_shape_id(self) -> int:
        ...

    @property
    def is_grouped(self) -> bool:
        ...

    @property
    def black_white_mode(self) -> BlackWhiteMode:
        ...

    @black_white_mode.setter
    def black_white_mode(self, value: BlackWhiteMode):
        ...

    @property
    def parent_group(self) -> IGroupShape:
        ...

    @property
    def as_i_hyperlink_container(self) -> IHyperlinkContainer:
        ...

    @property
    def as_i_slide_component(self) -> ISlideComponent:
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def hyperlink_click(self) -> IHyperlink:
        ...

    @hyperlink_click.setter
    def hyperlink_click(self, value: IHyperlink):
        ...

    @property
    def hyperlink_mouse_over(self) -> IHyperlink:
        ...

    @hyperlink_mouse_over.setter
    def hyperlink_mouse_over(self, value: IHyperlink):
        ...

    @property
    def hyperlink_manager(self) -> IHyperlinkManager:
        ...

    ...

class IInkBrush:
    '''Represents trace brush.'''
    @property
    def color(self) -> aspose.pydrawing.Color:
        '''Gets or sets the brush color for a line.'''
        ...

    @color.setter
    def color(self, value: aspose.pydrawing.Color):
        '''Gets or sets the brush color for a line.'''
        ...

    @property
    def size(self) -> aspose.pydrawing.SizeF:
        '''Gets or sets the brush size for a line in points.'''
        ...

    @size.setter
    def size(self, value: aspose.pydrawing.SizeF):
        '''Gets or sets the brush size for a line in points.'''
        ...

    ...

class IInkTrace:
    '''Represents handwritten line in an Ink object.'''
    @property
    def brush(self) -> IInkBrush:
        '''Gets Brush for the IInkLine :py:class:`aspose.slides.ink.IInkBrush`
                    Read-only.'''
        ...

    @property
    def points(self) -> List[aspose.pydrawing.PointF]:
        '''Gets points for the IInkLine :py:class:`aspose.pydrawing.PointF`
                    Read-only.'''
        ...

    ...

class Ink(aspose.slides.GraphicalObject):
    '''Represents an ink object on a slide.'''
    @overload
    def get_thumbnail(self) -> aspose.pydrawing.Bitmap:
        '''Returns shape thumbnail.
                    ShapeThumbnailBounds.Shape shape thumbnail bounds type is used by default.
        :returns: Shape thumbnail.'''
        ...

    @overload
    def get_thumbnail(self, bounds: ShapeThumbnailBounds, scale_x: float, scale_y: float) -> aspose.pydrawing.Bitmap:
        '''Returns shape thumbnail.
        :param bounds: Shape thumbnail bounds type.
        :param scale_x: X scale
        :param scale_y: Y scale
        :returns: Shape thumbnail or null in case when ShapeThumbnailBounds.Appearance is used and a shape doesn't have visible elements.'''
        ...

    @overload
    def get_image(self) -> IImage:
        '''Returns shape thumbnail.
                    ShapeThumbnailBounds.Shape shape thumbnail bounds type is used by default.
        :returns: Shape thumbnail.'''
        ...

    @overload
    def get_image(self, bounds: ShapeThumbnailBounds, scale_x: float, scale_y: float) -> IImage:
        '''Returns shape thumbnail.
        :param bounds: Shape thumbnail bounds type.
        :param scale_x: X scale
        :param scale_y: Y scale
        :returns: Shape thumbnail or null in case when ShapeThumbnailBounds.Appearance is used and a shape doesn't have visible elements.'''
        ...

    @overload
    def write_as_svg(self, stream: io.RawIOBase) -> None:
        '''Saves content of Shape as SVG file.
        :param stream: Target stream'''
        ...

    @overload
    def write_as_svg(self, stream: io.RawIOBase, svg_options: aspose.slides.export.ISVGOptions) -> None:
        '''Saves content of Shape as SVG file.
        :param stream: Target stream
        :param svg_options: SVG generation options'''
        ...

    def remove_placeholder(self) -> None:
        '''Defines that this shape isn't a placeholder.'''
        ...

    def add_placeholder(self, placeholder_to_copy_from: IPlaceholder) -> IPlaceholder:
        '''Adds a new placeholder if there is no and sets placeholder properties to a specified one.
        :param placeholder_to_copy_from: Placeholder to copy content from.
        :returns: New :py:attr:`aspose.slides.Shape.placeholder`.'''
        ...

    def get_base_placeholder(self) -> IShape:
        '''Returns a basic placeholder shape (shape from the layout and/or master slide that the current shape is inherited from).'''
        ...

    @property
    def is_text_holder(self) -> bool:
        ...

    @property
    def placeholder(self) -> IPlaceholder:
        '''Returns the placeholder for a shape. Returns null if the shape has no placeholder.
                    Read-only :py:class:`aspose.slides.IPlaceholder`.'''
        ...

    @property
    def custom_data(self) -> ICustomData:
        ...

    @property
    def raw_frame(self) -> IShapeFrame:
        ...

    @raw_frame.setter
    def raw_frame(self, value: IShapeFrame):
        ...

    @property
    def frame(self) -> IShapeFrame:
        '''Returns or sets the shape frame's properties.
                    Read/write :py:class:`aspose.slides.IShapeFrame`.'''
        ...

    @frame.setter
    def frame(self, value: IShapeFrame):
        '''Returns or sets the shape frame's properties.
                    Read/write :py:class:`aspose.slides.IShapeFrame`.'''
        ...

    @property
    def line_format(self) -> ILineFormat:
        ...

    @property
    def three_d_format(self) -> IThreeDFormat:
        ...

    @property
    def effect_format(self) -> IEffectFormat:
        ...

    @property
    def fill_format(self) -> IFillFormat:
        ...

    @property
    def hyperlink_click(self) -> IHyperlink:
        ...

    @hyperlink_click.setter
    def hyperlink_click(self, value: IHyperlink):
        ...

    @property
    def hyperlink_mouse_over(self) -> IHyperlink:
        ...

    @hyperlink_mouse_over.setter
    def hyperlink_mouse_over(self, value: IHyperlink):
        ...

    @property
    def hyperlink_manager(self) -> IHyperlinkManager:
        ...

    @property
    def hidden(self) -> bool:
        '''Determines whether the shape is hidden.
                    Read/write :py:class:`bool`.'''
        ...

    @hidden.setter
    def hidden(self, value: bool):
        '''Determines whether the shape is hidden.
                    Read/write :py:class:`bool`.'''
        ...

    @property
    def z_order_position(self) -> int:
        ...

    @property
    def connection_site_count(self) -> int:
        ...

    @property
    def rotation(self) -> float:
        '''Returns or sets the number of degrees the specified shape is rotated around
                    the z-axis. A positive value indicates clockwise rotation; a negative value
                    indicates counterclockwise rotation.
                    Read/write :py:class:`float`.'''
        ...

    @rotation.setter
    def rotation(self, value: float):
        '''Returns or sets the number of degrees the specified shape is rotated around
                    the z-axis. A positive value indicates clockwise rotation; a negative value
                    indicates counterclockwise rotation.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def x(self) -> float:
        '''Returns or sets the x-coordinate of the upper-left corner of the shape.
                    Read/write :py:class:`float`.'''
        ...

    @x.setter
    def x(self, value: float):
        '''Returns or sets the x-coordinate of the upper-left corner of the shape.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def y(self) -> float:
        '''Returns or sets the y-coordinate of the upper-left corner of the shape.
                    Read/write :py:class:`float`.'''
        ...

    @y.setter
    def y(self, value: float):
        '''Returns or sets the y-coordinate of the upper-left corner of the shape.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def width(self) -> float:
        '''Returns or sets the width of the shape.
                    Read/write :py:class:`float`.'''
        ...

    @width.setter
    def width(self, value: float):
        '''Returns or sets the width of the shape.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def height(self) -> float:
        '''Returns or sets the height of the shape.
                    Read/write :py:class:`float`.'''
        ...

    @height.setter
    def height(self, value: float):
        '''Returns or sets the height of the shape.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def black_white_mode(self) -> BlackWhiteMode:
        ...

    @black_white_mode.setter
    def black_white_mode(self, value: BlackWhiteMode):
        ...

    @property
    def unique_id(self) -> int:
        ...

    @property
    def office_interop_shape_id(self) -> int:
        ...

    @property
    def alternative_text(self) -> str:
        ...

    @alternative_text.setter
    def alternative_text(self, value: str):
        ...

    @property
    def alternative_text_title(self) -> str:
        ...

    @alternative_text_title.setter
    def alternative_text_title(self, value: str):
        ...

    @property
    def name(self) -> str:
        '''Returns or sets the name of a shape.
                    Must be not null. Use empty string value if needed.
                    Read/write :py:class:`str`.'''
        ...

    @name.setter
    def name(self, value: str):
        '''Returns or sets the name of a shape.
                    Must be not null. Use empty string value if needed.
                    Read/write :py:class:`str`.'''
        ...

    @property
    def is_decorative(self) -> bool:
        ...

    @is_decorative.setter
    def is_decorative(self, value: bool):
        ...

    @property
    def shape_lock(self) -> IGraphicalObjectLock:
        ...

    @property
    def is_grouped(self) -> bool:
        ...

    @property
    def parent_group(self) -> IGroupShape:
        ...

    @property
    def slide(self) -> IBaseSlide:
        '''Returns the parent slide of a shape.
                    Read-only :py:class:`aspose.slides.IBaseSlide`.'''
        ...

    @property
    def presentation(self) -> IPresentation:
        '''Returns the parent presentation of a slide.
                    Read-only :py:class:`aspose.slides.IPresentation`.'''
        ...

    @property
    def graphical_object_lock(self) -> IGraphicalObjectLock:
        ...

    @property
    def traces(self) -> List[IInkTrace]:
        '''Gets all traces containing in the IInk element :py:class:`aspose.slides.ink.IInkTrace`.
                    Read-only.'''
        ...

    @property
    def as_i_hyperlink_container(self) -> IHyperlinkContainer:
        ...

    @property
    def as_i_slide_component(self) -> ISlideComponent:
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def as_i_shape(self) -> IShape:
        ...

    @property
    def as_i_graphical_object(self) -> IGraphicalObject:
        ...

    ...

class InkBrush:
    '''Represents an inkBrush object.'''
    @property
    def color(self) -> aspose.pydrawing.Color:
        '''Gets or sets the brush color for a line.'''
        ...

    @color.setter
    def color(self, value: aspose.pydrawing.Color):
        '''Gets or sets the brush color for a line.'''
        ...

    @property
    def size(self) -> aspose.pydrawing.SizeF:
        '''Gets or sets the brush size for a line in points.'''
        ...

    @size.setter
    def size(self, value: aspose.pydrawing.SizeF):
        '''Gets or sets the brush size for a line in points.'''
        ...

    ...

class InkTrace:
    '''Represents an Trace object.
                A Trace element is used to record the data captured by the digitizer. 
                It contains a sequence of points encoded according to the specification given by the InkTraceFormat object.'''
    @property
    def brush(self) -> IInkBrush:
        '''Gets Brush for the IInkLine :py:class:`aspose.slides.ink.IInkBrush`
                    Read-only.'''
        ...

    @property
    def points(self) -> List[aspose.pydrawing.PointF]:
        '''Gets points for the IInkLine :py:class:`aspose.pydrawing.PointF`
                    Read-only.'''
        ...

    ...

