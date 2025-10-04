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

class Collect:
    '''Represents a group of methods intended to collect model objects of different types from :py:class:`aspose.slides.Presentation`.'''
    @staticmethod
    def shapes(pres: Presentation) -> Iterable[Shape]:
        '''Collects all instances of :py:class:`aspose.slides.Shape` in the :py:class:`aspose.slides.Presentation`.
        :param pres: Presentation to collect shapes
        :returns: Collection of all shapes that contain in the presentation'''
        ...

    ...

class Compress:
    '''Represents a group of methods intended to compress :py:class:`aspose.slides.Presentation`.'''
    @staticmethod
    def remove_unused_master_slides(pres: Presentation) -> None:
        '''Makes compression of the :py:class:`aspose.slides.Presentation` by removing unused master slides.
        :param pres: The presentation instance'''
        ...

    @staticmethod
    def remove_unused_layout_slides(pres: Presentation) -> None:
        '''Makes compression of the :py:class:`aspose.slides.Presentation` by removing unused layout slides.
        :param pres: The presentation instance'''
        ...

    @staticmethod
    def compress_embedded_fonts(pres: Presentation) -> None:
        '''Makes compression of the :py:class:`aspose.slides.Presentation` by removing unused characters from embedded fonts.
        :param pres: The presentation instance'''
        ...

    ...

class Convert:
    '''Represents a group of methods intended to convert :py:class:`aspose.slides.Presentation`.'''
    @overload
    @staticmethod
    def to_pdf(pres_path: str, out_path: str) -> None:
        '''Converts :py:class:`aspose.slides.Presentation` to PDF.
        :param pres_path: Path of the input presentation
        :param out_path: Output path'''
        ...

    @overload
    @staticmethod
    def to_pdf(pres_path: str, out_path: str, options: aspose.slides.export.IPdfOptions) -> None:
        '''Converts :py:class:`aspose.slides.Presentation` to PDF.
        :param pres_path: Path of the input presentation
        :param out_path: Output path
        :param options: Output PDF options'''
        ...

    @overload
    @staticmethod
    def to_pdf(pres: Presentation, out_path: str) -> None:
        '''Converts :py:class:`aspose.slides.Presentation` to PDF.
        :param pres: Input presentation
        :param out_path: Output path'''
        ...

    @overload
    @staticmethod
    def to_pdf(pres: Presentation, out_path: str, options: aspose.slides.export.IPdfOptions) -> None:
        '''Converts :py:class:`aspose.slides.Presentation` to PDF.
        :param pres: Input presentation
        :param out_path: Output path
        :param options: Output PDF options'''
        ...

    @overload
    @staticmethod
    def to_svg(pres_path: str) -> None:
        '''Converts :py:class:`aspose.slides.Presentation` to SVG.
        :param pres_path: Path of the input presentation'''
        ...

    @overload
    @staticmethod
    def to_svg(pres: Presentation, options: aspose.slides.export.ISVGOptions) -> None:
        '''Converts :py:class:`aspose.slides.Presentation` to SVG.
        :param pres: Input presentation
        :param options: SVG export options'''
        ...

    @staticmethod
    def auto_by_extension(pres_path: str, out_path: str) -> None:
        '''Converts :py:class:`aspose.slides.Presentation` using the passed output path extension to determine the required export format.
        :param pres_path: Path of the input presentation
        :param out_path: Output path'''
        ...

    ...

class ForEach:
    '''Represents a group of methods intended to iterate over different :py:class:`aspose.slides.Presentation` model objects.
                These methods can be useful if you need to iterate and change some Presentation' elements formatting or content,
                 e.g. change each portion formatting.'''
    ...

