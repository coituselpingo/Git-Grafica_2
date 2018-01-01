#! /usr/bin/python3.5

import sys

import graph_data_struct as gs
import grid as gr
from OpenGL import GL
from OpenGL import GLU
from OpenGL import GLUT

from prototype import cuadrics as cu


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

    grid = gr.grid_gen()
    grid.show()

    list_of_objects = []

    ellipsoid = cu.ellipsoid(5, 5, 5, 0.1)
    hiperboloid_1h = cu.hiperboloid_1h(1, 1, 1, 2, 0.1)
    hiperboloid_2h = cu.hiperboloid_2h(1, 1, 1, 2, 0.1)
    elliptic_parabolid = cu.elliptic_paraboloid(3, 3, 3, 2, 0.1)
    hyperbolic_parabolid = cu.hyperbolic_parabolid(1, 1, 1, 2, 0.1)
    elliptic_cylinder = cu.elliptic_cylinder(3, 6, 5, 0.1)
    hyperbolic_cylinder = cu.hyperbolic_cylinder(1, 1, 1, 0.1)
    parabolic_cylinder = cu.parabolic_cylinder(1, 4, 0.1)

    list_of_objects.append(ellipsoid)
    list_of_objects.append(hiperboloid_1h)
    list_of_objects.append(hiperboloid_2h)
    list_of_objects.append(elliptic_parabolid)
    list_of_objects.append(hyperbolic_parabolid)
    list_of_objects.append(elliptic_cylinder)
    list_of_objects.append(hyperbolic_cylinder)
    list_of_objects.append(parabolic_cylinder)

    while True:

        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        grid.plot()

        ########################################

        gs.plot_list(list_of_objects)

        ########################################

        GL.glFlush()
        GLUT.glutPostRedisplay()

        gs.control(list_of_objects, GLU)

    GLUT.glutMainLoop()

main()