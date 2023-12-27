import math as m
from typing import List, Tuple

import numpy as np

def define_triangle() -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    ### STUDENT CODE
    # TODO: Implement this function.

	# NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    P1 = np.array((3, -2, -5))
    P2 = np.array((-3, -3, 5))
    P3 = np.array((-3, 3, -3))
    ### END STUDENT CODE

    return P1, P2, P3

def define_triangle_vertices(P1:np.ndarray, P2:np.ndarray, P3:np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    ### STUDENT CODE
    # TODO: Implement this function.

	# NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    P1P2 = np.array((P2[0] - P1[0], P2[1] - P1[1], P2[2] - P1[2]))      #P2 - P1
    P2P3 = np.array((P3[0] - P2[0], P3[1] - P2[1], P3[2] - P2[2]))      #P3 - P2
    P3P1 = np.array((P1[0] - P3[0], P1[1] - P3[1], P1[2] - P3[2]))      #P1 - P3
    
    ### END STUDENT CODE

    return P1P2, P2P3, P3P1

def compute_lengths(P1P2:np.ndarray, P2P3:np.ndarray, P3P1:np.ndarray) -> List[float]:
    ### STUDENT CODE
    # TODO: Implement this function.

	# NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.
    norms = [0., 0., 0.]
    norms[0] = m.sqrt(m.sqrt(pow((pow(P1P2[0], 2) + pow(P1P2[1], 2)), 2)) + pow(P1P2[2], 2))
    norms[1] = m.sqrt(m.sqrt(pow((pow(P2P3[0], 2) + pow(P2P3[1], 2)), 2)) + pow(P2P3[2], 2))
    norms[2] = m.sqrt(m.sqrt(pow((pow(P3P1[0], 2) + pow(P3P1[1], 2)), 2)) + pow(P3P1[2], 2))

    
    ### END STUDENT CODE

    return norms

def compute_normal_vector(P1P2:np.ndarray, P2P3:np.ndarray, P3P1:np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    ### STUDENT CODE
    # TODO: Implement this function.

	# NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    n = np.cross(P1P2, P2P3)
    n_normalized = n / np.linalg.norm(n)
    ### END STUDENT CODE

    return n, n_normalized

def compute_triangle_area(n:np.ndarray) -> float:
    ### STUDENT CODE
    # TODO: Implement this function.

	# NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.
    
    area = np.linalg.norm(n) * 0.5
    ### END STUDENT CODE

    return area

def compute_angles(P1P2:np.ndarray,P2P3:np.ndarray,P3P1:np.ndarray) -> Tuple[float, float, float]:
    ### STUDENT CODE
    # TODO: Implement this function.

	# NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.
    
    alpha, beta, gamma = 0., 0., 0.
    a = np.arccos(np.dot(P1P2, P3P1)/(np.linalg.norm(P1P2)*np.linalg.norm(P3P1))) #dot = skalarprodukt
    b = np.arccos(np.dot(P1P2, P2P3)/(np.linalg.norm(P1P2)*np.linalg.norm(P2P3))) #lianlg.norm = länge
    c = np.arccos(np.dot(P3P1, P2P3)/(np.linalg.norm(P3P1)*np.linalg.norm(P2P3)))
    alpha = 180 - m.degrees(a) #spitzer winkel
    beta = 180 - m.degrees(b)
    gamma = 180 - m.degrees(c)
    ### END STUDENT CODE

    return alpha, beta, gamma

