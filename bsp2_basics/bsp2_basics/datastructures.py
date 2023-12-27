from typing import Tuple
import numpy as np
    
def define_structures() -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
        Defines the two vectors v1 and v2 as well as the matrix M determined by your matriculation number.
    """
    ### STUDENT CODE
    # TODO: Implement this function.

	# NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.
                                    #12224224
                                    #ABCDEFGH
    v1 = np.array([2,1,2])                    #DAC
    v2 = np.array([2,2,4])                    #FBE
    M = np.array([[2,2,2],[2,2,1],[4,4,2]])   #DBC BGA EHF
    
    ### END STUDENT CODE

    return v1, v2, M

def sequence(M : np.ndarray) -> np.ndarray:
    """
        Defines a vector given by the minimum and maximum digit of your matriculation number. Step size = 0.25.
    """
    ### STUDENT CODE
    # TODO: Implement this function.

	# NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.
    min_digit = np.min(M)
    max_digit = np.max(M)
    result = np.arange(min_digit, max_digit + 0.25, 0.25)
    

    ### END STUDENT CODE


    return result

def matrix(M : np.ndarray) -> np.ndarray:
    """
        Defines the 15x9 block matrix as described in the task description.
    """
    ### STUDENT CODE
    # TODO: Implement this function.

	# NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    r = np.zeros((15,9))
    helpArr = np.zeros((3,3))
    
    first = np.hstack((M, helpArr, M))
    second = np.hstack((helpArr, M, helpArr))

    r = np.vstack((first,second,first,second,first))
    r = r.astype(int)
    

    ### END STUDENT CODE

    return r


def dot_product(v1:np.ndarray, v2:np.ndarray) -> float:
    """
        Dot product of v1 and v2.
    """
    ### STUDENT CODE
    # TODO: Implement this function.

	# NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.
    r = 0
    for i in range(len(v1)):
        r = r + v1[i]*v2[i]

    ### END STUDENT CODE

    return r

def cross_product(v1:np.ndarray, v2:np.ndarray) -> np.ndarray:
    """
        Cross product of v1 and v2.
    """
    ### STUDENT CODE
    # TODO: Implement this function.

	# NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.
    
        
    r = np.zeros((3,1))
    r[0] = v1[1] * v2[2] - v1[2] * v2[1]
    r[1] = v1[2] * v2[0] - v1[0] * v2[2]
    r[2] = v1[0] * v2[1] - v1[1] * v2[0]
    r = r.astype(int)

    ### END STUDENT CODE

    return r

def vector_X_matrix(v:np.ndarray, M:np.ndarray) -> np.ndarray:
    """
        Defines the vector-matrix multiplication v*M.
    """
    ### STUDENT CODE
    # TODO: Implement this function.

	# NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.
    r = np.zeros((v.shape[0], M.shape[1]))
    
    for j in range(len(r)):
        for i in range(len(r)):
            r[j][i] = v[j] * (M[0][i] + M[1][i] + M[2][i])
        
    return r.astype(int)

def matrix_X_vector(M:np.ndarray, v:np.ndarray) -> np.ndarray:
    """
        Defines the matrix-vector multiplication M*v.
    """
    ### STUDENT CODE
    # TODO: Implement this function.

	# NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.
    r = np.zeros((3,1))

    for i in range(len(v)):
        for j in range(len(v)):
            r[i] += M[i][j] * v[j]
        
    ### END STUDENT CODE

    return r.astype(int)

def matrix_X_matrix(M1:np.ndarray, M2:np.ndarray) -> np.ndarray:
    """
        Defines the matrix multiplication M1*M2.
    """
    ### STUDENT CODE
    # TODO: Implement this function.

	# NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.
    r = np.zeros((M1.shape[0], M2.shape[1]))
    for i in range(3):
        for j in range(3):
            for k in range(3):
                r[i][j] += M1[i][k] * M2[k][j] 
    ### END STUDENT CODE

    return r.astype(int)

def matrix_Xc_matrix(M1:np.ndarray, M2:np.ndarray) -> np.ndarray:
    """
        Defines the element-wise matrix multiplication M1*M2 (Hadamard Product).
    """
    ### STUDENT CODE
    # TODO: Implement this function.

	# NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.
    r = np.zeros(M1.shape)

    for i in range(3):
        for j in range(3):
            r[i][j] = M1[i][j] * M2[i][j]
    ### END STUDENT CODE
    

    return r.astype(int)
