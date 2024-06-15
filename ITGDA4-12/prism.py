# Importing needed libraries
from OpenGL.GL import *
import numpy as np

class Prism:
    def __init__(self):
        # Defining the vertices of the prism as a numpy array
        self.prism_vertices = np.array([
            (-1, -1, -1),  # Bottom-left-back corner
            (1, -1, -1),   # Bottom-right-back corner
            (0, 1, -1),    # Top-middle-back corner
            (-1, -1, 1),   # Bottom-left-front corner
            (1, -1, 1),    # Bottom-right-front corner
            (0, 1, 1)      # Top-middle-front corner
        ], dtype='f')  # Explicitly defining the type as float for OpenGL compatibility

        # Defining the edges of the prism using pairs of vertex indices
        self.prism_edges = (
            (0, 1), (1, 2), (2, 0),  # Base edges
            (3, 4), (4, 5), (5, 3),  # Top edges
            (0, 3), (1, 4), (2, 5)   # Side edges connecting base to top
        )

    def draw(self):
        # Begin drawing lines
        glBegin(GL_LINES)
        for edge in self.prism_edges:
            glVertex3fv(self.prism_vertices[edge[0]])
            glVertex3fv(self.prism_vertices[edge[1]])
        # End drawing lines
        glEnd()
