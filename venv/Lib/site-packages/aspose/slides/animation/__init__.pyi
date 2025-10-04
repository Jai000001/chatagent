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

class AnimationTimeLine:
    '''Represents timeline of animation.'''
    @property
    def interactive_sequences(self) -> ISequenceCollection:
        ...

    @property
    def main_sequence(self) -> ISequence:
        ...

    @property
    def text_animation_collection(self) -> ITextAnimationCollection:
        ...

    ...

class Behavior:
    '''Represent base class behavior of effect.'''
    @property
    def accumulate(self) -> NullableBool:
        '''Represents whether animation behaviors are accumulated.
                    Read/write :py:enum:`aspose.slides.NullableBool`.'''
        ...

    @accumulate.setter
    def accumulate(self, value: NullableBool):
        '''Represents whether animation behaviors are accumulated.
                    Read/write :py:enum:`aspose.slides.NullableBool`.'''
        ...

    @property
    def additive(self) -> BehaviorAdditiveType:
        '''Represents whether the current animation behavior is combined with other running animations.
                    Read/write :py:enum:`aspose.slides.animation.BehaviorAdditiveType`.'''
        ...

    @additive.setter
    def additive(self, value: BehaviorAdditiveType):
        '''Represents whether the current animation behavior is combined with other running animations.
                    Read/write :py:enum:`aspose.slides.animation.BehaviorAdditiveType`.'''
        ...

    @property
    def properties(self) -> IBehaviorPropertyCollection:
        '''Represents properties of behavior.
                    Read-only :py:class:`aspose.slides.animation.IBehaviorPropertyCollection`.'''
        ...

    @property
    def timing(self) -> ITiming:
        '''Represents timing properties for the effect behavior.
                    Read/write :py:class:`aspose.slides.animation.ITiming`.'''
        ...

    @timing.setter
    def timing(self, value: ITiming):
        '''Represents timing properties for the effect behavior.
                    Read/write :py:class:`aspose.slides.animation.ITiming`.'''
        ...

    ...

class BehaviorCollection:
    '''Represents collection of behavior effects.'''
    def add(self, item: IBehavior) -> None:
        '''Add new behavior to a collection.
        :param item: Behavior to add.'''
        ...

    def index_of(self, item: IBehavior) -> int:
        '''Determines the index of a specific item in the :py:class:`System.Collections.Generic.IList`1`.
        :param item: The object to locate in the :py:class:`System.Collections.Generic.IList`1`.
        :returns: The index of ``item`` if found in the list; otherwise, -1.'''
        ...

    def insert(self, index: int, item: IBehavior) -> None:
        '''Inserts new behavior to a collection at the specified index.
        :param index: Index where new behavior should be inserted.
        :param item: Behavior to insert.'''
        ...

    def copy_to(self, array: List[IBehavior], array_index: int) -> None:
        '''Copies the elements of the :py:class:`System.Collections.Generic.ICollection`1` to an :py:class:`System.Array`, starting at a particular :py:class:`System.Array` index.
        :param array: The one-dimensional :py:class:`System.Array` that is the destination of the elements copied from :py:class:`System.Collections.Generic.ICollection`1`. The :py:class:`System.Array` must have zero-based indexing.
        :param array_index: The zero-based index in ``array`` at which copying begins.'''
        ...

    def remove(self, item: IBehavior) -> bool:
        '''Removes specified behavior from a collection.
        :param item: Behavior to remove.'''
        ...

    def remove_at(self, index: int) -> None:
        '''Removes behavior from a collection at the specified index.
        :param index: Index of a behavior to remove.'''
        ...

    def clear(self) -> None:
        '''Removes all behaviors from a collection.'''
        ...

    def contains(self, item: IBehavior) -> bool:
        '''Determines whether the :py:class:`System.Collections.Generic.ICollection`1` contains a specific value.
        :param item: The object to locate in the :py:class:`System.Collections.Generic.ICollection`1`.
        :returns: true if ``item`` is found in the :py:class:`System.Collections.Generic.ICollection`1`; otherwise, false.'''
        ...

    @property
    def count(self) -> int:
        '''Returns the number of behaviors in a collection.
                    Read-only :py:class:`int`.'''
        ...

    @property
    def is_read_only(self) -> bool:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IBehavior
        ...

    def __setitem__(self, key: int, value: IBehavior
        ...

    ...

class BehaviorFactory:
    '''Allows to create animation effects'''
    def __init__(self):
        ...

    def create_color_effect(self) -> IColorEffect:
        '''Creates color effect.
        :returns: Color effect.'''
        ...

    def create_command_effect(self) -> ICommandEffect:
        '''Creates command effect.
        :returns: Command effect.'''
        ...

    def create_filter_effect(self) -> IFilterEffect:
        '''Creates filter effect.
        :returns: Filter effect.'''
        ...

    def create_motion_effect(self) -> IMotionEffect:
        '''Creates motion effect.
        :returns: Motion effect.'''
        ...

    def create_property_effect(self) -> IPropertyEffect:
        '''Creates property effect.
        :returns: Property effect.'''
        ...

    def create_rotation_effect(self) -> IRotationEffect:
        '''Creates rotation effect.
        :returns: Rotation effect.'''
        ...

    def create_scale_effect(self) -> IScaleEffect:
        '''Creates scale effect.
        :returns: Scale effect.'''
        ...

    def create_set_effect(self) -> ISetEffect:
        '''Creates set effect.
        :returns: Set effect.'''
        ...

    ...

class BehaviorProperty:
    '''Represent property types for animation behavior.
                Follows the list of properties from https://msdn.microsoft.com/en-us/library/dd949052(v=office.15).aspx
                and https://msdn.microsoft.com/en-us/library/documentformat.openxml.presentation.attributename(v=office.15).aspx'''
    @staticmethod
    def get_or_create_by_value(property_value: str) -> BehaviorProperty:
        '''Looks for existing behavior property by value or creates new custom one with the specified value
        :param property_value: value of the property
        :returns: instance of BehaviorProperty'''
        ...

    @property
    def value(self) -> str:
        '''Value of the property'''
        ...

    @property
    def is_custom(self) -> bool:
        ...

    @classmethod
    @property
    def ppt_x(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def ppt_y(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def ppt_w(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def ppt_h(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def ppt_c(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def ppt_r(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def x_shear(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def y_shear(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def image(cls) -> BehaviorProperty:
        '''Represents 'image' property'''
        ...

    @classmethod
    @property
    def scale_x(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def scale_y(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def r(cls) -> BehaviorProperty:
        '''Represents 'r' property'''
        ...

    @classmethod
    @property
    def style_opacity(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def style_rotation(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def style_visibility(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def style_color(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def style_font_size(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def style_font_weight(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def style_font_style(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def style_font_family(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def style_text_effect_emboss(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def style_text_shadow(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def style_text_transform(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def style_text_decoration_underline(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def style_text_effect_outline(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def style_text_decoration_line_through(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def style_s_rotation(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def image_data_crop_top(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def image_data_crop_bottom(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def image_data_crop_left(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def image_data_crop_right(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def image_data_gain(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def image_data_blacklevel(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def image_data_gamma(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def image_data_grayscale(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def image_data_chromakey(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def fill_on(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def fill_type(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def fill_opacity(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def fill_color2(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def fill_method(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def fill_opacity2(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def fill_angle(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def fill_focus(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def fill_focus_position_x(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def fill_focus_position_y(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def fill_focus_size_x(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def fill_focus_size_y(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def stroke_on(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def stroke_color(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def stroke_weight(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def stroke_opacity(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def stroke_line_style(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def stroke_dash_style(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def stroke_fill_type(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def stroke_src(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def stroke_color2(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def stroke_image_size_x(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def stroke_image_size_y(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def stroke_start_arrow(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def stroke_end_arrow(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def stroke_start_arrow_width(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def stroke_start_arrow_length(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def stroke_end_arrow_width(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def stroke_end_arrow_length(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def shadow_on(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def shadow_type(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def shadow_color(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def shadow_color2(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def shadow_opacity(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def shadow_offset_x(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def shadow_offset_y(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def shadow_offset_2x(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def shadow_offset_2y(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def shadow_origin_x(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def shadow_origin_y(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def shadow_matrix_xto_x(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def shadow_matrix_xto_y(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def shadow_matrix_yto_x(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def shadow_matrix_yto_y(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def shadow_matrix_perspective_x(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def shadow_matrix_perspective_y(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def skew_on(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def skew_offset_x(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def skew_offset_y(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def skew_origin_x(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def skew_origin_y(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def skew_matrix_xto_x(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def skew_matrix_xto_y(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def skew_matrix_yto_x(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def skew_matrix_yto_y(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def skew_matrix_perspective_x(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def skew_matrix_perspective_y(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def extrusion_on(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def extrusion_type(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def extrusion_render(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def extrusion_view_point_origin_x(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def extrusion_view_point_origin_y(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def extrusion_view_point_x(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def extrusion_view_point_y(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def extrusion_view_point_z(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def extrusion_plane(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def extrusion_skew_angle(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def extrusion_skew_amt(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def extrusion_back_depth(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def extrusion_fore_depth(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def extrusion_orientation_x(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def extrusion_orientation_y(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def extrusion_orientation_z(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def extrusion_orientation_angle(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def extrusion_color(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def extrusion_rotation_angle_x(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def extrusion_rotation_angle_y(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def extrusion_lock_rotation_center(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def extrusion_auto_rotation_center(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def extrusion_rotation_center_x(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def extrusion_rotation_center_y(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def extrusion_rotation_center_z(cls) -> BehaviorProperty:
        ...

    @classmethod
    @property
    def extrusion_color_mode(cls) -> BehaviorProperty:
        ...

    ...

class BehaviorPropertyCollection:
    '''Represents timing properties for the effect behavior.'''
    def add(self, property_value: str) -> None:
        '''Adds a new property to the collection.
        :param property_value: Value of the property to add.'''
        ...

    def index_of(self, property_value: str) -> int:
        '''Determines the index of a specific item by property value in the :py:class:`System.Collections.Generic.IList`1`.
        :param property_value: value of the property
        :returns: The index of the property with the specified value'''
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    ...

class ColorEffect(Behavior):
    '''Represents a color effect for an animation behavior.'''
    def __init__(self):
        '''Creates new instance.'''
        ...

    @property
    def accumulate(self) -> NullableBool:
        '''Represents whether animation behaviors are accumulated.
                    Read/write :py:enum:`aspose.slides.NullableBool`.'''
        ...

    @accumulate.setter
    def accumulate(self, value: NullableBool):
        '''Represents whether animation behaviors are accumulated.
                    Read/write :py:enum:`aspose.slides.NullableBool`.'''
        ...

    @property
    def additive(self) -> BehaviorAdditiveType:
        '''Represents whether the current animation behavior is combined with other running animations.
                    Read/write :py:enum:`aspose.slides.animation.BehaviorAdditiveType`.'''
        ...

    @additive.setter
    def additive(self, value: BehaviorAdditiveType):
        '''Represents whether the current animation behavior is combined with other running animations.
                    Read/write :py:enum:`aspose.slides.animation.BehaviorAdditiveType`.'''
        ...

    @property
    def properties(self) -> IBehaviorPropertyCollection:
        '''Represents properties of behavior.
                    Read-only :py:class:`aspose.slides.animation.IBehaviorPropertyCollection`.'''
        ...

    @property
    def timing(self) -> ITiming:
        '''Represents timing properties for the effect behavior.
                    Read/write :py:class:`aspose.slides.animation.ITiming`.'''
        ...

    @timing.setter
    def timing(self, value: ITiming):
        '''Represents timing properties for the effect behavior.
                    Read/write :py:class:`aspose.slides.animation.ITiming`.'''
        ...

    @property
    def from_address(self) -> IColorFormat:
        ...

    @from_address.setter
    def from_address(self, value: IColorFormat):
        ...

    @property
    def to(self) -> IColorFormat:
        '''Describes resulting color for the animation color change.
                    Read/write :py:class:`aspose.slides.IColorFormat`.'''
        ...

    @to.setter
    def to(self, value: IColorFormat):
        '''Describes resulting color for the animation color change.
                    Read/write :py:class:`aspose.slides.IColorFormat`.'''
        ...

    @property
    def by(self) -> IColorOffset:
        '''Describes the relative offset value for the color animation.
                    Read/write :py:class:`aspose.slides.animation.IColorOffset`.'''
        ...

    @by.setter
    def by(self, value: IColorOffset):
        '''Describes the relative offset value for the color animation.
                    Read/write :py:class:`aspose.slides.animation.IColorOffset`.'''
        ...

    @property
    def color_space(self) -> ColorSpace:
        ...

    @color_space.setter
    def color_space(self, value: ColorSpace):
        ...

    @property
    def direction(self) -> ColorDirection:
        '''Specifies which direction to cycle the hue around the color wheel.
                    Read/write :py:enum:`aspose.slides.animation.ColorDirection`.'''
        ...

    @direction.setter
    def direction(self, value: ColorDirection):
        '''Specifies which direction to cycle the hue around the color wheel.
                    Read/write :py:enum:`aspose.slides.animation.ColorDirection`.'''
        ...

    @property
    def as_i_behavior(self) -> IBehavior:
        ...

    ...

class ColorOffset:
    '''Represent color offset.'''
    def __init__(self):
        ...

    @property
    def value0(self) -> float:
        '''Defines first value of offset.
                    Read/write :py:class:`float`.'''
        ...

    @value0.setter
    def value0(self, value: float):
        '''Defines first value of offset.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def value1(self) -> float:
        '''Defines second value of offset.
                    Read/write :py:class:`float`.'''
        ...

    @value1.setter
    def value1(self, value: float):
        '''Defines second value of offset.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def value2(self) -> float:
        '''Defines third value of offset.
                    Read/write :py:class:`float`.'''
        ...

    @value2.setter
    def value2(self, value: float):
        '''Defines third value of offset.
                    Read/write :py:class:`float`.'''
        ...

    ...

class CommandEffect(Behavior):
    '''Represents a command effect for an animation behavior.'''
    def __init__(self):
        '''Creates new instance.'''
        ...

    @property
    def accumulate(self) -> NullableBool:
        '''Represents whether animation behaviors are accumulated.
                    Read/write :py:enum:`aspose.slides.NullableBool`.'''
        ...

    @accumulate.setter
    def accumulate(self, value: NullableBool):
        '''Represents whether animation behaviors are accumulated.
                    Read/write :py:enum:`aspose.slides.NullableBool`.'''
        ...

    @property
    def additive(self) -> BehaviorAdditiveType:
        '''Represents whether the current animation behavior is combined with other running animations.
                    Read/write :py:enum:`aspose.slides.animation.BehaviorAdditiveType`.'''
        ...

    @additive.setter
    def additive(self, value: BehaviorAdditiveType):
        '''Represents whether the current animation behavior is combined with other running animations.
                    Read/write :py:enum:`aspose.slides.animation.BehaviorAdditiveType`.'''
        ...

    @property
    def properties(self) -> IBehaviorPropertyCollection:
        '''Represents properties of behavior.
                    Read-only :py:class:`aspose.slides.animation.IBehaviorPropertyCollection`.'''
        ...

    @property
    def timing(self) -> ITiming:
        '''Represents timing properties for the effect behavior.
                    Read/write :py:class:`aspose.slides.animation.ITiming`.'''
        ...

    @timing.setter
    def timing(self, value: ITiming):
        '''Represents timing properties for the effect behavior.
                    Read/write :py:class:`aspose.slides.animation.ITiming`.'''
        ...

    @property
    def type(self) -> CommandEffectType:
        '''Defines command effect type of behavior.
                    Read/write :py:enum:`aspose.slides.animation.CommandEffectType`.'''
        ...

    @type.setter
    def type(self, value: CommandEffectType):
        '''Defines command effect type of behavior.
                    Read/write :py:enum:`aspose.slides.animation.CommandEffectType`.'''
        ...

    @property
    def command_string(self) -> str:
        ...

    @command_string.setter
    def command_string(self, value: str):
        ...

    @property
    def shape_target(self) -> IShape:
        ...

    @shape_target.setter
    def shape_target(self, value: IShape):
        ...

    @property
    def as_i_behavior(self) -> IBehavior:
        ...

    ...

class Effect:
    '''Represents animation effect.'''
    @property
    def sequence(self) -> ISequence:
        '''Returns a sequence for an effect.
                    Read-only :py:class:`aspose.slides.animation.ISequence`.'''
        ...

    @property
    def text_animation(self) -> ITextAnimation:
        ...

    @property
    def preset_class_type(self) -> EffectPresetClassType:
        ...

    @preset_class_type.setter
    def preset_class_type(self, value: EffectPresetClassType):
        ...

    @property
    def type(self) -> EffectType:
        '''Defines type of effect.
                    Read/write :py:enum:`aspose.slides.animation.EffectType`.'''
        ...

    @type.setter
    def type(self, value: EffectType):
        '''Defines type of effect.
                    Read/write :py:enum:`aspose.slides.animation.EffectType`.'''
        ...

    @property
    def subtype(self) -> EffectSubtype:
        '''Defines subtype of effect.
                    Read/write :py:enum:`aspose.slides.animation.EffectSubtype`.'''
        ...

    @subtype.setter
    def subtype(self, value: EffectSubtype):
        '''Defines subtype of effect.
                    Read/write :py:enum:`aspose.slides.animation.EffectSubtype`.'''
        ...

    @property
    def behaviors(self) -> IBehaviorCollection:
        '''Returns collection of behavior for effect.
                    Read/write :py:class:`aspose.slides.animation.IBehaviorCollection`.'''
        ...

    @behaviors.setter
    def behaviors(self, value: IBehaviorCollection):
        '''Returns collection of behavior for effect.
                    Read/write :py:class:`aspose.slides.animation.IBehaviorCollection`.'''
        ...

    @property
    def timing(self) -> ITiming:
        '''Defines timing value for effect.
                    Read/write :py:class:`aspose.slides.animation.ITiming`.'''
        ...

    @timing.setter
    def timing(self, value: ITiming):
        '''Defines timing value for effect.
                    Read/write :py:class:`aspose.slides.animation.ITiming`.'''
        ...

    @property
    def target_shape(self) -> IShape:
        ...

    @property
    def sound(self) -> IAudio:
        '''Defined embedded sound for effect.
                    Read/write :py:class:`aspose.slides.IAudio`.'''
        ...

    @sound.setter
    def sound(self, value: IAudio):
        '''Defined embedded sound for effect.
                    Read/write :py:class:`aspose.slides.IAudio`.'''
        ...

    @property
    def stop_previous_sound(self) -> bool:
        ...

    @stop_previous_sound.setter
    def stop_previous_sound(self, value: bool):
        ...

    @property
    def after_animation_type(self) -> AfterAnimationType:
        ...

    @after_animation_type.setter
    def after_animation_type(self, value: AfterAnimationType):
        ...

    @property
    def after_animation_color(self) -> IColorFormat:
        ...

    @after_animation_color.setter
    def after_animation_color(self, value: IColorFormat):
        ...

    @property
    def animate_text_type(self) -> AnimateTextType:
        ...

    @animate_text_type.setter
    def animate_text_type(self, value: AnimateTextType):
        ...

    @property
    def delay_between_text_parts(self) -> float:
        ...

    @delay_between_text_parts.setter
    def delay_between_text_parts(self, value: float):
        ...

    ...

class FilterEffect(Behavior):
    '''Represent filter effect of behavior.'''
    def __init__(self):
        '''Default constructor.'''
        ...

    @property
    def accumulate(self) -> NullableBool:
        '''Represents whether animation behaviors are accumulated.
                    Read/write :py:enum:`aspose.slides.NullableBool`.'''
        ...

    @accumulate.setter
    def accumulate(self, value: NullableBool):
        '''Represents whether animation behaviors are accumulated.
                    Read/write :py:enum:`aspose.slides.NullableBool`.'''
        ...

    @property
    def additive(self) -> BehaviorAdditiveType:
        '''Represents whether the current animation behavior is combined with other running animations.
                    Read/write :py:enum:`aspose.slides.animation.BehaviorAdditiveType`.'''
        ...

    @additive.setter
    def additive(self, value: BehaviorAdditiveType):
        '''Represents whether the current animation behavior is combined with other running animations.
                    Read/write :py:enum:`aspose.slides.animation.BehaviorAdditiveType`.'''
        ...

    @property
    def properties(self) -> IBehaviorPropertyCollection:
        '''Represents properties of behavior.
                    Read-only :py:class:`aspose.slides.animation.IBehaviorPropertyCollection`.'''
        ...

    @property
    def timing(self) -> ITiming:
        '''Represents timing properties for the effect behavior.
                    Read/write :py:class:`aspose.slides.animation.ITiming`.'''
        ...

    @timing.setter
    def timing(self, value: ITiming):
        '''Represents timing properties for the effect behavior.
                    Read/write :py:class:`aspose.slides.animation.ITiming`.'''
        ...

    @property
    def reveal(self) -> FilterEffectRevealType:
        '''Represents that effect with behavior must reveal (in/out)
                    Read/write :py:enum:`aspose.slides.animation.FilterEffectRevealType`.'''
        ...

    @reveal.setter
    def reveal(self, value: FilterEffectRevealType):
        '''Represents that effect with behavior must reveal (in/out)
                    Read/write :py:enum:`aspose.slides.animation.FilterEffectRevealType`.'''
        ...

    @property
    def type(self) -> FilterEffectType:
        '''Represents type of filter effect.
                    Read/write :py:enum:`aspose.slides.animation.FilterEffectType`.'''
        ...

    @type.setter
    def type(self, value: FilterEffectType):
        '''Represents type of filter effect.
                    Read/write :py:enum:`aspose.slides.animation.FilterEffectType`.'''
        ...

    @property
    def subtype(self) -> FilterEffectSubtype:
        '''Represents subtype of filter effect.
                    Read/write :py:enum:`aspose.slides.animation.FilterEffectSubtype`.'''
        ...

    @subtype.setter
    def subtype(self, value: FilterEffectSubtype):
        '''Represents subtype of filter effect.
                    Read/write :py:enum:`aspose.slides.animation.FilterEffectSubtype`.'''
        ...

    @property
    def as_i_behavior(self) -> IBehavior:
        ...

    ...

class IBehavior:
    '''Represent base class behavior of effect.'''
    @property
    def accumulate(self) -> NullableBool:
        '''Represents whether animation behaviors are accumulated.
                    Read/write :py:enum:`aspose.slides.NullableBool`.'''
        ...

    @accumulate.setter
    def accumulate(self, value: NullableBool):
        '''Represents whether animation behaviors are accumulated.
                    Read/write :py:enum:`aspose.slides.NullableBool`.'''
        ...

    @property
    def additive(self) -> BehaviorAdditiveType:
        '''Represents whether the current animation behavior is combined with other running animations.
                    Read/write :py:enum:`aspose.slides.animation.BehaviorAdditiveType`.'''
        ...

    @additive.setter
    def additive(self, value: BehaviorAdditiveType):
        '''Represents whether the current animation behavior is combined with other running animations.
                    Read/write :py:enum:`aspose.slides.animation.BehaviorAdditiveType`.'''
        ...

    @property
    def properties(self) -> IBehaviorPropertyCollection:
        '''Represents properties of behavior.
                    Read-only :py:class:`aspose.slides.animation.IBehaviorPropertyCollection`.'''
        ...

    @property
    def timing(self) -> ITiming:
        '''Represents timing properties for the effect behavior.
                    Read/write :py:class:`aspose.slides.animation.ITiming`.'''
        ...

    @timing.setter
    def timing(self, value: ITiming):
        '''Represents timing properties for the effect behavior.
                    Read/write :py:class:`aspose.slides.animation.ITiming`.'''
        ...

    ...

class IBehaviorCollection:
    '''Represents collection of behavior effects.'''
    def add(self, item: IBehavior) -> None:
        '''Add new behavior to a collection.
        :param item: Behavior to add.'''
        ...

    def index_of(self, item: IBehavior) -> int:
        '''Determines the index of a specific item in the :py:class:`System.Collections.Generic.IList`1`.
        :param item: The object to locate in the :py:class:`System.Collections.Generic.IList`1`.
        :returns: The index of ``item`` if found in the list; otherwise, -1.'''
        ...

    def insert(self, index: int, item: IBehavior) -> None:
        '''Inserts new behavior to a collection at the specified index.
        :param index: Index where new behavior should be inserted.
        :param item: Behavior to insert.'''
        ...

    def remove(self, item: IBehavior) -> bool:
        '''Removes specified behavior from a collection.
        :param item: Behavior to remove.
        :returns: True if a behavior removed successfully :py:class:`bool`'''
        ...

    def remove_at(self, index: int) -> None:
        '''Removes behavior from a collection at the specified index.
        :param index: Index of a behavior to remove.'''
        ...

    def clear(self) -> None:
        '''Removes all behaviors from a collection.'''
        ...

    def contains(self, item: IBehavior) -> bool:
        '''Determines whether the :py:class:`System.Collections.Generic.ICollection`1` contains a specific value.
        :param item: The object to locate in the :py:class:`System.Collections.Generic.ICollection`1`.
        :returns: true if ``item`` is found in the :py:class:`System.Collections.Generic.ICollection`1`; otherwise, false.'''
        ...

    @property
    def count(self) -> int:
        '''Returns the number of behaviors in a collection.
                    Read-only :py:class:`int`.'''
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IBehavior
        ...

    def __setitem__(self, key: int, value: IBehavior
        ...

    ...

class IBehaviorFactory:
    '''Allows to create animation effects'''
    def create_color_effect(self) -> IColorEffect:
        '''Creates color effect.
        :returns: Color effect.'''
        ...

    def create_command_effect(self) -> ICommandEffect:
        '''Creates command effect.
        :returns: Command effect.'''
        ...

    def create_filter_effect(self) -> IFilterEffect:
        '''Creates filter effect.
        :returns: Filter effect.'''
        ...

    def create_motion_effect(self) -> IMotionEffect:
        '''Creates motion effect.
        :returns: Motion effect.'''
        ...

    def create_property_effect(self) -> IPropertyEffect:
        '''Creates property effect.
        :returns: Property effect.'''
        ...

    def create_rotation_effect(self) -> IRotationEffect:
        '''Creates rotation effect.
        :returns: Rotation effect.'''
        ...

    def create_scale_effect(self) -> IScaleEffect:
        '''Creates scale effect.
        :returns: Scale effect.'''
        ...

    def create_set_effect(self) -> ISetEffect:
        '''Creates set effect.
        :returns: Set effect.'''
        ...

    ...

class IBehaviorProperty:
    '''Represent property types for animation behavior.
                Follows the list of properties from https://msdn.microsoft.com/en-us/library/dd949052(v=office.15).aspx
                and https://msdn.microsoft.com/en-us/library/documentformat.openxml.presentation.attributename(v=office.15).aspx'''
    @property
    def value(self) -> str:
        '''Value of the property'''
        ...

    @property
    def is_custom(self) -> bool:
        ...

    ...

class IBehaviorPropertyCollection:
    '''Represents timing properties for the effect behavior.'''
    def add(self, property_value: str) -> None:
        '''Adds a new property to the collection.
        :param property_value: Value of the property to add.'''
        ...

    def index_of(self, property_value: str) -> int:
        '''Determines the index of a specific item by property value in the :py:class:`System.Collections.Generic.IList`1`.
        :param property_value: value of the property
        :returns: The index of the property with the specified value'''
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    ...

class IColorEffect:
    '''Represents a color effect for an animation behavior.'''
    @property
    def from_address(self) -> IColorFormat:
        ...

    @from_address.setter
    def from_address(self, value: IColorFormat):
        ...

    @property
    def to(self) -> IColorFormat:
        '''Describes resulting color for the animation color change.
                    Read/write :py:class:`aspose.slides.IColorFormat`.'''
        ...

    @to.setter
    def to(self, value: IColorFormat):
        '''Describes resulting color for the animation color change.
                    Read/write :py:class:`aspose.slides.IColorFormat`.'''
        ...

    @property
    def by(self) -> IColorOffset:
        '''Describes the relative offset value for the color animation.
                    Read/write :py:class:`aspose.slides.animation.IColorOffset`.'''
        ...

    @by.setter
    def by(self, value: IColorOffset):
        '''Describes the relative offset value for the color animation.
                    Read/write :py:class:`aspose.slides.animation.IColorOffset`.'''
        ...

    @property
    def color_space(self) -> ColorSpace:
        ...

    @color_space.setter
    def color_space(self, value: ColorSpace):
        ...

    @property
    def direction(self) -> ColorDirection:
        '''Specifies which direction to cycle the hue around the color wheel.
                    Read/write :py:enum:`aspose.slides.animation.ColorDirection`.'''
        ...

    @direction.setter
    def direction(self, value: ColorDirection):
        '''Specifies which direction to cycle the hue around the color wheel.
                    Read/write :py:enum:`aspose.slides.animation.ColorDirection`.'''
        ...

    @property
    def as_i_behavior(self) -> IBehavior:
        ...

    @property
    def accumulate(self) -> NullableBool:
        ...

    @accumulate.setter
    def accumulate(self, value: NullableBool):
        ...

    @property
    def additive(self) -> BehaviorAdditiveType:
        ...

    @additive.setter
    def additive(self, value: BehaviorAdditiveType):
        ...

    @property
    def properties(self) -> IBehaviorPropertyCollection:
        ...

    @property
    def timing(self) -> ITiming:
        ...

    @timing.setter
    def timing(self, value: ITiming):
        ...

    ...

class IColorOffset:
    '''Represent color offset.'''
    @property
    def value0(self) -> float:
        '''Defines first value of offset.
                    Read/write :py:class:`float`.'''
        ...

    @value0.setter
    def value0(self, value: float):
        '''Defines first value of offset.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def value1(self) -> float:
        '''Defines second value of offset.
                    Read/write :py:class:`float`.'''
        ...

    @value1.setter
    def value1(self, value: float):
        '''Defines second value of offset.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def value2(self) -> float:
        '''Defines third value of offset.
                    Read/write :py:class:`float`.'''
        ...

    @value2.setter
    def value2(self, value: float):
        '''Defines third value of offset.
                    Read/write :py:class:`float`.'''
        ...

    ...

class ICommandEffect:
    '''Represents a command effect for an animation behavior.'''
    @property
    def type(self) -> CommandEffectType:
        '''Defines command effect type of behavior.
                    Read/write :py:enum:`aspose.slides.animation.CommandEffectType`.'''
        ...

    @type.setter
    def type(self, value: CommandEffectType):
        '''Defines command effect type of behavior.
                    Read/write :py:enum:`aspose.slides.animation.CommandEffectType`.'''
        ...

    @property
    def command_string(self) -> str:
        ...

    @command_string.setter
    def command_string(self, value: str):
        ...

    @property
    def shape_target(self) -> IShape:
        ...

    @shape_target.setter
    def shape_target(self, value: IShape):
        ...

    @property
    def as_i_behavior(self) -> IBehavior:
        ...

    @property
    def accumulate(self) -> NullableBool:
        ...

    @accumulate.setter
    def accumulate(self, value: NullableBool):
        ...

    @property
    def additive(self) -> BehaviorAdditiveType:
        ...

    @additive.setter
    def additive(self, value: BehaviorAdditiveType):
        ...

    @property
    def properties(self) -> IBehaviorPropertyCollection:
        ...

    @property
    def timing(self) -> ITiming:
        ...

    @timing.setter
    def timing(self, value: ITiming):
        ...

    ...

class IEffect:
    '''Represents animation effect.'''
    @property
    def sequence(self) -> ISequence:
        '''Returns a sequence for an effect.
                    Read-only :py:class:`aspose.slides.animation.ISequence`.'''
        ...

    @property
    def text_animation(self) -> ITextAnimation:
        ...

    @property
    def preset_class_type(self) -> EffectPresetClassType:
        ...

    @preset_class_type.setter
    def preset_class_type(self, value: EffectPresetClassType):
        ...

    @property
    def type(self) -> EffectType:
        '''Defines type of effect.
                    Read/write :py:enum:`aspose.slides.animation.EffectType`.'''
        ...

    @type.setter
    def type(self, value: EffectType):
        '''Defines type of effect.
                    Read/write :py:enum:`aspose.slides.animation.EffectType`.'''
        ...

    @property
    def subtype(self) -> EffectSubtype:
        '''Defines subtype of effect.
                    Read/write :py:enum:`aspose.slides.animation.EffectSubtype`.'''
        ...

    @subtype.setter
    def subtype(self, value: EffectSubtype):
        '''Defines subtype of effect.
                    Read/write :py:enum:`aspose.slides.animation.EffectSubtype`.'''
        ...

    @property
    def behaviors(self) -> IBehaviorCollection:
        '''Returns collection of behavior for effect.
                    Read/write :py:class:`aspose.slides.animation.IBehaviorCollection`.'''
        ...

    @behaviors.setter
    def behaviors(self, value: IBehaviorCollection):
        '''Returns collection of behavior for effect.
                    Read/write :py:class:`aspose.slides.animation.IBehaviorCollection`.'''
        ...

    @property
    def timing(self) -> ITiming:
        '''Defines timing value for effect.
                    Read/write :py:class:`aspose.slides.animation.ITiming`.'''
        ...

    @timing.setter
    def timing(self, value: ITiming):
        '''Defines timing value for effect.
                    Read/write :py:class:`aspose.slides.animation.ITiming`.'''
        ...

    @property
    def target_shape(self) -> IShape:
        ...

    @property
    def sound(self) -> IAudio:
        '''Defined embedded sound for effect.
                    Read/write :py:class:`aspose.slides.IAudio`.'''
        ...

    @sound.setter
    def sound(self, value: IAudio):
        '''Defined embedded sound for effect.
                    Read/write :py:class:`aspose.slides.IAudio`.'''
        ...

    @property
    def stop_previous_sound(self) -> bool:
        ...

    @stop_previous_sound.setter
    def stop_previous_sound(self, value: bool):
        ...

    @property
    def after_animation_type(self) -> AfterAnimationType:
        ...

    @after_animation_type.setter
    def after_animation_type(self, value: AfterAnimationType):
        ...

    @property
    def after_animation_color(self) -> IColorFormat:
        ...

    @after_animation_color.setter
    def after_animation_color(self, value: IColorFormat):
        ...

    @property
    def animate_text_type(self) -> AnimateTextType:
        ...

    @animate_text_type.setter
    def animate_text_type(self, value: AnimateTextType):
        ...

    @property
    def delay_between_text_parts(self) -> float:
        ...

    @delay_between_text_parts.setter
    def delay_between_text_parts(self, value: float):
        ...

    ...

class IFilterEffect:
    '''Represent filter effect of behavior.'''
    @property
    def reveal(self) -> FilterEffectRevealType:
        '''Represents that effect with behavior must reveal (in/out)
                    Read/write :py:enum:`aspose.slides.animation.FilterEffectRevealType`.'''
        ...

    @reveal.setter
    def reveal(self, value: FilterEffectRevealType):
        '''Represents that effect with behavior must reveal (in/out)
                    Read/write :py:enum:`aspose.slides.animation.FilterEffectRevealType`.'''
        ...

    @property
    def type(self) -> FilterEffectType:
        '''Represents type of filter effect.
                    Read/write :py:enum:`aspose.slides.animation.FilterEffectType`.'''
        ...

    @type.setter
    def type(self, value: FilterEffectType):
        '''Represents type of filter effect.
                    Read/write :py:enum:`aspose.slides.animation.FilterEffectType`.'''
        ...

    @property
    def subtype(self) -> FilterEffectSubtype:
        '''Represents subtype of filter effect.
                    Read/write :py:enum:`aspose.slides.animation.FilterEffectSubtype`.'''
        ...

    @subtype.setter
    def subtype(self, value: FilterEffectSubtype):
        '''Represents subtype of filter effect.
                    Read/write :py:enum:`aspose.slides.animation.FilterEffectSubtype`.'''
        ...

    @property
    def as_i_behavior(self) -> IBehavior:
        ...

    @property
    def accumulate(self) -> NullableBool:
        ...

    @accumulate.setter
    def accumulate(self, value: NullableBool):
        ...

    @property
    def additive(self) -> BehaviorAdditiveType:
        ...

    @additive.setter
    def additive(self, value: BehaviorAdditiveType):
        ...

    @property
    def properties(self) -> IBehaviorPropertyCollection:
        ...

    @property
    def timing(self) -> ITiming:
        ...

    @timing.setter
    def timing(self, value: ITiming):
        ...

    ...

class IMotionCmdPath:
    '''Represent one command of a path.'''
    @property
    def points(self) -> List[aspose.pydrawing.PointF]:
        '''Specifies points of command.
                    Read/write :py:class:`aspose.pydrawing.PointF`[].'''
        ...

    @points.setter
    def points(self, value: List[aspose.pydrawing.PointF]):
        '''Specifies points of command.
                    Read/write :py:class:`aspose.pydrawing.PointF`[].'''
        ...

    @property
    def command_type(self) -> MotionCommandPathType:
        ...

    @command_type.setter
    def command_type(self, value: MotionCommandPathType):
        ...

    @property
    def is_relative(self) -> bool:
        ...

    @is_relative.setter
    def is_relative(self, value: bool):
        ...

    @property
    def points_type(self) -> MotionPathPointsType:
        ...

    @points_type.setter
    def points_type(self, value: MotionPathPointsType):
        ...

    ...

class IMotionEffect:
    '''Represent motion effect behavior of effect.'''
    @property
    def from_address(self) -> aspose.pydrawing.PointF:
        ...

    @from_address.setter
    def from_address(self, value: aspose.pydrawing.PointF):
        ...

    @property
    def to(self) -> aspose.pydrawing.PointF:
        '''Specifies the target location for an animation motion effect (in percents).
                    Read/write :py:class:`aspose.pydrawing.PointF`.'''
        ...

    @to.setter
    def to(self, value: aspose.pydrawing.PointF):
        '''Specifies the target location for an animation motion effect (in percents).
                    Read/write :py:class:`aspose.pydrawing.PointF`.'''
        ...

    @property
    def by(self) -> aspose.pydrawing.PointF:
        '''Describes the relative offset value for the animation (in percents).
                    Read/write :py:class:`aspose.pydrawing.PointF`.'''
        ...

    @by.setter
    def by(self, value: aspose.pydrawing.PointF):
        '''Describes the relative offset value for the animation (in percents).
                    Read/write :py:class:`aspose.pydrawing.PointF`.'''
        ...

    @property
    def rotation_center(self) -> aspose.pydrawing.PointF:
        ...

    @rotation_center.setter
    def rotation_center(self, value: aspose.pydrawing.PointF):
        ...

    @property
    def origin(self) -> MotionOriginType:
        '''Specifies what the origin of the motion path is relative to such as the layout of the slide,
                    or the parent.
                    Read/write :py:enum:`aspose.slides.animation.MotionOriginType`.'''
        ...

    @origin.setter
    def origin(self, value: MotionOriginType):
        '''Specifies what the origin of the motion path is relative to such as the layout of the slide,
                    or the parent.
                    Read/write :py:enum:`aspose.slides.animation.MotionOriginType`.'''
        ...

    @property
    def path(self) -> IMotionPath:
        '''Specifies the path primitive followed by coordinates for the animation motion.
                    Read/write :py:class:`aspose.slides.animation.IMotionPath`.'''
        ...

    @path.setter
    def path(self, value: IMotionPath):
        '''Specifies the path primitive followed by coordinates for the animation motion.
                    Read/write :py:class:`aspose.slides.animation.IMotionPath`.'''
        ...

    @property
    def path_edit_mode(self) -> MotionPathEditMode:
        ...

    @path_edit_mode.setter
    def path_edit_mode(self, value: MotionPathEditMode):
        ...

    @property
    def angle(self) -> float:
        '''Describes the relative angle of the motion path.
                    Read/write :py:class:`float`.'''
        ...

    @angle.setter
    def angle(self, value: float):
        '''Describes the relative angle of the motion path.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def as_i_behavior(self) -> IBehavior:
        ...

    @property
    def accumulate(self) -> NullableBool:
        ...

    @accumulate.setter
    def accumulate(self, value: NullableBool):
        ...

    @property
    def additive(self) -> BehaviorAdditiveType:
        ...

    @additive.setter
    def additive(self, value: BehaviorAdditiveType):
        ...

    @property
    def properties(self) -> IBehaviorPropertyCollection:
        ...

    @property
    def timing(self) -> ITiming:
        ...

    @timing.setter
    def timing(self, value: ITiming):
        ...

    ...

class IMotionPath:
    '''Represent motion path.'''
    def add(self, type: MotionCommandPathType, pts: List[aspose.pydrawing.PointF], pts_type: MotionPathPointsType, b_relative_coord: bool) -> IMotionCmdPath:
        '''Add new command to path
        :param type: Type of command for animation motion effect behavior :py:enum:`aspose.slides.animation.MotionCommandPathType`
        :param pts: Points array :py:class:`aspose.pydrawing.PointF`[]
        :param pts_type: Type of points in animation motion path :py:enum:`aspose.slides.animation.MotionPathPointsType`
        :param b_relative_coord: Indicates whether to use relative coordinates or not :py:class:`bool`
        :returns: Command of a path :py:class:`aspose.slides.animation.IMotionCmdPath`'''
        ...

    def insert(self, index: int, type: MotionCommandPathType, pts: List[aspose.pydrawing.PointF], pts_type: MotionPathPointsType, b_relative_coord: bool) -> None:
        '''Insert new command to path
        :param index: Index for command insertion :py:class:`int`
        :param type: Type of command for animation motion effect behavior :py:enum:`aspose.slides.animation.MotionCommandPathType`
        :param pts: Points array :py:class:`aspose.pydrawing.PointF`[]
        :param pts_type: Type of points in animation motion path :py:enum:`aspose.slides.animation.MotionPathPointsType`
        :param b_relative_coord: Indicates whether to use relative coordinates or not :py:class:`bool`'''
        ...

    def clear(self) -> None:
        '''Removes all commands from the collection.'''
        ...

    def remove(self, item: IMotionCmdPath) -> None:
        '''Removes specified commans from the collection.
        :param item: Motion path to remove :py:class:`aspose.slides.animation.IMotionCmdPath`'''
        ...

    def remove_at(self, index: int) -> None:
        '''Removes a command at the specified index.
        :param index: Index for removing command :py:class:`int`'''
        ...

    @property
    def count(self) -> int:
        '''Returns the number of paths in the collection.
                    Read-only :py:class:`int`.'''
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IMotionCmdPath
        ...

    ...

class IPoint:
    '''Represent animation point.'''
    @property
    def time(self) -> float:
        '''Represents time value.
                    Read/write :py:class:`float`.'''
        ...

    @time.setter
    def time(self, value: float):
        '''Represents time value.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def value(self) -> any:
        '''Represents point value.
                    Only: bool, ColorFormat, float, int, string.
                    Read/write :py:class:`any`.'''
        ...

    @value.setter
    def value(self, value: any):
        '''Represents point value.
                    Only: bool, ColorFormat, float, int, string.
                    Read/write :py:class:`any`.'''
        ...

    @property
    def formula(self) -> str:
        '''Formulas within values, from, to, by attributes can be made up of these:
                    Standard arithmetic operators: ‘+’, ‘-‘, ‘*’, ‘/’, ‘^’, ‘%’ (mod)
                    Constants: ‘pi’ ‘e’
                    Conditional operators: ‘abs’, ‘min’, ‘max’, ‘?’ (if)
                    Comparison operators: '==', '>=', '', '!=', '!'
                    Trigonometric operators: ‘sin()’, ‘cos()’, ‘tan()’, ‘asin()’, ‘acos()’, ‘atan()’
                    Natural logarithm ‘ln()’
                    Property references (host supported properties)
                    
                    for example: "#ppt_x+(cos(-2*pi*(1-$))*-#ppt_x-sin(-2*pi*(1-$))*(1-#ppt_y))*(1-$)"
                    Read/write :py:class:`str`.'''
        ...

    @formula.setter
    def formula(self, value: str):
        '''Formulas within values, from, to, by attributes can be made up of these:
                    Standard arithmetic operators: ‘+’, ‘-‘, ‘*’, ‘/’, ‘^’, ‘%’ (mod)
                    Constants: ‘pi’ ‘e’
                    Conditional operators: ‘abs’, ‘min’, ‘max’, ‘?’ (if)
                    Comparison operators: '==', '>=', '', '!=', '!'
                    Trigonometric operators: ‘sin()’, ‘cos()’, ‘tan()’, ‘asin()’, ‘acos()’, ‘atan()’
                    Natural logarithm ‘ln()’
                    Property references (host supported properties)
                    
                    for example: "#ppt_x+(cos(-2*pi*(1-$))*-#ppt_x-sin(-2*pi*(1-$))*(1-#ppt_y))*(1-$)"
                    Read/write :py:class:`str`.'''
        ...

    ...

class IPointCollection:
    '''Represents a collection of portions.'''
    @property
    def count(self) -> int:
        '''Returns the number of points in the collection.
                    Read-only :py:class:`int`.'''
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IPoint
        ...

    ...

class IPropertyEffect:
    '''Represent property effect behavior.'''
    @property
    def from_address(self) -> str:
        ...

    @from_address.setter
    def from_address(self, value: str):
        ...

    @property
    def to(self) -> str:
        '''Specifies the ending value for the animation.
                    Read/write :py:class:`str`.'''
        ...

    @to.setter
    def to(self, value: str):
        '''Specifies the ending value for the animation.
                    Read/write :py:class:`str`.'''
        ...

    @property
    def by(self) -> str:
        '''Specifies a relative offset value for the animation with respect to its
                    position before the start of the animation.
                    Read/write :py:class:`str`.'''
        ...

    @by.setter
    def by(self, value: str):
        '''Specifies a relative offset value for the animation with respect to its
                    position before the start of the animation.
                    Read/write :py:class:`str`.'''
        ...

    @property
    def value_type(self) -> PropertyValueType:
        ...

    @value_type.setter
    def value_type(self, value: PropertyValueType):
        ...

    @property
    def calc_mode(self) -> PropertyCalcModeType:
        ...

    @calc_mode.setter
    def calc_mode(self, value: PropertyCalcModeType):
        ...

    @property
    def points(self) -> IPointCollection:
        '''Specifies the points of the animation.
                    Read/write :py:class:`aspose.slides.animation.IPointCollection`.'''
        ...

    @points.setter
    def points(self, value: IPointCollection):
        '''Specifies the points of the animation.
                    Read/write :py:class:`aspose.slides.animation.IPointCollection`.'''
        ...

    @property
    def as_i_behavior(self) -> IBehavior:
        ...

    @property
    def accumulate(self) -> NullableBool:
        ...

    @accumulate.setter
    def accumulate(self, value: NullableBool):
        ...

    @property
    def additive(self) -> BehaviorAdditiveType:
        ...

    @additive.setter
    def additive(self, value: BehaviorAdditiveType):
        ...

    @property
    def properties(self) -> IBehaviorPropertyCollection:
        ...

    @property
    def timing(self) -> ITiming:
        ...

    @timing.setter
    def timing(self, value: ITiming):
        ...

    ...

class IRotationEffect:
    '''Represent rotation behavior of effect.'''
    @property
    def from_address(self) -> float:
        ...

    @from_address.setter
    def from_address(self, value: float):
        ...

    @property
    def to(self) -> float:
        '''Describes the ending value for the animation.
                    Read/write :py:class:`float`.'''
        ...

    @to.setter
    def to(self, value: float):
        '''Describes the ending value for the animation.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def by(self) -> float:
        '''Describes the relative offset value for the animation.
                    Read/write :py:class:`float`.'''
        ...

    @by.setter
    def by(self, value: float):
        '''Describes the relative offset value for the animation.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def as_i_behavior(self) -> IBehavior:
        ...

    @property
    def accumulate(self) -> NullableBool:
        ...

    @accumulate.setter
    def accumulate(self, value: NullableBool):
        ...

    @property
    def additive(self) -> BehaviorAdditiveType:
        ...

    @additive.setter
    def additive(self, value: BehaviorAdditiveType):
        ...

    @property
    def properties(self) -> IBehaviorPropertyCollection:
        ...

    @property
    def timing(self) -> ITiming:
        ...

    @timing.setter
    def timing(self, value: ITiming):
        ...

    ...

class IScaleEffect:
    '''Represents animation scale effect.'''
    @property
    def zoom_content(self) -> NullableBool:
        ...

    @zoom_content.setter
    def zoom_content(self, value: NullableBool):
        ...

    @property
    def from_address(self) -> aspose.pydrawing.PointF:
        ...

    @from_address.setter
    def from_address(self, value: aspose.pydrawing.PointF):
        ...

    @property
    def to(self) -> aspose.pydrawing.PointF:
        '''Specifies the target location for an animation scale effect (in percents).
                    Read/write :py:class:`aspose.pydrawing.PointF`.'''
        ...

    @to.setter
    def to(self, value: aspose.pydrawing.PointF):
        '''Specifies the target location for an animation scale effect (in percents).
                    Read/write :py:class:`aspose.pydrawing.PointF`.'''
        ...

    @property
    def by(self) -> aspose.pydrawing.PointF:
        '''describes the relative offset value for the animation (in percents).
                    Read/write :py:class:`aspose.pydrawing.PointF`.'''
        ...

    @by.setter
    def by(self, value: aspose.pydrawing.PointF):
        '''describes the relative offset value for the animation (in percents).
                    Read/write :py:class:`aspose.pydrawing.PointF`.'''
        ...

    @property
    def as_i_behavior(self) -> IBehavior:
        ...

    @property
    def accumulate(self) -> NullableBool:
        ...

    @accumulate.setter
    def accumulate(self, value: NullableBool):
        ...

    @property
    def additive(self) -> BehaviorAdditiveType:
        ...

    @additive.setter
    def additive(self, value: BehaviorAdditiveType):
        ...

    @property
    def properties(self) -> IBehaviorPropertyCollection:
        ...

    @property
    def timing(self) -> ITiming:
        ...

    @timing.setter
    def timing(self, value: ITiming):
        ...

    ...

class ISequence:
    '''Represents sequence (collection of effects).'''
    @overload
    def add_effect(self, shape: IShape, effect_type: EffectType, subtype: EffectSubtype, trigger_type: EffectTriggerType) -> IEffect:
        '''Add new effect to the end of sequence.
        :param shape: Shape object :py:class:`aspose.slides.IShape` for adding an effect
        :param effect_type: Type of an animation effect :py:enum:`aspose.slides.animation.EffectType`
        :param subtype: Subtypes of animation effect :py:enum:`aspose.slides.animation.EffectSubtype`
        :param trigger_type: Trigger type of effect :py:enum:`aspose.slides.animation.EffectTriggerType`
        :returns: New effect object :py:class:`aspose.slides.animation.IEffect`'''
        ...

    @overload
    def add_effect(self, paragraph: IParagraph, effect_type: EffectType, subtype: EffectSubtype, trigger_type: EffectTriggerType) -> IEffect:
        '''Add new animation effect for paragraph to the end of sequence.
        :param paragraph: Paragraph object :py:class:`aspose.slides.IParagraph`
        :param effect_type: Type of an animation effect :py:enum:`aspose.slides.animation.EffectType`
        :param subtype: Subtypes of animation effect :py:enum:`aspose.slides.animation.EffectSubtype`
        :param trigger_type: Trigger type of effect :py:enum:`aspose.slides.animation.EffectTriggerType`
        :returns: New effect object :py:class:`aspose.slides.animation.IEffect`'''
        ...

    @overload
    def add_effect(self, chart: aspose.slides.charts.IChart, type: EffectChartMajorGroupingType, index: int, effect_type: EffectType, subtype: EffectSubtype, trigger_type: EffectTriggerType) -> IEffect:
        '''Adds the new chart animation effect for category or series to the end of sequence.
        :param chart: Chart object :py:class:`aspose.slides.charts.IChart`
        :param type: Type of an animation effect :py:enum:`aspose.slides.animation.EffectChartMinorGroupingType`
        :param index: Index :py:class:`int`
        :param effect_type: Type of an animation effect :py:enum:`aspose.slides.animation.EffectType`
        :param subtype: Subtypes of animation effect :py:enum:`aspose.slides.animation.EffectSubtype`
        :param trigger_type: Trigger type of effect :py:enum:`aspose.slides.animation.EffectTriggerType`
        :returns: New effect object :py:class:`aspose.slides.animation.IEffect`'''
        ...

    @overload
    def add_effect(self, chart: aspose.slides.charts.IChart, type: EffectChartMinorGroupingType, series_index: int, categories_index: int, effect_type: EffectType, subtype: EffectSubtype, trigger_type: EffectTriggerType) -> IEffect:
        '''Adds the new chart animation effect for elements in category or series to the end of sequence.
        :param chart: Chart object :py:class:`aspose.slides.charts.IChart`
        :param type: Type of an animation effect :py:enum:`aspose.slides.animation.EffectChartMinorGroupingType`
        :param series_index: Index of chart series :py:class:`int`
        :param categories_index: Index of category :py:class:`int`
        :param effect_type: Type of an animation effect :py:enum:`aspose.slides.animation.EffectType`
        :param subtype: Subtypes of animation effect :py:enum:`aspose.slides.animation.EffectSubtype`
        :param trigger_type: Trigger type of effect :py:enum:`aspose.slides.animation.EffectTriggerType`
        :returns: New effect object :py:class:`aspose.slides.animation.IEffect`'''
        ...

    def remove(self, item: IEffect) -> None:
        '''Removes specified effect from a collection.
        :param item: Effect to remove.'''
        ...

    def remove_at(self, index: int) -> None:
        '''Removes an effect from a collection.
        :param index: Index of effect to remove :py:class:`int`'''
        ...

    def clear(self) -> None:
        '''Removes all effects from a collection.'''
        ...

    def remove_by_shape(self, shape: IShape) -> None:
        '''Remove effect for the specified shape.
        :param shape: Shape object :py:class:`aspose.slides.IShape`'''
        ...

    def get_effects_by_shape(self, shape: IShape) -> List[IEffect]:
        '''Returns array of effects for the specified shape.
        :param shape: Shape object :py:class:`aspose.slides.IShape`
        :returns: Array of effects :py:class:`aspose.slides.animation.IEffect`'''
        ...

    def get_effects_by_paragraph(self, paragraph: IParagraph) -> List[IEffect]:
        '''Returns array of effects for the specified paragraph.
        :param paragraph: Paragraph object :py:class:`aspose.slides.IParagraph`
        :returns: Array of effects :py:class:`aspose.slides.animation.IEffect`'''
        ...

    def get_count(self, shape: IShape) -> int:
        '''Returns count of effects for the specified shape.
        :param shape: Shape object :py:class:`aspose.slides.IShape`
        :returns: Count of effects :py:class:`int`'''
        ...

    @property
    def count(self) -> int:
        '''Returns the number of effects in a sequense.
                    Read-only :py:class:`int`.'''
        ...

    @property
    def trigger_shape(self) -> IShape:
        ...

    @trigger_shape.setter
    def trigger_shape(self, value: IShape):
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IEffect
        ...

    ...

class ISequenceCollection:
    '''Represents collection of interactive sequences.'''
    def add(self, shape_trigger: IShape) -> ISequence:
        '''Add new interactive sequence.
        :param shape_trigger: Shape object :py:class:`aspose.slides.IShape`
        :returns: New sequence :py:class:`aspose.slides.animation.ISequence`'''
        ...

    def remove(self, item: ISequence) -> None:
        '''Removes specified sequence from a collection.
        :param item: Sequence to remove.'''
        ...

    def remove_at(self, index: int) -> None:
        '''Removes sequence at the specified index.
        :param index: Index of element in the collection :py:class:`int`'''
        ...

    def clear(self) -> None:
        '''Removes all sequences from a collection.'''
        ...

    @property
    def count(self) -> int:
        '''Returns the number of elements in a collection
                    Read-only :py:class:`int`.'''
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> ISequence
        ...

    ...

class ISetEffect:
    '''Represents a set effect for an animation behavior.'''
    @property
    def to(self) -> any:
        '''Specifies the certain attribute of a effect after an animation effect.
                    Represents point value.
                    Only: bool, ColorFormat, float, int, string.
                    Read/write :py:class:`any`.'''
        ...

    @to.setter
    def to(self, value: any):
        '''Specifies the certain attribute of a effect after an animation effect.
                    Represents point value.
                    Only: bool, ColorFormat, float, int, string.
                    Read/write :py:class:`any`.'''
        ...

    @property
    def as_i_behavior(self) -> IBehavior:
        ...

    @property
    def accumulate(self) -> NullableBool:
        ...

    @accumulate.setter
    def accumulate(self, value: NullableBool):
        ...

    @property
    def additive(self) -> BehaviorAdditiveType:
        ...

    @additive.setter
    def additive(self, value: BehaviorAdditiveType):
        ...

    @property
    def properties(self) -> IBehaviorPropertyCollection:
        ...

    @property
    def timing(self) -> ITiming:
        ...

    @timing.setter
    def timing(self, value: ITiming):
        ...

    ...

class ITextAnimation:
    '''Represent text animation.'''
    def add_effect(self, effect_type: EffectType, subtype: EffectSubtype, trigger_type: EffectTriggerType) -> IEffect:
        '''Add new effect to the end of current sequence to end of group text animations.
                    Only valid if count of text paragraphs equal or greater of counts effect of this group!
        :param effect_type: Type of an animation effect :py:enum:`aspose.slides.animation.EffectType`
        :param subtype: Subtypes of animation effect :py:enum:`aspose.slides.animation.EffectSubtype`
        :param trigger_type: Trigger type of effect :py:enum:`aspose.slides.animation.EffectTriggerType`
        :returns: New effect object :py:class:`aspose.slides.animation.IEffect`'''
        ...

    @property
    def build_type(self) -> BuildType:
        ...

    @build_type.setter
    def build_type(self, value: BuildType):
        ...

    @property
    def effect_animate_background_shape(self) -> IEffect:
        ...

    @effect_animate_background_shape.setter
    def effect_animate_background_shape(self, value: IEffect):
        ...

    ...

class ITextAnimationCollection:
    '''Represents collection of text animations.'''
    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> ITextAnimation
        ...

    ...

class ITiming:
    '''Represents animation timing.'''
    @property
    def accelerate(self) -> float:
        '''Describes the percentage of duration accelerate behavior effect.
                    Read/write :py:class:`float`.'''
        ...

    @accelerate.setter
    def accelerate(self, value: float):
        '''Describes the percentage of duration accelerate behavior effect.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def decelerate(self) -> float:
        '''Describes the percentage of duration decelerate behavior effect.
                    Read/write :py:class:`float`.'''
        ...

    @decelerate.setter
    def decelerate(self, value: float):
        '''Describes the percentage of duration decelerate behavior effect.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def auto_reverse(self) -> bool:
        ...

    @auto_reverse.setter
    def auto_reverse(self, value: bool):
        ...

    @property
    def duration(self) -> float:
        '''Describes the duration of animation effect.
                    Read/write :py:class:`float`.'''
        ...

    @duration.setter
    def duration(self, value: float):
        '''Describes the duration of animation effect.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def repeat_count(self) -> float:
        ...

    @repeat_count.setter
    def repeat_count(self, value: float):
        ...

    @property
    def repeat_until_end_slide(self) -> bool:
        ...

    @repeat_until_end_slide.setter
    def repeat_until_end_slide(self, value: bool):
        ...

    @property
    def repeat_until_next_click(self) -> bool:
        ...

    @repeat_until_next_click.setter
    def repeat_until_next_click(self, value: bool):
        ...

    @property
    def repeat_duration(self) -> float:
        ...

    @repeat_duration.setter
    def repeat_duration(self, value: float):
        ...

    @property
    def restart(self) -> EffectRestartType:
        '''Specifies if a effect is to restart after complete.
                    Read/write :py:enum:`aspose.slides.animation.EffectRestartType`.'''
        ...

    @restart.setter
    def restart(self, value: EffectRestartType):
        '''Specifies if a effect is to restart after complete.
                    Read/write :py:enum:`aspose.slides.animation.EffectRestartType`.'''
        ...

    @property
    def speed(self) -> float:
        '''Specifies the percentage by which to speed up (or slow down) the timing.
                    Read/write :py:class:`float`.'''
        ...

    @speed.setter
    def speed(self, value: float):
        '''Specifies the percentage by which to speed up (or slow down) the timing.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def trigger_delay_time(self) -> float:
        ...

    @trigger_delay_time.setter
    def trigger_delay_time(self, value: float):
        ...

    @property
    def trigger_type(self) -> EffectTriggerType:
        ...

    @trigger_type.setter
    def trigger_type(self, value: EffectTriggerType):
        ...

    @property
    def rewind(self) -> bool:
        '''This attribute specifies if the effect will rewind when done playing.
                     Read/write :py:class:`bool`.'''
        ...

    @rewind.setter
    def rewind(self, value: bool):
        '''This attribute specifies if the effect will rewind when done playing.
                     Read/write :py:class:`bool`.'''
        ...

    ...

class MotionCmdPath:
    '''Represent one command of a path.'''
    @property
    def points(self) -> List[aspose.pydrawing.PointF]:
        '''Specifies points of command.
                    Read/write :py:class:`aspose.pydrawing.PointF`[].'''
        ...

    @points.setter
    def points(self, value: List[aspose.pydrawing.PointF]):
        '''Specifies points of command.
                    Read/write :py:class:`aspose.pydrawing.PointF`[].'''
        ...

    @property
    def command_type(self) -> MotionCommandPathType:
        ...

    @command_type.setter
    def command_type(self, value: MotionCommandPathType):
        ...

    @property
    def is_relative(self) -> bool:
        ...

    @is_relative.setter
    def is_relative(self, value: bool):
        ...

    @property
    def points_type(self) -> MotionPathPointsType:
        ...

    @points_type.setter
    def points_type(self, value: MotionPathPointsType):
        ...

    ...

class MotionEffect(Behavior):
    '''Represent motion effect behavior of effect.'''
    def __init__(self):
        '''Creates new instance.'''
        ...

    @property
    def accumulate(self) -> NullableBool:
        '''Represents whether animation behaviors are accumulated.
                    Read/write :py:enum:`aspose.slides.NullableBool`.'''
        ...

    @accumulate.setter
    def accumulate(self, value: NullableBool):
        '''Represents whether animation behaviors are accumulated.
                    Read/write :py:enum:`aspose.slides.NullableBool`.'''
        ...

    @property
    def additive(self) -> BehaviorAdditiveType:
        '''Represents whether the current animation behavior is combined with other running animations.
                    Read/write :py:enum:`aspose.slides.animation.BehaviorAdditiveType`.'''
        ...

    @additive.setter
    def additive(self, value: BehaviorAdditiveType):
        '''Represents whether the current animation behavior is combined with other running animations.
                    Read/write :py:enum:`aspose.slides.animation.BehaviorAdditiveType`.'''
        ...

    @property
    def properties(self) -> IBehaviorPropertyCollection:
        '''Represents properties of behavior.
                    Read-only :py:class:`aspose.slides.animation.IBehaviorPropertyCollection`.'''
        ...

    @property
    def timing(self) -> ITiming:
        '''Represents timing properties for the effect behavior.
                    Read/write :py:class:`aspose.slides.animation.ITiming`.'''
        ...

    @timing.setter
    def timing(self, value: ITiming):
        '''Represents timing properties for the effect behavior.
                    Read/write :py:class:`aspose.slides.animation.ITiming`.'''
        ...

    @property
    def from_address(self) -> aspose.pydrawing.PointF:
        ...

    @from_address.setter
    def from_address(self, value: aspose.pydrawing.PointF):
        ...

    @property
    def to(self) -> aspose.pydrawing.PointF:
        '''Specifies the target location for an animation motion effect (in percents).
                    Read/write :py:class:`aspose.pydrawing.PointF`.'''
        ...

    @to.setter
    def to(self, value: aspose.pydrawing.PointF):
        '''Specifies the target location for an animation motion effect (in percents).
                    Read/write :py:class:`aspose.pydrawing.PointF`.'''
        ...

    @property
    def by(self) -> aspose.pydrawing.PointF:
        '''Describes the relative offset value for the animation (in percents).
                    Read/write :py:class:`aspose.pydrawing.PointF`.'''
        ...

    @by.setter
    def by(self, value: aspose.pydrawing.PointF):
        '''Describes the relative offset value for the animation (in percents).
                    Read/write :py:class:`aspose.pydrawing.PointF`.'''
        ...

    @property
    def rotation_center(self) -> aspose.pydrawing.PointF:
        ...

    @rotation_center.setter
    def rotation_center(self, value: aspose.pydrawing.PointF):
        ...

    @property
    def origin(self) -> MotionOriginType:
        '''Specifies what the origin of the motion path is relative to such as the layout of the slide,
                    or the parent.
                    Read/write :py:enum:`aspose.slides.animation.MotionOriginType`.'''
        ...

    @origin.setter
    def origin(self, value: MotionOriginType):
        '''Specifies what the origin of the motion path is relative to such as the layout of the slide,
                    or the parent.
                    Read/write :py:enum:`aspose.slides.animation.MotionOriginType`.'''
        ...

    @property
    def path(self) -> IMotionPath:
        '''Specifies the path primitive followed by coordinates for the animation motion.
                    Read/write :py:class:`aspose.slides.animation.IMotionPath`.'''
        ...

    @path.setter
    def path(self, value: IMotionPath):
        '''Specifies the path primitive followed by coordinates for the animation motion.
                    Read/write :py:class:`aspose.slides.animation.IMotionPath`.'''
        ...

    @property
    def path_edit_mode(self) -> MotionPathEditMode:
        ...

    @path_edit_mode.setter
    def path_edit_mode(self, value: MotionPathEditMode):
        ...

    @property
    def angle(self) -> float:
        '''Describes the relative angle of the motion path.
                    Read/write :py:class:`float`.'''
        ...

    @angle.setter
    def angle(self, value: float):
        '''Describes the relative angle of the motion path.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def as_i_behavior(self) -> IBehavior:
        ...

    ...

class MotionPath:
    '''Represent motion path.'''
    def __init__(self):
        ...

    def add(self, type: MotionCommandPathType, pts: List[aspose.pydrawing.PointF], pts_type: MotionPathPointsType, b_relative_coord: bool) -> IMotionCmdPath:
        '''Add new command to path'''
        ...

    def insert(self, index: int, type: MotionCommandPathType, pts: List[aspose.pydrawing.PointF], pts_type: MotionPathPointsType, b_relative_coord: bool) -> None:
        '''Insert new command to path'''
        ...

    def clear(self) -> None:
        '''Removes all commands from the collection.'''
        ...

    def remove(self, item: IMotionCmdPath) -> None:
        '''Removes specified commans from the collection.
        :param item: Motion path to remove.'''
        ...

    def remove_at(self, index: int) -> None:
        '''Removes a command at the specified index.'''
        ...

    @property
    def count(self) -> int:
        '''Returns the number of paths in the collection.
                    Read-only :py:class:`int`.'''
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IMotionCmdPath
        ...

    ...

class Point:
    '''Represent animation point.'''
    def __init__(self):
        '''Default constructor.'''
        ...

    def __init__(self, time: float, value: any, formula: str):
        '''Create animation point with time, value and formula.'''
        ...

    @property
    def time(self) -> float:
        '''Represents time value.
                    Read/write :py:class:`float`.'''
        ...

    @time.setter
    def time(self, value: float):
        '''Represents time value.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def value(self) -> any:
        '''Represents point value.
                    Only: bool, ColorFormat, float, int, string.
                    Read/write :py:class:`any`.'''
        ...

    @value.setter
    def value(self, value: any):
        '''Represents point value.
                    Only: bool, ColorFormat, float, int, string.
                    Read/write :py:class:`any`.'''
        ...

    @property
    def formula(self) -> str:
        '''Formulas within values, from, to, by attributes can be made up of these:
                    Standard arithmetic operators: ‘+’, ‘-‘, ‘*’, ‘/’, ‘^’, ‘%’ (mod)
                    Constants: ‘pi’ ‘e’
                    Conditional operators: ‘abs’, ‘min’, ‘max’, ‘?’ (if)
                    Comparison operators: '==', '>=', '', '!=', '!'
                    Trigonometric operators: ‘sin()’, ‘cos()’, ‘tan()’, ‘asin()’, ‘acos()’, ‘atan()’
                    Natural logarithm ‘ln()’
                    Property references (host supported properties)
                    
                    for example: "#ppt_x+(cos(-2*pi*(1-$))*-#ppt_x-sin(-2*pi*(1-$))*(1-#ppt_y))*(1-$)"
                    Read/write :py:class:`str`.'''
        ...

    @formula.setter
    def formula(self, value: str):
        '''Formulas within values, from, to, by attributes can be made up of these:
                    Standard arithmetic operators: ‘+’, ‘-‘, ‘*’, ‘/’, ‘^’, ‘%’ (mod)
                    Constants: ‘pi’ ‘e’
                    Conditional operators: ‘abs’, ‘min’, ‘max’, ‘?’ (if)
                    Comparison operators: '==', '>=', '', '!=', '!'
                    Trigonometric operators: ‘sin()’, ‘cos()’, ‘tan()’, ‘asin()’, ‘acos()’, ‘atan()’
                    Natural logarithm ‘ln()’
                    Property references (host supported properties)
                    
                    for example: "#ppt_x+(cos(-2*pi*(1-$))*-#ppt_x-sin(-2*pi*(1-$))*(1-#ppt_y))*(1-$)"
                    Read/write :py:class:`str`.'''
        ...

    ...

class PointCollection:
    '''Represent collection of animation points.'''
    def __init__(self):
        ...

    @property
    def count(self) -> int:
        '''Returns the number of points in the collection.
                    Read-only :py:class:`int`.'''
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IPoint
        ...

    ...

class PropertyEffect(Behavior):
    '''Represent property effect behavior.'''
    def __init__(self):
        '''Creates new instance.'''
        ...

    @property
    def accumulate(self) -> NullableBool:
        '''Represents whether animation behaviors are accumulated.
                    Read/write :py:enum:`aspose.slides.NullableBool`.'''
        ...

    @accumulate.setter
    def accumulate(self, value: NullableBool):
        '''Represents whether animation behaviors are accumulated.
                    Read/write :py:enum:`aspose.slides.NullableBool`.'''
        ...

    @property
    def additive(self) -> BehaviorAdditiveType:
        '''Represents whether the current animation behavior is combined with other running animations.
                    Read/write :py:enum:`aspose.slides.animation.BehaviorAdditiveType`.'''
        ...

    @additive.setter
    def additive(self, value: BehaviorAdditiveType):
        '''Represents whether the current animation behavior is combined with other running animations.
                    Read/write :py:enum:`aspose.slides.animation.BehaviorAdditiveType`.'''
        ...

    @property
    def properties(self) -> IBehaviorPropertyCollection:
        '''Represents properties of behavior.
                    Read-only :py:class:`aspose.slides.animation.IBehaviorPropertyCollection`.'''
        ...

    @property
    def timing(self) -> ITiming:
        '''Represents timing properties for the effect behavior.
                    Read/write :py:class:`aspose.slides.animation.ITiming`.'''
        ...

    @timing.setter
    def timing(self, value: ITiming):
        '''Represents timing properties for the effect behavior.
                    Read/write :py:class:`aspose.slides.animation.ITiming`.'''
        ...

    @property
    def from_address(self) -> str:
        ...

    @from_address.setter
    def from_address(self, value: str):
        ...

    @property
    def to(self) -> str:
        '''Specifies the ending value for the animation.
                    Read/write :py:class:`str`.'''
        ...

    @to.setter
    def to(self, value: str):
        '''Specifies the ending value for the animation.
                    Read/write :py:class:`str`.'''
        ...

    @property
    def by(self) -> str:
        '''Specifies a relative offset value for the animation with respect to its
                    position before the start of the animation.
                    Read/write :py:class:`str`.'''
        ...

    @by.setter
    def by(self, value: str):
        '''Specifies a relative offset value for the animation with respect to its
                    position before the start of the animation.
                    Read/write :py:class:`str`.'''
        ...

    @property
    def value_type(self) -> PropertyValueType:
        ...

    @value_type.setter
    def value_type(self, value: PropertyValueType):
        ...

    @property
    def calc_mode(self) -> PropertyCalcModeType:
        ...

    @calc_mode.setter
    def calc_mode(self, value: PropertyCalcModeType):
        ...

    @property
    def points(self) -> IPointCollection:
        '''Specifies the points of the animation.
                    Read/write :py:class:`aspose.slides.animation.IPointCollection`.'''
        ...

    @points.setter
    def points(self, value: IPointCollection):
        '''Specifies the points of the animation.
                    Read/write :py:class:`aspose.slides.animation.IPointCollection`.'''
        ...

    @property
    def as_i_behavior(self) -> IBehavior:
        ...

    ...

class RotationEffect(Behavior):
    '''Represent rotation behavior of effect.'''
    def __init__(self):
        '''Creates new instance.'''
        ...

    @property
    def accumulate(self) -> NullableBool:
        '''Represents whether animation behaviors are accumulated.
                    Read/write :py:enum:`aspose.slides.NullableBool`.'''
        ...

    @accumulate.setter
    def accumulate(self, value: NullableBool):
        '''Represents whether animation behaviors are accumulated.
                    Read/write :py:enum:`aspose.slides.NullableBool`.'''
        ...

    @property
    def additive(self) -> BehaviorAdditiveType:
        '''Represents whether the current animation behavior is combined with other running animations.
                    Read/write :py:enum:`aspose.slides.animation.BehaviorAdditiveType`.'''
        ...

    @additive.setter
    def additive(self, value: BehaviorAdditiveType):
        '''Represents whether the current animation behavior is combined with other running animations.
                    Read/write :py:enum:`aspose.slides.animation.BehaviorAdditiveType`.'''
        ...

    @property
    def properties(self) -> IBehaviorPropertyCollection:
        '''Represents properties of behavior.
                    Read-only :py:class:`aspose.slides.animation.IBehaviorPropertyCollection`.'''
        ...

    @property
    def timing(self) -> ITiming:
        '''Represents timing properties for the effect behavior.
                    Read/write :py:class:`aspose.slides.animation.ITiming`.'''
        ...

    @timing.setter
    def timing(self, value: ITiming):
        '''Represents timing properties for the effect behavior.
                    Read/write :py:class:`aspose.slides.animation.ITiming`.'''
        ...

    @property
    def from_address(self) -> float:
        ...

    @from_address.setter
    def from_address(self, value: float):
        ...

    @property
    def to(self) -> float:
        '''Describes the ending value for the animation.
                    Read/write :py:class:`float`.'''
        ...

    @to.setter
    def to(self, value: float):
        '''Describes the ending value for the animation.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def by(self) -> float:
        '''Describes the relative offset value for the animation.
                    Read/write :py:class:`float`.'''
        ...

    @by.setter
    def by(self, value: float):
        '''Describes the relative offset value for the animation.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def as_i_behavior(self) -> IBehavior:
        ...

    ...

class ScaleEffect(Behavior):
    '''Represents animation scale effect.'''
    def __init__(self):
        '''Creates new instance.'''
        ...

    @property
    def accumulate(self) -> NullableBool:
        '''Represents whether animation behaviors are accumulated.
                    Read/write :py:enum:`aspose.slides.NullableBool`.'''
        ...

    @accumulate.setter
    def accumulate(self, value: NullableBool):
        '''Represents whether animation behaviors are accumulated.
                    Read/write :py:enum:`aspose.slides.NullableBool`.'''
        ...

    @property
    def additive(self) -> BehaviorAdditiveType:
        '''Represents whether the current animation behavior is combined with other running animations.
                    Read/write :py:enum:`aspose.slides.animation.BehaviorAdditiveType`.'''
        ...

    @additive.setter
    def additive(self, value: BehaviorAdditiveType):
        '''Represents whether the current animation behavior is combined with other running animations.
                    Read/write :py:enum:`aspose.slides.animation.BehaviorAdditiveType`.'''
        ...

    @property
    def properties(self) -> IBehaviorPropertyCollection:
        '''Represents properties of behavior.
                    Read-only :py:class:`aspose.slides.animation.IBehaviorPropertyCollection`.'''
        ...

    @property
    def timing(self) -> ITiming:
        '''Represents timing properties for the effect behavior.
                    Read/write :py:class:`aspose.slides.animation.ITiming`.'''
        ...

    @timing.setter
    def timing(self, value: ITiming):
        '''Represents timing properties for the effect behavior.
                    Read/write :py:class:`aspose.slides.animation.ITiming`.'''
        ...

    @property
    def zoom_content(self) -> NullableBool:
        ...

    @zoom_content.setter
    def zoom_content(self, value: NullableBool):
        ...

    @property
    def from_address(self) -> aspose.pydrawing.PointF:
        ...

    @from_address.setter
    def from_address(self, value: aspose.pydrawing.PointF):
        ...

    @property
    def to(self) -> aspose.pydrawing.PointF:
        '''Specifies the target location for an animation scale effect (in percents).
                    Read/write :py:class:`aspose.pydrawing.PointF`.'''
        ...

    @to.setter
    def to(self, value: aspose.pydrawing.PointF):
        '''Specifies the target location for an animation scale effect (in percents).
                    Read/write :py:class:`aspose.pydrawing.PointF`.'''
        ...

    @property
    def by(self) -> aspose.pydrawing.PointF:
        '''describes the relative offset value for the animation (in percents).
                    Read/write :py:class:`aspose.pydrawing.PointF`.'''
        ...

    @by.setter
    def by(self, value: aspose.pydrawing.PointF):
        '''describes the relative offset value for the animation (in percents).
                    Read/write :py:class:`aspose.pydrawing.PointF`.'''
        ...

    @property
    def as_i_behavior(self) -> IBehavior:
        ...

    ...

class Sequence:
    '''Represents sequence (collection of effects).'''
    @overload
    def add_effect(self, shape: IShape, effect_type: EffectType, subtype: EffectSubtype, trigger_type: EffectTriggerType) -> IEffect:
        '''Add new effect to the end of sequence.
        :param shape: Shape object :py:class:`aspose.slides.IShape` for adding an effect
        :param effect_type: Type of an animation effect :py:enum:`aspose.slides.animation.EffectType`
        :param subtype: Subtypes of animation effect :py:enum:`aspose.slides.animation.EffectSubtype`
        :param trigger_type: Trigger type of effect :py:enum:`aspose.slides.animation.EffectTriggerType`
        :returns: New effect object :py:class:`aspose.slides.animation.IEffect`'''
        ...

    @overload
    def add_effect(self, paragraph: IParagraph, effect_type: EffectType, subtype: EffectSubtype, trigger_type: EffectTriggerType) -> IEffect:
        '''Add new animation effect for paragraph to the end of sequence.
        :param paragraph: Paragraph object :py:class:`aspose.slides.IParagraph`
        :param effect_type: Type of an animation effect :py:enum:`aspose.slides.animation.EffectType`
        :param subtype: Subtypes of animation effect :py:enum:`aspose.slides.animation.EffectSubtype`
        :param trigger_type: Trigger type of effect :py:enum:`aspose.slides.animation.EffectTriggerType`
        :returns: New effect object :py:class:`aspose.slides.animation.IEffect`'''
        ...

    @overload
    def add_effect(self, chart: aspose.slides.charts.IChart, type: EffectChartMajorGroupingType, index: int, effect_type: EffectType, subtype: EffectSubtype, trigger_type: EffectTriggerType) -> IEffect:
        '''Adds the new chart animation effect for category or series to the end of sequence.
        :param chart: Chart object :py:class:`aspose.slides.charts.IChart`
        :param type: Type of an animation effect :py:enum:`aspose.slides.animation.EffectChartMinorGroupingType`
        :param index: Index :py:class:`int`
        :param effect_type: Type of an animation effect :py:enum:`aspose.slides.animation.EffectType`
        :param subtype: Subtypes of animation effect :py:enum:`aspose.slides.animation.EffectSubtype`
        :param trigger_type: Trigger type of effect :py:enum:`aspose.slides.animation.EffectTriggerType`
        :returns: New effect object :py:class:`aspose.slides.animation.IEffect`'''
        ...

    @overload
    def add_effect(self, chart: aspose.slides.charts.IChart, type: EffectChartMinorGroupingType, series_index: int, categories_index: int, effect_type: EffectType, subtype: EffectSubtype, trigger_type: EffectTriggerType) -> IEffect:
        '''Adds the new chart animation effect for elements in category or series to the end of sequence.
        :param chart: Chart object :py:class:`aspose.slides.charts.IChart`
        :param type: Type of an animation effect :py:enum:`aspose.slides.animation.EffectChartMinorGroupingType`
        :param series_index: Index of chart series :py:class:`int`
        :param categories_index: Index of category :py:class:`int`
        :param effect_type: Type of an animation effect :py:enum:`aspose.slides.animation.EffectType`
        :param subtype: Subtypes of animation effect :py:enum:`aspose.slides.animation.EffectSubtype`
        :param trigger_type: Trigger type of effect :py:enum:`aspose.slides.animation.EffectTriggerType`
        :returns: New effect object :py:class:`aspose.slides.animation.IEffect`'''
        ...

    def remove(self, item: IEffect) -> None:
        '''Removes specified effect from a collection.
        :param item: Effect to remove.'''
        ...

    def remove_at(self, index: int) -> None:
        '''Removes an effect from a collection.'''
        ...

    def clear(self) -> None:
        '''Removes all effects from a collection.'''
        ...

    def remove_by_shape(self, shape: IShape) -> None:
        '''Remove effect for the specified shape.'''
        ...

    def get_effects_by_shape(self, shape: IShape) -> List[IEffect]:
        '''Returns array of effects for the specified shape.'''
        ...

    def get_effects_by_paragraph(self, paragraph: IParagraph) -> List[IEffect]:
        '''Returns array of effects for the specified paragraph.'''
        ...

    def get_count(self, shape: IShape) -> int:
        '''Returns count of effects for the specified shape.'''
        ...

    @property
    def count(self) -> int:
        '''Returns the number of effects in a sequense.
                    Read-only :py:class:`int`.'''
        ...

    @property
    def trigger_shape(self) -> IShape:
        ...

    @trigger_shape.setter
    def trigger_shape(self, value: IShape):
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> IEffect
        ...

    ...

class SequenceCollection:
    '''Represents collection of interactive sequences.'''
    def add(self, shape_trigger: IShape) -> ISequence:
        '''Add new interactive sequence.
                    Read/write :py:class:`aspose.slides.animation.Sequence`.'''
        ...

    def remove(self, item: ISequence) -> None:
        '''Removes specified sequence from a collection.
        :param item: Sequence to remove.'''
        ...

    def remove_at(self, index: int) -> None:
        '''Removes sequence at the specified index.'''
        ...

    def clear(self) -> None:
        '''Removes all sequences from a collection.'''
        ...

    @property
    def count(self) -> int:
        '''Returns the number of elements in a collection
                    Read-only :py:class:`int`.'''
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> ISequence
        ...

    ...

class SetEffect(Behavior):
    '''Represents a set effect for an animation behavior.'''
    def __init__(self):
        '''Creates new instance.'''
        ...

    @property
    def accumulate(self) -> NullableBool:
        '''Represents whether animation behaviors are accumulated.
                    Read/write :py:enum:`aspose.slides.NullableBool`.'''
        ...

    @accumulate.setter
    def accumulate(self, value: NullableBool):
        '''Represents whether animation behaviors are accumulated.
                    Read/write :py:enum:`aspose.slides.NullableBool`.'''
        ...

    @property
    def additive(self) -> BehaviorAdditiveType:
        '''Represents whether the current animation behavior is combined with other running animations.
                    Read/write :py:enum:`aspose.slides.animation.BehaviorAdditiveType`.'''
        ...

    @additive.setter
    def additive(self, value: BehaviorAdditiveType):
        '''Represents whether the current animation behavior is combined with other running animations.
                    Read/write :py:enum:`aspose.slides.animation.BehaviorAdditiveType`.'''
        ...

    @property
    def properties(self) -> IBehaviorPropertyCollection:
        '''Represents properties of behavior.
                    Read-only :py:class:`aspose.slides.animation.IBehaviorPropertyCollection`.'''
        ...

    @property
    def timing(self) -> ITiming:
        '''Represents timing properties for the effect behavior.
                    Read/write :py:class:`aspose.slides.animation.ITiming`.'''
        ...

    @timing.setter
    def timing(self, value: ITiming):
        '''Represents timing properties for the effect behavior.
                    Read/write :py:class:`aspose.slides.animation.ITiming`.'''
        ...

    @property
    def to(self) -> any:
        '''Specifies the certain attribute of a effect after an animation effect.
                    Represents point value.
                    Only: bool, ColorFormat, float, int, string.
                    Read/write :py:class:`any`.'''
        ...

    @to.setter
    def to(self, value: any):
        '''Specifies the certain attribute of a effect after an animation effect.
                    Represents point value.
                    Only: bool, ColorFormat, float, int, string.
                    Read/write :py:class:`any`.'''
        ...

    @property
    def as_i_behavior(self) -> IBehavior:
        ...

    ...

class TextAnimation:
    '''Represent text animation.'''
    def __init__(self):
        ...

    def add_effect(self, effect_type: EffectType, subtype: EffectSubtype, trigger_type: EffectTriggerType) -> IEffect:
        '''Add new effect to the end of current sequence to end of group text animations.
                    Only valid if count of text paragraphs equal or greater of counts effect of this group!
        :param effect_type: Type of an animation effect :py:enum:`aspose.slides.animation.EffectType`
        :param subtype: Subtypes of animation effect :py:enum:`aspose.slides.animation.EffectSubtype`
        :param trigger_type: Trigger type of effect :py:enum:`aspose.slides.animation.EffectTriggerType`
        :returns: New effect object :py:class:`aspose.slides.animation.IEffect`'''
        ...

    @property
    def build_type(self) -> BuildType:
        ...

    @build_type.setter
    def build_type(self, value: BuildType):
        ...

    @property
    def effect_animate_background_shape(self) -> IEffect:
        ...

    @effect_animate_background_shape.setter
    def effect_animate_background_shape(self, value: IEffect):
        ...

    ...

class TextAnimationCollection:
    '''Represents collection of text animations.'''
    def __init__(self):
        ...

    def add(self) -> TextAnimation:
        '''Adds new text animation to the collection.
        :returns: Added ``TextAnimation``'''
        ...

    @property
    def as_i_collection(self) -> list:
        ...

    @property
    def as_i_enumerable(self) -> collections.abc.Iterable:
        ...

    def __getitem__(self, key: int) -> ITextAnimation
        ...

    ...

class Timing:
    '''Represents animation timing.'''
    @property
    def accelerate(self) -> float:
        '''Describes the percentage of duration accelerate behavior effect.
                    Read/write :py:class:`float`.'''
        ...

    @accelerate.setter
    def accelerate(self, value: float):
        '''Describes the percentage of duration accelerate behavior effect.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def decelerate(self) -> float:
        '''Describes the percentage of duration decelerate behavior effect.
                    Read/write :py:class:`float`.'''
        ...

    @decelerate.setter
    def decelerate(self, value: float):
        '''Describes the percentage of duration decelerate behavior effect.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def auto_reverse(self) -> bool:
        ...

    @auto_reverse.setter
    def auto_reverse(self, value: bool):
        ...

    @property
    def duration(self) -> float:
        '''Describes the duration of animation effect.
                    Read/write :py:class:`float`.'''
        ...

    @duration.setter
    def duration(self, value: float):
        '''Describes the duration of animation effect.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def repeat_count(self) -> float:
        ...

    @repeat_count.setter
    def repeat_count(self, value: float):
        ...

    @property
    def repeat_until_end_slide(self) -> bool:
        ...

    @repeat_until_end_slide.setter
    def repeat_until_end_slide(self, value: bool):
        ...

    @property
    def repeat_until_next_click(self) -> bool:
        ...

    @repeat_until_next_click.setter
    def repeat_until_next_click(self, value: bool):
        ...

    @property
    def repeat_duration(self) -> float:
        ...

    @repeat_duration.setter
    def repeat_duration(self, value: float):
        ...

    @property
    def restart(self) -> EffectRestartType:
        '''Specifies if a effect is to restart after complete.
                    Read/write :py:enum:`aspose.slides.animation.EffectRestartType`.'''
        ...

    @restart.setter
    def restart(self, value: EffectRestartType):
        '''Specifies if a effect is to restart after complete.
                    Read/write :py:enum:`aspose.slides.animation.EffectRestartType`.'''
        ...

    @property
    def rewind(self) -> bool:
        '''This attribute specifies if the effect will rewind when done playing.
                     Read/write :py:class:`bool`.'''
        ...

    @rewind.setter
    def rewind(self, value: bool):
        '''This attribute specifies if the effect will rewind when done playing.
                     Read/write :py:class:`bool`.'''
        ...

    @property
    def speed(self) -> float:
        '''Specifies the percentage by which to speed up (or slow down) the timing.
                    Read/write :py:class:`float`.'''
        ...

    @speed.setter
    def speed(self, value: float):
        '''Specifies the percentage by which to speed up (or slow down) the timing.
                    Read/write :py:class:`float`.'''
        ...

    @property
    def trigger_delay_time(self) -> float:
        ...

    @trigger_delay_time.setter
    def trigger_delay_time(self, value: float):
        ...

    @property
    def trigger_type(self) -> EffectTriggerType:
        ...

    @trigger_type.setter
    def trigger_type(self, value: EffectTriggerType):
        ...

    ...

class AfterAnimationType:
    '''Represents the after animation type of an animation effect.'''
    @classmethod
    @property
    def DO_NOT_DIM(cls) -> AfterAnimationType:
        '''Don't Dim after animation type.'''
        ...

    @classmethod
    @property
    def COLOR(cls) -> AfterAnimationType:
        '''Color after animation type.'''
        ...

    @classmethod
    @property
    def HIDE_AFTER_ANIMATION(cls) -> AfterAnimationType:
        '''Hide After Animation type'''
        ...

    @classmethod
    @property
    def HIDE_ON_NEXT_MOUSE_CLICK(cls) -> AfterAnimationType:
        '''Hide on Next Mouse Click after animation type.'''
        ...

    ...

class AnimateTextType:
    '''Represents the animate text type of an animation effect.'''
    @classmethod
    @property
    def ALL_AT_ONCE(cls) -> AnimateTextType:
        '''Animate all text at once.'''
        ...

    @classmethod
    @property
    def BY_WORD(cls) -> AnimateTextType:
        '''Animate text by word.'''
        ...

    @classmethod
    @property
    def BY_LETTER(cls) -> AnimateTextType:
        '''Animate text by letter.'''
        ...

    ...

class BehaviorAccumulateType:
    '''Represents types of accumulation of effect behaviors.'''
    @classmethod
    @property
    def NOT_DEFINED(cls) -> BehaviorAccumulateType:
        ...

    @classmethod
    @property
    def ALWAYS(cls) -> BehaviorAccumulateType:
        ...

    @classmethod
    @property
    def NONE(cls) -> BehaviorAccumulateType:
        ...

    ...

class BehaviorAdditiveType:
    '''Represents additive type for effect behavior.'''
    @classmethod
    @property
    def NOT_DEFINED(cls) -> BehaviorAdditiveType:
        ...

    @classmethod
    @property
    def NONE(cls) -> BehaviorAdditiveType:
        ...

    @classmethod
    @property
    def BASE(cls) -> BehaviorAdditiveType:
        ...

    @classmethod
    @property
    def SUM(cls) -> BehaviorAdditiveType:
        ...

    @classmethod
    @property
    def REPLACE(cls) -> BehaviorAdditiveType:
        ...

    @classmethod
    @property
    def MULTIPLY(cls) -> BehaviorAdditiveType:
        ...

    ...

class BuildType:
    '''Determines how text will appear on a shape during animation.'''
    @classmethod
    @property
    def AS_ONE_OBJECT(cls) -> BuildType:
        '''With containing shape.'''
        ...

    @classmethod
    @property
    def ALL_PARAGRAPHS_AT_ONCE(cls) -> BuildType:
        '''All paragraph.'''
        ...

    @classmethod
    @property
    def BY_LEVEL_PARAGRAPHS1(cls) -> BuildType:
        '''By groups of paragraphs of depth 1.'''
        ...

    @classmethod
    @property
    def BY_LEVEL_PARAGRAPHS2(cls) -> BuildType:
        '''By groups of paragraphs of depth 2.'''
        ...

    @classmethod
    @property
    def BY_LEVEL_PARAGRAPHS3(cls) -> BuildType:
        '''By groups of paragraphs of depth 3.'''
        ...

    @classmethod
    @property
    def BY_LEVEL_PARAGRAPHS4(cls) -> BuildType:
        '''By groups of paragraphs of depth 4.'''
        ...

    @classmethod
    @property
    def BY_LEVEL_PARAGRAPHS5(cls) -> BuildType:
        '''By groups of paragraphs of depth 5.'''
        ...

    ...

class ColorDirection:
    '''Represents color direction for color effect behavior.'''
    @classmethod
    @property
    def NOT_DEFINED(cls) -> ColorDirection:
        ...

    @classmethod
    @property
    def CLOCKWISE(cls) -> ColorDirection:
        ...

    @classmethod
    @property
    def COUNTER_CLOCKWISE(cls) -> ColorDirection:
        ...

    ...

class ColorSpace:
    '''Represents color space for color effect behavior.'''
    @classmethod
    @property
    def NOT_DEFINED(cls) -> ColorSpace:
        ...

    @classmethod
    @property
    def RGB(cls) -> ColorSpace:
        ...

    @classmethod
    @property
    def HSL(cls) -> ColorSpace:
        ...

    ...

class CommandEffectType:
    '''Represents command effect type for command effect behavior.'''
    @classmethod
    @property
    def NOT_DEFINED(cls) -> CommandEffectType:
        ...

    @classmethod
    @property
    def EVENT(cls) -> CommandEffectType:
        ...

    @classmethod
    @property
    def CALL(cls) -> CommandEffectType:
        ...

    @classmethod
    @property
    def VERB(cls) -> CommandEffectType:
        ...

    ...

class EffectChartMajorGroupingType:
    '''Represents the type of an animation effect for chart's element.'''
    @classmethod
    @property
    def BY_SERIES(cls) -> EffectChartMajorGroupingType:
        '''Animate chart by series'''
        ...

    @classmethod
    @property
    def BY_CATEGORY(cls) -> EffectChartMajorGroupingType:
        '''Animate chart by category'''
        ...

    ...

class EffectChartMinorGroupingType:
    '''Represents the type of an animation effect for chart's element in series or category.'''
    @classmethod
    @property
    def BY_ELEMENT_IN_SERIES(cls) -> EffectChartMinorGroupingType:
        '''Animate chart by element in series'''
        ...

    @classmethod
    @property
    def BY_ELEMENT_IN_CATEGORY(cls) -> EffectChartMinorGroupingType:
        '''Animate chart by element in category'''
        ...

    ...

class EffectFillType:
    '''Represent fill types.'''
    @classmethod
    @property
    def NOT_DEFINED(cls) -> EffectFillType:
        ...

    @classmethod
    @property
    def REMOVE(cls) -> EffectFillType:
        ...

    @classmethod
    @property
    def FREEZE(cls) -> EffectFillType:
        ...

    @classmethod
    @property
    def HOLD(cls) -> EffectFillType:
        ...

    @classmethod
    @property
    def TRANSITION(cls) -> EffectFillType:
        ...

    ...

class EffectPresetClassType:
    '''Represent effect class types.'''
    @classmethod
    @property
    def ENTRANCE(cls) -> EffectPresetClassType:
        '''Entrance effects class.
        
        Target shape types: All'''
        ...

    @classmethod
    @property
    def EXIT(cls) -> EffectPresetClassType:
        '''Exit effects class.
        
        Target shape types: All'''
        ...

    @classmethod
    @property
    def EMPHASIS(cls) -> EffectPresetClassType:
        '''Emphasis effects class.
        
        Target shape types: All'''
        ...

    @classmethod
    @property
    def PATH(cls) -> EffectPresetClassType:
        '''Motion Paths class.
        
        Target shape types: All'''
        ...

    @classmethod
    @property
    def MEDIA_CALL(cls) -> EffectPresetClassType:
        '''Media effects class.
        
        Target shape types: :py:class:`aspose.slides.IVideoFrame`, :py:class:`aspose.slides.IAudioFrame`'''
        ...

    @classmethod
    @property
    def OLE_ACTION_VERBS(cls) -> EffectPresetClassType:
        '''OLE Action Verbs class.
        
        Target shape types: :py:class:`aspose.slides.IOleObjectFrame`'''
        ...

    ...

class EffectRestartType:
    '''Represent restart types for timing.'''
    @classmethod
    @property
    def NOT_DEFINED(cls) -> EffectRestartType:
        ...

    @classmethod
    @property
    def ALWAYS(cls) -> EffectRestartType:
        ...

    @classmethod
    @property
    def WHEN_NOT_ACTIVE(cls) -> EffectRestartType:
        ...

    @classmethod
    @property
    def NEVER(cls) -> EffectRestartType:
        ...

    ...

class EffectSubtype:
    '''Represents subtypes of animation effect.'''
    @classmethod
    @property
    def NONE(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def ACROSS(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def BOTTOM(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def BOTTOM_LEFT(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def BOTTOM_RIGHT(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def CENTER(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def CLOCKWISE(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def COUNTER_CLOCKWISE(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def GRADUAL_AND_CYCLE_CLOCKWISE(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def GRADUAL_AND_CYCLE_COUNTER_CLOCKWISE(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def DOWN(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def DOWN_LEFT(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def DOWN_RIGHT(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def FONT_ALL_CAPS(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def FONT_BOLD(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def FONT_ITALIC(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def FONT_SHADOW(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def FONT_STRIKETHROUGH(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def FONT_UNDERLINE(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def GRADUAL(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def HORIZONTAL(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def HORIZONTAL_IN(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def HORIZONTAL_OUT(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def IN(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def IN_BOTTOM(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def IN_CENTER(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def IN_SLIGHTLY(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def INSTANT(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def LEFT(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def ORDINAL_MASK(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def OUT(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def OUT_BOTTOM(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def OUT_CENTER(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def OUT_SLIGHTLY(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def RIGHT(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def SLIGHTLY(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def TOP(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def TOP_LEFT(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def TOP_RIGHT(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def UP(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def UP_LEFT(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def UP_RIGHT(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def VERTICAL(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def VERTICAL_IN(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def VERTICAL_OUT(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def WHEEL1(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def WHEEL2(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def WHEEL3(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def WHEEL4(cls) -> EffectSubtype:
        ...

    @classmethod
    @property
    def WHEEL8(cls) -> EffectSubtype:
        ...

    ...

class EffectTriggerType:
    '''Represent trigger type of effect.'''
    @classmethod
    @property
    def AFTER_PREVIOUS(cls) -> EffectTriggerType:
        ...

    @classmethod
    @property
    def ON_CLICK(cls) -> EffectTriggerType:
        ...

    @classmethod
    @property
    def WITH_PREVIOUS(cls) -> EffectTriggerType:
        ...

    ...

class EffectType:
    '''Represents the type of an animation effect.'''
    @classmethod
    @property
    def APPEAR(cls) -> EffectType:
        '''Appear effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def CURVE_UP_DOWN(cls) -> EffectType:
        '''CurveUpDown effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def ASCEND(cls) -> EffectType:
        '''Ascend effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def BLAST(cls) -> EffectType:
        '''Blast effect. Class **Emphasis**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def BLINDS(cls) -> EffectType:
        '''Blinds effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        * 
        
        *'''
        ...

    @classmethod
    @property
    def BLINK(cls) -> EffectType:
        '''Blink effect. Class **Emphasis**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def BOLD_FLASH(cls) -> EffectType:
        '''BoldFlash effect. Class **Emphasis**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def BOLD_REVEAL(cls) -> EffectType:
        '''BoldReveal effect. Class **Emphasis**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def BOOMERANG(cls) -> EffectType:
        '''Boomerang effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def BOUNCE(cls) -> EffectType:
        '''Bounce effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def BOX(cls) -> EffectType:
        '''Box effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        * 
        
        *'''
        ...

    @classmethod
    @property
    def BRUSH_ON_COLOR(cls) -> EffectType:
        '''BrushOnColor effect. Class **Emphasis**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def BRUSH_ON_UNDERLINE(cls) -> EffectType:
        '''BrushOnUnderline effect. Class **Emphasis**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def CENTER_REVOLVE(cls) -> EffectType:
        '''CenterRevolve effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def CHANGE_FILL_COLOR(cls) -> EffectType:
        '''ChangeFillColor effect. Class **Emphasis**.
        
        Valid subtypes:
        
        * 
        
        * 
        
        * 
        
        *'''
        ...

    @classmethod
    @property
    def CHANGE_FONT(cls) -> EffectType:
        '''ChangeFont effect. Class **Emphasis**.
        
        Valid subtypes:
        
        * 
        
        *'''
        ...

    @classmethod
    @property
    def CHANGE_FONT_COLOR(cls) -> EffectType:
        '''ChangeFontColor effect. Class **Emphasis**.
        
        Valid subtypes:
        
        * 
        
        * 
        
        * 
        
        *'''
        ...

    @classmethod
    @property
    def CHANGE_FONT_SIZE(cls) -> EffectType:
        '''ChangeFontSize effect. Class **Emphasis**.
        
        Valid subtypes:
        
        * 
        
        *'''
        ...

    @classmethod
    @property
    def CHANGE_FONT_STYLE(cls) -> EffectType:
        '''ChangeFontSize effect. Class **Emphasis**.
        
        Valid subtypes:
        
        * 
        
        * 
        
        *'''
        ...

    @classmethod
    @property
    def CHANGE_LINE_COLOR(cls) -> EffectType:
        '''ChangeLineColor effect. Class **Emphasis**.
        
        Valid subtypes:
        
        * 
        
        * 
        
        * 
        
        *'''
        ...

    @classmethod
    @property
    def CHECKERBOARD(cls) -> EffectType:
        '''Checkerboard effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        * 
        
        *'''
        ...

    @classmethod
    @property
    def CIRCLE(cls) -> EffectType:
        '''ColorBlend effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        * 
        
        *'''
        ...

    @classmethod
    @property
    def COLOR_BLEND(cls) -> EffectType:
        '''BrushOnUnderline effect. Class **Emphasis**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def COLOR_TYPEWRITER(cls) -> EffectType:
        '''Checkerboard effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def COLOR_WAVE(cls) -> EffectType:
        '''ColorWave effect. Class **Emphasis**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def COMPLEMENTARY_COLOR(cls) -> EffectType:
        '''ComplementaryColor effect. Class **Emphasis**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def COMPLEMENTARY_COLOR2(cls) -> EffectType:
        '''ComplementaryColor2 effect. Class **Emphasis**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def COMPRESS(cls) -> EffectType:
        '''Compress effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def CONTRASTING_COLOR(cls) -> EffectType:
        '''ContrastingColor effect. Class **Emphasis**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def CRAWL(cls) -> EffectType:
        '''Crawl effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        * 
        
        * 
        
        * 
        
        *'''
        ...

    @classmethod
    @property
    def CREDITS(cls) -> EffectType:
        '''Credits effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def CUSTOM(cls) -> EffectType:
        '''Custom effect.'''
        ...

    @classmethod
    @property
    def DARKEN(cls) -> EffectType:
        '''Darken effect. Class **Emphasis**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def DESATURATE(cls) -> EffectType:
        '''Desaturate effect. Class **Emphasis**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def DESCEND(cls) -> EffectType:
        '''Descend effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def DIAMOND(cls) -> EffectType:
        '''Diamond effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        * 
        
        *'''
        ...

    @classmethod
    @property
    def DISSOLVE(cls) -> EffectType:
        '''Dissolve effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def EASE_IN_OUT(cls) -> EffectType:
        '''Dissolve effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def EXPAND(cls) -> EffectType:
        '''Expand effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def FADE(cls) -> EffectType:
        '''Fade effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def FADED_SWIVEL(cls) -> EffectType:
        '''FadedSwivel effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def FADED_ZOOM(cls) -> EffectType:
        '''FadedZoom effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def FLASH_BULB(cls) -> EffectType:
        '''FlashBulb effect. Class **Emphasis**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def FLASH_ONCE(cls) -> EffectType:
        '''FlashOnce effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def FLICKER(cls) -> EffectType:
        '''Flicker effect. Class **Emphasis**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def FLIP(cls) -> EffectType:
        '''Flip effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def FLOAT(cls) -> EffectType:
        '''Float effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def FLY(cls) -> EffectType:
        '''Fly effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        * 
        
        * 
        
        * 
        
        * 
        
        * 
        
        * 
        
        * 
        
        *'''
        ...

    @classmethod
    @property
    def FOLD(cls) -> EffectType:
        '''Fold effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def GLIDE(cls) -> EffectType:
        '''Glide effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def GROW_AND_TURN(cls) -> EffectType:
        '''GrowAndTurn effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def GROW_SHRINK(cls) -> EffectType:
        '''GrowShrink effect. Class **Emphasis**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def GROW_WITH_COLOR(cls) -> EffectType:
        '''GrowWithColor effect. Class **Emphasis**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def LIGHTEN(cls) -> EffectType:
        '''Lighten effect. Class **Emphasis**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def LIGHT_SPEED(cls) -> EffectType:
        '''LightSpeed effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def MEDIA_PAUSE(cls) -> EffectType:
        '''MediaPause effect. Class **Media**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def MEDIA_PLAY(cls) -> EffectType:
        '''MediaPlay effect. Class **Media**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def MEDIA_STOP(cls) -> EffectType:
        '''MediaStop effect. Class **Media**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_4_POINT_STAR(cls) -> EffectType:
        '''Path4PointStar effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_5_POINT_STAR(cls) -> EffectType:
        '''Path5PointStar effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_6_POINT_STAR(cls) -> EffectType:
        '''Path6PointStar effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_8_POINT_STAR(cls) -> EffectType:
        '''Path8PointStar effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_ARC_DOWN(cls) -> EffectType:
        '''PathArcDown effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_ARC_LEFT(cls) -> EffectType:
        '''PathArcLeft effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_ARC_RIGHT(cls) -> EffectType:
        '''PathArcRight effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_ARC_UP(cls) -> EffectType:
        '''PathArcUp effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_BEAN(cls) -> EffectType:
        '''PathBean effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_BOUNCE_LEFT(cls) -> EffectType:
        '''PathBounceLeft effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_BOUNCE_RIGHT(cls) -> EffectType:
        '''PathBounceRight effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_BUZZSAW(cls) -> EffectType:
        '''PathBuzzsaw effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_CIRCLE(cls) -> EffectType:
        '''PathCircle effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_CRESCENT_MOON(cls) -> EffectType:
        '''PathCrescentMoon effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_CURVED_SQUARE(cls) -> EffectType:
        '''PathCurvedSquare effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_CURVED_X(cls) -> EffectType:
        '''PathCurvedX effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_CURVY_LEFT(cls) -> EffectType:
        '''PathCurvyLeft effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_CURVY_RIGHT(cls) -> EffectType:
        '''PathCurvyRight effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_CURVY_STAR(cls) -> EffectType:
        '''PathCurvyStar effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_DECAYING_WAVE(cls) -> EffectType:
        '''PathDecayingWave effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_DIAGONAL_DOWN_RIGHT(cls) -> EffectType:
        '''PathDiagonalDownRight effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_DIAGONAL_UP_RIGHT(cls) -> EffectType:
        '''PathDiagonalUpRight effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_DIAMOND(cls) -> EffectType:
        '''PathDiamond effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_DOWN(cls) -> EffectType:
        '''PathDown effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_EQUAL_TRIANGLE(cls) -> EffectType:
        '''PathEqualTriangle effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_FIGURE_8_FOUR(cls) -> EffectType:
        '''PathFigure8Four effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_FOOTBALL(cls) -> EffectType:
        '''PathFootball effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_FUNNEL(cls) -> EffectType:
        '''PathFunnel effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_HEART(cls) -> EffectType:
        '''PathHeart effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_HEARTBEAT(cls) -> EffectType:
        '''PathHeartbeat effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_HEXAGON(cls) -> EffectType:
        '''PathHexagon effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_HORIZONTAL_FIGURE8(cls) -> EffectType:
        '''PathHorizontalFigure8 effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_INVERTED_SQUARE(cls) -> EffectType:
        '''PathInvertedSquare effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_INVERTED_TRIANGLE(cls) -> EffectType:
        '''PathInvertedTriangle effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_LEFT(cls) -> EffectType:
        '''PathLeft effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_LOOPDE_LOOP(cls) -> EffectType:
        '''PathLoopdeLoop effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_NEUTRON(cls) -> EffectType:
        '''PathNeutron effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_OCTAGON(cls) -> EffectType:
        '''PathOctagon effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_PARALLELOGRAM(cls) -> EffectType:
        '''PathParallelogram effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_PEANUT(cls) -> EffectType:
        '''PathPeanut effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_PENTAGON(cls) -> EffectType:
        '''PathPentagon effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_PLUS(cls) -> EffectType:
        '''PathPlus effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_POINTY_STAR(cls) -> EffectType:
        '''PathPointyStar effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_RIGHT(cls) -> EffectType:
        '''PathRight effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_RIGHT_TRIANGLE(cls) -> EffectType:
        '''PathRightTriangle effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_S_CURVE1(cls) -> EffectType:
        '''PathSCurve1 effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_S_CURVE2(cls) -> EffectType:
        '''PathSCurve2 effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_SINE_WAVE(cls) -> EffectType:
        '''PathSineWave effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_SPIRAL_LEFT(cls) -> EffectType:
        '''PathSpiralLeft effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_SPIRAL_RIGHT(cls) -> EffectType:
        '''PathSpiralRight effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_SPRING(cls) -> EffectType:
        '''PathSpring effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_SQUARE(cls) -> EffectType:
        '''PathSquare effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_STAIRS_DOWN(cls) -> EffectType:
        '''PathStairsDown effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_SWOOSH(cls) -> EffectType:
        '''PathSwoosh effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_TEARDROP(cls) -> EffectType:
        '''PathTeardrop effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_TRAPEZOID(cls) -> EffectType:
        '''PathTrapezoid effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_TURN_DOWN(cls) -> EffectType:
        '''PathTurnDown effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_TURN_RIGHT(cls) -> EffectType:
        '''PathTurnRight effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_TURN_UP(cls) -> EffectType:
        '''PathTurnUp effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_TURN_UP_RIGHT(cls) -> EffectType:
        '''PathTurnUpRight effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_UP(cls) -> EffectType:
        '''PathUp effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_USER(cls) -> EffectType:
        '''PathUser effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_VERTICAL_FIGURE8(cls) -> EffectType:
        '''PathVerticalFigure8 effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_WAVE(cls) -> EffectType:
        '''PathWave effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PATH_ZIGZAG(cls) -> EffectType:
        '''PathZigzag effect. Class **Path**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PEEK(cls) -> EffectType:
        '''Peek effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PINWHEEL(cls) -> EffectType:
        '''Pinwheel effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def PLUS(cls) -> EffectType:
        '''Plus effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        * 
        
        *'''
        ...

    @classmethod
    @property
    def RANDOM_BARS(cls) -> EffectType:
        '''RandomBars effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        * 
        
        *'''
        ...

    @classmethod
    @property
    def RANDOM_EFFECTS(cls) -> EffectType:
        '''RandomEffects effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def RISE_UP(cls) -> EffectType:
        '''RandomEffects effect. Class **Entrance**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def SHIMMER(cls) -> EffectType:
        '''Shimmer effect. Class **Emphasis**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def SLING(cls) -> EffectType:
        '''RandomEffects effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def SPIN(cls) -> EffectType:
        '''Spin effect. Class **Emphasis**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def SPINNER(cls) -> EffectType:
        '''Spinner effect. Class **Emphasis**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def SPIRAL(cls) -> EffectType:
        '''Spiral effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def SPLIT(cls) -> EffectType:
        '''Split effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        * 
        
        * 
        
        * 
        
        *'''
        ...

    @classmethod
    @property
    def STRETCH(cls) -> EffectType:
        '''Stretch effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        * 
        
        * 
        
        * 
        
        * 
        
        *'''
        ...

    @classmethod
    @property
    def STRIPS(cls) -> EffectType:
        '''Stretch effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        * 
        
        * 
        
        * 
        
        *'''
        ...

    @classmethod
    @property
    def STYLE_EMPHASIS(cls) -> EffectType:
        '''StyleEmphasis effect. Class **Emphasis**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def SWISH(cls) -> EffectType:
        '''Swish effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def SWIVEL(cls) -> EffectType:
        '''Swivel effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        * 
        
        *'''
        ...

    @classmethod
    @property
    def TEETER(cls) -> EffectType:
        '''Teeter effect. Class **Emphasis**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def THREAD(cls) -> EffectType:
        '''Thread effect. Class **Emphasis**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def TRANSPARENCY(cls) -> EffectType:
        '''Transparency effect. Class **Emphasis**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def UNFOLD(cls) -> EffectType:
        '''Unfold effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def VERTICAL_GROW(cls) -> EffectType:
        '''VerticalGrow effect. Class **Emphasis**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def WAVE(cls) -> EffectType:
        '''Wave effect. Class **Emphasis**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def WEDGE(cls) -> EffectType:
        '''Wedge effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def WHEEL(cls) -> EffectType:
        '''Wedge effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        * 
        
        * 
        
        * 
        
        * 
        
        *'''
        ...

    @classmethod
    @property
    def WHIP(cls) -> EffectType:
        '''Whip effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def WIPE(cls) -> EffectType:
        '''Wedge effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        * 
        
        * 
        
        * 
        
        *'''
        ...

    @classmethod
    @property
    def MAGNIFY(cls) -> EffectType:
        '''Magnify effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def ZOOM(cls) -> EffectType:
        '''Zoom effect. Class **Entrance** or **Exit**.
        
        Valid subtypes:
        
        * 
        
        * 
        
        * 
        
        * 
        
        * 
        
        * 
        
        * 
        
        *'''
        ...

    @classmethod
    @property
    def OLE_OBJECT_SHOW(cls) -> EffectType:
        '''OLEObjectShow effect. Class **OLEActionVerbs**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def OLE_OBJECT_EDIT(cls) -> EffectType:
        '''OLEObjectEdit effect. Class **OLEActionVerbs**.
        
        Valid subtypes:
        
        *'''
        ...

    @classmethod
    @property
    def OLE_OBJECT_OPEN(cls) -> EffectType:
        '''OLEObjectOpen effect. Class **OLEActionVerbs**.
        
        Valid subtypes:
        
        *'''
        ...

    ...

class FilterEffectRevealType:
    '''Represents filter reveal type.'''
    @classmethod
    @property
    def NOT_DEFINED(cls) -> FilterEffectRevealType:
        ...

    @classmethod
    @property
    def NONE(cls) -> FilterEffectRevealType:
        ...

    @classmethod
    @property
    def IN(cls) -> FilterEffectRevealType:
        ...

    @classmethod
    @property
    def OUT(cls) -> FilterEffectRevealType:
        ...

    ...

class FilterEffectSubtype:
    '''Represents filter effect subtypes.'''
    @classmethod
    @property
    def NONE(cls) -> FilterEffectSubtype:
        ...

    @classmethod
    @property
    def ACROSS(cls) -> FilterEffectSubtype:
        ...

    @classmethod
    @property
    def DOWN(cls) -> FilterEffectSubtype:
        ...

    @classmethod
    @property
    def DOWN_LEFT(cls) -> FilterEffectSubtype:
        ...

    @classmethod
    @property
    def DOWN_RIGHT(cls) -> FilterEffectSubtype:
        ...

    @classmethod
    @property
    def FROM_BOTTOM(cls) -> FilterEffectSubtype:
        ...

    @classmethod
    @property
    def FROM_LEFT(cls) -> FilterEffectSubtype:
        ...

    @classmethod
    @property
    def FROM_RIGHT(cls) -> FilterEffectSubtype:
        ...

    @classmethod
    @property
    def FROM_TOP(cls) -> FilterEffectSubtype:
        ...

    @classmethod
    @property
    def HORIZONTAL(cls) -> FilterEffectSubtype:
        ...

    @classmethod
    @property
    def IN(cls) -> FilterEffectSubtype:
        ...

    @classmethod
    @property
    def IN_HORIZONTAL(cls) -> FilterEffectSubtype:
        ...

    @classmethod
    @property
    def IN_VERTICAL(cls) -> FilterEffectSubtype:
        ...

    @classmethod
    @property
    def LEFT(cls) -> FilterEffectSubtype:
        ...

    @classmethod
    @property
    def OUT(cls) -> FilterEffectSubtype:
        ...

    @classmethod
    @property
    def OUT_HORIZONTAL(cls) -> FilterEffectSubtype:
        ...

    @classmethod
    @property
    def OUT_VERTICAL(cls) -> FilterEffectSubtype:
        ...

    @classmethod
    @property
    def RIGHT(cls) -> FilterEffectSubtype:
        ...

    @classmethod
    @property
    def SPOKES1(cls) -> FilterEffectSubtype:
        ...

    @classmethod
    @property
    def SPOKES2(cls) -> FilterEffectSubtype:
        ...

    @classmethod
    @property
    def SPOKES3(cls) -> FilterEffectSubtype:
        ...

    @classmethod
    @property
    def SPOKES4(cls) -> FilterEffectSubtype:
        ...

    @classmethod
    @property
    def SPOKES8(cls) -> FilterEffectSubtype:
        ...

    @classmethod
    @property
    def UP(cls) -> FilterEffectSubtype:
        ...

    @classmethod
    @property
    def UP_LEFT(cls) -> FilterEffectSubtype:
        ...

    @classmethod
    @property
    def UP_RIGHT(cls) -> FilterEffectSubtype:
        ...

    @classmethod
    @property
    def VERTICAL(cls) -> FilterEffectSubtype:
        ...

    ...

class FilterEffectType:
    '''Represents filter effect types.'''
    @classmethod
    @property
    def NONE(cls) -> FilterEffectType:
        ...

    @classmethod
    @property
    def BARN(cls) -> FilterEffectType:
        ...

    @classmethod
    @property
    def BLINDS(cls) -> FilterEffectType:
        ...

    @classmethod
    @property
    def BOX(cls) -> FilterEffectType:
        ...

    @classmethod
    @property
    def CHECKERBOARD(cls) -> FilterEffectType:
        ...

    @classmethod
    @property
    def CIRCLE(cls) -> FilterEffectType:
        ...

    @classmethod
    @property
    def DIAMOND(cls) -> FilterEffectType:
        ...

    @classmethod
    @property
    def DISSOLVE(cls) -> FilterEffectType:
        ...

    @classmethod
    @property
    def FADE(cls) -> FilterEffectType:
        ...

    @classmethod
    @property
    def IMAGE(cls) -> FilterEffectType:
        ...

    @classmethod
    @property
    def PIXELATE(cls) -> FilterEffectType:
        ...

    @classmethod
    @property
    def PLUS(cls) -> FilterEffectType:
        ...

    @classmethod
    @property
    def RANDOM_BAR(cls) -> FilterEffectType:
        ...

    @classmethod
    @property
    def SLIDE(cls) -> FilterEffectType:
        ...

    @classmethod
    @property
    def STRETCH(cls) -> FilterEffectType:
        ...

    @classmethod
    @property
    def STRIPS(cls) -> FilterEffectType:
        ...

    @classmethod
    @property
    def WEDGE(cls) -> FilterEffectType:
        ...

    @classmethod
    @property
    def WHEEL(cls) -> FilterEffectType:
        ...

    @classmethod
    @property
    def WIPE(cls) -> FilterEffectType:
        ...

    ...

class MotionCommandPathType:
    '''Represent types of command for animation motion effect behavior.'''
    @classmethod
    @property
    def MOVE_TO(cls) -> MotionCommandPathType:
        ...

    @classmethod
    @property
    def LINE_TO(cls) -> MotionCommandPathType:
        ...

    @classmethod
    @property
    def CURVE_TO(cls) -> MotionCommandPathType:
        ...

    @classmethod
    @property
    def CLOSE_LOOP(cls) -> MotionCommandPathType:
        ...

    @classmethod
    @property
    def END(cls) -> MotionCommandPathType:
        ...

    ...

class MotionOriginType:
    '''Specifies what the origin of the motion path is relative to.
                Such as the layout of the slide, or the parent.'''
    @classmethod
    @property
    def NOT_DEFINED(cls) -> MotionOriginType:
        ...

    @classmethod
    @property
    def PARENT(cls) -> MotionOriginType:
        ...

    @classmethod
    @property
    def LAYOUT(cls) -> MotionOriginType:
        ...

    ...

class MotionPathEditMode:
    '''Specifies how the motion path moves when the target shape is moved'''
    @classmethod
    @property
    def NOT_DEFINED(cls) -> MotionPathEditMode:
        ...

    @classmethod
    @property
    def RELATIVE(cls) -> MotionPathEditMode:
        ...

    @classmethod
    @property
    def FIXED(cls) -> MotionPathEditMode:
        ...

    ...

class MotionPathPointsType:
    '''Represent types of points in animation motion path.'''
    @classmethod
    @property
    def NONE(cls) -> MotionPathPointsType:
        ...

    @classmethod
    @property
    def AUTO(cls) -> MotionPathPointsType:
        ...

    @classmethod
    @property
    def CORNER(cls) -> MotionPathPointsType:
        ...

    @classmethod
    @property
    def STRAIGHT(cls) -> MotionPathPointsType:
        ...

    @classmethod
    @property
    def SMOOTH(cls) -> MotionPathPointsType:
        ...

    @classmethod
    @property
    def CURVE_AUTO(cls) -> MotionPathPointsType:
        ...

    @classmethod
    @property
    def CURVE_CORNER(cls) -> MotionPathPointsType:
        ...

    @classmethod
    @property
    def CURVE_STRAIGHT(cls) -> MotionPathPointsType:
        ...

    @classmethod
    @property
    def CURVE_SMOOTH(cls) -> MotionPathPointsType:
        ...

    ...

class PropertyCalcModeType:
    '''Represent calc mode for animation property.'''
    @classmethod
    @property
    def NOT_DEFINED(cls) -> PropertyCalcModeType:
        ...

    @classmethod
    @property
    def DISCRETE(cls) -> PropertyCalcModeType:
        ...

    @classmethod
    @property
    def LINEAR(cls) -> PropertyCalcModeType:
        ...

    @classmethod
    @property
    def FORMULA(cls) -> PropertyCalcModeType:
        ...

    ...

class PropertyValueType:
    '''Represent property value types.'''
    @classmethod
    @property
    def NOT_DEFINED(cls) -> PropertyValueType:
        ...

    @classmethod
    @property
    def STRING(cls) -> PropertyValueType:
        ...

    @classmethod
    @property
    def NUMBER(cls) -> PropertyValueType:
        ...

    @classmethod
    @property
    def COLOR(cls) -> PropertyValueType:
        ...

    ...

