from OpenGL import GL
from OpenGL import GLU
from OpenGL import GLUT

import graph_data_struct as gs
import LPlotter as lp
import grammar_interpreter as gm
import grid as gr
import math
import copy as copy
from homework import control as control_menu

import quaternion as quat
import sys


class LSystem:
    def __init__(self, grammar, origin, startAngle, angle, length):
        self.grammar = grammar
        self.graf_object = gs.GraphicalObject()

        self.origin = origin
        self.startAngle = startAngle
        self.angle = angle
        self.length = length

    def makeGrew(self,age):
        self.graf_object = lp.l_systemGraphObject(self.grammar.make_grew(age),
                                                  self.origin, self.startAngle,
                                                  self.angle, self.length)
    def plotAge(self, age):
        self.makeGrew(age)
        self.graf_object.plot()

    def getGraficalObject(self):
        return self.graf_object

