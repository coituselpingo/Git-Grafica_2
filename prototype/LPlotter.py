import copy as copy
import math

import graph_data_struct as gs

from prototype import quaternion as quat


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

    return outputObject

