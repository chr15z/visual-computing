from typing import List

import numpy as np
import matplotlib.pyplot as plt
import math as m

def define_transformations() -> List[np.ndarray]:
    """
        Returns the four transformations t_1, .., t_4 to transform the quadrat. 
        The transformations are determined by using mscale, mrotate and mtranslate.
    """
    ### STUDENT CODE
    # TODO: Implement this function.

	# NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.
    
    t1, t2, t3, t4 = np.zeros((3,3)), np.zeros((3,3)), np.zeros((3,3)), np.zeros((3,3)),
    t1 = mtranslate(-3,0) @ mrotate(55) 
    t2 = mrotate(55) @ mtranslate(-3,0) 
    t3 = mtranslate(3,1) @ mrotate(70) @ mscale(3, 2)
    t4 = mscale(1, 3) @ mrotate(45)

    ### END STUDENT CODE

    return [t1, t2, t3, t4]

def mscale(sx : float, sy : float) -> np.ndarray:
    """
        Defines a scale matrix. The scales are determined by s_x in x and s_y in y dimension.
    """
    ### STUDENT CODE
    # TODO: Implement this function.

	# NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    m = np.zeros((3,3))
    m[0][0] = sx
    m[1][1] = sy
    m[2][2] = 1


    ### END STUDENT CODE

    return m

def mrotate(angle : float) -> np.ndarray:
    """
        Defines a rotation matrix (z-axis) determined by the angle in degree (!).
    """
    ### STUDENT CODE
    # TODO: Implement this function.

	# NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    m = np.zeros((3,3))
    angle = np.deg2rad(angle)
    
    c = np.cos(angle)
    s = np.sin(angle)
    m = np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
    ### END STUDENT CODE

    return m
    
def mtranslate(tx : float, ty : float) -> np.ndarray:
    """
        Defines a translation matrix. t_x in x, t_y in y direction.
    """
    ### STUDENT CODE
    # TODO: Implement this function.

	# NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    m = np.zeros((3,3))
    m = np.array([[1,0,tx],[0,1,ty],[0,0,1]])
    ### END STUDENT CODE

    return m

def transform_vertices(v : np.ndarray, m : np.ndarray) -> np.ndarray:
    """
        transform the (3xN) vertices given by v with the (3x3) transformation matrix determined by m.
    """
    ### STUDENT CODE
    # TODO: Implement this function.

	# NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    out = np.zeros((m.shape[0],v.shape[1]))
    
    out = m @ v
    ### END STUDENT CODE

    return out

def display_vertices(v : np.ndarray, title : str) -> None:
    """
        Plot the vertices in a matplotlib figure.
    """
    # create the figure and set the title
    plt.figure()
    plt.axis('square')

    plt.title(title)

    # x and y limits
    plt.xlim((-6,6))
    plt.ylim((-6,6))
    plt.xticks(range(-6,6))
    plt.yticks(range(-6,6))

    # plot coordinate axis
    plt.axvline(color='black')
    plt.axhline(color='black')
    plt.grid()
    
    # we just add the last element, so plot can do our job :)
    v_ = np.concatenate((v, v[:, 0].reshape(3,-1)), axis=1)

    plt.plot(v_[0, :], v_[1, :], linewidth=3)
    plt.show()
