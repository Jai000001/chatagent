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

class ShapeUtil:
    '''Offer methods which helps to process shapes objects.'''
    @staticmethod
    def graphics_path_to_geometry_path(graphics_path: aspose.pydrawing.Drawing2D.GraphicsPath) -> IGeometryPath:
        '''Converts a :py:class:`aspose.pydrawing.Drawing2D.GraphicsPath` to the :py:class:`aspose.slides.IGeometryPath`
        :param graphics_path: Graphics path
        :returns: Geometry path'''
        ...

    @staticmethod
    def geometry_path_to_graphics_path(geometry_path: IGeometryPath) -> aspose.pydrawing.Drawing2D.GraphicsPath:
        '''Converts :py:class:`aspose.slides.IGeometryPath` to :py:class:`aspose.pydrawing.Drawing2D.GraphicsPath`.
                    
                    GraphicsPath can be transformed in a different ways using its convenient methods and then transformed back into
                    the :py:class:`aspose.slides.IGeometryPath` to use in :py:class:`aspose.slides.GeometryShape` via :py:func:`Aspose.Slides.Util.ShapeUtil.GraphicsPathToGeometryPath(System.Drawing.Drawing2.` method.
        :returns: Graphics path'''
        ...

    ...

class SlideUtil:
    '''Offer methods which help to search shapes and text in a presentation.'''
    @overload
    @staticmethod
    def find_shape(pres: IPresentation, alt_text: str) -> IShape:
        '''Find shape by alternative text in a PPTX presentation.
        :param pres: Scanned presentation.
        :param alt_text: Alternative text of a shape.
        :returns: Shape or null.'''
        ...

    @overload
    @staticmethod
    def find_shape(slide: IBaseSlide, alt_text: str) -> IShape:
        '''Find shape by alternative text on a slide in a PPTX presentation.
        :param slide: Scanned slide.
        :param alt_text: Alternative text of a shape.
        :returns: Shape or null.'''
        ...

    @overload
    @staticmethod
    def align_shapes(alignment_type: ShapesAlignmentType, align_to_slide: bool, slide: IBaseSlide) -> None:
        '''Changes the placement of all shapes on the slide. Aligns shapes to the margins or the edge of the slide
                    or align them relative to each other.
        :param alignment_type: Determines which type of alignment will be applied.
        :param align_to_slide: If true, shapes will be aligned relative to the slide edges.
        :param slide: Parent slide.'''
        ...

    @overload
    @staticmethod
    def align_shapes(alignment_type: ShapesAlignmentType, align_to_slide: bool, slide: IBaseSlide, shape_indexes: List[int]) -> None:
        '''Changes the placement of selected shapes on the slide. Aligns shapes to the margins or the edge of the slide
                     or align them relative to each other.
        :param alignment_type: Determines which type of alignment will be applied.
        :param align_to_slide: If true, shapes will be aligned relative to the slide edges.
        :param slide: Parent slide.
        :param shape_indexes: Indexes of shapes to be aligned.'''
        ...

    @overload
    @staticmethod
    def align_shapes(alignment_type: ShapesAlignmentType, align_to_slide: bool, group_shape: IGroupShape) -> None:
        '''Changes the placement of all shapes within group shape. Aligns shapes to the margins or the edge of the slide
                    or align them relative to each other.
        :param alignment_type: Determines which type of alignment will be applied.
        :param align_to_slide: If true, shapes will be aligned relative to the slide edges.
        :param group_shape: Parent group shape.'''
        ...

    @overload
    @staticmethod
    def align_shapes(alignment_type: ShapesAlignmentType, align_to_slide: bool, group_shape: IGroupShape, shape_indexes: List[int]) -> None:
        '''Changes the placement of selected shapes within group shape. Aligns shapes to the margins or the edge of the slide
                    or align them relative to each other.
        :param alignment_type: Determines which type of alignment will be applied.
        :param align_to_slide: If true, shapes will be aligned relative to the slide edges.
        :param group_shape: Parent group shape.
        :param shape_indexes: Indexes of shapes to be aligned.'''
        ...

    @staticmethod
    def find_and_replace_text(presentation: IPresentation, with_masters: bool, find: str, replace: str, format: PortionFormat) -> None:
        '''Finds and replaces text in presentation with given format
        :param presentation: Scanned presentation.
        :param with_masters: Determines whether master slides should be scanned.
        :param find: String value to find.
        :param replace: String value to replace.
        :param format: Format for replacing text portion. If null then will be used format of the first 
                    character of the found string'''
        ...

    @staticmethod
    def get_all_text_boxes(slide: IBaseSlide) -> List[ITextFrame]:
        '''Returns all text frames on a slide in a PPTX presentation.
        :param slide: Scanned slide.
        :returns: Array of :py:class:`aspose.slides.TextFrame` objects.'''
        ...

    @staticmethod
    def get_all_text_frames(pres: IPresentation, with_masters: bool) -> List[ITextFrame]:
        '''Returns all text frames in a PPTX presentation.
        :param pres: Scanned presentation.
        :param with_masters: Determines whether master slides should be scanned.
        :returns: Array of :py:class:`aspose.slides.TextFrame` objects.'''
        ...

    ...

