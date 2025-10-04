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

class ISmartArt:
    '''Represents a SmartArt diagram.'''
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
    def all_nodes(self) -> ISmartArtNodeCollection:
        ...

    @property
    def nodes(self) -> ISmartArtNodeCollection:
        '''Returns collections of root nodes in SmartArt object.
                    Read-only :py:class:`aspose.slides.smartart.ISmartArtNodeCollection`.'''
        ...

    @property
    def layout(self) -> SmartArtLayoutType:
        '''Return or set layout of the SmartArt object.
                    Read/write :py:enum:`aspose.slides.smartart.SmartArtLayoutType`.'''
        ...

    @layout.setter
    def layout(self, value: SmartArtLayoutType):
        '''Return or set layout of the SmartArt object.
                    Read/write :py:enum:`aspose.slides.smartart.SmartArtLayoutType`.'''
        ...

    @property
    def quick_style(self) -> SmartArtQuickStyleType:
        ...

    @quick_style.setter
    def quick_style(self, value: SmartArtQuickStyleType):
        ...

    @property
    def color_style(self) -> SmartArtColorType:
        ...

    @color_style.setter
    def color_style(self, value: SmartArtColorType):
        ...

    @property
    def is_reversed(self) -> bool:
        ...

    @is_reversed.setter
    def is_reversed(self, value: bool):
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

class ISmartArtNode:
    '''Represents node of a SmartArt diagram.'''
    def remove(self) -> bool:
        '''Remove current node.
        :returns: ``True`` if removed succesfully, otherwise ``false``.'''
        ...

    @property
    def child_nodes(self) -> ISmartArtNodeCollection:
        ...

    @property
    def shapes(self) -> ISmartArtShapeCollection:
        '''Returns collections of all shapes associated with the node.
                    Read-only :py:class:`aspose.slides.smartart.ISmartArtShapeCollection`.'''
        ...

    @property
    def text_frame(self) -> ITextFrame:
        ...

    @property
    def is_assistant(self) -> bool:
        ...

    @is_assistant.setter
    def is_assistant(self, value: bool):
        ...

    @property
    def level(self) -> int:
        '''Returns nesting level of the node.
                    Read-only :py:class:`int`.'''
        ...

    @property
    def bullet_fill_format(self) -> IFillFormat:
        ...

    @property
    def position(self) -> int:
        '''Returns or sets zero-based position of the node among sibling nodes.
                    Read/write :py:class:`int`.'''
        ...

    @position.setter
    def position(self, value: int):
        '''Returns or sets zero-based position of the node among sibling nodes.
                    Read/write :py:class:`int`.'''
        ...

    @property
    def is_hidden(self) -> bool:
        ...

    @property
    def organization_chart_layout(self) -> OrganizationChartLayoutType:
        ...

    @organization_chart_layout.setter
    def organization_chart_layout(self, value: OrganizationChartLayoutType):
        ...

    ...

class ISmartArtNodeCollection:
    '''Represents a collection of SmartArt nodes.'''
    @overload
    def remove_node(self, index: int) -> None:
        '''Remove node or sub node by index.
        :param index: Zero-based index of node'''
        ...

    @overload
    def remove_node(self, node_obj: ISmartArtNode) -> None:
        '''Remove node or sub node.
        :param node_obj: Node to remove.'''
        ...

    def add_node(self) -> ISmartArtNode:
        '''Add new node or sub node.
        :returns: Added node'''
        ...

    def add_node_by_position(self, position: int) -> ISmartArtNode:
        '''Add new node in the selected position of nodes collection.
        :param position: Zero-base node position.
        :returns: Added node'''
        ...

    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> ISmartArtNode
        ...

    ...

class ISmartArtShape:
    '''Represents a shape inside SmartArt diagram'''
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

    def get_geometry_paths(self) -> List[IGeometryPath]:
        ...

    def set_geometry_path(self, geometry_path: IGeometryPath) -> None:
        ...

    def set_geometry_paths(self, geometry_paths: List[IGeometryPath]) -> None:
        ...

    def create_shape_elements(self) -> List[IShapeElement]:
        ...

    def add_placeholder(self, placeholder_to_copy_from: IPlaceholder) -> IPlaceholder:
        ...

    def remove_placeholder(self) -> None:
        ...

    def get_base_placeholder(self) -> IShape:
        ...

    @property
    def text_frame(self) -> ITextFrame:
        ...

    @property
    def as_i_geometry_shape(self) -> IGeometryShape:
        ...

    @property
    def shape_style(self) -> IShapeStyle:
        ...

    @property
    def shape_type(self) -> ShapeType:
        ...

    @shape_type.setter
    def shape_type(self, value: ShapeType):
        ...

    @property
    def adjustments(self) -> IAdjustValueCollection:
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
    def shape_lock(self) -> IBaseShapeLock:
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

class ISmartArtShapeCollection:
    '''Represents a collection of SmartArt shapes'''
    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> ISmartArtShape
        ...

    ...

class SmartArt(aspose.slides.GraphicalObject):
    '''Represents a SmartArt diagram'''
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
    def all_nodes(self) -> ISmartArtNodeCollection:
        ...

    @property
    def nodes(self) -> ISmartArtNodeCollection:
        '''Returns collections of root nodes in SmartArt object.
                    Read-only :py:class:`aspose.slides.smartart.ISmartArtNodeCollection`.'''
        ...

    @property
    def layout(self) -> SmartArtLayoutType:
        '''Returns or sets layout of the SmartArt object.
                    Read/write :py:enum:`aspose.slides.smartart.SmartArtLayoutType`.'''
        ...

    @layout.setter
    def layout(self, value: SmartArtLayoutType):
        '''Returns or sets layout of the SmartArt object.
                    Read/write :py:enum:`aspose.slides.smartart.SmartArtLayoutType`.'''
        ...

    @property
    def quick_style(self) -> SmartArtQuickStyleType:
        ...

    @quick_style.setter
    def quick_style(self, value: SmartArtQuickStyleType):
        ...

    @property
    def color_style(self) -> SmartArtColorType:
        ...

    @color_style.setter
    def color_style(self, value: SmartArtColorType):
        ...

    @property
    def is_reversed(self) -> bool:
        ...

    @is_reversed.setter
    def is_reversed(self, value: bool):
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

class SmartArtNode:
    '''Represents node of a SmartArt object'''
    def remove(self) -> bool:
        '''Remove current node.
        :returns: ``True`` if removed succesfully, otherwise ``false``'''
        ...

    @property
    def child_nodes(self) -> ISmartArtNodeCollection:
        ...

    @property
    def shapes(self) -> ISmartArtShapeCollection:
        '''Returns collections of all shapes associated with the node.
                    Read-only :py:class:`aspose.slides.smartart.ISmartArtShapeCollection`.'''
        ...

    @property
    def text_frame(self) -> ITextFrame:
        ...

    @property
    def is_assistant(self) -> bool:
        ...

    @is_assistant.setter
    def is_assistant(self, value: bool):
        ...

    @property
    def level(self) -> int:
        '''Returns nesting level of the node.
                    Read-only :py:class:`int`.'''
        ...

    @property
    def bullet_fill_format(self) -> IFillFormat:
        ...

    @property
    def position(self) -> int:
        '''Returns or sets zero-based position of node among sibling nodes.
                    Read/write :py:class:`int`.'''
        ...

    @position.setter
    def position(self, value: int):
        '''Returns or sets zero-based position of node among sibling nodes.
                    Read/write :py:class:`int`.'''
        ...

    @property
    def is_hidden(self) -> bool:
        ...

    @property
    def organization_chart_layout(self) -> OrganizationChartLayoutType:
        ...

    @organization_chart_layout.setter
    def organization_chart_layout(self, value: OrganizationChartLayoutType):
        ...

    ...

class SmartArtNodeCollection:
    '''Represents a collection of SmartArt nodes.'''
    @overload
    def remove_node(self, index: int) -> None:
        '''Remove node or sub node by index
        :param index: Zero-based index of node'''
        ...

    @overload
    def remove_node(self, node: ISmartArtNode) -> None:
        '''Remove node or sub node
        :param node: Node to remove'''
        ...

    def add_node(self) -> ISmartArtNode:
        '''Add new smart art node or sub node.
        :returns: Added node'''
        ...

    def add_node_by_position(self, position: int) -> ISmartArtNode:
        '''Add new node in the selected position of nodes collection
        :param position: Zero-base node position
        :returns: Added node'''
        ...

    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> ISmartArtNode
        ...

    ...

class SmartArtShape(aspose.slides.GeometryShape):
    '''Represents SmartArt shape'''
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

    def get_geometry_paths(self) -> List[IGeometryPath]:
        '''Returns the copy of path of the geometry shape. Coordinates are relative to the left top corner of the shape.
        :returns: Array of :py:class:`aspose.slides.IGeometryPath`'''
        ...

    def set_geometry_path(self, geometry_path: IGeometryPath) -> None:
        '''Updates shape geometry from :py:class:`aspose.slides.IGeometryPath` object. Coordinates must be relative to the left
                     top corner of the shape.
                     Changes the type of the shape (:py:attr:`aspose.slides.GeometryShape.shape_type`) to :py:attr:`aspose.slides.ShapeType.CUSTOM`.
        :param geometry_path: Geometry path'''
        ...

    def set_geometry_paths(self, geometry_paths: List[IGeometryPath]) -> None:
        '''Updates shape geometry from array of :py:class:`aspose.slides.IGeometryPath`. Coordinates must be relative to the left
                     top corner of the shape.
                     Changes the type of the shape (:py:attr:`aspose.slides.GeometryShape.shape_type`) to :py:attr:`aspose.slides.ShapeType.CUSTOM`.
        :param geometry_paths: Array geometry paths'''
        ...

    def create_shape_elements(self) -> List[IShapeElement]:
        '''Creates and returns array of shape's elements.
        :returns: Array of :py:class:`aspose.slides.ShapeElement`'''
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
    def shape_lock(self) -> IBaseShapeLock:
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
    def shape_style(self) -> IShapeStyle:
        ...

    @property
    def shape_type(self) -> ShapeType:
        ...

    @shape_type.setter
    def shape_type(self, value: ShapeType):
        ...

    @property
    def adjustments(self) -> IAdjustValueCollection:
        '''Returns a collection of shape's adjustment values.
                    Read-only :py:class:`aspose.slides.IAdjustValueCollection`.'''
        ...

    @property
    def text_frame(self) -> ITextFrame:
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
    def as_i_geometry_shape(self) -> IGeometryShape:
        ...

    ...

class SmartArtShapeCollection:
    '''Represents a collection of a SmartArt shapes'''
    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> ISmartArtShape
        ...

    ...

class OrganizationChartLayoutType:
    '''Represents formatting type the child nodes in an organization chart'''
    @classmethod
    @property
    def INITIAL(cls) -> OrganizationChartLayoutType:
        '''Initial layout type'''
        ...

    @classmethod
    @property
    def STANDART(cls) -> OrganizationChartLayoutType:
        '''Places child nodes horizontally below the parent node.'''
        ...

    @classmethod
    @property
    def BOTH_HANGING(cls) -> OrganizationChartLayoutType:
        '''Places child nodes vertically below the parent node on both the left and the right side.'''
        ...

    @classmethod
    @property
    def LEFT_HANGING(cls) -> OrganizationChartLayoutType:
        '''Places child nodes vertically below the parent node on the left side.'''
        ...

    @classmethod
    @property
    def RIGHT_HANGING(cls) -> OrganizationChartLayoutType:
        '''Places child nodes vertically below the parent node on the right side.'''
        ...

    ...

class SmartArtColorType:
    '''Represents color scheme of a SmartArt diagram.'''
    @classmethod
    @property
    def DARK_1_OUTLINE(cls) -> SmartArtColorType:
        '''Dark1Outline'''
        ...

    @classmethod
    @property
    def DARK_2_OUTLINE(cls) -> SmartArtColorType:
        '''Dark2Outline'''
        ...

    @classmethod
    @property
    def DARK_FILL(cls) -> SmartArtColorType:
        '''DarkFill'''
        ...

    @classmethod
    @property
    def COLORFUL_ACCENT_COLORS(cls) -> SmartArtColorType:
        '''ColorfulAccentColors'''
        ...

    @classmethod
    @property
    def COLORFUL_ACCENT_COLORS_2TO_3(cls) -> SmartArtColorType:
        '''ColorfulAccentColors2to3'''
        ...

    @classmethod
    @property
    def COLORFUL_ACCENT_COLORS_3TO_4(cls) -> SmartArtColorType:
        '''ColorfulAccentColors3to4'''
        ...

    @classmethod
    @property
    def COLORFUL_ACCENT_COLORS_4TO_5(cls) -> SmartArtColorType:
        '''ColorfulAccentColors4to5'''
        ...

    @classmethod
    @property
    def COLORFUL_ACCENT_COLORS_5TO_6(cls) -> SmartArtColorType:
        '''ColorfulAccentColors5to6'''
        ...

    @classmethod
    @property
    def COLORED_OUTLINE_ACCENT1(cls) -> SmartArtColorType:
        '''ColoredOutlineAccent1'''
        ...

    @classmethod
    @property
    def COLORED_FILL_ACCENT1(cls) -> SmartArtColorType:
        '''ColoredFillAccent1'''
        ...

    @classmethod
    @property
    def GRADIENT_RANGE_ACCENT1(cls) -> SmartArtColorType:
        '''GradientRangeAccent1'''
        ...

    @classmethod
    @property
    def GRADIENT_LOOP_ACCENT1(cls) -> SmartArtColorType:
        '''GradientLoopAccent1'''
        ...

    @classmethod
    @property
    def TRANSPARENT_GRADIENT_RANGE_ACCENT1(cls) -> SmartArtColorType:
        '''TransparentGradientRangeAccent1'''
        ...

    @classmethod
    @property
    def COLORED_OUTLINE_ACCENT2(cls) -> SmartArtColorType:
        '''ColoredOutlineAccent2'''
        ...

    @classmethod
    @property
    def COLORED_FILL_ACCENT2(cls) -> SmartArtColorType:
        '''ColoredFillAccent2'''
        ...

    @classmethod
    @property
    def GRADIENT_RANGE_ACCENT2(cls) -> SmartArtColorType:
        '''GradientRangeAccent2'''
        ...

    @classmethod
    @property
    def GRADIENT_LOOP_ACCENT2(cls) -> SmartArtColorType:
        '''GradientLoopAccent2'''
        ...

    @classmethod
    @property
    def TRANSPARENT_GRADIENT_RANGE_ACCENT2(cls) -> SmartArtColorType:
        '''TransparentGradientRangeAccent2'''
        ...

    @classmethod
    @property
    def COLORED_OUTLINE_ACCENT3(cls) -> SmartArtColorType:
        '''ColoredOutlineAccent3'''
        ...

    @classmethod
    @property
    def COLORED_FILL_ACCENT3(cls) -> SmartArtColorType:
        '''ColoredFillAccent3'''
        ...

    @classmethod
    @property
    def GRADIENT_RANGE_ACCENT3(cls) -> SmartArtColorType:
        '''GradientRangeAccent3'''
        ...

    @classmethod
    @property
    def GRADIENT_LOOP_ACCENT3(cls) -> SmartArtColorType:
        '''GradientLoopAccent3'''
        ...

    @classmethod
    @property
    def TRANSPARENT_GRADIENT_RANGE_ACCENT3(cls) -> SmartArtColorType:
        '''TransparentGradientRangeAccent3'''
        ...

    @classmethod
    @property
    def COLORED_OUTLINE_ACCENT4(cls) -> SmartArtColorType:
        '''ColoredOutlineAccent4'''
        ...

    @classmethod
    @property
    def COLORED_FILL_ACCENT4(cls) -> SmartArtColorType:
        '''ColoredFillAccent4'''
        ...

    @classmethod
    @property
    def GRADIENT_RANGE_ACCENT4(cls) -> SmartArtColorType:
        '''GradientRangeAccent4'''
        ...

    @classmethod
    @property
    def GRADIENT_LOOP_ACCENT4(cls) -> SmartArtColorType:
        '''GradientLoopAccent4'''
        ...

    @classmethod
    @property
    def TRANSPARENT_GRADIENT_RANGE_ACCENT4(cls) -> SmartArtColorType:
        '''TransparentGradientRangeAccent4'''
        ...

    @classmethod
    @property
    def COLORED_OUTLINE_ACCENT5(cls) -> SmartArtColorType:
        '''ColoredOutlineAccent5'''
        ...

    @classmethod
    @property
    def COLORED_FILL_ACCENT5(cls) -> SmartArtColorType:
        '''ColoredFillAccent5'''
        ...

    @classmethod
    @property
    def GRADIENT_RANGE_ACCENT5(cls) -> SmartArtColorType:
        '''GradientRangeAccent5'''
        ...

    @classmethod
    @property
    def GRADIENT_LOOP_ACCENT5(cls) -> SmartArtColorType:
        '''GradientLoopAccent5'''
        ...

    @classmethod
    @property
    def TRANSPARENT_GRADIENT_RANGE_ACCENT5(cls) -> SmartArtColorType:
        '''TransparentGradientRangeAccent5'''
        ...

    @classmethod
    @property
    def COLORED_OUTLINE_ACCENT6(cls) -> SmartArtColorType:
        '''ColoredOutlineAccent6'''
        ...

    @classmethod
    @property
    def COLORED_FILL_ACCENT6(cls) -> SmartArtColorType:
        '''ColoredFillAccent6'''
        ...

    @classmethod
    @property
    def GRADIENT_RANGE_ACCENT6(cls) -> SmartArtColorType:
        '''GradientRangeAccent6'''
        ...

    @classmethod
    @property
    def GRADIENT_LOOP_ACCENT6(cls) -> SmartArtColorType:
        '''GradientLoopAccent6'''
        ...

    @classmethod
    @property
    def TRANSPARENT_GRADIENT_RANGE_ACCENT6(cls) -> SmartArtColorType:
        '''TransparentGradientRangeAccent6'''
        ...

    ...

class SmartArtLayoutType:
    '''Represents layout type of a SmartArt diagram.'''
    @classmethod
    @property
    def ACCENT_PROCESS(cls) -> SmartArtLayoutType:
        '''Use to show a progression, a timeline, or sequential steps in a task, process, or workflow. Works well for illustrating both Level 1 and Level 2 text.'''
        ...

    @classmethod
    @property
    def ACCENTED_PICTURE(cls) -> SmartArtLayoutType:
        '''Use to show a central, photographic idea with related ideas on the side. The top Level 1 text appears over the central picture. Corresponding text for other Level 1 shapes appear next to the small circular pictures. This layout also works well with no text.'''
        ...

    @classmethod
    @property
    def ALTERNATING_FLOW(cls) -> SmartArtLayoutType:
        '''Use to show groups of information or sequential steps in a task, process, or workflow. Emphasizes the interaction or relationships among the groups of information.'''
        ...

    @classmethod
    @property
    def ALTERNATING_HEXAGONS(cls) -> SmartArtLayoutType:
        '''Use to represent a series of interconnected ideas. Level 1 text appears inside the hexagons. Level 2 text appears outside the shapes.'''
        ...

    @classmethod
    @property
    def ALTERNATING_PICTURE_BLOCKS(cls) -> SmartArtLayoutType:
        '''Use to show a series of pictures from top to bottom. Text appears alternately on the right or left of the picture.'''
        ...

    @classmethod
    @property
    def ALTERNATING_PICTURE_CIRCLES(cls) -> SmartArtLayoutType:
        '''Use to show a set of pictures with text. The corresponding text appears in the central circles with the images alternating from left to right.'''
        ...

    @classmethod
    @property
    def ARROW_RIBBON(cls) -> SmartArtLayoutType:
        '''Use to show either related or contrasting concepts with some connection, such as opposing forces. The first two lines of Level 1 text are used for text in the arrows. Unused text does not appear, but remains available if you switch layouts.'''
        ...

    @classmethod
    @property
    def ASCENDING_PICTURE_ACCENT_PROCESS(cls) -> SmartArtLayoutType:
        '''Use to show an ascending series of pictures with descriptive text. Works best with a small amount of text.'''
        ...

    @classmethod
    @property
    def BALANCE(cls) -> SmartArtLayoutType:
        '''Use to compare or show the relationship between two ideas. Each of the first two lines of Level 1 text corresponds to text at the top of one side of the center point. Emphasizes Level 2 text, which is limited to four shapes on each side of the center point. The balance tips towards the side with the most shapes containing Level 2 text. Unused text does not appear, but remains available if you switch layouts.'''
        ...

    @classmethod
    @property
    def BASIC_BENDING_PROCESS(cls) -> SmartArtLayoutType:
        '''Use to show a progression or sequential steps in a task, process, or workflow. Maximizes both horizontal and vertical display space for shapes.'''
        ...

    @classmethod
    @property
    def BASIC_BLOCK_LIST(cls) -> SmartArtLayoutType:
        '''Use to show non-sequential or grouped blocks of information. Maximizes both horizontal and vertical display space for shapes.'''
        ...

    @classmethod
    @property
    def BASIC_CHEVRON_PROCESS(cls) -> SmartArtLayoutType:
        '''Use to show a progression; a timeline; sequential steps in a task, process, or workflow; or to emphasize movement or direction. Level 1 text appears inside an arrow shape while Level 2 text appears below the arrow shapes.'''
        ...

    @classmethod
    @property
    def BASIC_CYCLE(cls) -> SmartArtLayoutType:
        '''Use to represent a continuing sequence of stages, tasks, or events in a circular flow. Emphasizes the stages or steps rather than the connecting arrows or flow. Works best with Level 1 text only.'''
        ...

    @classmethod
    @property
    def BASIC_MATRIX(cls) -> SmartArtLayoutType:
        '''Use to show the relationship of components to a whole in quadrants. The first four lines of Level 1 text appear in the quadrants. Unused text does not appear, but remains available if you switch layouts.'''
        ...

    @classmethod
    @property
    def BASIC_PIE(cls) -> SmartArtLayoutType:
        '''Use to show how individual parts form a whole. The first seven lines of Level 1 text correspond to the evenly distributed wedge or pie shapes. The top Level 1 text shape appears outside of the rest of the pie for emphasis. Unused text does not appear, but remains available if you switch layouts.'''
        ...

    @classmethod
    @property
    def BASIC_PROCESS(cls) -> SmartArtLayoutType:
        '''Use to show a progression or sequential steps in a task, process, or workflow.'''
        ...

    @classmethod
    @property
    def BASIC_PYRAMID(cls) -> SmartArtLayoutType:
        '''Use to show proportional, interconnected, or hierarchical relationships with the largest component on the bottom and narrowing up. Level 1 text appears in the pyramid segments and Level 2 text appears in shapes alongside each segment.'''
        ...

    @classmethod
    @property
    def BASIC_RADIAL(cls) -> SmartArtLayoutType:
        '''Use to show the relationship to a central idea in a cycle. The first line of Level 1 text corresponds to the central shape, and its Level 2 text corresponds to the surrounding circular shapes. Unused text does not appear, but remains available if you switch layouts.'''
        ...

    @classmethod
    @property
    def BASIC_TARGET(cls) -> SmartArtLayoutType:
        '''Use to show containment, gradations, or hierarchical relationships. The first five lines of Level 1 text are associated with a circle. Unused text does not appear, but remains available if you switch layouts.'''
        ...

    @classmethod
    @property
    def BASIC_TIMELINE(cls) -> SmartArtLayoutType:
        '''Use to show sequential steps in a task, process, or workflow, or to show timeline information. Works well with both Level 1 and Level 2 text.'''
        ...

    @classmethod
    @property
    def BASIC_VENN(cls) -> SmartArtLayoutType:
        '''Use to show overlapping or interconnected relationships. The first seven lines of Level 1 text correspond with a circle. If there are four or fewer lines of Level 1 text, the text is inside the circles. If there are more than four lines of Level 1 text, the text is outside of the circles. Unused text does not appear, but remains available if you switch layouts.'''
        ...

    @classmethod
    @property
    def BENDING_PICTURE_ACCENT_LIST(cls) -> SmartArtLayoutType:
        '''Use to show non-sequential or grouped blocks of information. The small circular shapes are designed to contain pictures. Works well for illustrating both Level 1 and Level 2 text. Maximizes both horizontal and vertical display space for shapes.'''
        ...

    @classmethod
    @property
    def BENDING_PICTURE_BLOCKS(cls) -> SmartArtLayoutType:
        '''Use to show a series of pictures. The box covering the bottom corner can contain small amounts of text.'''
        ...

    @classmethod
    @property
    def BENDING_PICTURE_CAPTION(cls) -> SmartArtLayoutType:
        '''Use to show a sequential series of pictures. The box covering the bottom corner can contain small amounts of text.'''
        ...

    @classmethod
    @property
    def BENDING_PICTURE_CAPTION_LIST(cls) -> SmartArtLayoutType:
        '''Use to show a series of pictures. The title and description appear in a callout shape under each picture.'''
        ...

    @classmethod
    @property
    def BENDING_PICTURE_SEMI_TRANSPARENT_TEXT(cls) -> SmartArtLayoutType:
        '''Use to show a series of pictures. A semi-transparent box covers the lower portion of the picture and contains all levels of text.'''
        ...

    @classmethod
    @property
    def BLOCK_CYCLE(cls) -> SmartArtLayoutType:
        '''Use to represent a continuing sequence of stages, tasks, or events in a circular flow. Emphasizes the stages or steps rather than the connecting arrows or flow.'''
        ...

    @classmethod
    @property
    def BUBBLE_PICTURE_LIST(cls) -> SmartArtLayoutType:
        '''Use to show a series of pictures. Can contain up to eight Level 1 pictures. Unused text and pictures do not appear, but remain available if you switch layouts. Works best with small amounts of text.'''
        ...

    @classmethod
    @property
    def CAPTIONED_PICTURES(cls) -> SmartArtLayoutType:
        '''Use to show pictures with multiple levels of text.  Works best with a small amount of Level 1 text and a medium amount of Level 2 text.'''
        ...

    @classmethod
    @property
    def CHEVRON_LIST(cls) -> SmartArtLayoutType:
        '''Use to show a progression through several processes that make up an overall workflow. Also works for illustrating contrasting processes. The Level 1 text corresponds to the first arrow shape on the left, while the Level 2 text corresponds to horizontal sub-steps for each shape that contains Level 1 text.'''
        ...

    @classmethod
    @property
    def CIRCLE_ACCENT_TIMELINE(cls) -> SmartArtLayoutType:
        '''Use to show a series of events or timeline information. Level 1 text appears next to larger circular shapes. Level 2 text appears next to smaller circular shapes.'''
        ...

    @classmethod
    @property
    def CIRCLE_ARROW_PROCESS(cls) -> SmartArtLayoutType:
        '''Use to show sequential items with supporting text for each item. This diagram works best with small amounts of Level 1 text.'''
        ...

    @classmethod
    @property
    def CIRCLE_PICTURE_HIERARCHY(cls) -> SmartArtLayoutType:
        '''Use to show hierarchical information or reporting relationships in an organization. Pictures appear in circles and corresponding text appears next to the pictures.'''
        ...

    @classmethod
    @property
    def CIRCLE_RELATIONSHIP(cls) -> SmartArtLayoutType:
        '''Use to show the relationship to or from a central idea. Level 2 text is added non-sequentially and is limited to five items. There can only be one Level 1 item.'''
        ...

    @classmethod
    @property
    def CIRCULAR_BENDING_PROCESS(cls) -> SmartArtLayoutType:
        '''Use to show a long or non-linear sequence or steps in a task, process, or workflow. Works best with Level 1 text only. Maximizes both horizontal and vertical display space for shapes.'''
        ...

    @classmethod
    @property
    def CIRCULAR_PICTURE_CALLOUT(cls) -> SmartArtLayoutType:
        '''Use to show a central idea and sub-ideas or related items. The text for the first picture covers the lower portion of the picture. The corresponding text for other Level 1 shapes appears next to the small circular pictures. This diagram also works well with no text.'''
        ...

    @classmethod
    @property
    def CLOSED_CHEVRON_PROCESS(cls) -> SmartArtLayoutType:
        '''Use to show a progression, a timeline, or sequential steps in a task, process, or workflow, or to emphasize movement or direction. Can be used to emphasize information in the starting shape. Works best with Level 1 text only.'''
        ...

    @classmethod
    @property
    def CONTINUOUS_ARROW_PROCESS(cls) -> SmartArtLayoutType:
        '''Use to show a timeline or sequential steps in a task, process, or workflow. Works best with Level 1 text because each line of Level 1 text appears inside the arrow shape. Level 2 text appears outside the arrow shape.'''
        ...

    @classmethod
    @property
    def CONTINUOUS_BLOCK_PROCESS(cls) -> SmartArtLayoutType:
        '''Use to show a progression or sequential steps in a task, process, or workflow. Works best with minimal Level 1 and Level 2 text.'''
        ...

    @classmethod
    @property
    def CONTINUOUS_CYCLE(cls) -> SmartArtLayoutType:
        '''Use to represent a continuing sequence of stages, tasks, or events in a circular flow. Emphasizes the connection between all components. Works best with Level 1 text only.'''
        ...

    @classmethod
    @property
    def CONTINUOUS_PICTURE_LIST(cls) -> SmartArtLayoutType:
        '''Use to show groups of interconnected information. The circular shapes are designed to contain pictures.'''
        ...

    @classmethod
    @property
    def CONVERGING_ARROWS(cls) -> SmartArtLayoutType:
        '''Use to show ideas or concepts that converge to a central point. Works best with Level 1 text only.'''
        ...

    @classmethod
    @property
    def CONVERGING_RADIAL(cls) -> SmartArtLayoutType:
        '''Use to show relationships of concepts or components to a central idea in a cycle. The first line of Level 1 text corresponds to the central circular shape and the lines of Level 2 text correspond to the surrounding rectangular shapes. Unused text does not appear, but remains available if you switch layouts.'''
        ...

    @classmethod
    @property
    def COUNTERBALANCE_ARROWS(cls) -> SmartArtLayoutType:
        '''Use to show two opposing ideas or concepts. Each of the first two lines of Level 1 text corresponds to an arrow and works well with Level 2 text. Unused text does not appear, but remains available if you switch layouts.'''
        ...

    @classmethod
    @property
    def CYCLE_MATRIX(cls) -> SmartArtLayoutType:
        '''Use to show the relationship to a central idea in a cyclical progression. Each of the first four lines of Level 1 text corresponds to a wedge or pie shape, and Level 2 text appears in a rectangular shape to the side of the wedge or pie shape. Unused text does not appear, but remains available if you switch layouts.'''
        ...

    @classmethod
    @property
    def DESCENDING_BLOCK_LIST(cls) -> SmartArtLayoutType:
        '''Use to show groups of related ideas or lists of information. The text shapes decrease in height sequentially, and the Level 1 text displays vertically.'''
        ...

    @classmethod
    @property
    def DESCENDING_PROCESS(cls) -> SmartArtLayoutType:
        '''Use to show a descending series of events. The first Level 1 text is at the top of arrow, and the last Level 1 text displays at the bottom of the arrow. Only the first seven Level 1 items appear. Works best with small to medium amounts of text.'''
        ...

    @classmethod
    @property
    def DETAILED_PROCESS(cls) -> SmartArtLayoutType:
        '''Use with large amounts of Level 2 text to show a progression through stages.'''
        ...

    @classmethod
    @property
    def DIVERGING_ARROWS(cls) -> SmartArtLayoutType:
        '''Use to show ideas or concepts that progress outward from a central source. Works best with Level 1 text only.'''
        ...

    @classmethod
    @property
    def DIVERGING_RADIAL(cls) -> SmartArtLayoutType:
        '''Use to show relationships to a central idea in a cycle. The first Level 1 line of text corresponds to the central circular shape. Emphasizes the surrounding circles rather than the central idea. Unused text does not appear, but remains available if you switch layouts.'''
        ...

    @classmethod
    @property
    def EQUATION(cls) -> SmartArtLayoutType:
        '''Use to show sequential steps or tasks that depict a plan or result. The last Level 1 line of text appears after the equals sign (=).Works best with Level 1 text only.'''
        ...

    @classmethod
    @property
    def FRAMED_TEXT_PICTURE(cls) -> SmartArtLayoutType:
        '''Use to show pictures with corresponding Level 1 text displayed in a frame.'''
        ...

    @classmethod
    @property
    def FUNNEL(cls) -> SmartArtLayoutType:
        '''Use to show the filtering of information or how parts merge into a whole. Emphasizes the final outcome. Can contain up to four lines of Level 1 text; the last of these four Level 1 text lines appears below the funnel and the other lines  correspond to a circular shape. Unused text does not appear, but remains available if you switch layouts.'''
        ...

    @classmethod
    @property
    def GEAR(cls) -> SmartArtLayoutType:
        '''Use to show interlocking ideas. Each of the first three lines of Level 1 text corresponds to a gear shape, and their corresponding Level 2 text appears in rectangles next to the gear shape. Unused text does not appear, but remains available if you switch layouts.'''
        ...

    @classmethod
    @property
    def GRID_MATRIX(cls) -> SmartArtLayoutType:
        '''Use to show the placement of concepts along two axes. Emphasizes the individual components rather than the whole. The first four lines of Level 1 text appear in the quadrants. Unused text does not appear, but remains available if you switch layouts.'''
        ...

    @classmethod
    @property
    def GROUPED_LIST(cls) -> SmartArtLayoutType:
        '''Use to show groups and sub-groups of information, or steps and sub-steps in a task, process, or workflow. Level 1 text corresponds to the top level horizontal shapes, and Level 2 text corresponds to vertical sub-steps under each related top level shape. Works well for emphasizing sub-groups or sub-steps, hierarchical information, or multiple lists of information.'''
        ...

    @classmethod
    @property
    def HALF_CIRCLE_ORGANIZATION_CHART(cls) -> SmartArtLayoutType:
        '''Use to show hierarchical information or reporting relationships in an organization. The assistant shapes and Org Chart hanging layouts are available with this layout.'''
        ...

    @classmethod
    @property
    def HEXAGON_CLUSTER(cls) -> SmartArtLayoutType:
        '''Use to show pictures with associated descriptive text. Small hexagons indicate the picture and text pair. Works best with small amounts of text.'''
        ...

    @classmethod
    @property
    def HIERARCHY(cls) -> SmartArtLayoutType:
        '''Use to show hierarchical relationships progressing from top to bottom.'''
        ...

    @classmethod
    @property
    def HIERARCHY_LIST(cls) -> SmartArtLayoutType:
        '''Use to show hierarchical relationships progressing across groups. Can also be used to group or list information.'''
        ...

    @classmethod
    @property
    def HORIZONTAL_BULLET_LIST(cls) -> SmartArtLayoutType:
        '''Use to show non-sequential or grouped lists of information. Works well with large amounts of text. All text has the same level of emphasis, and direction is not implied.'''
        ...

    @classmethod
    @property
    def HORIZONTAL_HIERARCHY(cls) -> SmartArtLayoutType:
        '''Use to show hierarchical relationships progressing horizontally. Works well for decision trees.'''
        ...

    @classmethod
    @property
    def HORIZONTAL_LABELED_HIERARCHY(cls) -> SmartArtLayoutType:
        '''Use to show hierarchical relationships progressing horizontally and grouped hierarchically. Emphasizes heading or level 1 text. The first line of Level 1 text appears in the shape at the beginning of the hierarchy, and the second and all subsequent lines of Level 1 text appear at the top of the tall rectangles.'''
        ...

    @classmethod
    @property
    def HORIZONTAL_MULTI_LEVEL_HIERARCHY(cls) -> SmartArtLayoutType:
        '''Use to show large amounts of hierarchical information progressing horizontally. The top of the hierarchy is displayed vertically. This layout supports many levels in the hierarchy.'''
        ...

    @classmethod
    @property
    def HORIZONTAL_ORGANIZATION_CHART(cls) -> SmartArtLayoutType:
        '''Use to show hierarchical information horizontally or reporting relationships in an organization. The assistant shape and the Org Chart hanging layouts are available with this layout.'''
        ...

    @classmethod
    @property
    def HORIZONTAL_PICTURE_LIST(cls) -> SmartArtLayoutType:
        '''Use to show non-sequential or grouped information with an emphasis on related pictures. The top shapes are designed to contain pictures.'''
        ...

    @classmethod
    @property
    def INCREASING_ARROWS_PROCESS(cls) -> SmartArtLayoutType:
        '''Use to show sequential and overlapping steps in a process. Limited to five Level 1 items. Level 2 can contain large amounts of text.'''
        ...

    @classmethod
    @property
    def INCREASING_CIRCLE_PROCESS(cls) -> SmartArtLayoutType:
        '''Use to show a series of steps, with the interior of the circle increasing with each step. Limited to seven Level 1 steps but unlimited Level 2 items. Works well with large amounts of Level 2 text.'''
        ...

    @classmethod
    @property
    def INVERTED_PYRAMID(cls) -> SmartArtLayoutType:
        '''Use to show proportional, interconnected, or hierarchical relationships with the largest component on the top and narrowing down. Level 1 text appears in the pyramid segments and Level 2 text appears in shapes alongside each segment.'''
        ...

    @classmethod
    @property
    def LABELED_HIERARCHY(cls) -> SmartArtLayoutType:
        '''Use to show hierarchical relationships progressing from top to bottom and grouped hierarchically. Emphasizes heading or level 1 text. The first line of Level 1 text appears in the shape at the beginning of the hierarchy, and all subsequent lines of Level 1 text appear to the left of the long rectangles.'''
        ...

    @classmethod
    @property
    def LINEAR_VENN(cls) -> SmartArtLayoutType:
        '''Use to show overlapping relationships in a sequence. Works best with Level 1 text only.'''
        ...

    @classmethod
    @property
    def LINED_LIST(cls) -> SmartArtLayoutType:
        '''Use to show large amounts of text divided into categories and subcategories. Works well with multiple levels of text. Text at the same level is separated by lines.'''
        ...

    @classmethod
    @property
    def MULTIDIRECTIONAL_CYCLE(cls) -> SmartArtLayoutType:
        '''Use to represent a continuing sequence of stages, tasks, or events that can occur in any direction.'''
        ...

    @classmethod
    @property
    def NAMEAND_TITLE_ORGANIZATION_CHART(cls) -> SmartArtLayoutType:
        '''Use to show hierarchical information or reporting relationships in an organization. To enter text in the title box, type directly in the smaller rectangular shape. The assistant shape and Org Chart hanging layouts are available with this layout.'''
        ...

    @classmethod
    @property
    def NESTED_TARGET(cls) -> SmartArtLayoutType:
        '''Use to show containment relationships. Each of the first three lines of Level 1 text correspond to the upper left text in the shapes, and Level 2 text corresponds to the smaller shapes. Works best with minimal Level 2 lines of text. Unused text does not appear, but remains available if you switch layouts.'''
        ...

    @classmethod
    @property
    def NONDIRECTIONAL_CYCLE(cls) -> SmartArtLayoutType:
        '''Use to represent a continuing sequence of stages, tasks, or events in a circular flow. Each shape has the same level of importance. Works well when direction does not need to be indicated.'''
        ...

    @classmethod
    @property
    def OPPOSING_ARROWS(cls) -> SmartArtLayoutType:
        '''Use to show two opposing ideas, or ideas that diverge from a central point. Each of the first two lines of Level 1 text corresponds to an arrow. Unused text does not appear, but remains available if you switch layouts.'''
        ...

    @classmethod
    @property
    def OPPOSING_IDEAS(cls) -> SmartArtLayoutType:
        '''Use to show two opposing or contrasting ideas. Can have one or two Level 1 items. Each Level 1 text can contain multiple sub-levels. Works well with large amounts of text.'''
        ...

    @classmethod
    @property
    def ORGANIZATION_CHART(cls) -> SmartArtLayoutType:
        '''Use to show hierarchical information or reporting relationships in an organization. The assistant shape and the Org Chart hanging layouts are available with this layout.'''
        ...

    @classmethod
    @property
    def PHASED_PROCESS(cls) -> SmartArtLayoutType:
        '''Use to show three phases of a process. Limited to three Level 1 items. The first two Level 1 items can each contain four Level 2 items, and the third Level 1 item can contain an unlimited number of Level 2 items.  Works best with small amounts of text.'''
        ...

    @classmethod
    @property
    def PICTURE_ACCENT_BLOCKS(cls) -> SmartArtLayoutType:
        '''Use to show a group of pictures in blocks starting from the corner. The corresponding text displays vertically. Works well as an accent on title or sub-title slides or for section breaks of a document.'''
        ...

    @classmethod
    @property
    def PICTURE_ACCENT_LIST(cls) -> SmartArtLayoutType:
        '''Use to show grouped or related information. The small shapes on the upper corners are designed to contain pictures. Emphasizes Level 2 text over Level 1 text, and is a good choice for large amounts of Level 2 text.'''
        ...

    @classmethod
    @property
    def PICTURE_ACCENT_PROCESS(cls) -> SmartArtLayoutType:
        '''Use to show sequential steps in a task, process, or workflow. The rectangular shapes in the background are designed to contain pictures.'''
        ...

    @classmethod
    @property
    def PICTURE_CAPTION_LIST(cls) -> SmartArtLayoutType:
        '''Use to show non-sequential or grouped blocks of information. The top shapes are designed to contain pictures and pictures are emphasized over text. Works well for pictures with short text captions.'''
        ...

    @classmethod
    @property
    def PICTURE_GRID(cls) -> SmartArtLayoutType:
        '''Use to show pictures laid out on a square grid. Best with a small amount of Level 1 text, which appears above the picture.'''
        ...

    @classmethod
    @property
    def PICTURE_LINEUP(cls) -> SmartArtLayoutType:
        '''Use to show a series of pictures side by side. Level 1 text covers the top of the picture. Level 2 text appears below the picture.'''
        ...

    @classmethod
    @property
    def PICTURE_STRIPS(cls) -> SmartArtLayoutType:
        '''Use to show a series of pictures from top to bottom with Level 1 text beside each.'''
        ...

    @classmethod
    @property
    def PIE_PROCESS(cls) -> SmartArtLayoutType:
        '''Use to show steps in a process with each pie slice increasing in size up to seven shapes.  Level 1 text displays vertically.'''
        ...

    @classmethod
    @property
    def PLUSAND_MINUS(cls) -> SmartArtLayoutType:
        '''Use to show the pros and cons of  two ideas. Each Level 1 text can contain multiple sub-levels. Works well with large amounts of text. Limited to two Level 1 items.'''
        ...

    @classmethod
    @property
    def PROCESS_ARROWS(cls) -> SmartArtLayoutType:
        '''Use to show information illustrating a process or workflow. Level 1 text appears in the circular shapes and Level 2 text appears in the arrow shapes. Works best for minimal text and to emphasize movement or direction.'''
        ...

    @classmethod
    @property
    def PROCESS_LIST(cls) -> SmartArtLayoutType:
        '''Use to show multiple groups of information or steps and sub-steps in a task, process, or workflow. Level 1 text corresponds to the top horizontal shapes, and Level 2 text corresponds to vertical sub-steps under each related top level shape.'''
        ...

    @classmethod
    @property
    def PYRAMID_LIST(cls) -> SmartArtLayoutType:
        '''Use to show proportional, interconnected, or hierarchical relationships. Text appears in the rectangular shapes on top of the pyramid background.'''
        ...

    @classmethod
    @property
    def RADIAL_CLUSTER(cls) -> SmartArtLayoutType:
        '''Use to show data that relates to a central idea or theme. The top Level 1 text appears in the center. Level 2 text appears in surrounding shapes. Can contain up to seven Level 2 shapes. Unused text does not appear, but remains available if you switch layouts. Works best with small amounts of text.'''
        ...

    @classmethod
    @property
    def RADIAL_CYCLE(cls) -> SmartArtLayoutType:
        '''Use to show the relationship to a central idea. Emphasizes both information in the center circle and how information in the outer ring of circles contributes to the central idea. The first Level 1 line of text corresponds to the central circle, and its Level 2 text corresponds to the outer ring of circles. Unused text does not appear, but remains available if you switch layouts.'''
        ...

    @classmethod
    @property
    def RADIAL_LIST(cls) -> SmartArtLayoutType:
        '''Use to show relationships to a central idea in a cycle. The center shape can contain a picture. Level 1 text appears in the smaller circles and any related Level 2 text appears to the side of the smaller circles.'''
        ...

    @classmethod
    @property
    def RADIAL_VENN(cls) -> SmartArtLayoutType:
        '''Use to show both overlapping relationships and the relationship to a central idea in a cycle. The first line of Level 1 text corresponds to the central shape and the lines of Level 2 text correspond to the surrounding circular shapes. Unused text does not appear, but remains available if you switch layouts.'''
        ...

    @classmethod
    @property
    def RANDOM_TO_RESULT_PROCESS(cls) -> SmartArtLayoutType:
        '''Use to show, through a series of steps, how several chaotic  ideas can result in a unified goal or idea. Supports multiple items of Level 1 text, but the first and last Level 1 corresponding shapes are fixed. Works best with small amounts of Level 1 text and medium amounts of Level 2 text.'''
        ...

    @classmethod
    @property
    def REPEATING_BENDING_PROCESS(cls) -> SmartArtLayoutType:
        '''Use to show a progression or sequential steps in a task, process, or workflow. Maximizes both horizontal and vertical display space for shapes.'''
        ...

    @classmethod
    @property
    def REVERSE_LIST(cls) -> SmartArtLayoutType:
        '''Use to change between two items. Only the first two items of text display, and each item can contain a large amount of text. Works well to show a change between two items or shift in order.'''
        ...

    @classmethod
    @property
    def SEGMENTED_CYCLE(cls) -> SmartArtLayoutType:
        '''Use to show a progression or a sequence of stages, tasks, or events in a circular flow. Emphasizes the interconnected pieces. Each of the first seven lines of Level 1 text corresponds to a wedge or pie shape. Unused text does not appear, but remains available if you switch layouts.'''
        ...

    @classmethod
    @property
    def SEGMENTED_PROCESS(cls) -> SmartArtLayoutType:
        '''Use to show a progression or sequential steps in a task, process, or workflow. Emphasizes Level 2 text, since each line appears in a separate shape.'''
        ...

    @classmethod
    @property
    def SEGMENTED_PYRAMID(cls) -> SmartArtLayoutType:
        '''Use to show containment, proportional, or interconnected relationships. The first nine lines of Level 1 text appear in the triangular shapes. Unused text does not appear, but remains available if you switch layouts. Works best with Level 1 text only.'''
        ...

    @classmethod
    @property
    def SNAPSHOT_PICTURE_LIST(cls) -> SmartArtLayoutType:
        '''Use to show pictures with explanatory text. Level 2 text can display lists of information. Works well with a large amount of  text.'''
        ...

    @classmethod
    @property
    def SPIRAL_PICTURE(cls) -> SmartArtLayoutType:
        '''Use to show a series of up to five pictures with corresponding Level 1 captions that spiral in to the center.'''
        ...

    @classmethod
    @property
    def SQUARE_ACCENT_LIST(cls) -> SmartArtLayoutType:
        '''Use to show lists of information divided into categories. Level 2 text appears beside a small square shape. Works well with large amounts of Level 2 text.'''
        ...

    @classmethod
    @property
    def STACKED_LIST(cls) -> SmartArtLayoutType:
        '''Use to show groups of information or steps in a task, process, or workflow. Circular shapes contain Level 1 text, and the corresponding rectangles contain Level 2 text. Works well for numerous details and minimal Level 1 text.'''
        ...

    @classmethod
    @property
    def STACKED_VENN(cls) -> SmartArtLayoutType:
        '''Use to show overlapping relationships. A good choice for emphasizing growth or gradation. Works best with Level 1 text only. The first seven lines of Level 1 text correspond to a circular shape. Unused text does not appear, but remains available if you switch layouts.'''
        ...

    @classmethod
    @property
    def STAGGERED_PROCESS(cls) -> SmartArtLayoutType:
        '''Use to show a downward progression through stages. Each of the first five lines of Level 1 text corresponds with a rectangle. Unused text does not appear, but remains available if you switch layouts.'''
        ...

    @classmethod
    @property
    def STEP_DOWN_PROCESS(cls) -> SmartArtLayoutType:
        '''Use to show a descending process with multiple steps and sub-steps. Works best with small amounts of text.'''
        ...

    @classmethod
    @property
    def STEP_UP_PROCESS(cls) -> SmartArtLayoutType:
        '''Use to show an ascending series of steps or lists of information.'''
        ...

    @classmethod
    @property
    def SUB_STEP_PROCESS(cls) -> SmartArtLayoutType:
        '''Use to show a multi-step process with sub-steps between each instance of Level 1 text. Works best with small amounts of text and is limited to seven Level 1 steps. Each Level 1 step can have unlimited sub-steps.'''
        ...

    @classmethod
    @property
    def TABLE_HIERARCHY(cls) -> SmartArtLayoutType:
        '''Use to show groups of information built from top to bottom, and the hierarchies within each group. This layout does not contain connecting lines.'''
        ...

    @classmethod
    @property
    def TABLE_LIST(cls) -> SmartArtLayoutType:
        '''Use to show grouped or related information of equal value. The first Level 1 line of text corresponds to the top shape and its Level 2 text is used for the subsequent lists.'''
        ...

    @classmethod
    @property
    def TARGET_LIST(cls) -> SmartArtLayoutType:
        '''Use to show interrelated or overlapping information. Each of the first seven lines of Level 1 text appears in the rectangular shape. Unused text does not appear, but remains available if you switch layouts. Works well with both Level 1 and Level 2 text.'''
        ...

    @classmethod
    @property
    def TEXT_CYCLE(cls) -> SmartArtLayoutType:
        '''Use to represent a continuing sequence of stages, tasks, or events in a circular flow. Emphasizes the arrows or flow rather than the stages or steps. Works best with Level 1 text only.'''
        ...

    @classmethod
    @property
    def TITLE_PICTURE_LINEUP(cls) -> SmartArtLayoutType:
        '''Use to show a series of pictures that each have their own title and description. Level 1 text appears in the box above the picture. Level 2 text appears below the picture.'''
        ...

    @classmethod
    @property
    def TITLED_MATRIX(cls) -> SmartArtLayoutType:
        '''Use to show the relationships of four quadrants to a whole. The first line of Level 1 text corresponds to the central shape, and the first four lines of Level 2 text appear in the quadrants. Unused text does not appear, but remains available if you switch layouts.'''
        ...

    @classmethod
    @property
    def TITLED_PICTURE_ACCENT_LIST(cls) -> SmartArtLayoutType:
        '''Use to show lists of information with an accent picture for each Level 2 text. Level 1 text displays in a separate box at the top of the list.'''
        ...

    @classmethod
    @property
    def TITLED_PICTURE_BLOCKS(cls) -> SmartArtLayoutType:
        '''Use to show a series of pictures. Level 1 text appears above each picture. Level 2 text appears to the side and slightly overlapping each picture.'''
        ...

    @classmethod
    @property
    def TRAPEZOID_LIST(cls) -> SmartArtLayoutType:
        '''Use to show grouped or related information of equal value. Works well with large amounts of text.'''
        ...

    @classmethod
    @property
    def UPWARD_ARROW(cls) -> SmartArtLayoutType:
        '''Use to show a progression or steps that trend upward in a task, process, or workflow. Each of the first five lines of Level 1 text corresponds to a point on the arrow. Works best with minimal text. Unused text does not appear, but remains available if you switch layouts.'''
        ...

    @classmethod
    @property
    def VERTICAL_ACCENT_LIST(cls) -> SmartArtLayoutType:
        '''Use to show lists of information. Level 2 text appears in rectangular shapes over vertical chevrons. Emphasizes Level 2 text over Level 1 text, and is a good choice for medium amounts of Level 2 text.'''
        ...

    @classmethod
    @property
    def VERTICAL_ARROW_LIST(cls) -> SmartArtLayoutType:
        '''Use to show a progression or sequential steps in a task, process, or workflow that move toward a common goal. Works well for bulleted lists of information.'''
        ...

    @classmethod
    @property
    def VERTICAL_BENDING_PROCESS(cls) -> SmartArtLayoutType:
        '''Use to show a progression or sequential steps in a task, process, or workflow. Maximizes both horizontal and vertical display space for shapes. Places more emphasis on the interrelationships among the shapes than on direction or movement.'''
        ...

    @classmethod
    @property
    def VERTICAL_BLOCK_LIST(cls) -> SmartArtLayoutType:
        '''Use to show groups of information or steps in a task, process, or workflow. Works well with large amounts of Level 2 text. A good choice for text with a main point and multiple sub-points.'''
        ...

    @classmethod
    @property
    def VERTICAL_BOX_LIST(cls) -> SmartArtLayoutType:
        '''Use to show several groups of information, especially groups with large amounts of Level 2 text. A good choice for bulleted lists of information.'''
        ...

    @classmethod
    @property
    def VERTICAL_BULLET_LIST(cls) -> SmartArtLayoutType:
        '''Use to show non-sequential or grouped blocks of information. Works well for lists with long headings or top level information.'''
        ...

    @classmethod
    @property
    def VERTICAL_CHEVRON_LIST(cls) -> SmartArtLayoutType:
        '''Use to show a progression or sequential steps in a task, process, or workflow, or to emphasize movement or direction. Emphasizes Level 2 text over Level 1 text, and is a good choice for large amounts of Level 2 text.'''
        ...

    @classmethod
    @property
    def VERTICAL_CIRCLE_LIST(cls) -> SmartArtLayoutType:
        '''Use to show sequential or grouped data. Works best for Level 1 text, which displays next to a large circular shape. Lower levels of text are separated with smaller circular shapes.'''
        ...

    @classmethod
    @property
    def VERTICAL_CURVED_LIST(cls) -> SmartArtLayoutType:
        '''Use to show a curved list of information. To add pictures to the accent circle shapes, apply a picture fill.'''
        ...

    @classmethod
    @property
    def VERTICAL_EQUATION(cls) -> SmartArtLayoutType:
        '''Use to show sequential steps or tasks that depict a plan or result. The last Level 1 line of text appears after the arrow. Works best with Level 1 text only.'''
        ...

    @classmethod
    @property
    def VERTICAL_PICTURE_ACCENT_LIST(cls) -> SmartArtLayoutType:
        '''Use to show non-sequential or grouped blocks of information. The small circles are designed to contain pictures.'''
        ...

    @classmethod
    @property
    def VERTICAL_PICTURE_LIST(cls) -> SmartArtLayoutType:
        '''Use to show non-sequential or grouped blocks of information. The small shapes on the left are designed to contain pictures.'''
        ...

    @classmethod
    @property
    def VERTICAL_PROCESS(cls) -> SmartArtLayoutType:
        '''Use to show a progression or sequential steps in a task, process, or workflow from top to bottom. Works best with Level 1 text, since the vertical space is limited.'''
        ...

    @classmethod
    @property
    def CUSTOM(cls) -> SmartArtLayoutType:
        '''Represents a SmartArt diagram with custom layout template'''
        ...

    @classmethod
    @property
    def PICTURE_ORGANIZATION_CHART(cls) -> SmartArtLayoutType:
        '''Use to show hierarchical information or reporting relationships in an organization, with corresponding pictures. The assistant shape and Org Chart hanging layouts are available with this layout.'''
        ...

    ...

class SmartArtQuickStyleType:
    '''Represents style scheme of a SmartArt diagram.'''
    @classmethod
    @property
    def SIMPLE_FILL(cls) -> SmartArtQuickStyleType:
        '''SimpleFill'''
        ...

    @classmethod
    @property
    def WHITE_OUTLINE(cls) -> SmartArtQuickStyleType:
        '''WhiteOutline'''
        ...

    @classmethod
    @property
    def SUBTLE_EFFECT(cls) -> SmartArtQuickStyleType:
        '''SubtleEffect'''
        ...

    @classmethod
    @property
    def MODERATE_EFFECT(cls) -> SmartArtQuickStyleType:
        '''ModerateEffect'''
        ...

    @classmethod
    @property
    def INTENCE_EFFECT(cls) -> SmartArtQuickStyleType:
        '''IntenceEffect'''
        ...

    @classmethod
    @property
    def POLISHED(cls) -> SmartArtQuickStyleType:
        '''Polished'''
        ...

    @classmethod
    @property
    def INSET(cls) -> SmartArtQuickStyleType:
        '''Inset'''
        ...

    @classmethod
    @property
    def CARTOON(cls) -> SmartArtQuickStyleType:
        '''Cartoon'''
        ...

    @classmethod
    @property
    def POWDER(cls) -> SmartArtQuickStyleType:
        '''Powder'''
        ...

    @classmethod
    @property
    def BRICK_SCENE(cls) -> SmartArtQuickStyleType:
        '''BrickScene'''
        ...

    @classmethod
    @property
    def FLAT_SCENE(cls) -> SmartArtQuickStyleType:
        '''FlatScene'''
        ...

    @classmethod
    @property
    def METALLIC_SCENE(cls) -> SmartArtQuickStyleType:
        '''MetallicScene'''
        ...

    @classmethod
    @property
    def SUNSET_SCENE(cls) -> SmartArtQuickStyleType:
        '''SunsetScene'''
        ...

    @classmethod
    @property
    def BIRDS_EYE_SCENE(cls) -> SmartArtQuickStyleType:
        '''BirdsEyeScene'''
        ...

    ...

