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
cylinderhead = OBJM.read_obj("./proyect-models/cylinderhead.obj")

head.translate()
spherehead.translate()
conehead.translate()
cylinderhead.translate()

head_list = head.point_set_collection
spherehead_list = spherehead.point_set_collection
conehead_list = conehead.point_set_collection
cylinderhead_list = cylinderhead.point_set_collection

if (len(head_list) == len(conehead_list)
    and len(head_list) == len(spherehead_list)
    and len(head_list) == len(cylinderhead_list)):
    print("this shit works")
else:
    print("this shit isnt working")
    exit()

head.scale(10)
head.on_self_rotate_z(180, "+")
head.on_self_rotate_y(180, "+")
head.translate()
head.translate(GD.Point(0, 0, 5))

head.on_self_rotate_y(45, "-")
head.on_self_rotate_x(45, "-")
head.on_self_rotate_z(45, "-")

spherehead.scale(10)
spherehead.on_self_rotate_z(180, "+")
spherehead.on_self_rotate_y(180, "+")
spherehead.translate()
spherehead.translate(GD.Point(0, 0, 5))

spherehead.on_self_rotate_y(45, "-")
spherehead.on_self_rotate_x(45, "-")
spherehead.on_self_rotate_z(45, "-")

conehead.scale(10)
conehead.on_self_rotate_z(180, "+")
conehead.on_self_rotate_y(180, "+")
conehead.translate()
conehead.translate(GD.Point(0, 0, 5))

conehead.on_self_rotate_y(45, "-")
conehead.on_self_rotate_x(45, "-")
conehead.on_self_rotate_z(45, "-")

cylinderhead.scale(10)
cylinderhead.on_self_rotate_z(180, "+")
cylinderhead.on_self_rotate_y(180, "+")
cylinderhead.translate()
cylinderhead.translate(GD.Point(0, 0, 5))

cylinderhead.on_self_rotate_y(45, "-")
cylinderhead.on_self_rotate_x(45, "-")
cylinderhead.on_self_rotate_z(45, "-")

head.show()


def main():
    GLUT.glutInit(sys.argv)
    GLUT.glutInitDisplayMode(GLUT.GLUT_SINGLE | GLUT.GLUT_RGBA | GLUT.GLUT_DEPTH)
    GLUT.glutInitWindowSize(400, 400)
    GLUT.glutInitWindowPosition(200, 200)

    GLUT.glutCreateWindow("Grafica 2")

    """
    GL.glLightfv(GL.GL_LIGHT0, GL.GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
    GL.glLightfv(GL.GL_LIGHT0, GL.GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
    GL.glLightfv(GL.GL_LIGHT0, GL.GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    GL.glLightfv(GL.GL_LIGHT0, GL.GL_POSITION, [1.0, 1.0, 1.0, 0.0])

    GL.glEnable(GL.GL_NORMALIZE)
    GL.glEnable(GL.GL_LIGHTING)
    GL.glEnable(GL.GL_LIGHT0)
    """

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

    head.morph(spherehead, 0.01, 2, True)

    while True:
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        grid.plot()

        ########################################

        head.morph(spherehead, 0.01, 2)

        ########################################

        GL.glFlush()
        GLUT.glutPostRedisplay()
        input("Pause")

    GLUT.glutMainLoop()

main()