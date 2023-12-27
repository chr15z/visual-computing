# Copyright TU Wien (2022) - EVC: Task5
# Institute of Computer Graphics and Algorithms.

import numpy as np
from numpy.matlib import repmat

from MeshVertex import MeshVertex
from Framebuffer import Framebuffer
from MeshVertex import MeshVertex

def fill_rasterization(mesh : MeshVertex, framebuffer : Framebuffer):
    """ applies the fill rasterization algorithm. Draws a mesh to the Framebuffer."""

    for i in range(mesh.faces.shape[0]):
        v1 = mesh.get_face(i).get_vertex(0)
        for j in range(mesh.faces[i][0]-1):
            i, j = np.array(i).reshape(np.asarray(i).size), np.array(j).reshape(np.asarray(j).size)

            v2 = mesh.get_face(i).get_vertex(j)
            v3 = mesh.get_face(i).get_vertex(j+1)
            draw_triangle(framebuffer, v1, v2, v3)


def line_eq(A : float, B : float, C : float, x : float, y : float) -> float:
    """defines the line equation described by the provided parameters and
        returns the distance of a point (x, y) to this line.
        A    ... line equation parameter 1
        B    ... line equation parameter 2
        C    ... line equation parameter 3
        x    ... x coordinate of point to test against the line
        y    ... y coordinate of point to test against the line
        res  ... distance of the point (x, y) to the line (A, B, C)."""

    ### STUDENT CODE
    # TODO 3:   Implement this function.
    # NOTE:     The following lines can be removed. They prevent the framework
    #           from crashing.


    res = A * x + B * y + C
 
    ### END STUDENT CODE


    return res

def draw_triangle(framebuffer : Framebuffer, v1 : MeshVertex, v2 : MeshVertex, v3 : MeshVertex):
    """ draws a triangle defined by v1,v2,v3 to the given framebuffer"""
    
    x1, y1, depth1 = v1.get_screen_coordinates()
    x2, y2, depth2 = v2.get_screen_coordinates()
    x3, y3, depth3 = v3.get_screen_coordinates()

    col1 = v1.get_color()
    col2 = v2.get_color()
    col3 = v3.get_color()

    # calc triangle area * 2
    a = ((x3-x1)*(y2-y1) - (x2-x1)*(y3-y1))

    if not np.isclose(a, 0):
        # Swap order of clockwise triangle to make them counter-clockwise
        if a < 0:
            t = x2
            x2 = x3 
            x3 = t

            t = y2
            y2 = y3
            y3 = t

            t = depth2
            depth2 = depth3
            depth3 = t

            t = col2
            col2 = col3
            col3 = t

        ### STUDENT CODE
        # TODO 3: Implement this function.
        # HINT:   Don't forget to implement the function lineEq!
        #         Read the instructions and tutorial.py for further explanations!
        # BONUS:  Solve this task without using loops.
    
    #Ai 
    A1 = -(y3-y2)
    A2 = -(y1-y3)
    A3 = -(y2-y1)

    #Bi 
    B1 = x3-x2; 
    B2 = x1-x3; 
    B3 = x2-x1

    #distance to origin
    C1 = -((A1*x2)+(B1*y2))
    C2 = -((A2*x3)+(B2*y3))
    C3 = -((A3*x1)+(B3*y1))

    #Oi 
    O1 = line_eq(A1,B1,C1,x1,y1)
    if O1 == 1:
        O1 = 10**-10 #10^(-10)

    O2 = line_eq(A2,B2,C2,x2,y2)
    if O2 == 1:
        O2 = 10**-10
        
    O3 = line_eq(A3,B3,C3,x3,y3)
    if O3 == 1:
        O3 = 10**-10
       
    #Boundingbox
    xCoords = [x1,x2,x3]
    yCoords = [y1,y2,y3]

    minX = int(min(xCoords))
    maxX = int(max(xCoords))

    minY = int(min(yCoords))
    maxY = int(max(yCoords))

    for x in range(minX,maxX):
        for y in range(minY,maxY):
            OP1 = line_eq(A1,B1,C1,x,y)
            OP2 = line_eq(A2,B2,C2,x,y)
            OP3 = line_eq(A3,B3,C3,x,y)

            if OP1 <= 0 and OP2 <= 0 and OP3 <= 0: #Wenn alle 3 <=0 ist der Punkt im Dreieck
                alpha = OP1/O1
                beta = OP2/O2
                gamma = OP3/O3

                framebuffer.set_pixel([x],[y],MeshVertex.barycentric_mix(depth1,depth2,depth3,alpha,beta,gamma),
                                      MeshVertex.barycentric_mix(col1,col2,col3,alpha,beta,gamma))


        ### END STUDENT CODE

