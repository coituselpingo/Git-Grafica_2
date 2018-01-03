#! /usr/bin/python3.5

import copy
import os
import sys
import copy
import numpy as np

from OpenGL import GL
from OpenGL import GLU
from OpenGL import GLUT

import libg2f.OBJGraphData as GD
import libg2f.Grid as GR
import libg2f.OBJobject_manager as OBJM

head = OBJM.read_obj("./proyect-models/head.obj")
spherehead = OBJM.read_obj("./proyect-models/spherehead.obj")
conehead = OBJM.read_obj("./proyect-models/conehead.obj")

head.translate()
spherehead.translate()
conehead.translate()

head_list = head.point_set_collection
spherehead_list = spherehead.point_set_collection
conehead_list = conehead.point_set_collection

if (len(head_list) == len(conehead_list) and len(head_list) == len(spherehead_list)):
    print("this shit works")
else:
    print("this shit isnt working")
    exit()

#JEFFRI TU CODIGO VA AQUI



#DESDE AQUI YA NO

head.scale(10)
head.on_self_rotate_z(180, "+")
head.on_self_rotate_y(180, "+")
head.translate()
head.translate(GD.Point(0, 0, 5))
head.show()

head.on_self_rotate_y(45, "-")
head.on_self_rotate_x(45, "-")
head.on_self_rotate_z(45, "-")


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