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

class AlphaBiLevel(ImageTransformOperation):
    '''Represents an Alpha Bi-Level effect.
                Alpha (Opacity) values less than the threshold are changed to 0 (fully transparent) and
                alpha values greater than or equal to the threshold are changed to 100% (fully opaque).'''
    def get_effective(self) -> IAlphaBiLevelEffectiveData:
        '''Gets effective Alpha Bi-Level effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IAlphaBiLevelEffectiveData`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def threshold(self) -> float:
        '''Returns effect threshold.
                    Read/write :py:class:`float`.'''
        ...

    @threshold.setter
    def threshold(self, value: float):
        '''Returns effect threshold.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class AlphaCeiling(ImageTransformOperation):
    '''Represents an Alpha Ceiling effect.
                Alpha (opacity) values greater than zero are changed to 100%.
                In other words, anything partially opaque becomes fully opaque.'''
    def get_effective(self) -> IAlphaCeilingEffectiveData:
        '''Gets effective Alpha Ceiling effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IAlphaCeilingEffectiveData`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class AlphaFloor(ImageTransformOperation):
    '''Represents an Alpha Floor effect.
                Alpha (opacity) values less than 100% are changed to zero.
                In other words, anything partially transparent becomes fully transparent.'''
    def get_effective(self) -> IAlphaFloorEffectiveData:
        '''Gets effective Alpha Floor effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IAlphaFloorEffectiveData`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class AlphaInverse(ImageTransformOperation):
    '''Represents an Alpha Inverse effect.
                Alpha (opacity) values are inverted by subtracting from 100%.'''
    def get_effective(self) -> IAlphaInverseEffectiveData:
        '''Gets effective Alpha Inverse effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IAlphaInverseEffectiveData`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class AlphaModulate(ImageTransformOperation):
    '''Represents an Alpha Modulate effect.
                Effect alpha (opacity) values are multiplied by a fixed percentage.
                The effect container specifies an effect containing alpha values to modulate.'''
    def get_effective(self) -> IAlphaModulateEffectiveData:
        '''Gets effective Alpha Modulate effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IAlphaModulateEffectiveData`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class AlphaModulateFixed(ImageTransformOperation):
    '''Represents an Alpha Modulate Fixed effect.
                Effect alpha (opacity) values are multiplied by a fixed percentage.'''
    def get_effective(self) -> IAlphaModulateFixedEffectiveData:
        '''Gets effective Alpha Modulate Fixed effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IAlphaModulateFixedEffectiveData`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def amount(self) -> float:
        '''Returns an amount of effect in percents.
                    Read/write :py:class:`float`.'''
        ...

    @amount.setter
    def amount(self, value: float):
        '''Returns an amount of effect in percents.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class AlphaReplace(ImageTransformOperation):
    '''Represents and Alpha Replace effect.
                Effect alpha (opacity) values are replaced by a fixed alpha.'''
    def get_effective(self) -> IAlphaReplaceEffectiveData:
        '''Gets effective Alpha Replace effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IAlphaReplaceEffectiveData`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class BiLevel(ImageTransformOperation):
    '''Represents a Bi-Level (black/white) effect.
                Input colors whose luminance is less than the specified threshold value are changed to black.
                Input colors whose luminance are greater than or equal the specified value are set to white.
                The alpha effect values are unaffected by this effect.'''
    def get_effective(self) -> IBiLevelEffectiveData:
        '''Gets effective Bi-Level effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IBiLevelEffectiveData`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class Blur(ImageTransformOperation):
    '''Represents a Blur effect that is applied to the entire shape, including its fill.
                All color channels, including alpha, are affected.'''
    def get_effective(self) -> IBlurEffectiveData:
        '''Gets effective Blur effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IBlurEffectiveData`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def radius(self) -> float:
        '''Returns or sets blur radius.
                    Read/write :py:class:`float`.'''
        ...

    @radius.setter
    def radius(self, value: float):
        '''Returns or sets blur radius.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def grow(self) -> bool:
        '''Determines whether the bounds of the object should be grown as a result of the blurring.
                    True indicates the bounds are grown while false indicates that they are not.
                    Read/write :py:class:`bool`.'''
        ...

    @grow.setter
    def grow(self, value: bool):
        '''Determines whether the bounds of the object should be grown as a result of the blurring.
                    True indicates the bounds are grown while false indicates that they are not.
                    Read/write :py:class:`bool`.'''
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class ColorChange(ImageTransformOperation):
    '''Represents a Color Change effect.
                Instances of FromColor are replaced with instances of ToColor.'''
    def get_effective(self) -> IColorChangeEffectiveData:
        '''Gets effective Color Change effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IColorChangeEffectiveData`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def from_color(self) -> IColorFormat:
        ...

    @property
    def to_color(self) -> IColorFormat:
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class ColorReplace(ImageTransformOperation):
    '''Represents a Color Replacement effect.
                All effect colors are changed to a fixed color.
                Alpha values are unaffected.'''
    def get_effective(self) -> IColorReplaceEffectiveData:
        '''Gets effective Color Replacement effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IColorReplaceEffectiveData`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def color(self) -> IColorFormat:
        '''Returns color format which will replace color of every pixel.
                    Read-only :py:class:`aspose.slides.IColorFormat`.'''
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class Duotone(ImageTransformOperation):
    '''Represents a Duotone effect.
                For each pixel, combines Color1 and Color2 through a linear interpolation
                to determine the new color for that pixel.'''
    def get_effective(self) -> IDuotoneEffectiveData:
        '''Gets effective Duotone effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IDuotoneEffectiveData`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def color1(self) -> IColorFormat:
        '''Returns target color format for dark pixels.
                    Read-only :py:class:`aspose.slides.IColorFormat`.'''
        ...

    @property
    def color2(self) -> IColorFormat:
        '''Returns target color format for light pixels.
                    Read-only :py:class:`aspose.slides.IColorFormat`.'''
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class EffectFactory:
    '''Allows to create effects'''
    def __init__(self):
        ...

    def create_glow(self) -> IGlow:
        '''Creates Glow effect.
        :returns: Glow effect.'''
        ...

    def create_inner_shadow(self) -> IInnerShadow:
        '''Creates Inner shafow effect.
        :returns: Inner shafow effect.'''
        ...

    def create_outer_shadow(self) -> IOuterShadow:
        '''Creates Outer shadow effect.
        :returns: Outer shadow effect.'''
        ...

    def create_preset_shadow(self) -> IPresetShadow:
        '''Creates Preset shadow effect.
        :returns: Preset shadow effect.'''
        ...

    def create_reflection(self) -> IReflection:
        '''Creates Reflection effect.
        :returns: Reflection effect.'''
        ...

    def create_soft_edge(self) -> ISoftEdge:
        '''Creates Soft Edge effect.
        :returns: Soft Edge effect.'''
        ...

    @property
    def image_transform_operation_factory(self) -> IImageTransformOperationFactory:
        ...

    ...

class FillOverlay(ImageTransformOperation):
    '''Represents a Fill Overlay effect. A fill overlay may be used to specify
                an additional fill for an object and blend the two fills together.'''
    def get_effective(self) -> IFillOverlayEffectiveData:
        '''Gets effective Fill Overlay effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IFillOverlayEffectiveData`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def fill_format(self) -> IFillFormat:
        ...

    @property
    def blend(self) -> FillBlendMode:
        '''FillBlendMode.
                    Read/write :py:enum:`aspose.slides.FillBlendMode`.'''
        ...

    @blend.setter
    def blend(self, value: FillBlendMode):
        '''FillBlendMode.
                    Read/write :py:enum:`aspose.slides.FillBlendMode`.'''
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class Glow:
    '''Represents a Glow effect, in which a color blurred outline 
                is added outside the edges of the object.'''
    def get_effective(self) -> IGlowEffectiveData:
        '''Gets effective Glow effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IGlowEffectiveData`.'''
        ...

    @property
    def radius(self) -> float:
        '''Radius.
                    Read/write :py:class:`float`.'''
        ...

    @radius.setter
    def radius(self, value: float):
        '''Radius.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def color(self) -> IColorFormat:
        '''Color format.
                    Read-only :py:class:`aspose.slides.IColorFormat`.'''
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class GrayScale(ImageTransformOperation):
    '''Represents a Gray Scale effect. Converts all effect color values to a shade of gray,
                corresponding to their luminance. Effect alpha (opacity) values are unaffected.'''
    def get_effective(self) -> IGrayScaleEffectiveData:
        '''Gets effective Gray Scale effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IGrayScaleEffectiveData`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class HSL(ImageTransformOperation):
    '''Represents a Hue/Saturation/Luminance effect.
                The hue, saturation, and luminance may each be adjusted relative to its current value.'''
    def get_effective(self) -> IHSLEffectiveData:
        '''Gets effective Hue/Saturation/Luminance effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IHSLEffectiveData`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IAlphaBiLevel:
    '''Represents an Alpha Bi-Level effect.
                Alpha (Opacity) values less than the threshold are changed to 0 (fully transparent) and
                alpha values greater than or equal to the threshold are changed to 100% (fully opaque).'''
    def get_effective(self) -> IAlphaBiLevelEffectiveData:
        ...

    @property
    def threshold(self) -> float:
        '''Returns effect threshold.
                    Read/write :py:class:`float`.'''
        ...

    @threshold.setter
    def threshold(self, value: float):
        '''Returns effect threshold.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IAlphaBiLevelEffectiveData:
    '''Immutable object which represents an Alpha Bi-Level effect.
                Alpha (Opacity) values less than the threshold are changed to 0 (fully transparent) and
                alpha values greater than or equal to the threshold are changed to 100% (fully opaque).'''
    @property
    def threshold(self) -> float:
        '''Returns effect threshold.
                    Read-only :py:class:`float`.'''
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IAlphaCeiling:
    '''Represents an Alpha Ceiling effect.
                Alpha (opacity) values greater than zero are changed to 100%.
                In other words, anything partially opaque becomes fully opaque.'''
    def get_effective(self) -> IAlphaCeilingEffectiveData:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IAlphaCeilingEffectiveData:
    '''Immutable object which represents an Alpha Ceiling effect.
                Alpha (opacity) values greater than zero are changed to 100%.
                In other words, anything partially opaque becomes fully opaque.'''
    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IAlphaFloor:
    '''Represents an Alpha Floor effect.
                Alpha (opacity) values less than 100% are changed to zero.
                In other words, anything partially transparent becomes fully transparent.'''
    def get_effective(self) -> IAlphaFloorEffectiveData:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IAlphaFloorEffectiveData:
    '''Immutable object which represents an Alpha Floor effect.
                Alpha (opacity) values less than 100% are changed to zero.
                In other words, anything partially transparent becomes fully transparent.'''
    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IAlphaInverse:
    '''Represents an Alpha Inverse effect.
                Alpha (opacity) values are inverted by subtracting from 100%.'''
    def get_effective(self) -> IAlphaInverseEffectiveData:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IAlphaInverseEffectiveData:
    '''Immutable object which represents an Alpha Inverse effect.
                Alpha (opacity) values are inverted by subtracting from 100%.'''
    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IAlphaModulate:
    '''Represents an Alpha Modulate effect.
                Effect alpha (opacity) values are multiplied by a fixed percentage.
                The effect container specifies an effect containing alpha values to modulate.'''
    def get_effective(self) -> IAlphaModulateEffectiveData:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IAlphaModulateEffectiveData:
    '''Immutable object which represents an Alpha Modulate effect.
                Effect alpha (opacity) values are multiplied by a fixed percentage.
                The effect container specifies an effect containing alpha values to modulate.'''
    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IAlphaModulateFixed:
    '''Represents an Alpha Modulate Fixed effect.
                Effect alpha (opacity) values are multiplied by a fixed percentage.'''
    def get_effective(self) -> IAlphaModulateFixedEffectiveData:
        ...

    @property
    def amount(self) -> float:
        '''Returns an amount of effect in percents.
                    Read/write :py:class:`float`.'''
        ...

    @amount.setter
    def amount(self, value: float):
        '''Returns an amount of effect in percents.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IAlphaModulateFixedEffectiveData:
    '''Immutable object which represents an Alpha Modulate Fixed effect.
                Effect alpha (opacity) values are multiplied by a fixed percentage.'''
    @property
    def amount(self) -> float:
        '''Returns an amount of effect in percents.
                    Read-only :py:class:`float`.'''
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IAlphaReplace:
    '''Represents base IImageTransformOperation interface.'''
    def get_effective(self) -> IAlphaReplaceEffectiveData:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IAlphaReplaceEffectiveData:
    '''Immutable object which represents and Alpha Replace effect.
                Effect alpha (opacity) values are replaced by a fixed alpha.'''
    @property
    def alpha(self) -> float:
        '''Returns new alpha value in the interval [0..1]
                    Read-only :py:class:`float`.'''
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IBiLevel:
    '''Represents base IImageTransformOperation interface.'''
    def get_effective(self) -> IBiLevelEffectiveData:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IBiLevelEffectiveData:
    '''Immutable object which represents a Bi-Level (black/white) effect.
                Input colors whose luminance is less than the specified threshold value are changed to black.
                Input colors whose luminance are greater than or equal the specified value are set to white.
                The alpha effect values are unaffected by this effect.'''
    @property
    def threshold(self) -> float:
        '''Returns the threshold value.
                    Read-only :py:class:`float`.'''
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IBlur:
    '''Represents a Blur effect that is applied to the entire shape, including its fill.
                All color channels, including alpha, are affected.'''
    def get_effective(self) -> IBlurEffectiveData:
        ...

    @property
    def radius(self) -> float:
        '''Returns or sets blur radius.
                    Read/write :py:class:`float`.'''
        ...

    @radius.setter
    def radius(self, value: float):
        '''Returns or sets blur radius.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def grow(self) -> bool:
        '''Determines whether the bounds of the object should be grown as a result of the blurring.
                    True indicates the bounds are grown while false indicates that they are not.
                    Read/write :py:class:`bool`.'''
        ...

    @grow.setter
    def grow(self, value: bool):
        '''Determines whether the bounds of the object should be grown as a result of the blurring.
                    True indicates the bounds are grown while false indicates that they are not.
                    Read/write :py:class:`bool`.'''
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IBlurEffectiveData:
    '''Immutable object which represents a Blur effect that is applied to the entire shape, including its fill.
                All color channels, including alpha, are affected.'''
    @property
    def radius(self) -> float:
        '''Returns or sets blur radius.
                    Read-only :py:class:`float`.'''
        ...

    @property
    def grow(self) -> bool:
        '''Determines whether the bounds of the object should be grown as a result of the blurring.
                    True indicates the bounds are grown while false indicates that they are not.
                    Read-only :py:class:`bool`.'''
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IColorChange:
    '''Represents a Color Change effect.
                Instances of FromColor are replaced with instances of ToColor.'''
    def get_effective(self) -> IColorChangeEffectiveData:
        ...

    @property
    def from_color(self) -> IColorFormat:
        ...

    @property
    def to_color(self) -> IColorFormat:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IColorChangeEffectiveData:
    '''Immutable object which represents a Color Change effect.
                Instances of FromColor are replaced with instances of ToColor.'''
    @property
    def from_color(self) -> aspose.pydrawing.Color:
        ...

    @property
    def to_color(self) -> aspose.pydrawing.Color:
        ...

    @property
    def use_alpha(self) -> bool:
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IColorReplace:
    '''Represents a Color Replacement effect.'''
    def get_effective(self) -> IColorReplaceEffectiveData:
        ...

    @property
    def color(self) -> IColorFormat:
        '''Returns color format which will replace color of every pixel.
                    Read-only :py:class:`aspose.slides.IColorFormat`.'''
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IColorReplaceEffectiveData:
    '''Immutable object which represents a Color Replacement effect.
                All effect colors are changed to a fixed color.
                Alpha values are unaffected.'''
    @property
    def color(self) -> aspose.pydrawing.Color:
        '''Returns color format which will replace color of every pixel.
                    Read-only :py:class:`aspose.pydrawing.Color`.'''
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IDuotone:
    '''Represents a Duotone effect.'''
    def get_effective(self) -> IDuotoneEffectiveData:
        ...

    @property
    def color1(self) -> IColorFormat:
        '''Returns target color format for dark pixels.
                    Read-only :py:class:`aspose.slides.IColorFormat`.'''
        ...

    @property
    def color2(self) -> IColorFormat:
        '''Returns target color format for light pixels.
                    Read-only :py:class:`aspose.slides.IColorFormat`.'''
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IDuotoneEffectiveData:
    '''Immutable object which represents a Duotone effect.
                For each pixel, combines clr1 and clr2 through a linear interpolation
                to determine the new color for that pixel.'''
    @property
    def color1(self) -> aspose.pydrawing.Color:
        '''Returns target color format for dark pixels.
                    Read-only :py:class:`aspose.pydrawing.Color`.'''
        ...

    @property
    def color2(self) -> aspose.pydrawing.Color:
        '''Returns target color format for light pixels.
                    Read-only :py:class:`aspose.pydrawing.Color`.'''
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IEffectEffectiveData:
    '''Base class for immutable objects, which represent effect.'''
    ...

class IEffectFactory:
    '''Allows to create effects' instances'''
    def create_glow(self) -> IGlow:
        '''Creates Glow effect.
        :returns: Glow effect.'''
        ...

    def create_inner_shadow(self) -> IInnerShadow:
        '''Creates Inner shafow effect.
        :returns: Inner shafow effect.'''
        ...

    def create_outer_shadow(self) -> IOuterShadow:
        '''Creates Outer shadow effect.
        :returns: Outer shadow effect.'''
        ...

    def create_preset_shadow(self) -> IPresetShadow:
        '''Creates Preset shadow effect.
        :returns: Preset shadow effect.'''
        ...

    def create_reflection(self) -> IReflection:
        '''Creates Reflection effect.
        :returns: Reflection effect.'''
        ...

    def create_soft_edge(self) -> ISoftEdge:
        '''Creates Soft Edge effect.
        :returns: Soft Edge effect.'''
        ...

    @property
    def image_transform_operation_factory(self) -> IImageTransformOperationFactory:
        ...

    ...

class IFillOverlay:
    '''Represents a Fill Overlay effect. A fill overlay may be used to specify
                an additional fill for an object and blend the two fills together.'''
    def get_effective(self) -> IFillOverlayEffectiveData:
        ...

    @property
    def blend(self) -> FillBlendMode:
        '''FillBlendMode.
                    Read/write :py:enum:`aspose.slides.FillBlendMode`.'''
        ...

    @blend.setter
    def blend(self, value: FillBlendMode):
        '''FillBlendMode.
                    Read/write :py:enum:`aspose.slides.FillBlendMode`.'''
        ...

    @property
    def fill_format(self) -> IFillFormat:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IFillOverlayEffectiveData:
    '''Immutable object which represents a Fill Overlay effect. A fill overlay may be used to specify
                an additional fill for an object and blend the two fills together.'''
    @property
    def blend(self) -> FillBlendMode:
        '''FillBlendMode.
                    Read-only :py:enum:`aspose.slides.FillBlendMode`.'''
        ...

    @property
    def fill_format(self) -> IFillFormatEffectiveData:
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IGlow:
    '''Represents a Glow effect, in which a color blurred outline 
                is added outside the edges of the object.'''
    def get_effective(self) -> IGlowEffectiveData:
        ...

    @property
    def radius(self) -> float:
        '''Radius.
                    Read/write :py:class:`float`.'''
        ...

    @radius.setter
    def radius(self, value: float):
        '''Radius.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def color(self) -> IColorFormat:
        '''Color format.
                    Read-only :py:class:`aspose.slides.IColorFormat`.'''
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IGlowEffectiveData:
    '''Immutable object which represents a Glow effect, in which a color blurred outline 
                is added outside the edges of the object.'''
    @property
    def radius(self) -> float:
        '''Radius.
                    Read-only :py:class:`float`.'''
        ...

    @property
    def color(self) -> aspose.pydrawing.Color:
        '''Color.
                    Read-only :py:class:`aspose.pydrawing.Color`.'''
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IGrayScale:
    '''Represents IImageTransformOperation interface.'''
    def get_effective(self) -> IGrayScaleEffectiveData:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IGrayScaleEffectiveData:
    '''Immutable object which representsepresents a Gray Scale effect. Converts all effect color values to a shade of gray,
                corresponding to their luminance. Effect alpha (opacity) values are unaffected.'''
    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IHSL:
    '''Represents a Hue/Saturation/Luminance effect.
                The hue, saturation, and luminance may each be adjusted relative to its current value.'''
    def get_effective(self) -> IHSLEffectiveData:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IHSLEffectiveData:
    '''Represents a Hue/Saturation/Luminance effect.
                The hue, saturation, and luminance may each be adjusted relative to its current value.'''
    @property
    def hue(self) -> float:
        '''Returns hue percentage.
                    Read-only :py:class:`float`.'''
        ...

    @property
    def saturation(self) -> float:
        '''Returns saturation percentage.
                    Read-only :py:class:`float`.'''
        ...

    @property
    def luminance(self) -> float:
        '''Returns luminance percentage.
                    Read-only :py:class:`float`.'''
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IImageTransformOCollectionEffectiveData:
    '''Immutable object that represents a readonly collection of effective image transform effects.'''
    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IEffectEffectiveData
        ...

    ...

class IImageTransformOperation:
    '''Represents abstract image transformation effect.'''
    ...

class IImageTransformOperationCollection:
    '''Represents a collection of effects apllied to an image.'''
    def remove_at(self, index: int) -> None:
        '''Removes an image effect from a collection at the specified index.
        :param index: Index of an image effect that should be deleted.'''
        ...

    def add_alpha_bi_level_effect(self, threshold: float) -> IAlphaBiLevel:
        '''Adds the new Alpha Bi-Level effect to the end of a collection.
        :param threshold: The threshold value for the alpha bi-level effect.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_alpha_ceiling_effect(self) -> IAlphaCeiling:
        '''Adds the new Alpha Ceiling effect to the end of a collection.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_alpha_floor_effect(self) -> IAlphaFloor:
        '''Adds the new Alpha Floor effect to the end of a collection.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_alpha_inverse_effect(self) -> IAlphaInverse:
        '''Adds the new Alpha Inverse effect to the end of a collection.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_alpha_modulate_effect(self) -> IAlphaModulate:
        '''Adds the new Alpha Modulate effect to the end of a collection.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_alpha_modulate_fixed_effect(self, amount: float) -> IAlphaModulateFixed:
        '''Adds the new Alpha Modulate Fixed effect to the end of a collection.
        :param amount: The percentage amount to scale the alpha.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_alpha_replace_effect(self, alpha: float) -> IAlphaReplace:
        '''Adds the new Alpha Replace effect to the end of a collection.
        :param alpha: The new opacity value.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_bi_level_effect(self, threshold: float) -> IBiLevel:
        '''Adds the new Bi-Level (black/white) effect to the end of a collection.
        :param threshold: the luminance threshold for the Bi-Level effect.
                    Values greater than or equal to the threshold are set to white.
                    Values lesser than the threshold are set to black.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_blur_effect(self, radius: float, grow: bool) -> IBlur:
        '''Adds the new Blur effect to the end of a collection.
        :param radius: The radius of blur.
        :param grow: Specifies whether the bounds of the object should be grown as a result of the blurring.
                    True indicates the bounds are grown while false indicates that they are not.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_color_change_effect(self) -> IColorChange:
        '''Adds the new Color Change effect to the end of a collection.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_color_replace_effect(self) -> IColorReplace:
        '''Adds the new Color Replacement effect to the end of a collection.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_duotone_effect(self) -> IDuotone:
        '''Adds the new Duotone effect to the end of a collection.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_fill_overlay_effect(self) -> IFillOverlay:
        '''Adds the new Fill Overlay effect to the end of a collection.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_gray_scale_effect(self) -> IGrayScale:
        '''Adds the new Gray Scale effect to the end of a collection.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_hsl_effect(self, hue: float, saturation: float, luminance: float) -> IHSL:
        '''Adds the new Hue/Saturation/Luminance effect to the end of a collection.
        :param hue: The number of degrees by which the hue is adjusted.
        :param saturation: The percentage by which the saturation is adjusted.
        :param luminance: The percentage by which the luminance is adjusted.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_luminance_effect(self, brightness: float, contrast: float) -> ILuminance:
        '''Adds the new Luminance effect to the end of a collection.
        :param brightness: The percent to change the brightness.
        :param contrast: The percent to change the contrast.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_tint_effect(self, hue: float, amount: float) -> ITint:
        '''Adds the new Tint effect to the end of a collection.
        :param hue: The hue towards which to tint.
        :param amount: Specifies by how much the color value is shifted.
        :returns: Index of the new image effect in a collection.'''
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IImageTransformOperation
        ...

    ...

class IImageTransformOperationFactory:
    '''Allows to create image effects' instances'''
    def create_alpha_bi_level(self, threshold: float) -> IAlphaBiLevel:
        '''Creates Alpha BiLevel effect.
        :param threshold: Threshold.
        :returns: Alpha BiLevel effect.'''
        ...

    def create_alph_ceiling(self) -> IAlphaCeiling:
        '''Creates Alpha Ceiling effect.
        :returns: Alpha Ceiling effect.'''
        ...

    def create_alpha_floor(self) -> IAlphaFloor:
        '''Creates Alpha floor effect.
        :returns: Alpha floor effect.'''
        ...

    def create_alpha_inverse(self) -> IAlphaInverse:
        '''Creates Alpha inverse effect.
        :returns: Alpha inverst effect.'''
        ...

    def create_alpha_modulate(self) -> IAlphaModulate:
        '''Creates Alpha modulate effect.
        :returns: Alpha modulate effect.'''
        ...

    def create_alpha_modulate_fixed(self, amount: float) -> IAlphaModulateFixed:
        '''Creates Alpha modulate fixed effect.
        :param amount: Amount.
        :returns: Alpha modulate fixed effect.'''
        ...

    def create_alpha_replace(self, alpha: float) -> IAlphaReplace:
        '''Creates Alpha replace effect.
        :param alpha: Alpha
        :returns: Alpha replace effect.'''
        ...

    def create_bi_level(self, threshold: float) -> IBiLevel:
        '''Creates BiLevel effect.
        :param threshold: Threshold.
        :returns: BiLevel effect.'''
        ...

    def create_blur(self, radius: float, grow: bool) -> IBlur:
        '''Creates Blur effect.
        :param radius: Radius.
        :param grow: Grow.
        :returns: Blur effect.'''
        ...

    def create_color_change(self) -> IColorChange:
        '''Creates Color change effect.
        :returns: Color change effect.'''
        ...

    def create_color_replace(self) -> IColorReplace:
        '''Creates Color replace effect.
        :returns: Color replace effect.'''
        ...

    def create_duotone(self) -> IDuotone:
        '''Creates Duotone effect.
        :returns: Duotone effect.'''
        ...

    def create_fill_overlay(self) -> IFillOverlay:
        '''Creates Fill overlay effect.
        :returns: Fill overlay effect.'''
        ...

    def create_gray_scale(self) -> IGrayScale:
        '''Creates Gray scale effect.
        :returns: Returns gray scale effect.'''
        ...

    def create_hsl(self, hue: float, saturation: float, luminance: float) -> IHSL:
        '''Creates Hue Saturation Luminance effect.
        :param hue: Hue.
        :param saturation: Saturation.
        :param luminance: Luminance.
        :returns: HSL effect.'''
        ...

    def create_luminance(self, brightness: float, contrast: float) -> ILuminance:
        '''Createtes Luminance effect.
        :param brightness: Brightness.
        :param contrast: Contrast.
        :returns: Luminance effect.'''
        ...

    def create_tint(self, hue: float, amount: float) -> ITint:
        '''Creates Tint effect.
        :param hue: Hue.
        :param amount: Amount.
        :returns: Tint effect.'''
        ...

    ...

class IInnerShadow:
    '''Represents a inner shadow effect.'''
    def get_effective(self) -> IInnerShadowEffectiveData:
        ...

    @property
    def blur_radius(self) -> float:
        ...

    @blur_radius.setter
    def blur_radius(self, value: float):
        ...

    @property
    def direction(self) -> float:
        '''Direction of shadow.
                    Read/write :py:class:`float`.'''
        ...

    @direction.setter
    def direction(self, value: float):
        '''Direction of shadow.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def distance(self) -> float:
        '''Distance of shadow.
                    Read/write :py:class:`float`.'''
        ...

    @distance.setter
    def distance(self, value: float):
        '''Distance of shadow.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def shadow_color(self) -> IColorFormat:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IInnerShadowEffectiveData:
    '''Immutable object which represents a inner shadow effect.'''
    @property
    def blur_radius(self) -> float:
        ...

    @property
    def direction(self) -> float:
        '''Direction of shadow.
                    Read-only :py:class:`float`.'''
        ...

    @property
    def distance(self) -> float:
        '''Distance of shadow.
                    Read-only :py:class:`float`.'''
        ...

    @property
    def shadow_color(self) -> aspose.pydrawing.Color:
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class ILuminance:
    '''Represents a Luminance effect.
                Brightness linearly shifts all colors closer to white or black.
                Contrast scales all colors to be either closer or further apart.'''
    def get_effective(self) -> ILuminanceEffectiveData:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class ILuminanceEffectiveData:
    '''Represents a Luminance effect.
                Brightness linearly shifts all colors closer to white or black.
                Contrast scales all colors to be either closer or further apart.'''
    @property
    def brightness(self) -> float:
        '''Brightness.
                    Read-only :py:class:`float`.'''
        ...

    @property
    def contrast(self) -> float:
        '''Contrast.
                    Read-only :py:class:`float`.'''
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IOuterShadow:
    '''Represents an Outer Shadow effect.'''
    def get_effective(self) -> IOuterShadowEffectiveData:
        ...

    @property
    def blur_radius(self) -> float:
        ...

    @blur_radius.setter
    def blur_radius(self, value: float):
        ...

    @property
    def direction(self) -> float:
        '''Direction of shadow.
                    Read/write :py:class:`float`.'''
        ...

    @direction.setter
    def direction(self, value: float):
        '''Direction of shadow.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def distance(self) -> float:
        '''Distance of shadow.
                    Read/write :py:class:`float`.'''
        ...

    @distance.setter
    def distance(self, value: float):
        '''Distance of shadow.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def shadow_color(self) -> IColorFormat:
        ...

    @property
    def rectangle_align(self) -> RectangleAlignment:
        ...

    @rectangle_align.setter
    def rectangle_align(self, value: RectangleAlignment):
        ...

    @property
    def skew_horizontal(self) -> float:
        ...

    @skew_horizontal.setter
    def skew_horizontal(self, value: float):
        ...

    @property
    def skew_vertical(self) -> float:
        ...

    @skew_vertical.setter
    def skew_vertical(self, value: float):
        ...

    @property
    def rotate_shadow_with_shape(self) -> bool:
        ...

    @rotate_shadow_with_shape.setter
    def rotate_shadow_with_shape(self, value: bool):
        ...

    @property
    def scale_horizontal(self) -> float:
        ...

    @scale_horizontal.setter
    def scale_horizontal(self, value: float):
        ...

    @property
    def scale_vertical(self) -> float:
        ...

    @scale_vertical.setter
    def scale_vertical(self, value: float):
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IOuterShadowEffectiveData:
    '''Immutable object which represents an Outer Shadow effect.'''
    @property
    def blur_radius(self) -> float:
        ...

    @property
    def direction(self) -> float:
        '''Direction of shadow.
                    Read-only :py:class:`float`.'''
        ...

    @property
    def distance(self) -> float:
        '''Distance of shadow.
                    Read-only :py:class:`float`.'''
        ...

    @property
    def shadow_color(self) -> aspose.pydrawing.Color:
        ...

    @property
    def rectangle_align(self) -> RectangleAlignment:
        ...

    @property
    def skew_horizontal(self) -> float:
        ...

    @property
    def skew_vertical(self) -> float:
        ...

    @property
    def rotate_shadow_with_shape(self) -> bool:
        ...

    @property
    def scale_horizontal(self) -> float:
        ...

    @property
    def scale_vertical(self) -> float:
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IPresetShadow:
    '''Represents a Preset Shadow effect.'''
    def get_effective(self) -> IPresetShadowEffectiveData:
        ...

    @property
    def direction(self) -> float:
        '''Direction of shadow.
                    Read/write :py:class:`float`.'''
        ...

    @direction.setter
    def direction(self, value: float):
        '''Direction of shadow.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def distance(self) -> float:
        '''Distance of shadow.
                    Read/write :py:class:`float`.'''
        ...

    @distance.setter
    def distance(self, value: float):
        '''Distance of shadow.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def shadow_color(self) -> IColorFormat:
        ...

    @property
    def preset(self) -> PresetShadowType:
        '''Preset.
                    Read/write :py:enum:`aspose.slides.PresetShadowType`.'''
        ...

    @preset.setter
    def preset(self, value: PresetShadowType):
        '''Preset.
                    Read/write :py:enum:`aspose.slides.PresetShadowType`.'''
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IPresetShadowEffectiveData:
    '''Immutable object which represents a Preset Shadow effect.'''
    @property
    def direction(self) -> float:
        '''Direction of shadow.
                    Read-only :py:class:`float`.'''
        ...

    @property
    def distance(self) -> float:
        '''Distance of shadow.
                    Read-only :py:class:`float`.'''
        ...

    @property
    def shadow_color(self) -> aspose.pydrawing.Color:
        ...

    @property
    def preset(self) -> PresetShadowType:
        '''Preset.
                    Read-only :py:enum:`aspose.slides.PresetShadowType`.'''
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class IReflection:
    '''Represents a reflection effect.'''
    def get_effective(self) -> IReflectionEffectiveData:
        ...

    @property
    def start_pos_alpha(self) -> float:
        ...

    @start_pos_alpha.setter
    def start_pos_alpha(self, value: float):
        ...

    @property
    def end_pos_alpha(self) -> float:
        ...

    @end_pos_alpha.setter
    def end_pos_alpha(self, value: float):
        ...

    @property
    def fade_direction(self) -> float:
        ...

    @fade_direction.setter
    def fade_direction(self, value: float):
        ...

    @property
    def start_reflection_opacity(self) -> float:
        ...

    @start_reflection_opacity.setter
    def start_reflection_opacity(self, value: float):
        ...

    @property
    def end_reflection_opacity(self) -> float:
        ...

    @end_reflection_opacity.setter
    def end_reflection_opacity(self, value: float):
        ...

    @property
    def blur_radius(self) -> float:
        ...

    @blur_radius.setter
    def blur_radius(self, value: float):
        ...

    @property
    def direction(self) -> float:
        '''Direction of reflection.
                    Read/write :py:class:`float`.'''
        ...

    @direction.setter
    def direction(self, value: float):
        '''Direction of reflection.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def distance(self) -> float:
        '''Distance of reflection.
                    Read/write :py:class:`float`.'''
        ...

    @distance.setter
    def distance(self, value: float):
        '''Distance of reflection.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def rectangle_align(self) -> RectangleAlignment:
        ...

    @rectangle_align.setter
    def rectangle_align(self, value: RectangleAlignment):
        ...

    @property
    def skew_horizontal(self) -> float:
        ...

    @skew_horizontal.setter
    def skew_horizontal(self, value: float):
        ...

    @property
    def skew_vertical(self) -> float:
        ...

    @skew_vertical.setter
    def skew_vertical(self, value: float):
        ...

    @property
    def rotate_shadow_with_shape(self) -> bool:
        ...

    @rotate_shadow_with_shape.setter
    def rotate_shadow_with_shape(self, value: bool):
        ...

    @property
    def scale_horizontal(self) -> float:
        ...

    @scale_horizontal.setter
    def scale_horizontal(self, value: float):
        ...

    @property
    def scale_vertical(self) -> float:
        ...

    @scale_vertical.setter
    def scale_vertical(self, value: float):
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class IReflectionEffectiveData:
    '''Immutable object which represents a Reflection effect.'''
    @property
    def start_pos_alpha(self) -> float:
        ...

    @property
    def end_pos_alpha(self) -> float:
        ...

    @property
    def fade_direction(self) -> float:
        ...

    @property
    def start_reflection_opacity(self) -> float:
        ...

    @property
    def end_reflection_opacity(self) -> float:
        ...

    @property
    def blur_radius(self) -> float:
        ...

    @property
    def direction(self) -> float:
        '''Direction of reflection.
                    Read-only :py:class:`float`.'''
        ...

    @property
    def distance(self) -> float:
        '''Distance of reflection.
                    Read-only :py:class:`float`.'''
        ...

    @property
    def rectangle_align(self) -> RectangleAlignment:
        ...

    @property
    def skew_horizontal(self) -> float:
        ...

    @property
    def skew_vertical(self) -> float:
        ...

    @property
    def rotate_shadow_with_shape(self) -> bool:
        ...

    @property
    def scale_horizontal(self) -> float:
        ...

    @property
    def scale_vertical(self) -> float:
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class ISoftEdge:
    '''Represents a Soft Edge effect. 
                The edges of the shape are blurred, while the fill is not affected.'''
    def get_effective(self) -> ISoftEdgeEffectiveData:
        ...

    @property
    def radius(self) -> float:
        '''Specifies the radius of blur to apply to the edges.
                    Read/write :py:class:`float`.'''
        ...

    @radius.setter
    def radius(self, value: float):
        '''Specifies the radius of blur to apply to the edges.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class ISoftEdgeEffectiveData:
    '''Immutable object which represents a soft edge effect. 
                The edges of the shape are blurred, while the fill is not affected.'''
    @property
    def radius(self) -> float:
        '''Specifies the radius of blur to apply to the edges.
                    Read-only :py:class:`float`.'''
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class ITint:
    '''Represents a Tint effect.
                Shifts effect color values towards/away from hue by the specified amount.'''
    def get_effective(self) -> ITintEffectiveData:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class ITintEffectiveData:
    '''Immutable object which represents a Tint effect.
                Shifts effect color values towards/away from hue by the specified amount.'''
    @property
    def hue(self) -> float:
        '''Returns hue.
                    Read-only :py:class:`float`.'''
        ...

    @property
    def amount(self) -> float:
        '''Returns effect amount.
                    Read-only :py:class:`float`.'''
        ...

    @property
    def as_i_effect_effective_data(self) -> IEffectEffectiveData:
        ...

    ...

class ImageTransformOCollectionEffectiveData:
    '''Immutable object that represents a readonly collection of effective image transform effects.'''
    def __init__(self):
        ...

    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IEffectEffectiveData
        ...

    ...

class ImageTransformOperation(aspose.slides.PVIObject):
    '''Represents abstract image transformation effect.'''
    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    ...

class ImageTransformOperationCollection(aspose.slides.PVIObject):
    '''Represents a collection of effects apllied to an image.'''
    def remove_at(self, index: int) -> None:
        '''Removes an image effect from a collection at the specified index.
        :param index: Index of an image effect that should be deleted.'''
        ...

    def add_alpha_bi_level_effect(self, threshold: float) -> IAlphaBiLevel:
        '''Adds the new Alpha Bi-Level effect to the end of a collection.
        :param threshold: The threshold value for the alpha bi-level effect.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_alpha_ceiling_effect(self) -> IAlphaCeiling:
        '''Adds the new Alpha Ceiling effect to the end of a collection.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_alpha_floor_effect(self) -> IAlphaFloor:
        '''Adds the new Alpha Floor effect to the end of a collection.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_alpha_inverse_effect(self) -> IAlphaInverse:
        '''Adds the new Alpha Inverse effect to the end of a collection.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_alpha_modulate_effect(self) -> IAlphaModulate:
        '''Adds the new Alpha Modulate effect to the end of a collection.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_alpha_modulate_fixed_effect(self, amount: float) -> IAlphaModulateFixed:
        '''Adds the new Alpha Modulate Fixed effect to the end of a collection.
        :param amount: The percentage amount to scale the alpha.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_alpha_replace_effect(self, alpha: float) -> IAlphaReplace:
        '''Adds the new Alpha Replace effect to the end of a collection.
        :param alpha: The new opacity value.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_bi_level_effect(self, threshold: float) -> IBiLevel:
        '''Adds the new Bi-Level (black/white) effect to the end of a collection.
        :param threshold: the luminance threshold for the Bi-Level effect.
                    Values greater than or equal to the threshold are set to white.
                    Values lesser than the threshold are set to black.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_blur_effect(self, radius: float, grow: bool) -> IBlur:
        '''Adds the new Blur effect to the end of a collection.
        :param radius: The radius of blur.
        :param grow: Specifies whether the bounds of the object should be grown as a result of the blurring.
                    True indicates the bounds are grown while false indicates that they are not.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_color_change_effect(self) -> IColorChange:
        '''Adds the new Color Change effect to the end of a collection.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_color_replace_effect(self) -> IColorReplace:
        '''Adds the new Color Replacement effect to the end of a collection.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_duotone_effect(self) -> IDuotone:
        '''Adds the new Duotone effect to the end of a collection.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_fill_overlay_effect(self) -> IFillOverlay:
        '''Adds the new Fill Overlay effect to the end of a collection.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_gray_scale_effect(self) -> IGrayScale:
        '''Adds the new Gray Scale effect to the end of a collection.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_hsl_effect(self, hue: float, saturation: float, luminance: float) -> IHSL:
        '''Adds the new Hue/Saturation/Luminance effect to the end of a collection.
        :param hue: The number of degrees by which the hue is adjusted.
        :param saturation: The percentage by which the saturation is adjusted.
        :param luminance: The percentage by which the luminance is adjusted.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_luminance_effect(self, brightness: float, contrast: float) -> ILuminance:
        '''Adds the new Luminance effect to the end of a collection.
        :param brightness: The percent to change the brightness.
        :param contrast: The percent to change the contrast.
        :returns: Index of the new image effect in a collection.'''
        ...

    def add_tint_effect(self, hue: float, amount: float) -> ITint:
        '''Adds the new Tint effect to the end of a collection.
        :param hue: The hue towards which to tint.
        :param amount: Specifies by how much the color value is shifted.
        :returns: Index of the new image effect in a collection.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IImageTransformOperation
        ...

    ...

class ImageTransformOperationFactory:
    '''Allows to create image transform operations'''
    def __init__(self):
        ...

    def create_alpha_bi_level(self, threshold: float) -> IAlphaBiLevel:
        '''Creates Alpha BiLevel effect.
        :param threshold: Threshold.
        :returns: Alpha BiLevel effect.'''
        ...

    def create_alph_ceiling(self) -> IAlphaCeiling:
        '''Creates Alpha Ceiling effect.
        :returns: Alpha Ceiling effect.'''
        ...

    def create_alpha_floor(self) -> IAlphaFloor:
        '''Creates Alpha floor effect.
        :returns: Alpha floor effect.'''
        ...

    def create_alpha_inverse(self) -> IAlphaInverse:
        '''Creates Alpha inverse effect.
        :returns: Alpha inverst effect.'''
        ...

    def create_alpha_modulate(self) -> IAlphaModulate:
        '''Creates Alpha modulate effect.
        :returns: Alpha modulate effect.'''
        ...

    def create_alpha_modulate_fixed(self, amount: float) -> IAlphaModulateFixed:
        '''Creates Alpha modulate fixed effect.
        :param amount: Amount.
        :returns: Alpha modulate fixed effect.'''
        ...

    def create_alpha_replace(self, alpha: float) -> IAlphaReplace:
        '''Creates Alpha replace effect.
        :param alpha: Alpha
        :returns: Alpha replace effect.'''
        ...

    def create_bi_level(self, threshold: float) -> IBiLevel:
        '''Creates BiLevel effect.
        :param threshold: Threshold.
        :returns: BiLevel effect.'''
        ...

    def create_blur(self, radius: float, grow: bool) -> IBlur:
        '''Creates Blur effect.
        :param radius: Radius.
        :param grow: Grow.
        :returns: Blur effect.'''
        ...

    def create_color_change(self) -> IColorChange:
        '''Creates Color change effect.
        :returns: Color change effect.'''
        ...

    def create_color_replace(self) -> IColorReplace:
        '''Creates Color replace effect.
        :returns: Color replace effect.'''
        ...

    def create_duotone(self) -> IDuotone:
        '''Creates Duotone effect.
        :returns: Duotone effect.'''
        ...

    def create_fill_overlay(self) -> IFillOverlay:
        '''Creates Fill overlay effect.
        :returns: Fill overlay effect.'''
        ...

    def create_gray_scale(self) -> IGrayScale:
        '''Creates Gray scale effect.
        :returns: Returns gray scale effect.'''
        ...

    def create_hsl(self, hue: float, saturation: float, luminance: float) -> IHSL:
        '''Creates Hue Saturation Luminance effect.
        :param hue: Hue.
        :param saturation: Saturation.
        :param luminance: Luminance.
        :returns: HSL effect.'''
        ...

    def create_luminance(self, brightness: float, contrast: float) -> ILuminance:
        '''Createtes Luminance effect.
        :param brightness: Brightness.
        :param contrast: Contrast.
        :returns: Luminance effect.'''
        ...

    def create_tint(self, hue: float, amount: float) -> ITint:
        '''Creates Tint effect.
        :param hue: Hue.
        :param amount: Amount.
        :returns: Tint effect.'''
        ...

    ...

class InnerShadow:
    '''Represents a Inner Shadow effect.'''
    def get_effective(self) -> IInnerShadowEffectiveData:
        '''Gets effective Inner Shadow effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IInnerShadowEffectiveData`.'''
        ...

    @property
    def blur_radius(self) -> float:
        ...

    @blur_radius.setter
    def blur_radius(self, value: float):
        ...

    @property
    def direction(self) -> float:
        '''Direction of shadow.
                    Read/write :py:class:`float`.'''
        ...

    @direction.setter
    def direction(self, value: float):
        '''Direction of shadow.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def distance(self) -> float:
        '''Distance of shadow.
                    Read/write :py:class:`float`.'''
        ...

    @distance.setter
    def distance(self, value: float):
        '''Distance of shadow.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def shadow_color(self) -> IColorFormat:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class Luminance(ImageTransformOperation):
    '''Represents a Luminance effect.
                Brightness linearly shifts all colors closer to white or black.
                Contrast scales all colors to be either closer or further apart.'''
    def get_effective(self) -> ILuminanceEffectiveData:
        '''Gets effective Luminance effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.ILuminanceEffectiveData`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class OuterShadow:
    '''Represents an Outer Shadow effect.'''
    def get_effective(self) -> IOuterShadowEffectiveData:
        '''Gets effective Outer Shadow effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IOuterShadowEffectiveData`.'''
        ...

    @property
    def blur_radius(self) -> float:
        ...

    @blur_radius.setter
    def blur_radius(self, value: float):
        ...

    @property
    def direction(self) -> float:
        '''Direction of shadow.
                    Read/write :py:class:`float`.'''
        ...

    @direction.setter
    def direction(self, value: float):
        '''Direction of shadow.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def distance(self) -> float:
        '''Distance of shadow.
                    Read/write :py:class:`float`.'''
        ...

    @distance.setter
    def distance(self, value: float):
        '''Distance of shadow.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def shadow_color(self) -> IColorFormat:
        ...

    @property
    def rectangle_align(self) -> RectangleAlignment:
        ...

    @rectangle_align.setter
    def rectangle_align(self, value: RectangleAlignment):
        ...

    @property
    def skew_horizontal(self) -> float:
        ...

    @skew_horizontal.setter
    def skew_horizontal(self, value: float):
        ...

    @property
    def skew_vertical(self) -> float:
        ...

    @skew_vertical.setter
    def skew_vertical(self, value: float):
        ...

    @property
    def rotate_shadow_with_shape(self) -> bool:
        ...

    @rotate_shadow_with_shape.setter
    def rotate_shadow_with_shape(self, value: bool):
        ...

    @property
    def scale_horizontal(self) -> float:
        ...

    @scale_horizontal.setter
    def scale_horizontal(self, value: float):
        ...

    @property
    def scale_vertical(self) -> float:
        ...

    @scale_vertical.setter
    def scale_vertical(self, value: float):
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class PresetShadow:
    '''Represents a Preset Shadow effect.'''
    def get_effective(self) -> IPresetShadowEffectiveData:
        '''Gets effective Preset Shadow effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IPresetShadowEffectiveData`.'''
        ...

    @property
    def direction(self) -> float:
        '''Direction of shadow.
                    Read/write :py:class:`float`.'''
        ...

    @direction.setter
    def direction(self, value: float):
        '''Direction of shadow.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def distance(self) -> float:
        '''Distance of shadow.
                    Read/write :py:class:`float`.'''
        ...

    @distance.setter
    def distance(self, value: float):
        '''Distance of shadow.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def shadow_color(self) -> IColorFormat:
        ...

    @property
    def preset(self) -> PresetShadowType:
        '''Preset.
                    Read/write :py:enum:`aspose.slides.PresetShadowType`.'''
        ...

    @preset.setter
    def preset(self, value: PresetShadowType):
        '''Preset.
                    Read/write :py:enum:`aspose.slides.PresetShadowType`.'''
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class Reflection:
    '''Represents a Reflection effect.'''
    def get_effective(self) -> IReflectionEffectiveData:
        '''Gets effective Reflection effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.IReflectionEffectiveData`.'''
        ...

    @property
    def start_pos_alpha(self) -> float:
        ...

    @start_pos_alpha.setter
    def start_pos_alpha(self, value: float):
        ...

    @property
    def end_pos_alpha(self) -> float:
        ...

    @end_pos_alpha.setter
    def end_pos_alpha(self, value: float):
        ...

    @property
    def fade_direction(self) -> float:
        ...

    @fade_direction.setter
    def fade_direction(self, value: float):
        ...

    @property
    def start_reflection_opacity(self) -> float:
        ...

    @start_reflection_opacity.setter
    def start_reflection_opacity(self, value: float):
        ...

    @property
    def end_reflection_opacity(self) -> float:
        ...

    @end_reflection_opacity.setter
    def end_reflection_opacity(self, value: float):
        ...

    @property
    def blur_radius(self) -> float:
        ...

    @blur_radius.setter
    def blur_radius(self, value: float):
        ...

    @property
    def direction(self) -> float:
        '''Direction of reflection.
                    Read/write :py:class:`float`.'''
        ...

    @direction.setter
    def direction(self, value: float):
        '''Direction of reflection.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def distance(self) -> float:
        '''Distance of reflection.
                    Read/write :py:class:`float`.'''
        ...

    @distance.setter
    def distance(self, value: float):
        '''Distance of reflection.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def rectangle_align(self) -> RectangleAlignment:
        ...

    @rectangle_align.setter
    def rectangle_align(self, value: RectangleAlignment):
        ...

    @property
    def skew_horizontal(self) -> float:
        ...

    @skew_horizontal.setter
    def skew_horizontal(self, value: float):
        ...

    @property
    def skew_vertical(self) -> float:
        ...

    @skew_vertical.setter
    def skew_vertical(self, value: float):
        ...

    @property
    def rotate_shadow_with_shape(self) -> bool:
        ...

    @rotate_shadow_with_shape.setter
    def rotate_shadow_with_shape(self, value: bool):
        ...

    @property
    def scale_horizontal(self) -> float:
        ...

    @scale_horizontal.setter
    def scale_horizontal(self, value: float):
        ...

    @property
    def scale_vertical(self) -> float:
        ...

    @scale_vertical.setter
    def scale_vertical(self, value: float):
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class SoftEdge:
    '''Represents a soft edge effect. 
                The edges of the shape are blurred, while the fill is not affected.'''
    def get_effective(self) -> ISoftEdgeEffectiveData:
        '''Gets effective Soft Edge effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.ISoftEdgeEffectiveData`.'''
        ...

    @property
    def radius(self) -> float:
        '''Specifies the radius of blur to apply to the edges.
                    Read/write :py:class:`float`.'''
        ...

    @radius.setter
    def radius(self, value: float):
        '''Specifies the radius of blur to apply to the edges.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

class Tint(ImageTransformOperation):
    '''Represents a Tint effect.
                Shifts effect color values towards/away from hue by the specified amount.'''
    def get_effective(self) -> ITintEffectiveData:
        '''Gets effective Tint effect data with the inheritance applied.
        :returns: A :py:class:`aspose.slides.effects.ITintEffectiveData`.'''
        ...

    @property
    def as_i_presentation_component(self) -> IPresentationComponent:
        ...

    @property
    def slide(self) -> IBaseSlide:
        ...

    @property
    def presentation(self) -> IPresentation:
        ...

    @property
    def as_i_image_transform_operation(self) -> IImageTransformOperation:
        ...

    ...

