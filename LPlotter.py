import re
from OpenGL import GL
from OpenGL import GLU
from OpenGL import GLUT

import graph_data_struct as gs
import grid as gr
import math
import copy as copy
from homework import control as control_menu

import quaternion as quat
import sys

def angle_beteween_vector(vect1, vect2):
    return math.asin((vect2[1] - vect1[1]) / (vect2[0] - vect1[0]))

def turtle_sentence(expresion):
    carry = ""
    for letter in expresion:
        if letter == "F" or letter == "+" or letter == "-" or letter == "[" or letter == "]":
            carry += letter
        else:
            pass

    return carry


def turtle_edge(ref_point, angle, length):

    carry_point = copy.copy(ref_point)
    carry_x = carry_point[0]
    carry_point[0] = length

    carry_y = carry_point[1]

    carry_point[1] -= carry_y

    carry_point = quat.rotate(carry_point, "z", angle)

    carry_point[0] += carry_x
    carry_point[1] += carry_y

    carry_point[0] = round(carry_point[0], 2)
    carry_point[1] = round(carry_point[1], 2)
    carry_point[2] = round(carry_point[2], 2)

    return [copy.copy(ref_point), carry_point]


def turtle_plotter(expresion, origin, startAngle, angle, length):
    edge_container = []

    carry_sentence = []
    carry_pile = []
    angle_pile = []

    carry_origin = origin
    carry_angle = startAngle
    for letter in expresion:
        if letter == "F":
            edge = turtle_edge(carry_origin, carry_angle, length)
            carry_sentence.append(edge)
            print(edge)
            carry_origin = edge[1]
        elif letter == "+":
            carry_angle += angle
        elif letter == "-":
            carry_angle -= angle
        elif letter == "[":
            angle_pile.append(carry_angle)
            carry_pile.append(carry_sentence)
            carry_sentence = []
        elif letter == "]":
            edge_container += carry_sentence
            carry_sentence = carry_pile.pop()
            carry_origin = carry_sentence[len(carry_sentence)-1][1]
            carry_angle = angle_pile.pop()
        else:
            pass

    for edge in carry_sentence:
        edge_container.append(edge)

    return edge_container

def l_systemGraphObject(expresion, origin, startAngle, angle, length):
    edges = turtle_plotter(expresion, origin, startAngle, angle, length)

    outputObject = gs.GraphicalObject()

    for pair in edges:
        outputObject.push_edge(gs.Point(pair[0][0], pair[0][1], pair[0][2]), gs.Point(pair[1][0], pair[1][1], pair[1][2]))

    outputObject.show()
    return outputObject



print(turtle_plotter("FFFF[+FF[+]FF[-]+]FFFF[-FF[+]FF[-]+]+FF[+]FF[-]+", [0, 0, 0], 90, 45, 5))

print(turtle_sentence("FFFF[+FF[+X]FF[-X]+X]FFFF[-FF[+X]FF[-X]+X]+FF[+X]FF[-X]+X"))

test_tree = l_systemGraphObject("FFFF[+FF[+]FF[-]+]FFFF[-FF[+]FF[-]+]+FF[+]FF[-]+", [0, 0, 0], 90, 45, 5)
test_tree.show()
list_of_objects = [test_tree]


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
    GL.glMatrixMode(GL.GL_MODELVIEW)

    GLU.gluPerspective(100, 1.0, 1.0, 100.0)
    GL.glTranslatef(0.0, 0.0, 0.0)
    GLU.gluLookAt(10, 10, 10, 0, 0, 0, 0, 1, 0)

    grid = gr.grid_gen(100,gs.Color(0.5, 1, 1))

    while True:

        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

        grid.show()
        grid.plot()

        ########################################

        for ref_object in list_of_objects:
            ref_object.plot()

        ########################################

        GL.glFlush()
        GLUT.glutPostRedisplay()

        control_menu(list_of_objects)

    GLUT.glutMainLoop()

main()
