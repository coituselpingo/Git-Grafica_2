import re
import OpenGL.GL as GL
import OpenGL.GLU as GLU
import OpenGL.GLUT as GLUT

import graph_data_struct as gs

import copy as copy

import quaternion as quat

def turtle_sentence(expresion):
    carry = ""
    for letter in expresion:
        if letter == "F" or letter == "+" or letter == "-" or letter == "[" or letter == "]":
            carry += letter
        else:
            pass

    return carry


def turtle_edge(ref_point, angle, length, ref_object):

    carry_point = copy.copy(ref_point)
    carry_point[0] += length

    carry_point = quat.rotate(carry_point, "z", angle)
    ref_object.append([copy.copy(ref_point), copy.copy(carry_point)])

    return carry_point


def turtle_plotter(expresion, angle, length):
    expresion = turtle_sentence(expresion)
    origin = [0, 0, 0]
    tree = []

    F_counter = 0
    first = True

    event_stack = [[origin, angle]]

    for letter in expresion:
        [sub_origin, sub_angle] = event_stack.pop()
        if letter == "F":
            F_counter += 1
            print(tree)
            turtle_edge(origin, angle, F_counter*length, tree)
        else:
            pass
            first = False

    return tree

print(turtle_plotter("FFFF", 90, 5))


print(turtle_sentence("FFFF[+FF[+X]FF[-X]+X]FFFF[-FF[+X]FF[-X]+X]+FF[+X]FF[-X]+X"))