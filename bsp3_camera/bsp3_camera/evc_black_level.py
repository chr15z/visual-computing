# Copyright TU Wien (2022) - EVC: Task3
# Computer Vision Lab
# Institute of Computer Graphics and Algorithms

from typing import Tuple

import numpy as np
from PIL import Image
from PIL.TiffTags import TAGS


def evc_read_file_info(filename: str) -> Tuple[int, Tuple]:
    """evc_read_file_info extracts the black level (blackLevel) and the neutral
    white value (asShotNeutral) from the image file specified by filename.
    
      INPUT
      filename... 		    filename of the image
    
      OUTPUT
      blackLevel... 		    black level, which is stored in the image infos
      asShotNeutral... 	    neutral white value, which is stored in the image"""

    ### STUDENT CODE
    #TODO:  Implement this function.
    #HINT: 	'PIL.TiffTags.TAGS' might be useful.
    #NOTE:  The following two lines can be removed. They prevent the
    #       framework from crashing.
    img = Image.open(filename)
    meta_dict = {TAGS[key]: img.tag[key] for key in img.tag_v2}
    blackLevel = meta_dict.get('BlackLevel')          # Extract the black level from the metadata
    asShotNeutral = meta_dict.get('AsShotNeutral')    # Extract the neutral white value from the metadata

    ### END STUDENT CODE
    
    
    return blackLevel[0], asShotNeutral
    
def evc_transform_colors(input_image: np.ndarray, blackLevel: float) -> np.ndarray:
    """evc_transform_colors adjusts the contrast such that black (blackLevel and
    values below) becomes 0 and white becomes 1.
    The white value of the input image is 65535.
    
      INPUT
      input_image...            input image
      blackLevel... 		black level of the input image
    
      OUTPUT
      result... 			image in double format where all values are
                          transformed from the interval [blackLevel, 65535]
                          to [0, 1]. All values below the black level have to
                          be 0."""

    ### STUDENT CODE
    #TODO:  Implement this function.
    #NOTE:  The following line can be removed. It prevents the framework
    #       from crashing.

    result = input_image.astype(float)
    result[result < blackLevel] = 0 # Set all values below the black level to 0
    result = result / np.max(result) # Clip the values to the range [0, 1] (a>1 -> 1 and a<0 -> 0)

    #result = np.zeros(input_image.shape)
    ### END STUDENT CODE
    
    
    return result
