from typing import Any, Dict, List, Literal, TypeAlias, TypedDict

from numpy.typing import NDArray

from facefusion.types import VisionFrame

FaceSwapperModel = Literal['blendswap_256', 'ghost_1_256', 'ghost_2_256', 'ghost_3_256', 'hififace_unofficial_256', 'hyperswap_1a_256', 'hyperswap_1b_256', 'hyperswap_1c_256', 'inswapper_128', 'inswapper_128_fp16', 'simswap_256', 'simswap_unofficial_512', 'uniface_256']

FaceSwapperSet : TypeAlias = Dict[FaceSwapperModel, List[str]]

FaceSwapperInputs = TypedDict('FaceSwapperInputs',
{
	'reference_vision_frame' : VisionFrame,
	'source_vision_frames' : List[VisionFrame],
	'target_vision_frame' : VisionFrame,
	'temp_vision_frame' : VisionFrame
})

FaceSwapperWeight : TypeAlias = float
