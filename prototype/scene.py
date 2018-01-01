#! /usr/bin/python3.5

import sys

import graph_data_struct as gs
from OpenGL import GL
from OpenGL import GLUT

scale_option = "rgb"

def Base():

    ref_color = gs.Color(0.501,0.349,0.219)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_TRIANGLES)#1
    GL.glVertex2f(102,329)
    GL.glVertex2f(160,422)
    GL.glVertex2f(191,365)
    GL.glEnd()

    ref_color = gs.Color(0.411,0.278,0.172)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_TRIANGLES)#2
    GL.glVertex2f(102,329)
    GL.glVertex2f(178,344)
    GL.glVertex2f(191,365)
    GL.glEnd()

    ref_color = gs.Color(0.2,0.149,0.082)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_TRIANGLES)#3
    GL.glVertex2f(160,422)
    GL.glVertex2f(191,365)
    GL.glVertex2f(205,430)
    GL.glEnd()

    ref_color = gs.Color(0.337,0.235,0.098)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)#4
    GL.glVertex2f(178,344)
    GL.glVertex2f(191,365)
    GL.glVertex2f(291,385)
    GL.glVertex2f(312,367)
    GL.glEnd()

    ref_color = gs.Color(0.301,0.2,0.133)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_TRIANGLES)#5
    GL.glVertex2f(191,365)
    GL.glVertex2f(205,430)
    GL.glVertex2f(228,463)
    GL.glEnd()

    ref_color = gs.Color(0.411,0.278,0.172)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_TRIANGLES)#6
    GL.glVertex2f(191,365)
    GL.glVertex2f(228,463)
    GL.glVertex2f(291,385)
    GL.glEnd()

    ref_color = gs.Color(0.309,0.2,0.145)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_TRIANGLES)#7
    GL.glVertex2f(228,463)
    GL.glVertex2f(291,385)
    GL.glVertex2f(348,495)

    GL.glEnd()

    ref_color = gs.Color(0.2,0.149,0.086)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_TRIANGLES)#8
    GL.glVertex2f(228,463)
    GL.glVertex2f(303,508)
    GL.glVertex2f(348,495)
    GL.glEnd()

    ref_color = gs.Color(0.250,0.192,0.109)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_TRIANGLES)#9
    GL.glVertex2f(348,495)
    GL.glVertex2f(291,385)
    GL.glVertex2f(377,440)

    GL.glEnd()

    ref_color = gs.Color(0.301,0.211,0.090)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_TRIANGLES)#11
    GL.glVertex2f(413,348)
    GL.glVertex2f(291,385)
    GL.glVertex2f(377,440)

    GL.glEnd()

    ref_color = gs.Color(0.250,0.192,0.117)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_TRIANGLES)#10
    GL.glVertex2f(413,348)
    GL.glVertex2f(291,385)
    GL.glVertex2f(312,367)
    GL.glEnd()

    ref_color = gs.Color(0.2,0.149,0.086)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_TRIANGLES)#12
    GL.glVertex2f(348,495)
    GL.glVertex2f(407,459)
    GL.glVertex2f(377,440)
    GL.glEnd()

    ref_color = gs.Color(0.250,0.192,0.109)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_TRIANGLES)#13
    GL.glVertex2f(407,459)
    GL.glVertex2f(377,440)
    GL.glVertex2f(413,348)
    GL.glEnd()

    ref_color = gs.Color(0.250,0.192,0.109)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_TRIANGLES)#13*14
    GL.glVertex2f(407,459)
    GL.glVertex2f(451,402)
    GL.glVertex2f(413,348)
    GL.glEnd()

    ref_color = gs.Color(0.2,0.149,0.082)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_TRIANGLES)#14
    GL.glVertex2f(451,402)
    GL.glVertex2f(377,440)
    GL.glVertex2f(413,348)
    GL.glEnd()

    ref_color = gs.Color(0.250,0.192,0.109)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_TRIANGLES)#15
    GL.glVertex2f(451,402)
    GL.glVertex2f(413,348)
    GL.glVertex2f(476,347)
    GL.glEnd()

    ref_color = gs.Color(0.333,0.239,0.105)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_TRIANGLES)#16
    GL.glVertex2f(451,402)
    GL.glVertex2f(476,347)
    GL.glVertex2f(504,367)
    GL.glEnd()

    ref_color = gs.Color(0.333,0.239,0.105)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_TRIANGLES)#17
    GL.glVertex2f(476,347)
    GL.glVertex2f(504,367)
    GL.glVertex2f(512,329)
    GL.glEnd()

    ref_color = gs.Color(0.278,0.470,0.121)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)
    GL.glVertex2f(102,329)
    GL.glVertex2f(178,344)
    GL.glVertex2f(312,367)
    GL.glVertex2f(413,348)
    GL.glVertex2f(476,347)
    GL.glVertex2f(512,329)
    GL.glVertex2f(440,295)
    GL.glVertex2f(387,284)
    GL.glVertex2f(208,282)
    GL.glVertex2f(102,329)
    GL.glEnd()


def piedra( x,  y):

    ref_color = gs.Color(0.372,0.403,0.360)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)
    GL.glVertex2f(201+x,330+y)
    GL.glVertex2f(192+x,340+y)
    GL.glVertex2f(211+x,343+y)
    GL.glVertex2f(211+x,338+y)
    GL.glEnd()

    ref_color = gs.Color(0.215,0.219,0.164)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)
    GL.glVertex2f(201+x,330+y)
    GL.glVertex2f(192+x,340+y)
    GL.glVertex2f(186+x,335+y)
    GL.glVertex2f(196+x,325+y)
    GL.glEnd()

    ref_color = gs.Color(0.564,0.537,0.474)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)
    GL.glVertex2f(196+x,325+y)
    GL.glVertex2f(201+x,330+y)
    GL.glVertex2f(211+x,338+y)
    GL.glVertex2f(217+x,330+y)
    GL.glVertex2f(206+x,320+y)

    GL.glEnd()

    ref_color = gs.Color(0.215,0.219,0.164)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)
    GL.glVertex2f(211+x,343+y)
    GL.glVertex2f(211+x,338+y)
    GL.glVertex2f(217+x,338+y)
    GL.glVertex2f(220+x,342+y)
    GL.glEnd()

    ref_color = gs.Color(0.372,0.403,0.360)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)
    GL.glVertex2f(211+x,338+y)
    GL.glVertex2f(217+x,338+y)
    GL.glVertex2f(220+x,342+y)
    GL.glVertex2f(222+x,340+y)
    GL.glVertex2f(217+x,330+y)
    GL.glEnd()


def cerro():

    ref_color = gs.Color(0.462,0.462,0.462)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)
    GL.glVertex2f(316,327)
    GL.glVertex2f(269,298)
    GL.glVertex2f(321,154)
    GL.glVertex2f(329,182)
    GL.glEnd()

    ref_color = gs.Color(0.950,0.954,0.962)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_TRIANGLES)
    GL.glVertex2f(321,154)
    GL.glVertex2f(329,182)
    GL.glVertex2f(339,101)#punta
    GL.glEnd()

    ref_color = gs.Color(0.380,0.380,0.380)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)
    GL.glVertex2f(316,327)
    GL.glVertex2f(329,182)#*
    GL.glVertex2f(347,155)#*
    GL.glVertex2f(378,321)
    GL.glEnd()

    ref_color = gs.Color(0.850,0.854,0.862)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_TRIANGLES)
    GL.glVertex2f(329,182)#*
    GL.glVertex2f(347,155)#*
    GL.glVertex2f(339,101)#punta
    GL.glEnd()

    ref_color = gs.Color(0.282,0.282,0.274)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)
    GL.glVertex2f(347,155)#*
    GL.glVertex2f(378,321)
    GL.glVertex2f(412,295)
    GL.glVertex2f(368,181)#*
    GL.glEnd()

    ref_color = gs.Color(0.750,0.754,0.762)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_TRIANGLES)
    GL.glVertex2f(368,181)#*
    GL.glVertex2f(347,155)#*
    GL.glVertex2f(339,101)#punta
    GL.glEnd()


def oso():

    ref_color = gs.Color(0.678,0.603,0.580)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)
    GL.glVertex2f(104,296)
    GL.glVertex2f(111,301)
    GL.glVertex2f(116,299)#
    GL.glEnd()

    ref_color = gs.Color(0.827,0.650,0.529)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)
    GL.glVertex2f(104,296)
    GL.glVertex2f(110,289)
    GL.glVertex2f(116,299)#
    GL.glEnd()

    ref_color = gs.Color(0.407,0.278,0.219)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)
    GL.glVertex2f(155,314)
    GL.glVertex2f(155,327)#pes
    GL.glVertex2f(165,334)#pes
    GL.glVertex2f(169,316)
    GL.glVertex2f(167,307)
    GL.glEnd()

    ref_color = gs.Color(0.572,0.458,0.403)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)#pseuñas
    GL.glVertex2f(155,327)#pes
    GL.glVertex2f(165,334)#pes
    GL.glVertex2f(149,334)
    GL.glEnd()

    ref_color = gs.Color(0.454,0.325,0.250)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)
    GL.glVertex2f(128,297)
    GL.glVertex2f(110,289)
    GL.glVertex2f(116,299)#
    GL.glEnd()

    ref_color = gs.Color(0.694,0.529,0.443)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)
    GL.glVertex2f(126,296)
    GL.glVertex2f(128,294)
    GL.glVertex2f(127,266)
    GL.glVertex2f(118,270)#
    GL.glVertex2f(108,285)
    GL.glVertex2f(110,289)
    GL.glEnd()

    ref_color = gs.Color(0,0,0)
    GL.glBegin
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()
    
    GL.glBegin(GL.GL_POLYGON)
    GL.glVertex2f(110,289)
    GL.glVertex2f(113,293)
    GL.glVertex2f(114,290)
    GL.glEnd()

    ref_color = gs.Color(0.345,0.196,0.121)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)
    GL.glVertex2f(113,274)
    GL.glVertex2f(115,282)
    GL.glVertex2f(122,281)
    GL.glVertex2f(119,282)
    GL.glEnd()

    ref_color = gs.Color(0.454,0.305,0.121)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)
    GL.glVertex2f(113,274)
    GL.glVertex2f(115,282)
    GL.glVertex2f(122,281)
    GL.glVertex2f(121,278)
    GL.glEnd()


    ref_color = gs.Color(0.670,0.470,0.349)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)
    GL.glVertex2f(127,266)
    GL.glVertex2f(126,296)
    GL.glVertex2f(139,300)#*
    GL.glVertex2f(139,261)#*
    GL.glEnd()

    ref_color = gs.Color(0.545,0.360,0.282)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)
    GL.glVertex2f(139,261)#*
    GL.glVertex2f(139,305)
    #glVertex2f(129,315)
    #glVertex2f(135,330)
    GL.glVertex2f(168,308)
    GL.glVertex2f(156,268)#*
    GL.glVertex2f(139,261)#*
    GL.glEnd()

    ref_color = gs.Color(0.415,0.313,0.262)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)#lomo triangulo
    GL.glVertex2f(152,258)
    GL.glVertex2f(156,268)#*
    GL.glVertex2f(139,261)#*
    GL.glEnd()

    ref_color = gs.Color(0.666,0.505,0.419)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)#lomo triangulo
    GL.glVertex2f(152,258)
    GL.glVertex2f(156,268)#*
    GL.glVertex2f(165,261)
    GL.glEnd()

    ref_color = gs.Color(0.545,0.360,0.282)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)
    GL.glVertex2f(139,305)
    GL.glVertex2f(129,315)
    GL.glVertex2f(135,330)
    GL.glVertex2f(168,308)
    GL.glVertex2f(156,268)#*
    GL.glEnd()

    ref_color = gs.Color(0.572,0.458,0.403)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)#pseuñas
    GL.glVertex2f(129,315)
    GL.glVertex2f(135,330)
    GL.glVertex2f(127,333)
    GL.glEnd()

    ref_color = gs.Color(0.803,0.627,0.537)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_TRIANGLES)#
    GL.glVertex2f(156,268)#*
    GL.glVertex2f(165,261)
    GL.glVertex2f(168,308)
    GL.glEnd()

    ref_color = gs.Color(0.674,0.478,0.349)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_QUADS)#barriga
    GL.glVertex2f(165,261)
    GL.glVertex2f(168,308)
    GL.glVertex2f(203,301)
    GL.glVertex2f(207,257)
    GL.glEnd()

    ref_color = gs.Color(0.407,0.278,0.219)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_TRIANGLES)#barriga triangulo bajo
    GL.glVertex2f(168,308)
    GL.glVertex2f(203,301)
    GL.glVertex2f(203,315)
    GL.glEnd()


    #atras

    ref_color = gs.Color(0.525,0.364,0.294)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)#traser
    GL.glVertex2f(239,325)#pes
    GL.glVertex2f(245,333)#pes
    GL.glVertex2f(233,333)
    GL.glEnd()

    ref_color = gs.Color(0.286,0.196,0.164)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)#traser
    GL.glVertex2f(238,286)
    GL.glVertex2f(225,307)
    GL.glVertex2f(239,325)#pes
    GL.glVertex2f(245,333)#pes
    GL.glVertex2f(252,321)
    GL.glVertex2f(238,286)
    GL.glEnd()

    ref_color = gs.Color(0.529,0.360,0.298)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)#cola
    GL.glVertex2f(240,285)
    GL.glVertex2f(233,295)
    GL.glVertex2f(245,292)
    GL.glEnd()

    ref_color = gs.Color(0.407,0.278,0.219)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)#traser
    GL.glVertex2f(234,275)
    GL.glVertex2f(223,307)
    GL.glVertex2f(227,307)
    GL.glVertex2f(240,285)
    GL.glEnd()


    ref_color = gs.Color(0.556,0.372,0.301)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)#pata trasera
    GL.glVertex2f(207,257)
    GL.glVertex2f(203,301)
    GL.glVertex2f(203,315)
    GL.glVertex2f(206,326)#pes
    GL.glVertex2f(209,333)#pes
    GL.glVertex2f(220,334)
    GL.glVertex2f(234,275)
    GL.glEnd()

    ref_color = gs.Color(0.572,0.458,0.403)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)#pata trasera
    GL.glVertex2f(206,326)#pes
    GL.glVertex2f(209,333)#pes
    GL.glVertex2f(198,333)
    GL.glEnd()
    

def nube( x,  y):

    ref_color = gs.Color(0.984,0.988,0.996)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_TRIANGLES)#1
    GL.glVertex2f(355+x,310+y)
    GL.glVertex2f(414+x,330+y)
    GL.glVertex2f(412+x,312+y)
    GL.glEnd()

    ref_color = gs.Color(0.866,0.878,0.756)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_TRIANGLES)#2
    GL.glVertex2f(355+x,310+y)
    GL.glVertex2f(414+x,330+y)
    GL.glVertex2f(390+x,340+y)
    GL.glEnd()

    ref_color = gs.Color(0.843,0.819,0.772)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)#3
    GL.glVertex2f(412+x,312+y)
    GL.glVertex2f(414+x,330+y)
    GL.glVertex2f(451+x,325+y)
    GL.glVertex2f(433+x,309+y)
    GL.glEnd()

    ref_color = gs.Color(0.956,0.945,0.886)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_TRIANGLES)#4
    GL.glVertex2f(414+x,330+y)
    GL.glVertex2f(451+x,325+y)
    GL.glVertex2f(491+x,341+y)
    GL.glEnd()

    ref_color = gs.Color(0.894,0.862,0.811)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_TRIANGLES)#10
    GL.glVertex2f(414+x,330+y)
    GL.glVertex2f(455+x,335+y)
    GL.glVertex2f(459+x,350+y)
    GL.glEnd()

    ref_color = gs.Color(0.835,0.827,0.768)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_TRIANGLES)#5
    GL.glVertex2f(414+x,330+y)
    GL.glVertex2f(390+x,340+y)
    GL.glVertex2f(459+x,350+y)
    GL.glEnd()

    ref_color = gs.Color(0.984,0.980,0.972)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)#6
    GL.glVertex2f(451+x,325+y)
    GL.glVertex2f(433+x,309+y)
    GL.glVertex2f(484+x,297+y)
    GL.glEnd()

    ref_color = gs.Color(0.886,0.882,0.803)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)#7
    GL.glVertex2f(451+x,325+y)
    GL.glVertex2f(484+x,297+y)
    GL.glVertex2f(478+x,316+y)
    GL.glEnd()

    ref_color = gs.Color(0.827,0.823,0.752)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)#7.5
    GL.glVertex2f(451+x,325+y)
    GL.glVertex2f(478+x,316+y)
    GL.glVertex2f(491+x,341+y)
    GL.glEnd()

    ref_color = gs.Color(0.960,0.952,0.901)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)#9
    GL.glVertex2f(484+x,297+y)
    GL.glVertex2f(478+x,316+y)
    GL.glVertex2f(548+x,325+y)
    GL.glEnd()
    ref_color = gs.Color(0.803,0.792,0.733)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)#8
    GL.glVertex2f(548+x,325+y)
    GL.glVertex2f(478+x,316+y)
    GL.glVertex2f(491+x,341+y)
    GL.glEnd()

    ref_color = gs.Color(0.796,0.784,0.709)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_TRIANGLES)#11
    GL.glVertex2f(491+x,341+y)
    GL.glVertex2f(455+x,335+y)
    GL.glVertex2f(459+x,350+y)
    GL.glEnd()


def arbol( x,  y):

    ref_color = gs.Color(0.203,0.129,0.101)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)
    GL.glVertex2f(244+x,320+y)
    GL.glVertex2f(244+x,282+y)
    GL.glVertex2f(247+x,282+y)
    GL.glVertex2f(249+x,320+y)
    GL.glEnd()

    ref_color = gs.Color(0.290,0.180,0.137)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)
    GL.glVertex2f(244+x,320+y)
    GL.glVertex2f(244+x,282+y)
    GL.glVertex2f(240+x,282+y)
    GL.glVertex2f(240+x,318+y)
    GL.glEnd()

    ref_color = gs.Color(0.129,0.243,0.121)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_TRIANGLES)
    GL.glVertex2f(255+x,284+y)
    GL.glVertex2f(233+x,279+y)
    GL.glVertex2f(230+x,282+y)
    GL.glEnd()

    ref_color = gs.Color(0.105,0.176,0.082)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_TRIANGLES)
    GL.glVertex2f(255+x,284+y)
    GL.glVertex2f(233+x,279+y)
    GL.glVertex2f(250+x,260+y)
    GL.glEnd()

    ref_color = gs.Color(0.156,0.258,0.105)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_TRIANGLES)
    GL.glVertex2f(233+x,255+y)
    GL.glVertex2f(233+x,279+y)
    GL.glVertex2f(250+x,260+y)
    GL.glEnd()

    ref_color = gs.Color(0.129,0.227,0.113)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_TRIANGLES)
    GL.glVertex2f(255+x,284+y)
    GL.glVertex2f(269+x,263+y)
    GL.glVertex2f(250+x,260+y)
    GL.glEnd()

    ref_color = gs.Color(0.121,0.2,0.101)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_TRIANGLES)
    GL.glVertex2f(254+x,239+y)
    GL.glVertex2f(269+x,263+y)
    GL.glVertex2f(250+x,260+y)
    GL.glEnd()

    ref_color = gs.Color(0.219,0.372,0.164)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)
    GL.glVertex2f(233+x,255+y)
    GL.glVertex2f(250+x,260+y)
    GL.glVertex2f(254+x,239+y)
    GL.glVertex2f(225+x,248+y)
    GL.glEnd()

    ref_color = gs.Color(0.219,0.372,0.164)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)
    GL.glVertex2f(254+x,239+y)
    GL.glVertex2f(225+x,248+y)
    GL.glVertex2f(235+x,235+y)
    GL.glEnd()

    ref_color = gs.Color(0.188,0.321,0.125)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)
    GL.glVertex2f(225+x,248+y)
    GL.glVertex2f(220+x,266+y)
    GL.glVertex2f(233+x,280+y)
    GL.glVertex2f(233+x,255+y)
    GL.glEnd()

    ref_color = gs.Color(0.105,0.176,0.082)
    ref_color.color_mode(scale_option)
    ref_color.set_entity_color()

    GL.glBegin(GL.GL_POLYGON)
    GL.glVertex2f(220+x,266+y)
    GL.glVertex2f(233+x,280+y)
    GL.glVertex2f(230+x,281+y)
    GL.glEnd()


def graficar():

    GL.glClear(GL.GL_COLOR_BUFFER_BIT)
    Base()
    cerro()
    arbol(0,-10)
    piedra(70,2)
    arbol(60,10)
    arbol(34,34)
    arbol(155,10)
    arbol(115,20)
    arbol(196,20)
    oso()
    piedra(25,2)
    piedra(200,2)
    piedra(130,2)
    piedra(275,-6)
    nube(0,-35)
    nube(30,150)
    nube(-300,140)
    nube(50,-200)
    nube(-200,-180)
    nube(-350,-115)

    GL.glFlush()


def redimensionar(w, h):
    GL.glViewport(0,0,w,h)
    GL.glMatrixMode(GL.GL_PROJECTION)
    GL.glLoadIdentity()
    GL.glOrtho(0,591,550,0,-1,1)


def main(mode):

    global scale_option
    scale_option = mode

    GLUT.glutInit(sys.argv)
    GLUT.glutInitDisplayMode(GLUT.GLUT_SINGLE | GLUT.GLUT_RGB)
    GLUT.glutInitWindowSize(800, 650)
    GLUT.glutInitWindowPosition(300, 30)
    GLUT.glutCreateWindow(mode.upper())

    GL.glClearColor(0.650, 0.780, 0.8, 0)

    GL.glClear(GL.GL_COLOR_BUFFER_BIT)

    GLUT.glutDisplayFunc(graficar)
    GLUT.glutReshapeFunc(redimensionar)

    GLUT.glutMainLoop()


try:
    option = sys.argv[1]
    if len(sys.argv) > 2:
        sys.exit(1)
except:
    print("Number of Atributes Exceded - Needed [1]")
    sys.exit(1)

try:
    option = option.upper()
    option = option.lower()
except:
    sys.exit(1)

if option == "-h" or option == "help":
    print("""
    
    Color Mode's Aviable:
    [only type]
    [Mode:\t\tcomand]
    
    RGB :\t\trgb
    CMYK :\t\tcmyk
    YUV :\t\tyuv
    HSL :\t\thsl
    HSV :\t\thsv
    \n
    """)
    sys.exit(1)
else:
    pass

if option == "rgb":
    pass
elif option == "cmyk":
    pass
elif option == "yuv":
    pass
elif option == "hsl":
    pass
elif option == "hsv":
    pass
else:
    print("""
    Comand Not Aviable - Try [-h] [help]
    """)
    sys.exit(1)

main(option)