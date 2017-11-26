import bresenham3d as br
import graph_data_struct as gd
import grid as gr

import OpenGL.GL as GL
import OpenGL.GLU as GLU
import OpenGL.GLUT as GLUT


class RubikCubeElement(gd.GraphicalObject):

    def __int__(self, down_vertex, edge_length):
        self.ref_vertex = down_vertex
        self.length = edge_length

        self.generate()

    def generate(self):
        pass

    def create_vertex(self):


