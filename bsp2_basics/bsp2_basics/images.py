import numpy as np
import scipy.ndimage
from PIL import Image

import utils


def read_img(inp:str) -> Image.Image:
    """
        Returns a PIL Image given by its input path.
    """
    img =  Image.open(inp)
    return img

def convert(img:Image.Image) -> np.ndarray:
    """
        Converts a PIL image [0,255] to a numpy array [0,1].
    """
    ### STUDENT CODE
    # TODO: Implement this function.

	# NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    out = np.array(img)
    out = out.astype(float) / 255

    ### END STUDENT CODE
    return out

def switch_channels(img:np.ndarray) -> np.ndarray:
    """
        Swaps the red and green channel of a RGB iamge given by a numpy array.
    """
    ### STUDENT CODE
    # TODO: Implement this function.
    out = np.array(img)
    for i in range(len(out)):
            for j in range(len(out)):
                temp = out[i][j][0]
                out[i][j][0] = out[i][j][1]
                out[i][j][1] = temp

	# NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    ### END STUDENT CODE

    return out

def image_mark_green(img:np.ndarray) -> np.ndarray:
    """
        returns a numpy-array (HxW) with 1 where the green channel of the input image is greater or equal than 0.7, otherwise zero.
    """
    ### STUDENT CODE
    # TODO: Implement this function.

	# NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    mask = np.zeros((img.shape[0], img.shape[1])) # 2D Array height x width  
    mask[:,:] = np.where(img[:,:,1]< 0.7, False, True) # if green value (1) > 0.7 -> True 

    ### END STUDENT CODE

    return mask


def image_masked(img:np.ndarray, mask:np.ndarray) -> np.ndarray:
    """
        sets the pixels of the input image to zero where the mask is 1.
    """
    ### STUDENT CODE
    # TODO: Implement this function.

	# NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    out = np.array(img)
    out[:,:,0] = np.where(mask[:,:], 0, out[:,:,0]) #if mask[x,y] == true: set to 0
    out[:,:,1] = np.where(mask[:,:], 0, out[:,:,1])
    out[:,:,2] = np.where(mask[:,:], 0, out[:,:,2])
    
    ### END STUDENT CODE

    return out

def grayscale(img:np.ndarray) -> np.ndarray:
    """
        Returns a grayscale image of the input. Use utils.rgb2gray().
    """
    ### STUDENT CODE
    # TODO: Implement this function.

	# NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    out = utils.rgb2gray(img)
    ### END STUDENT CODE

    return out

def cut_and_reshape(img_gray:np.ndarray) -> np.ndarray:
    """
        Cuts the image in half (x-dim) and stacks it together in y-dim.
    """
    ### STUDENT CODE
    # TODO: Implement this function.

	# NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    out = np.array(img_gray)
    first, second = np.hsplit(out, 2)
    out = np.concatenate((second, first))
    
    ### END STUDENT CODE

    return out

def filter_image(img:np.ndarray) -> np.ndarray:
    """
        filters the image with the gaussian kernel given below. 
    """
    gaussian = utils.gauss_filter(5, 2) # liefert ein array zurück

    ### STUDENT CODE
    # TODO: Implement this function.

	# NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    out = np.zeros(img.shape)
    
    imgPadded = np.pad(img,((2,2),(2,2),(0,0)),'constant')      #erstellt neues Array mit "Rand" 2 nach oben unten 2 nach links rechts 0 im 3d raum. constant = 0en

    for i in range(2,len(imgPadded)-4):
        for j in range(2,len(imgPadded[0])-4):
            
            out[i-2,j-2,0] = np.sum(imgPadded[i-2:i+3,j-2:j+3,0]*gaussian)  #R
            out[i-2,j-2,1] = np.sum(imgPadded[i-2:i+3,j-2:j+3,1]*gaussian)  #G
            out[i-2,j-2,2] = np.sum(imgPadded[i-2:i+3,j-2:j+3,2]*gaussian)  #B


    ### END STUDENT CODE

    return out

def horizontal_edges(img:np.ndarray) -> np.ndarray:
    """
        Defines a sobel kernel to extract horizontal edges and convolves the image with it.
    """
    ### STUDENT CODE
    # TODO: Implement this function.

	# NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    out = np.array(img)
    sobelFilter = np.array([[1,2,1],[0,0,0], [-1,-2,-1]]) # horizontal
    # sobelFilter = np.array([[1,0,-1],[2,0,-2], [1,0,-1]]) # verikal
    out = scipy.ndimage.correlate(out, sobelFilter)


    ### END STUDENT CODE

    return out
