#! /usr/bin/python3.5

import copy
import os
import sys
import copy
import numpy as np

from OpenGL import GL
from OpenGL import GLU
from OpenGL import GLUT

import libg2f.GraphData as GD
import libg2f.Grid as GR

head = GD.GraphicalObject()
head.push_edge(GD.Point(0.27889942, -0.05260135, -0.90838462), GD.Point(0.29209942, -0.05690133, -0.91828461), None, None, True)
head.push_edge(GD.Point(0.29209942, -0.05690133, -0.91828461), GD.Point(0.24099951, -0.06310134, -0.94708455), None, None, True)
head.push_edge(GD.Point(0.24099951, -0.06310134, -0.94708455), GD.Point(0.23729951, -0.05490135, -0.92678462), None, None, True)


head.show_points()
head.show_edges()
head.translate()
head.scale(50)
head.show()

def main():
    GLUT.glutInit(sys.argv)
    GLUT.glutInitDisplayMode(GLUT.GLUT_SINGLE | GLUT.GLUT_RGBA | GLUT.GLUT_DEPTH)
    GLUT.glutInitWindowSize(400, 400)
    GLUT.glutInitWindowPosition(200, 200)

    GLUT.glutCreateWindow("Grafica 2")

    GL.glDepthFunc(GL.GL_LEQUAL)
    GL.glEnable(GL.GL_DEPTH_TEST)
    GL.glClearDepth(1.0)
    GL.glClearColor(0.650, 0.780, 0.8, 0)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
    GL.glMatrixMode(GL.GL_PROJECTION)
    GL.glLoadIdentity()
    #GL.glOrtho(-20, 20, -20, 20, -20, 20)
    GL.glMatrixMode(GL.GL_MODELVIEW)

    GLU.gluPerspective(100, 1.0, 1.0, 100.0)
    GL.glTranslatef(0.0, 0.0, 0.0)
    GLU.gluLookAt(10, 10, 10, 0, 0, 0, 0, 1, 0)

    grid = GR.grid_gen()
    grid.show()

    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
    grid.plot()

    ########################################

    head.plot()

    ########################################

    GL.glFlush()
    GLUT.glutPostRedisplay()

    GLUT.glutMainLoop()

main()