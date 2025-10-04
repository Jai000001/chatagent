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

class CornerDirectionTransition(TransitionValueBase):
    '''Corner direction slide transition effect.'''
    @property
    def direction(self) -> TransitionCornerDirectionType:
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionCornerDirectionType`.'''
        ...

    @direction.setter
    def direction(self, value: TransitionCornerDirectionType):
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionCornerDirectionType`.'''
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class EightDirectionTransition(TransitionValueBase):
    '''Eight direction slide transition effect.'''
    @property
    def direction(self) -> TransitionEightDirectionType:
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionEightDirectionType`.'''
        ...

    @direction.setter
    def direction(self, value: TransitionEightDirectionType):
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionEightDirectionType`.'''
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class EmptyTransition(TransitionValueBase):
    '''Empty slide transition effect.'''
    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class FlyThroughTransition(TransitionValueBase):
    '''Fly-through slide transition effect.'''
    @property
    def direction(self) -> TransitionInOutDirectionType:
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionInOutDirectionType`.'''
        ...

    @direction.setter
    def direction(self, value: TransitionInOutDirectionType):
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionInOutDirectionType`.'''
        ...

    @property
    def has_bounce(self) -> bool:
        ...

    @has_bounce.setter
    def has_bounce(self, value: bool):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class GlitterTransition(TransitionValueBase):
    '''Glitter slide transition effect.'''
    @property
    def direction(self) -> TransitionSideDirectionType:
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionSideDirectionType`.'''
        ...

    @direction.setter
    def direction(self, value: TransitionSideDirectionType):
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionSideDirectionType`.'''
        ...

    @property
    def pattern(self) -> TransitionPattern:
        '''Specifies the shape of the visuals used during the transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionPattern`.'''
        ...

    @pattern.setter
    def pattern(self, value: TransitionPattern):
        '''Specifies the shape of the visuals used during the transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionPattern`.'''
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class ICornerDirectionTransition:
    '''Corner direction slide transition effect.'''
    @property
    def direction(self) -> TransitionCornerDirectionType:
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionCornerDirectionType`.'''
        ...

    @direction.setter
    def direction(self, value: TransitionCornerDirectionType):
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionCornerDirectionType`.'''
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class IEightDirectionTransition:
    '''Eight direction slide transition effect.'''
    @property
    def direction(self) -> TransitionEightDirectionType:
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionEightDirectionType`.'''
        ...

    @direction.setter
    def direction(self, value: TransitionEightDirectionType):
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionEightDirectionType`.'''
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class IEmptyTransition:
    '''Empty slide transition effect.'''
    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class IFlyThroughTransition:
    '''Fly-through slide transition effect.'''
    @property
    def direction(self) -> TransitionInOutDirectionType:
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionInOutDirectionType`.'''
        ...

    @direction.setter
    def direction(self, value: TransitionInOutDirectionType):
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionInOutDirectionType`.'''
        ...

    @property
    def has_bounce(self) -> bool:
        ...

    @has_bounce.setter
    def has_bounce(self, value: bool):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class IGlitterTransition:
    '''Glitter slide transition effect.'''
    @property
    def direction(self) -> TransitionSideDirectionType:
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionSideDirectionType`.'''
        ...

    @direction.setter
    def direction(self, value: TransitionSideDirectionType):
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionSideDirectionType`.'''
        ...

    @property
    def pattern(self) -> TransitionPattern:
        '''Specifies the shape of the visuals used during the transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionPattern`.'''
        ...

    @pattern.setter
    def pattern(self, value: TransitionPattern):
        '''Specifies the shape of the visuals used during the transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionPattern`.'''
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class IInOutTransition:
    '''In-Out slide transition effect.'''
    @property
    def direction(self) -> TransitionInOutDirectionType:
        '''Direction of a transition effect.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionInOutDirectionType`.'''
        ...

    @direction.setter
    def direction(self, value: TransitionInOutDirectionType):
        '''Direction of a transition effect.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionInOutDirectionType`.'''
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class ILeftRightDirectionTransition:
    '''Left-right direction slide transition effect.'''
    @property
    def direction(self) -> TransitionLeftRightDirectionType:
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionLeftRightDirectionType`.'''
        ...

    @direction.setter
    def direction(self, value: TransitionLeftRightDirectionType):
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionLeftRightDirectionType`.'''
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class IMorphTransition:
    '''Ripple slide transition effect.'''
    @property
    def morph_type(self) -> TransitionMorphType:
        ...

    @morph_type.setter
    def morph_type(self, value: TransitionMorphType):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class IOptionalBlackTransition:
    '''Optional black slide transition effect.'''
    @property
    def from_black(self) -> bool:
        ...

    @from_black.setter
    def from_black(self, value: bool):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class IOrientationTransition:
    '''Orientation slide transition effect.'''
    @property
    def direction(self) -> Orientation:
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.Orientation`.'''
        ...

    @direction.setter
    def direction(self, value: Orientation):
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.Orientation`.'''
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class IRevealTransition:
    '''Reveal slide transition effect.'''
    @property
    def direction(self) -> TransitionLeftRightDirectionType:
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionLeftRightDirectionType`.'''
        ...

    @direction.setter
    def direction(self, value: TransitionLeftRightDirectionType):
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionLeftRightDirectionType`.'''
        ...

    @property
    def through_black(self) -> bool:
        ...

    @through_black.setter
    def through_black(self, value: bool):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class IRippleTransition:
    '''Ripple slide transition effect.'''
    @property
    def direction(self) -> TransitionCornerAndCenterDirectionType:
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionCornerAndCenterDirectionType`.'''
        ...

    @direction.setter
    def direction(self, value: TransitionCornerAndCenterDirectionType):
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionCornerAndCenterDirectionType`.'''
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class IShredTransition:
    '''Shred slide transition effect.'''
    @property
    def direction(self) -> TransitionInOutDirectionType:
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionInOutDirectionType`.'''
        ...

    @direction.setter
    def direction(self, value: TransitionInOutDirectionType):
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionInOutDirectionType`.'''
        ...

    @property
    def pattern(self) -> TransitionShredPattern:
        '''Specifies the shape of the visuals used during the transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionShredPattern`.'''
        ...

    @pattern.setter
    def pattern(self, value: TransitionShredPattern):
        '''Specifies the shape of the visuals used during the transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionShredPattern`.'''
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class ISideDirectionTransition:
    '''Side direction slide transition effect.'''
    @property
    def direction(self) -> TransitionSideDirectionType:
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionSideDirectionType`.'''
        ...

    @direction.setter
    def direction(self, value: TransitionSideDirectionType):
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionSideDirectionType`.'''
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class ISplitTransition:
    '''Split slide transition effect.'''
    @property
    def direction(self) -> TransitionInOutDirectionType:
        '''Direction of transition split.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionInOutDirectionType`.'''
        ...

    @direction.setter
    def direction(self, value: TransitionInOutDirectionType):
        '''Direction of transition split.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionInOutDirectionType`.'''
        ...

    @property
    def orientation(self) -> Orientation:
        '''Orientation of transition split.
                    Read/write :py:enum:`aspose.slides.Orientation`.'''
        ...

    @orientation.setter
    def orientation(self, value: Orientation):
        '''Orientation of transition split.
                    Read/write :py:enum:`aspose.slides.Orientation`.'''
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class ITransitionValueBase:
    '''Represents base class for slide transition effects.'''
    ...

class IWheelTransition:
    '''Wheel slide transition effect.'''
    @property
    def spokes(self) -> int:
        '''Number spokes of wheel transition.
                    Read/write :py:class:`int`.'''
        ...

    @spokes.setter
    def spokes(self, value: int):
        '''Number spokes of wheel transition.
                    Read/write :py:class:`int`.'''
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class InOutTransition(TransitionValueBase):
    '''In-Out slide transition effect.'''
    @property
    def direction(self) -> TransitionInOutDirectionType:
        '''Direction of a transition effect.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionInOutDirectionType`.'''
        ...

    @direction.setter
    def direction(self, value: TransitionInOutDirectionType):
        '''Direction of a transition effect.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionInOutDirectionType`.'''
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class LeftRightDirectionTransition(TransitionValueBase):
    '''Left-right direction slide transition effect.'''
    @property
    def direction(self) -> TransitionLeftRightDirectionType:
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionLeftRightDirectionType`.'''
        ...

    @direction.setter
    def direction(self, value: TransitionLeftRightDirectionType):
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionLeftRightDirectionType`.'''
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class MorphTransition(TransitionValueBase):
    '''Ripple slide transition effect.'''
    @property
    def morph_type(self) -> TransitionMorphType:
        ...

    @morph_type.setter
    def morph_type(self, value: TransitionMorphType):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class OptionalBlackTransition(TransitionValueBase):
    '''Optional black slide transition effect.'''
    @property
    def from_black(self) -> bool:
        ...

    @from_black.setter
    def from_black(self, value: bool):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class OrientationTransition(TransitionValueBase):
    '''Orientation slide transition effect.'''
    @property
    def direction(self) -> Orientation:
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.Orientation`.'''
        ...

    @direction.setter
    def direction(self, value: Orientation):
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.Orientation`.'''
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class RevealTransition(TransitionValueBase):
    '''Reveal slide transition effect.'''
    @property
    def direction(self) -> TransitionLeftRightDirectionType:
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionLeftRightDirectionType`.'''
        ...

    @direction.setter
    def direction(self, value: TransitionLeftRightDirectionType):
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionLeftRightDirectionType`.'''
        ...

    @property
    def through_black(self) -> bool:
        ...

    @through_black.setter
    def through_black(self, value: bool):
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class RippleTransition(TransitionValueBase):
    '''Ripple slide transition effect.'''
    @property
    def direction(self) -> TransitionCornerAndCenterDirectionType:
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionCornerAndCenterDirectionType`.'''
        ...

    @direction.setter
    def direction(self, value: TransitionCornerAndCenterDirectionType):
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionCornerAndCenterDirectionType`.'''
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class ShredTransition(TransitionValueBase):
    '''Shred slide transition effect.'''
    @property
    def direction(self) -> TransitionInOutDirectionType:
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionInOutDirectionType`.'''
        ...

    @direction.setter
    def direction(self, value: TransitionInOutDirectionType):
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionInOutDirectionType`.'''
        ...

    @property
    def pattern(self) -> TransitionShredPattern:
        '''Specifies the shape of the visuals used during the transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionShredPattern`.'''
        ...

    @pattern.setter
    def pattern(self, value: TransitionShredPattern):
        '''Specifies the shape of the visuals used during the transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionShredPattern`.'''
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class SideDirectionTransition(TransitionValueBase):
    '''Side direction slide transition effect.'''
    @property
    def direction(self) -> TransitionSideDirectionType:
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionSideDirectionType`.'''
        ...

    @direction.setter
    def direction(self, value: TransitionSideDirectionType):
        '''Direction of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionSideDirectionType`.'''
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class SlideShowTransition:
    '''Represents slide show transition.'''
    @property
    def sound(self) -> IAudio:
        '''Returns or sets the embedded audio data.
                    Read/write :py:class:`aspose.slides.IAudio`.'''
        ...

    @sound.setter
    def sound(self, value: IAudio):
        '''Returns or sets the embedded audio data.
                    Read/write :py:class:`aspose.slides.IAudio`.'''
        ...

    @property
    def sound_mode(self) -> TransitionSoundMode:
        ...

    @sound_mode.setter
    def sound_mode(self, value: TransitionSoundMode):
        ...

    @property
    def sound_loop(self) -> bool:
        ...

    @sound_loop.setter
    def sound_loop(self, value: bool):
        ...

    @property
    def advance_on_click(self) -> bool:
        ...

    @advance_on_click.setter
    def advance_on_click(self, value: bool):
        ...

    @property
    def advance_after(self) -> bool:
        ...

    @advance_after.setter
    def advance_after(self, value: bool):
        ...

    @property
    def advance_after_time(self) -> int:
        ...

    @advance_after_time.setter
    def advance_after_time(self, value: int):
        ...

    @property
    def speed(self) -> TransitionSpeed:
        '''Specifies the transition speed that is to be used when transitioning from the current slide
                    to the next.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionSpeed`.'''
        ...

    @speed.setter
    def speed(self, value: TransitionSpeed):
        '''Specifies the transition speed that is to be used when transitioning from the current slide
                    to the next.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionSpeed`.'''
        ...

    @property
    def value(self) -> ITransitionValueBase:
        '''Slide show transition value.
                    Read-only :py:class:`aspose.slides.slideshow.ITransitionValueBase`.'''
        ...

    @property
    def type(self) -> TransitionType:
        '''Type of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionType`.'''
        ...

    @type.setter
    def type(self, value: TransitionType):
        '''Type of transition.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionType`.'''
        ...

    @property
    def sound_is_built_in(self) -> bool:
        ...

    @sound_is_built_in.setter
    def sound_is_built_in(self, value: bool):
        ...

    @property
    def sound_name(self) -> str:
        ...

    @sound_name.setter
    def sound_name(self, value: str):
        ...

    ...

class SplitTransition(TransitionValueBase):
    '''Split slide transition effect.'''
    @property
    def direction(self) -> TransitionInOutDirectionType:
        '''Direction of transition split.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionInOutDirectionType`.'''
        ...

    @direction.setter
    def direction(self, value: TransitionInOutDirectionType):
        '''Direction of transition split.
                    Read/write :py:enum:`aspose.slides.slideshow.TransitionInOutDirectionType`.'''
        ...

    @property
    def orientation(self) -> Orientation:
        '''Orientation of transition split.
                    Read/write :py:enum:`aspose.slides.Orientation`.'''
        ...

    @orientation.setter
    def orientation(self, value: Orientation):
        '''Orientation of transition split.
                    Read/write :py:enum:`aspose.slides.Orientation`.'''
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class TransitionValueBase:
    '''Base class for slide transition effects.'''
    ...

class WheelTransition(TransitionValueBase):
    '''Wheel slide transition effect.'''
    @property
    def spokes(self) -> int:
        '''Number spokes of wheel transition.
                    Read/write :py:class:`int`.'''
        ...

    @spokes.setter
    def spokes(self, value: int):
        '''Number spokes of wheel transition.
                    Read/write :py:class:`int`.'''
        ...

    @property
    def as_i_transition_value_base(self) -> ITransitionValueBase:
        ...

    ...

class TransitionCornerAndCenterDirectionType:
    '''Specifies a direction restricted to the corners and center.'''
    @classmethod
    @property
    def LEFT_DOWN(cls) -> TransitionCornerAndCenterDirectionType:
        ...

    @classmethod
    @property
    def LEFT_UP(cls) -> TransitionCornerAndCenterDirectionType:
        ...

    @classmethod
    @property
    def RIGHT_DOWN(cls) -> TransitionCornerAndCenterDirectionType:
        ...

    @classmethod
    @property
    def RIGHT_UP(cls) -> TransitionCornerAndCenterDirectionType:
        ...

    @classmethod
    @property
    def CENTER(cls) -> TransitionCornerAndCenterDirectionType:
        ...

    ...

class TransitionCornerDirectionType:
    '''Represent corner direction transition types.'''
    @classmethod
    @property
    def LEFT_DOWN(cls) -> TransitionCornerDirectionType:
        ...

    @classmethod
    @property
    def LEFT_UP(cls) -> TransitionCornerDirectionType:
        ...

    @classmethod
    @property
    def RIGHT_DOWN(cls) -> TransitionCornerDirectionType:
        ...

    @classmethod
    @property
    def RIGHT_UP(cls) -> TransitionCornerDirectionType:
        ...

    ...

class TransitionEightDirectionType:
    '''Represent eight direction transition types.'''
    @classmethod
    @property
    def LEFT_DOWN(cls) -> TransitionEightDirectionType:
        ...

    @classmethod
    @property
    def LEFT_UP(cls) -> TransitionEightDirectionType:
        ...

    @classmethod
    @property
    def RIGHT_DOWN(cls) -> TransitionEightDirectionType:
        ...

    @classmethod
    @property
    def RIGHT_UP(cls) -> TransitionEightDirectionType:
        ...

    @classmethod
    @property
    def LEFT(cls) -> TransitionEightDirectionType:
        ...

    @classmethod
    @property
    def UP(cls) -> TransitionEightDirectionType:
        ...

    @classmethod
    @property
    def DOWN(cls) -> TransitionEightDirectionType:
        ...

    @classmethod
    @property
    def RIGHT(cls) -> TransitionEightDirectionType:
        ...

    ...

class TransitionInOutDirectionType:
    '''Represent in or out direction transition types.'''
    @classmethod
    @property
    def IN(cls) -> TransitionInOutDirectionType:
        ...

    @classmethod
    @property
    def OUT(cls) -> TransitionInOutDirectionType:
        ...

    ...

class TransitionLeftRightDirectionType:
    '''Specifies a direction restricted to the values of left and right.'''
    @classmethod
    @property
    def LEFT(cls) -> TransitionLeftRightDirectionType:
        ...

    @classmethod
    @property
    def RIGHT(cls) -> TransitionLeftRightDirectionType:
        ...

    ...

class TransitionMorphType:
    '''Represent a type of morph transition.'''
    @classmethod
    @property
    def BY_OBJECT(cls) -> TransitionMorphType:
        '''Morph transition will be performed considering shapes as indivisible objects.'''
        ...

    @classmethod
    @property
    def BY_WORD(cls) -> TransitionMorphType:
        '''Morph transition will be performed with transferring text by words where possible.'''
        ...

    @classmethod
    @property
    def BY_CHAR(cls) -> TransitionMorphType:
        '''Morph transition will be performed with transferring text by characters where possible.'''
        ...

    ...

class TransitionPattern:
    '''Specifies a geometric pattern that tiles together to fill a larger area.'''
    @classmethod
    @property
    def DIAMOND(cls) -> TransitionPattern:
        '''Diamond tile pattern'''
        ...

    @classmethod
    @property
    def HEXAGON(cls) -> TransitionPattern:
        '''Hexagon tile pattern'''
        ...

    ...

class TransitionShredPattern:
    '''Specifies a geometric shape that tiles together to fill a larger area.'''
    @classmethod
    @property
    def STRIP(cls) -> TransitionShredPattern:
        '''Vertical strips'''
        ...

    @classmethod
    @property
    def RECTANGLE(cls) -> TransitionShredPattern:
        '''Small rectangles'''
        ...

    ...

class TransitionSideDirectionType:
    '''Represent side direction transition types.'''
    @classmethod
    @property
    def LEFT(cls) -> TransitionSideDirectionType:
        ...

    @classmethod
    @property
    def UP(cls) -> TransitionSideDirectionType:
        ...

    @classmethod
    @property
    def DOWN(cls) -> TransitionSideDirectionType:
        ...

    @classmethod
    @property
    def RIGHT(cls) -> TransitionSideDirectionType:
        ...

    ...

class TransitionSoundMode:
    '''Represent sound mode of transition.'''
    @classmethod
    @property
    def NOT_DEFINED(cls) -> TransitionSoundMode:
        ...

    @classmethod
    @property
    def START_SOUND(cls) -> TransitionSoundMode:
        ...

    @classmethod
    @property
    def STOP_PREVOIUS_SOUND(cls) -> TransitionSoundMode:
        ...

    ...

class TransitionSpeed:
    '''Represent transition speed types.'''
    @classmethod
    @property
    def FAST(cls) -> TransitionSpeed:
        ...

    @classmethod
    @property
    def MEDIUM(cls) -> TransitionSpeed:
        ...

    @classmethod
    @property
    def SLOW(cls) -> TransitionSpeed:
        ...

    ...

class TransitionType:
    '''Represent slide show transition type.'''
    @classmethod
    @property
    def NONE(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def BLINDS(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def CHECKER(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def CIRCLE(cls) -> TransitionType:
        '''Relates to transition Shape (with option Circle) in PowerPoint 2010.'''
        ...

    @classmethod
    @property
    def COMB(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def COVER(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def CUT(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def DIAMOND(cls) -> TransitionType:
        '''Relates to transition Shape (with option Diamond) in PowerPoint 2010.'''
        ...

    @classmethod
    @property
    def DISSOLVE(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def FADE(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def NEWSFLASH(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def PLUS(cls) -> TransitionType:
        '''Relates to transition Shape (with option Plus) in PowerPoint 2010.'''
        ...

    @classmethod
    @property
    def PULL(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def PUSH(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def RANDOM(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def RANDOM_BAR(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def SPLIT(cls) -> TransitionType:
        '''Equivalent to transition Wipe in PowerPoint 2010.'''
        ...

    @classmethod
    @property
    def STRIPS(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def WEDGE(cls) -> TransitionType:
        '''Relates to transition Clock (with option Wedge) in PowerPoint 2010.'''
        ...

    @classmethod
    @property
    def WHEEL(cls) -> TransitionType:
        '''Relates to transition Clock (with option Clockwise) in PowerPoint 2010.'''
        ...

    @classmethod
    @property
    def WIPE(cls) -> TransitionType:
        ...

    @classmethod
    @property
    def ZOOM(cls) -> TransitionType:
        '''Relates to transition Shape (with options In/Out) in PowerPoint 2010.
                    See also :py:attr:`aspose.slides.slideshow.TransitionType.WARP` that relates to transition Zoom in PowerPoint 2010.'''
        ...

    @classmethod
    @property
    def VORTEX(cls) -> TransitionType:
        '''Available in PowerPoint 2010.'''
        ...

    @classmethod
    @property
    def SWITCH(cls) -> TransitionType:
        '''Available in PowerPoint 2010.'''
        ...

    @classmethod
    @property
    def FLIP(cls) -> TransitionType:
        '''Available in PowerPoint 2010.'''
        ...

    @classmethod
    @property
    def RIPPLE(cls) -> TransitionType:
        '''Available in PowerPoint 2010.'''
        ...

    @classmethod
    @property
    def HONEYCOMB(cls) -> TransitionType:
        '''Available in PowerPoint 2010.'''
        ...

    @classmethod
    @property
    def CUBE(cls) -> TransitionType:
        '''Available in PowerPoint 2010.'''
        ...

    @classmethod
    @property
    def BOX(cls) -> TransitionType:
        '''Available in PowerPoint 2010.'''
        ...

    @classmethod
    @property
    def ROTATE(cls) -> TransitionType:
        '''Available in PowerPoint 2010.'''
        ...

    @classmethod
    @property
    def ORBIT(cls) -> TransitionType:
        '''Available in PowerPoint 2010.'''
        ...

    @classmethod
    @property
    def DOORS(cls) -> TransitionType:
        '''Available in PowerPoint 2010.'''
        ...

    @classmethod
    @property
    def WINDOW(cls) -> TransitionType:
        '''Available in PowerPoint 2010.'''
        ...

    @classmethod
    @property
    def FERRIS(cls) -> TransitionType:
        '''Available in PowerPoint 2010.'''
        ...

    @classmethod
    @property
    def GALLERY(cls) -> TransitionType:
        '''Available in PowerPoint 2010.'''
        ...

    @classmethod
    @property
    def CONVEYOR(cls) -> TransitionType:
        '''Available in PowerPoint 2010.'''
        ...

    @classmethod
    @property
    def PAN(cls) -> TransitionType:
        '''Available in PowerPoint 2010.'''
        ...

    @classmethod
    @property
    def GLITTER(cls) -> TransitionType:
        '''Available in PowerPoint 2010.'''
        ...

    @classmethod
    @property
    def WARP(cls) -> TransitionType:
        '''Relates to transition Zoom in PowerPoint 2010.
                    Available in PowerPoint 2010.'''
        ...

    @classmethod
    @property
    def FLYTHROUGH(cls) -> TransitionType:
        '''Available in PowerPoint 2010.'''
        ...

    @classmethod
    @property
    def FLASH(cls) -> TransitionType:
        '''Available in PowerPoint 2010.'''
        ...

    @classmethod
    @property
    def SHRED(cls) -> TransitionType:
        '''Available in PowerPoint 2010.'''
        ...

    @classmethod
    @property
    def REVEAL(cls) -> TransitionType:
        '''Available in PowerPoint 2010.'''
        ...

    @classmethod
    @property
    def WHEEL_REVERSE(cls) -> TransitionType:
        '''Relates to transition Clock (with option Counterclockwise) in PowerPoint 2010.
                    Available in PowerPoint 2010.'''
        ...

    @classmethod
    @property
    def FALL_OVER(cls) -> TransitionType:
        '''Available in PowerPoint 2013.'''
        ...

    @classmethod
    @property
    def DRAPE(cls) -> TransitionType:
        '''Available in PowerPoint 2013.'''
        ...

    @classmethod
    @property
    def CURTAINS(cls) -> TransitionType:
        '''Available in PowerPoint 2013.'''
        ...

    @classmethod
    @property
    def WIND(cls) -> TransitionType:
        '''Available in PowerPoint 2013.'''
        ...

    @classmethod
    @property
    def PRESTIGE(cls) -> TransitionType:
        '''Available in PowerPoint 2013.'''
        ...

    @classmethod
    @property
    def FRACTURE(cls) -> TransitionType:
        '''Available in PowerPoint 2013.'''
        ...

    @classmethod
    @property
    def CRUSH(cls) -> TransitionType:
        '''Available in PowerPoint 2013.'''
        ...

    @classmethod
    @property
    def PEEL_OFF(cls) -> TransitionType:
        '''Available in PowerPoint 2013.'''
        ...

    @classmethod
    @property
    def PAGE_CURL_DOUBLE(cls) -> TransitionType:
        '''Available in PowerPoint 2013.'''
        ...

    @classmethod
    @property
    def PAGE_CURL_SINGLE(cls) -> TransitionType:
        '''Available in PowerPoint 2013.'''
        ...

    @classmethod
    @property
    def AIRPLANE(cls) -> TransitionType:
        '''Available in PowerPoint 2013.'''
        ...

    @classmethod
    @property
    def ORIGAMI(cls) -> TransitionType:
        '''Available in PowerPoint 2013.'''
        ...

    @classmethod
    @property
    def MORPH(cls) -> TransitionType:
        '''Relates to transition Morph (with option Type) in PowerPoint 2019.'''
        ...

    ...

