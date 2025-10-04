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

class BaseOverrideThemeManager(BaseThemeManager):
    '''Base class for classes that provide access to different types of overriden themes.'''
    def create_theme_effective(self) -> IThemeEffectiveData:
        '''Returns the theme object.'''
        ...

    def apply_color_scheme(self, scheme: IExtraColorScheme) -> None:
        '''Applies extra color scheme to a slide.'''
        ...

    @property
    def override_theme(self) -> IOverrideTheme:
        ...

    @override_theme.setter
    def override_theme(self, value: IOverrideTheme):
        ...

    @property
    def is_override_theme_enabled(self) -> bool:
        ...

    @property
    def as_i_theme_manager(self) -> IThemeManager:
        ...

    ...

class BaseThemeManager:
    '''Base class for classes that provide access to different types of themes.'''
    ...

class ChartThemeManager(BaseOverrideThemeManager):
    '''Provides access to chart theme overriden.'''
    def create_theme_effective(self) -> IThemeEffectiveData:
        '''Returns the theme object.'''
        ...

    def apply_color_scheme(self, scheme: IExtraColorScheme) -> None:
        '''Applies extra color scheme to a slide.'''
        ...

    @property
    def override_theme(self) -> IOverrideTheme:
        ...

    @override_theme.setter
    def override_theme(self, value: IOverrideTheme):
        ...

    @property
    def is_override_theme_enabled(self) -> bool:
        ...

    @property
    def as_i_theme_manager(self) -> IThemeManager:
        ...

    ...

class ColorScheme:
    '''Stores theme-defined colors.'''
    @property
    def dark1(self) -> IColorFormat:
        '''First dark color in the scheme.
                    Read-only :py:class:`aspose.slides.IColorFormat`.'''
        ...

    @property
    def light1(self) -> IColorFormat:
        '''First light color in the scheme.
                    Read-only :py:class:`aspose.slides.IColorFormat`.'''
        ...

    @property
    def dark2(self) -> IColorFormat:
        '''Second dark color in the scheme.
                    Read-only :py:class:`aspose.slides.IColorFormat`.'''
        ...

    @property
    def light2(self) -> IColorFormat:
        '''Second light color in the scheme.
                    Read-only :py:class:`aspose.slides.IColorFormat`.'''
        ...

    @property
    def accent1(self) -> IColorFormat:
        '''First accent color in the scheme.
                    Read-only :py:class:`aspose.slides.IColorFormat`.'''
        ...

    @property
    def accent2(self) -> IColorFormat:
        '''Second accent color in the scheme.
                    Read-only :py:class:`aspose.slides.IColorFormat`.'''
        ...

    @property
    def accent3(self) -> IColorFormat:
        '''Third accent color in the scheme.
                    Read-only :py:class:`aspose.slides.IColorFormat`.'''
        ...

    @property
    def accent4(self) -> IColorFormat:
        '''Fourth accent color in the scheme.
                    Read-only :py:class:`aspose.slides.IColorFormat`.'''
        ...

    @property
    def accent5(self) -> IColorFormat:
        '''Fifth accent color in the scheme.
                    Read-only :py:class:`aspose.slides.IColorFormat`.'''
        ...

    @property
    def accent6(self) -> IColorFormat:
        '''Sixth accent color in the scheme.
                    Read-only :py:class:`aspose.slides.IColorFormat`.'''
        ...

    @property
    def hyperlink(self) -> IColorFormat:
        '''Color for the hyperlinks.
                    Read-only :py:class:`aspose.slides.IColorFormat`.'''
        ...

    @property
    def followed_hyperlink(self) -> IColorFormat:
        ...

    @property
    def slide(self) -> IBaseSlide:
        '''Returns the parent slide.
                    Read-only :py:class:`aspose.slides.IBaseSlide`.'''
        ...

    @property
    def presentation(self) -> IPresentation:
        '''Returns the parent presentation.
                    Read-only :py:class:`aspose.slides.IPresentation`.'''
        ...

    @property
    def as_i_slide_component(self) -> ISlideComponent:
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    ...

class EffectStyle:
    '''Represents an effect style.'''
    @property
    def effect_format(self) -> IEffectFormat:
        ...

    @property
    def three_d_format(self) -> IThreeDFormat:
        ...

    ...

class EffectStyleCollection:
    '''Represents a collection of effect styles.'''
    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IEffectStyle
        ...

    ...

class ExtraColorScheme:
    '''Represents an additional color scheme which can be assigned to a slide.'''
    @property
    def name(self) -> str:
        '''Returns a name of this scheme.
                    Read-only :py:class:`str`.'''
        ...

    @property
    def color_scheme(self) -> IColorScheme:
        ...

    ...

class ExtraColorSchemeCollection:
    '''Represents a collection of additional color schemes.'''
    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IExtraColorScheme
        ...

    ...

class FillFormatCollection:
    '''Represents the collection of fill styles.'''
    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IFillFormat
        ...

    ...

class FontScheme:
    '''Stores theme-defined fonts.'''
    @property
    def minor(self) -> IFonts:
        '''Returns the fonts collection for a "body" part of the slide.
                    Read-only :py:class:`aspose.slides.IFonts`.'''
        ...

    @property
    def major(self) -> IFonts:
        '''Returns the fonts collection for a "heading" part of the slide.
                    Read-only :py:class:`aspose.slides.IFonts`.'''
        ...

    @property
    def name(self) -> str:
        '''Returns the font scheme name.
                    Read/write :py:class:`str`.'''
        ...

    @name.setter
    def name(self, value: str):
        '''Returns the font scheme name.
                    Read/write :py:class:`str`.'''
        ...

    ...

class FormatScheme:
    '''Stores theme-defined formats for the shapes.'''
    @property
    def fill_styles(self) -> IFillFormatCollection:
        ...

    @property
    def line_styles(self) -> ILineFormatCollection:
        ...

    @property
    def effect_styles(self) -> IEffectStyleCollection:
        ...

    @property
    def background_fill_styles(self) -> IFillFormatCollection:
        ...

    @property
    def slide(self) -> IBaseSlide:
        '''Returns the parent slide.
                    Read-only :py:class:`aspose.slides.IBaseSlide`.'''
        ...

    @property
    def presentation(self) -> IPresentation:
        '''Returns the parent presentation.
                    Read-only :py:class:`aspose.slides.IPresentation`.'''
        ...

    @property
    def as_i_slide_component(self) -> ISlideComponent:
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    ...

class IColorScheme:
    '''Stores theme-defined colors.'''
    @property
    def dark1(self) -> IColorFormat:
        '''First dark color in the scheme.
                    Read-only :py:class:`aspose.slides.IColorFormat`.'''
        ...

    @property
    def light1(self) -> IColorFormat:
        '''First light color in the scheme.
                    Read-only :py:class:`aspose.slides.IColorFormat`.'''
        ...

    @property
    def dark2(self) -> IColorFormat:
        '''Second dark color in the scheme.
                    Read-only :py:class:`aspose.slides.IColorFormat`.'''
        ...

    @property
    def light2(self) -> IColorFormat:
        '''Second light color in the scheme.
                    Read-only :py:class:`aspose.slides.IColorFormat`.'''
        ...

    @property
    def accent1(self) -> IColorFormat:
        '''First accent color in the scheme.
                    Read-only :py:class:`aspose.slides.IColorFormat`.'''
        ...

    @property
    def accent2(self) -> IColorFormat:
        '''Second accent color in the scheme.
                    Read-only :py:class:`aspose.slides.IColorFormat`.'''
        ...

    @property
    def accent3(self) -> IColorFormat:
        '''Third accent color in the scheme.
                    Read-only :py:class:`aspose.slides.IColorFormat`.'''
        ...

    @property
    def accent4(self) -> IColorFormat:
        '''Fourth accent color in the scheme.
                    Read-only :py:class:`aspose.slides.IColorFormat`.'''
        ...

    @property
    def accent5(self) -> IColorFormat:
        '''Fifth accent color in the scheme.
                    Read-only :py:class:`aspose.slides.IColorFormat`.'''
        ...

    @property
    def accent6(self) -> IColorFormat:
        '''Sixth accent color in the scheme.
                    Read-only :py:class:`aspose.slides.IColorFormat`.'''
        ...

    @property
    def hyperlink(self) -> IColorFormat:
        '''Color for the hyperlinks.
                    Read-only :py:class:`aspose.slides.IColorFormat`.'''
        ...

    @property
    def followed_hyperlink(self) -> IColorFormat:
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

    ...

class IColorSchemeEffectiveData:
    '''Immutable object which contains effective color scheme properties.'''
    @property
    def dark1(self) -> aspose.pydrawing.Color:
        '''First dark color in the scheme.
                    Read-only :py:class:`aspose.pydrawing.Color`.'''
        ...

    @property
    def light1(self) -> aspose.pydrawing.Color:
        '''First light color in the scheme.
                    Read-only :py:class:`aspose.pydrawing.Color`.'''
        ...

    @property
    def dark2(self) -> aspose.pydrawing.Color:
        '''Second dark color in the scheme.
                    Read-only :py:class:`aspose.pydrawing.Color`.'''
        ...

    @property
    def light2(self) -> aspose.pydrawing.Color:
        '''Second light color in the scheme.
                    Read-only :py:class:`aspose.pydrawing.Color`.'''
        ...

    @property
    def accent1(self) -> aspose.pydrawing.Color:
        '''First accent color in the scheme.
                    Read-only :py:class:`aspose.pydrawing.Color`.'''
        ...

    @property
    def accent2(self) -> aspose.pydrawing.Color:
        '''Second accent color in the scheme.
                    Read-only :py:class:`aspose.pydrawing.Color`.'''
        ...

    @property
    def accent3(self) -> aspose.pydrawing.Color:
        '''Third accent color in the scheme.
                    Read-only :py:class:`aspose.pydrawing.Color`.'''
        ...

    @property
    def accent4(self) -> aspose.pydrawing.Color:
        '''Fourth accent color in the scheme.
                    Read-only :py:class:`aspose.pydrawing.Color`.'''
        ...

    @property
    def accent5(self) -> aspose.pydrawing.Color:
        '''Fifth accent color in the scheme.
                    Read-only :py:class:`aspose.pydrawing.Color`.'''
        ...

    @property
    def accent6(self) -> aspose.pydrawing.Color:
        '''Sixth accent color in the scheme.
                    Read-only :py:class:`aspose.pydrawing.Color`.'''
        ...

    @property
    def hyperlink(self) -> aspose.pydrawing.Color:
        '''Color for the hyperlinks.
                    Read-only :py:class:`aspose.pydrawing.Color`.'''
        ...

    @property
    def followed_hyperlink(self) -> aspose.pydrawing.Color:
        ...

    ...

class IEffectStyle:
    '''Represents an effect style.'''
    @property
    def effect_format(self) -> IEffectFormat:
        ...

    @property
    def three_d_format(self) -> IThreeDFormat:
        ...

    ...

class IEffectStyleCollection:
    '''Represents a collection of effect styles.'''
    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IEffectStyle
        ...

    ...

class IEffectStyleCollectionEffectiveData:
    '''Immutable object that represents a readonly collection of effective effect styles.'''
    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IEffectStyleEffectiveData
        ...

    ...

class IEffectStyleEffectiveData:
    '''Immutable object which contains effective effect style properties.'''
    @property
    def effect_format(self) -> IEffectFormatEffectiveData:
        ...

    @property
    def three_d_format(self) -> IThreeDFormatEffectiveData:
        ...

    ...

class IExtraColorScheme:
    '''Represents an additional color scheme which can be assigned to a slide.'''
    @property
    def name(self) -> str:
        '''Returns a name of this scheme.
                    Read-only :py:class:`str`.'''
        ...

    @property
    def color_scheme(self) -> IColorScheme:
        ...

    ...

class IExtraColorSchemeCollection:
    '''Represents a collection of additional color schemes.'''
    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IExtraColorScheme
        ...

    ...

class IFillFormatCollection:
    '''Represents the collection of fill styles.'''
    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IFillFormat
        ...

    ...

class IFillFormatCollectionEffectiveData:
    '''Immutable object that represents a readonly collection of effective fill formats.'''
    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IFillFormatEffectiveData
        ...

    ...

class IFontScheme:
    '''Stores theme-defined fonts.'''
    @property
    def minor(self) -> IFonts:
        '''Returns the fonts collection for a "body" part of the slide.
                    Read-only :py:class:`aspose.slides.IFonts`.'''
        ...

    @property
    def major(self) -> IFonts:
        '''Returns the fonts collection for a "heading" part of the slide.
                    Read-only :py:class:`aspose.slides.IFonts`.'''
        ...

    @property
    def name(self) -> str:
        '''Returns the font scheme name.
                    Read/write :py:class:`str`.'''
        ...

    @name.setter
    def name(self, value: str):
        '''Returns the font scheme name.
                    Read/write :py:class:`str`.'''
        ...

    ...

class IFontSchemeEffectiveData:
    '''Immutable object which contains effective font scheme properties.'''
    @property
    def minor(self) -> IFontsEffectiveData:
        '''Returns the fonts collection for a "body" part of the slide.
                    Read-only :py:class:`aspose.slides.IFontsEffectiveData`.'''
        ...

    @property
    def major(self) -> IFontsEffectiveData:
        '''Returns the fonts collection for a "heading" part of the slide.
                    Read-only :py:class:`aspose.slides.IFontsEffectiveData`.'''
        ...

    @property
    def name(self) -> str:
        '''Returns the font scheme name.
                    Read-only :py:class:`str`.'''
        ...

    ...

class IFormatScheme:
    '''Stores theme-defined formats for the shapes.'''
    @property
    def fill_styles(self) -> IFillFormatCollection:
        ...

    @property
    def line_styles(self) -> ILineFormatCollection:
        ...

    @property
    def effect_styles(self) -> IEffectStyleCollection:
        ...

    @property
    def background_fill_styles(self) -> IFillFormatCollection:
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

    ...

class IFormatSchemeEffectiveData:
    '''Immutable object which contains effective format scheme properties.'''
    def get_fill_styles(self, style_color: aspose.pydrawing.Color) -> IFillFormatCollectionEffectiveData:
        '''Returns a collection of theme defined fill styles.
        :param style_color: Color :py:class:`aspose.pydrawing.Color`
        :returns: Collection of effective fill formats :py:class:`aspose.slides.theme.IFillFormatCollectionEffectiveData`'''
        ...

    def get_line_styles(self, style_color: aspose.pydrawing.Color) -> ILineFormatCollectionEffectiveData:
        '''Returns a collection of theme defined line styles.
        :param style_color: Color :py:class:`aspose.pydrawing.Color`
        :returns: Collection of effective line formats :py:class:`aspose.slides.theme.ILineFormatCollectionEffectiveData`'''
        ...

    def get_effect_styles(self, style_color: aspose.pydrawing.Color) -> IEffectStyleCollectionEffectiveData:
        '''Returns a collection of theme defined effect styles.
        :param style_color: Color :py:class:`aspose.pydrawing.Color`
        :returns: Collection of effective effect styles :py:class:`aspose.slides.theme.IEffectStyleCollectionEffectiveData`'''
        ...

    def get_background_fill_styles(self, style_color: aspose.pydrawing.Color) -> IFillFormatCollectionEffectiveData:
        '''Returns a collection of theme defined background fill styles.
        :param style_color: Color :py:class:`aspose.pydrawing.Color`
        :returns: Collection of effective background fill formats :py:class:`aspose.slides.theme.IFillFormatCollectionEffectiveData`'''
        ...

    ...

class ILineFormatCollection:
    '''Represents the collection of line styles.'''
    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> ILineFormat
        ...

    ...

class ILineFormatCollectionEffectiveData:
    '''Immutable object that represents a readonly collection of effective line formats.'''
    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> ILineFormatEffectiveData
        ...

    ...

class IMasterTheme:
    '''Represents a master theme.'''
    def get_effective(self) -> IThemeEffectiveData:
        ...

    @property
    def extra_color_schemes(self) -> IExtraColorSchemeCollection:
        ...

    @property
    def name(self) -> str:
        '''Returns the name of a theme.
                    Read/write :py:class:`str`.'''
        ...

    @name.setter
    def name(self, value: str):
        '''Returns the name of a theme.
                    Read/write :py:class:`str`.'''
        ...

    @property
    def as_i_theme(self) -> ITheme:
        ...

    @property
    def color_scheme(self) -> IColorScheme:
        ...

    @property
    def font_scheme(self) -> IFontScheme:
        ...

    @property
    def format_scheme(self) -> IFormatScheme:
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    ...

class IMasterThemeManager:
    '''Provides access to presentation master theme.'''
    def create_theme_effective(self) -> IThemeEffectiveData:
        ...

    def apply_color_scheme(self, scheme: IExtraColorScheme) -> None:
        ...

    @property
    def is_override_theme_enabled(self) -> bool:
        ...

    @is_override_theme_enabled.setter
    def is_override_theme_enabled(self, value: bool):
        ...

    @property
    def override_theme(self) -> IMasterTheme:
        ...

    @override_theme.setter
    def override_theme(self, value: IMasterTheme):
        ...

    @property
    def as_i_theme_manager(self) -> IThemeManager:
        ...

    ...

class IMasterThemeable:
    '''Represent master theme manager.'''
    def create_theme_effective(self) -> IThemeEffectiveData:
        ...

    @property
    def theme_manager(self) -> IMasterThemeManager:
        ...

    @property
    def as_i_themeable(self) -> IThemeable:
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

    ...

class IOverrideTheme:
    '''Represents a overriding theme.'''
    def init_color_scheme(self) -> None:
        '''Init ColorScheme with new object for overriding ColorScheme of InheritedTheme.'''
        ...

    def init_color_scheme_from(self, color_scheme: IColorScheme) -> None:
        '''Init ColorScheme with new object for overriding ColorScheme of InheritedTheme.
        :param color_scheme: Data to initialize from.'''
        ...

    def init_color_scheme_from_inherited(self) -> None:
        '''Init ColorScheme with new object for overriding ColorScheme of InheritedTheme. And initialize data of this new object with data of the ColorScheme of InheritedTheme.'''
        ...

    def init_font_scheme(self) -> None:
        '''Init FontScheme with new object for overriding FontScheme of InheritedTheme.'''
        ...

    def init_font_scheme_from(self, font_scheme: IFontScheme) -> None:
        '''Init FontScheme with new object for overriding FontScheme of InheritedTheme.
        :param font_scheme: Data to initialize from.'''
        ...

    def init_font_scheme_from_inherited(self) -> None:
        '''Init FontScheme with new object for overriding FontScheme of InheritedTheme. And initialize data of this new object with data of the FontScheme of InheritedTheme.'''
        ...

    def init_format_scheme(self) -> None:
        '''Init FormatScheme with new object for overriding FormatScheme of InheritedTheme.'''
        ...

    def init_format_scheme_from(self, format_scheme: IFormatScheme) -> None:
        '''Init FormatScheme with new object for overriding FormatScheme of InheritedTheme.
        :param format_scheme: Data to initialize from.'''
        ...

    def init_format_scheme_from_inherited(self) -> None:
        '''Init FormatScheme with new object for overriding FormatScheme of InheritedTheme. And initialize data of this new object with data of the FormatScheme of InheritedTheme.'''
        ...

    def clear(self) -> None:
        '''Set ColorScheme, FontScheme, FormatScheme to null to disable any overriding with this theme object.'''
        ...

    def get_effective(self) -> IThemeEffectiveData:
        ...

    @property
    def is_empty(self) -> bool:
        ...

    @property
    def as_i_theme(self) -> ITheme:
        ...

    @property
    def color_scheme(self) -> IColorScheme:
        ...

    @property
    def font_scheme(self) -> IFontScheme:
        ...

    @property
    def format_scheme(self) -> IFormatScheme:
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    ...

class IOverrideThemeManager:
    '''Provides access to different types of overriden themes.'''
    def create_theme_effective(self) -> IThemeEffectiveData:
        ...

    def apply_color_scheme(self, scheme: IExtraColorScheme) -> None:
        ...

    @property
    def is_override_theme_enabled(self) -> bool:
        ...

    @property
    def override_theme(self) -> IOverrideTheme:
        ...

    @override_theme.setter
    def override_theme(self, value: IOverrideTheme):
        ...

    @property
    def as_i_theme_manager(self) -> IThemeManager:
        ...

    ...

class IOverrideThemeable:
    '''Represents override theme manager.'''
    def create_theme_effective(self) -> IThemeEffectiveData:
        ...

    @property
    def theme_manager(self) -> IOverrideThemeManager:
        ...

    @property
    def as_i_themeable(self) -> IThemeable:
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

    ...

class ITheme:
    '''Represents a theme.'''
    def get_effective(self) -> IThemeEffectiveData:
        '''Gets effective theme data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.theme.IThemeEffectiveData`.'''
        ...

    @property
    def color_scheme(self) -> IColorScheme:
        ...

    @property
    def font_scheme(self) -> IFontScheme:
        ...

    @property
    def format_scheme(self) -> IFormatScheme:
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    ...

class IThemeEffectiveData:
    '''Immutable object which contains effective theme properties.'''
    def get_color_scheme(self, style_color: aspose.pydrawing.Color) -> IColorSchemeEffectiveData:
        '''Returns the color scheme.
        :param style_color: Color :py:class:`aspose.pydrawing.Color`
        :returns: Color scheme :py:class:`aspose.slides.theme.IColorSchemeEffectiveData`'''
        ...

    @property
    def font_scheme(self) -> IFontSchemeEffectiveData:
        ...

    @property
    def format_scheme(self) -> IFormatSchemeEffectiveData:
        ...

    ...

class IThemeManager:
    '''Represent theme properties.'''
    def create_theme_effective(self) -> IThemeEffectiveData:
        '''Returns the theme object.
        :returns: Theme object :py:class:`aspose.slides.theme.IThemeEffectiveData`'''
        ...

    def apply_color_scheme(self, scheme: IExtraColorScheme) -> None:
        '''Applies extra color scheme to a slide.
        :param scheme: Extra color scheme :py:class:`aspose.slides.theme.IExtraColorScheme`'''
        ...

    ...

class IThemeable:
    '''Represents objects that can be themed with :py:class:`aspose.slides.theme.ITheme`.'''
    def create_theme_effective(self) -> IThemeEffectiveData:
        '''Returns an effective theme for this themeable object.
        :returns: Effective theme :py:class:`aspose.slides.theme.IThemeEffectiveData`'''
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

    ...

class LayoutSlideThemeManager(BaseOverrideThemeManager):
    '''Provides access to layout slide theme overriden.'''
    def create_theme_effective(self) -> IThemeEffectiveData:
        '''Returns the theme object.'''
        ...

    def apply_color_scheme(self, scheme: IExtraColorScheme) -> None:
        '''Applies extra color scheme to a slide.'''
        ...

    @property
    def override_theme(self) -> IOverrideTheme:
        ...

    @override_theme.setter
    def override_theme(self, value: IOverrideTheme):
        ...

    @property
    def is_override_theme_enabled(self) -> bool:
        ...

    @property
    def as_i_theme_manager(self) -> IThemeManager:
        ...

    ...

class LineFormatCollection:
    '''Represents the collection of line styles.'''
    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> ILineFormat
        ...

    ...

class MasterTheme(Theme):
    '''Represents a master theme.'''
    def get_effective(self) -> IThemeEffectiveData:
        '''Gets effective theme data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.theme.IThemeEffectiveData`.'''
        ...

    @property
    def color_scheme(self) -> IColorScheme:
        ...

    @property
    def font_scheme(self) -> IFontScheme:
        ...

    @property
    def format_scheme(self) -> IFormatScheme:
        ...

    @property
    def presentation(self) -> IPresentation:
        '''Returns the parent presentation.
                    Read-only :py:class:`aspose.slides.IPresentation`.'''
        ...

    @property
    def extra_color_schemes(self) -> IExtraColorSchemeCollection:
        ...

    @property
    def name(self) -> str:
        '''Returns the name of a theme.
                    Read/write :py:class:`str`.'''
        ...

    @name.setter
    def name(self, value: str):
        '''Returns the name of a theme.
                    Read/write :py:class:`str`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def as_i_theme(self) -> ITheme:
        ...

    ...

class MasterThemeManager(BaseThemeManager):
    '''Provides access to presentation master theme.'''
    def create_theme_effective(self) -> IThemeEffectiveData:
        '''Returns the theme object.'''
        ...

    def apply_color_scheme(self, scheme: IExtraColorScheme) -> None:
        '''Applies extra color scheme to a slide.'''
        ...

    @property
    def override_theme(self) -> IMasterTheme:
        ...

    @override_theme.setter
    def override_theme(self, value: IMasterTheme):
        ...

    @property
    def is_override_theme_enabled(self) -> bool:
        ...

    @is_override_theme_enabled.setter
    def is_override_theme_enabled(self, value: bool):
        ...

    @property
    def as_i_theme_manager(self) -> IThemeManager:
        ...

    ...

class NotesSlideThemeManager(BaseOverrideThemeManager):
    '''Provides access to notes slide theme overriden.'''
    def create_theme_effective(self) -> IThemeEffectiveData:
        '''Returns the theme object.'''
        ...

    def apply_color_scheme(self, scheme: IExtraColorScheme) -> None:
        '''Applies extra color scheme to a slide.'''
        ...

    @property
    def override_theme(self) -> IOverrideTheme:
        ...

    @override_theme.setter
    def override_theme(self, value: IOverrideTheme):
        ...

    @property
    def is_override_theme_enabled(self) -> bool:
        ...

    @property
    def as_i_theme_manager(self) -> IThemeManager:
        ...

    ...

class OverrideTheme(Theme):
    '''Represents a overriding theme.'''
    def get_effective(self) -> IThemeEffectiveData:
        '''Gets effective theme data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.theme.IThemeEffectiveData`.'''
        ...

    def init_color_scheme(self) -> None:
        '''Init ColorScheme with new object for overriding ColorScheme of InheritedTheme.'''
        ...

    def init_color_scheme_from(self, color_scheme: IColorScheme) -> None:
        '''Init ColorScheme with new object for overriding ColorScheme of InheritedTheme.
        :param color_scheme: Data to initialize from.'''
        ...

    def init_color_scheme_from_inherited(self) -> None:
        '''Init ColorScheme with new object for overriding ColorScheme of InheritedTheme. And initialize data of this new object with data of the ColorScheme of InheritedTheme.'''
        ...

    def init_font_scheme(self) -> None:
        '''Init FontScheme with new object for overriding FontScheme of InheritedTheme.'''
        ...

    def init_font_scheme_from(self, font_scheme: IFontScheme) -> None:
        '''Init FontScheme with new object for overriding FontScheme of InheritedTheme.
        :param font_scheme: Data to initialize from.'''
        ...

    def init_font_scheme_from_inherited(self) -> None:
        '''Init FontScheme with new object for overriding FontScheme of InheritedTheme. And initialize data of this new object with data of the FontScheme of InheritedTheme.'''
        ...

    def init_format_scheme(self) -> None:
        '''Init FormatScheme with new object for overriding FormatScheme of InheritedTheme.'''
        ...

    def init_format_scheme_from(self, format_scheme: IFormatScheme) -> None:
        '''Init FormatScheme with new object for overriding FormatScheme of InheritedTheme.
        :param format_scheme: Data to initialize from.'''
        ...

    def init_format_scheme_from_inherited(self) -> None:
        '''Init FormatScheme with new object for overriding FormatScheme of InheritedTheme. And initialize data of this new object with data of the FormatScheme of InheritedTheme.'''
        ...

    def clear(self) -> None:
        '''Set ColorScheme, FontScheme, FormatScheme to null to disable any overriding with this theme object.'''
        ...

    @property
    def color_scheme(self) -> IColorScheme:
        ...

    @property
    def font_scheme(self) -> IFontScheme:
        ...

    @property
    def format_scheme(self) -> IFormatScheme:
        ...

    @property
    def presentation(self) -> IPresentation:
        '''Returns the parent presentation.
                    Read-only :py:class:`aspose.slides.IPresentation`.'''
        ...

    @property
    def is_empty(self) -> bool:
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def as_i_theme(self) -> ITheme:
        ...

    ...

class SlideThemeManager(BaseOverrideThemeManager):
    '''Provides access to slide theme overriden.'''
    def create_theme_effective(self) -> IThemeEffectiveData:
        '''Returns the theme object.'''
        ...

    def apply_color_scheme(self, scheme: IExtraColorScheme) -> None:
        '''Applies extra color scheme to a slide.'''
        ...

    @property
    def override_theme(self) -> IOverrideTheme:
        ...

    @override_theme.setter
    def override_theme(self, value: IOverrideTheme):
        ...

    @property
    def is_override_theme_enabled(self) -> bool:
        ...

    @property
    def as_i_theme_manager(self) -> IThemeManager:
        ...

    ...

class Theme:
    '''Represents a theme.'''
    def get_effective(self) -> IThemeEffectiveData:
        '''Gets effective theme data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.theme.IThemeEffectiveData`.'''
        ...

    @property
    def color_scheme(self) -> IColorScheme:
        ...

    @property
    def font_scheme(self) -> IFontScheme:
        ...

    @property
    def format_scheme(self) -> IFormatScheme:
        ...

    @property
    def presentation(self) -> IPresentation:
        '''Returns the parent presentation.
                    Read-only :py:class:`aspose.slides.IPresentation`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    ...

