# Importing needed libraries
import pygame 
from pygame.locals import *
from OpenGL.GL import *

#Defining a class for the Cube (Cube)
class Cube:
    def __init__(self):
        #Defining the vertices of the cube (cube_vertices) in a list
        self.cube_vertices = [
            [1, -1, -1],
            [1, 1, -1],
            [-1, 1, -1],
            [-1, -1, -1],
            [1, -1, 1],
            [1, 1, 1],
            [-1, -1, 1],
            [-1, 1, 1]
        ]
        

        #Defining the edges of the cube as pairs of vertex indices (cube_edges ) in a list
        self.cube_edges  = [
            (0, 1), (0, 4), (0, 3), (1, 2),
            (1, 5), (2, 3), (2, 7), (3, 6),
            (4, 5), (4, 6), (5, 7), (6, 7)
        ]

    #The method  used to draw the cube using OpenGL
    def draw(self):
        #Making sure to specify each vertex using function draw_edge
        def draw_edge(vertex): 
            glVertex3fv(self.cube_vertices[vertex])

        glBegin(GL_LINES)  #Drawing lines
        for edge in self.cube_edges :  #Iterating through each edge
            for vertex in edge:  #Iterating through the vertices in the edge
                draw_edge(vertex)  
        glEnd()  #The end of drawing the lines
