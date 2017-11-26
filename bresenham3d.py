#! /usr/bin/python3.5

import graph_data_struct as gs
import quaternion as quat
import grid as gr

import math
import sys
import copy
import os

from OpenGL import GL
from OpenGL import GLU
from OpenGL import GLUT

"""
def bresenham(x0, y0, x1, y1):
    list_of_points = []

    dx = x1 - x0
    dy = y1 - y0

    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0

    D = 2*dy - dx
    y = 0

    for x in range(dx + 1):
        list_of_points.append([x0 + x*xx + y*yx, y0 + x*xy + y*yy])
        if D > 0:
            y += 1
            D -= dx
        D += dy

    return list_of_points


def bresenham_3d(first_point, second_point):

    set_points = []

    xy = bresenham(first_point[0], first_point[1], second_point[0], second_point[1])
    yz = bresenham(first_point[1], first_point[2], second_point[1], second_point[2])
    xz = bresenham(first_point[0], first_point[2], second_point[0], second_point[2])
    print(xy)
    print(yz)
    print(xz)

    for control_xz in xz:
        x = control_xz[0]
        y = None
        z = control_xz[1]

        top_xy = len(xy)
        top_yz = len(yz)

        DO = True
        index_xy = 0
        while DO:
            if xy[index_xy][0] == x:
                y = xy[index_xy][1]

                do_flag = True
                index_yz = 0
                while do_flag:
                    if yz[index_yz][1] == z or y == yz[index_yz][0]:
                        set_points.append((x, y, z))
                    index_yz += 1
                    if index_yz == top_yz:
                        do_flag = False

            index_xy += 1
            if index_xy == top_xy:
                DO = False

    return (sorted(list(set(set_points))))
"""


def bresenham_3d(p1, p2):

    [x1, y1, z1] = p1
    [x2, y2, z2] = p2

    output = []

    point = []
    point.append(x1)
    point.append(y1)
    point.append(z1)

    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1

    if dx < 0:
        x_inc = -1
    else:
        x_inc = 1
    l = int(math.fabs(dx))

    if dy < 0:
        y_inc = -1
    else:
        y_inc = 1
    m = int(math.fabs(dy))

    if dz < 0:
        z_inc = -1
    else:
        z_inc = 1
    n = int(math.fabs(dz))

    dx2 = l * 2
    dy2 = m * 2
    dz2 = n * 2

    if l >= m and l >= n:
        err_1 = dy2 - l
        err_2 = dz2 - l

        for i in range(0, l, 1):
            output.append([point[0], point[1], point[2]])
            if err_1 > 0:
                point[1] += y_inc
                err_1 -= dx2

            if err_2 > 0:
                point[2] += z_inc
                err_2 -= dx2

            err_1 += dy2
            err_2 += dz2
            point[0] += x_inc

    elif m >= l and m >= n:
        err_1 = dx2 - m
        err_2 = dz2 - m
        for i in range(0, m, 1):
            output.append([point[0], point[1], point[2]])
            if err_1 > 0:
                point[0] += x_inc
                err_1 -= dy2

            if err_2 > 0:
                point[2] += z_inc
                err_2 -= dy2

            err_1 += dx2
            err_2 += dz2
            point[1] += y_inc

    else:
        err_1 = dy2 - n
        err_2 = dx2 - n
        for i in range(0, n, 1):
            output.append([point[0], point[1], point[2]])
            if err_1 > 0:
                point[1] += y_inc
                err_1 -= dz2

            if err_2 > 0:
                point[0] += x_inc
                err_2 -= dz2

            err_1 += dy2
            err_2 += dx2
            point[2] += z_inc

    output.append([point[0], point[1], point[2]])

    return output


def main(p_0, p_i):
    GLUT.glutInit(sys.argv)
    GLUT.glutInitDisplayMode(GLUT.GLUT_SINGLE | GLUT.GLUT_RGBA | GLUT.GLUT_DEPTH)
    GLUT.glutInitWindowSize(400, 400)
    GLUT.glutInitWindowPosition(200, 200)

    GLUT.glutCreateWindow("Grafica 2")

    GL.glDepthFunc(GL.GL_LEQUAL)
    GL.glEnable(GL.GL_DEPTH_TEST)
    GL.glClearDepth(1.0)
    GL.glClearColor(0.0, 0.0, 0.0, 0.0)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
    GL.glMatrixMode(GL.GL_PROJECTION)
    GL.glLoadIdentity()
    GL.glMatrixMode(GL.GL_MODELVIEW)

    GLU.gluPerspective(100, 1.0, 1.0, 100.0)
    GL.glTranslatef(0.0, 0.0, 0.0)
    GLU.gluLookAt(10, 10, 10, 0, 0, 0, 0, 1, 0)

    points = bresenham_3d(p_0, p_i)

    print(points)


    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

    grid = gr.grid_gen(200, gs.Color(204/255, 0, 0))
    grid.show()
    grid.plot()

    ########################################

    GL.glPointSize(5)
    GL.glColor3f(1.0, 1.0, 1.0)
    #GL.glBegin(GL.GL_LINES)
    GL.glBegin(GL.GL_POINTS)
    #carry_ref = points[0]
    for ref_point in points:
        #coordinates = ref_point
        #GL.glVertex3f(carry_ref[0], carry_ref[1], carry_ref[2])
        GL.glVertex3f(ref_point[0], ref_point[1], ref_point[2])
        #carry_ref = ref_point

    GL.glEnd()

    ########################################

    GL.glFlush()
    GLUT.glutPostRedisplay()

    GLUT.glutMainLoop()

main([0, 0, 5], [10, 10, -5])


