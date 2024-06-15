# Importing needed libraries
import pygame
from pygame.locals import *
from OpenGL.GL import *
import numpy as np

class Pyramid:
    def __init__(self):
        # Defining the vertices of the pyramid as a numpy array
        self.pyramid_vertices = np.array([
            (1, -1, -1),  # Bottom-right-front corner
            (1, 1, -1),   # Top-right-front corner
            (-1, 1, -1),  # Top-left-front corner
            (-1, -1, -1), # Bottom-left-front corner
            (0, 0, 1)     # Apex of the pyramid
        ], dtype='f')  # Explicitly defining the type as float for OpenGL compatibility

        # Defining the edges of the pyramid using pairs of vertex indices
        self.pyramid_edges = (
            (0, 1), (0, 2), (0, 3),  # Base edges
            (1, 2), (1, 3), (2, 3),  # Base edges
            (4, 0), (4, 1), (4, 2), (4, 3)  # Side edges connecting the apex
        )

    def draw(self):
        # Begin drawing lines
        glBegin(GL_LINES)
        for edge in self.pyramid_edges:
            glVertex3fv(self.pyramid_vertices[edge[0]])
            glVertex3fv(self.pyramid_vertices[edge[1]])
        # End drawing lines
        glEnd()
