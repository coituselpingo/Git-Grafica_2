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

young = OBJM.read_obj("./proyect-models/young.obj")
kid = OBJM.read_obj("./proyect-models/kid.obj")
youngold = OBJM.read_obj("./proyect-models/youngold.obj")

young.translate()
kid.translate()
youngold.translate()

young_list = young.point_set_collection
kid_list = kid.point_set_collection
youngold_list = youngold.point_set_collection

if len(young_list) == len(kid_list) and len(young_list) == len(youngold_list):
    print("this shit works")
else:
    print("this shit isnt working")
    exit()

scale_ratio = 3
translate_point = GD.Point()
translate_point.set_coord([0, 5, 0])

young.scale(scale_ratio)
young.translate(translate_point)

kid.scale(scale_ratio)
kid.translate(translate_point)

youngold.scale(scale_ratio)
youngold.translate(translate_point)

young.show()
kid.show()
youngold.show()

print("here ist'r are laggy")


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
    GLU.gluLookAt(0, 10, 10, 0, 0, 0, 0, 1, 0)

    grid = GR.grid_gen()
    #grid.show()

    kid.morph(youngold, 100, True)

    while True:
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        grid.plot()

        ########################################

        kid.morph(youngold, 100)

        ########################################

        GL.glFlush()
        GLUT.glutPostRedisplay()
        input("Pause")

    GLUT.glutMainLoop()

main()