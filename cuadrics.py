import graph_data_struct as gs
import grid as gr
import quaternion as quat
import numpy as np

import math
import sys
import copy
import os

from OpenGL import GL
from OpenGL import GLU
from OpenGL import GLUT

def ellipsoid(a, b, c, step = 0.5, object_color = None):
    if object_color is None:
        object_color = gs.Color(0.0, 0.2, 0.5)
    else:
        pass

    u_step = step
    v_step = step

    ellipsoid = gs.GraphicalObject()
    ellipsoid.set_name("ellipsoid")

    u_top = 2*math.pi
    u_down = 0

    v_top = math.pi
    v_down = 0

    #coordinates: x = a cos(u) sen(v) y = b sen(u) sen(v) z = c cos(v))

    first_edge = []
    v = v_down
    for u in quat.frange(u_down, u_top, u_step):
        x_value = a * math.cos(u) * math.sin(v)
        y_value = b * math.sin(u) * math.sin(v)
        first_edge.append(gs.Point(x_value, y_value, c))

    carry_ref = first_edge[0]
    for ref_point in first_edge:
        ellipsoid.push_edge(carry_ref, ref_point, object_color)

        carry_ref = ref_point

    last_edge = []
    last_edge = first_edge

    for v in quat.frange(v_down, v_top, v_step):
        carry_edge = []
        z_value = c * math.cos(v)
        for u in quat.frange(u_down, u_top, u_step):
            x_value = a * math.cos(u) * math.sin(v)
            y_value = b * math.sin(u) * math.sin(v)
            carry_edge.append(gs.Point(x_value, y_value, z_value))

        ##SE EMPIEZA A GENERAR LOS BORDES
        carry_ref = carry_edge[0]
        index = 0
        for ref_point in carry_edge:
            ##Generan Bordes Respecto a XY
            ellipsoid.push_edge(carry_ref, ref_point, object_color)

            ##Generan Bordes respecto a Z
            ellipsoid.push_edge(carry_ref, last_edge[index], object_color)

            carry_ref = ref_point
            index += 1

        last_edge = carry_edge


    return ellipsoid

def hiperboloid_1h(a, b, c, dom, step = 0.5, object_color = None):
    if object_color is None:
        object_color = gs.Color(0.0, 0.2, 0.5)
    else:
        pass

    u_step = step
    v_step = step

    hiperboloid_1h = gs.GraphicalObject()
    hiperboloid_1h.set_name("hiperboloid")

    u_top = 2*math.pi
    u_down = 0

    v_top = dom
    v_down = -1*dom

    #hiperboloide de una hojas  x = a cos(u) cosh(v)  y = b sen(u) cosh(v) z =  c senh(v)) u = 0,2pi , v = R

    first_edge = []
    v = v_down
    o = c * math.sinh(v)
    for u in quat.frange(u_down, u_top, u_step):
        x_value = a * math.cos(u) * math.cosh(v)
        y_value = b * math.sin(u) * math.cosh(v)
        first_edge.append(gs.Point(x_value, y_value, o))

    carry_ref = first_edge[0]
    for ref_point in first_edge:
        hiperboloid_1h.push_edge(carry_ref, ref_point, object_color)

        carry_ref = ref_point

    last_edge = []
    last_edge = first_edge

    for v in quat.frange(v_down, v_top, v_step):
        carry_edge = []
        z_value = c * math.sinh(v)
        for u in quat.frange(u_down, u_top, u_step):
            x_value = a * math.cos(u) * math.cosh(v)
            y_value = b * math.sin(u) * math.cosh(v)
            carry_edge.append(gs.Point(x_value, y_value, z_value))

        ##SE EMPIEZA A GENERAR LOS BORDES
        carry_ref = carry_edge[0]
        index = 0
        for ref_point in carry_edge:
            ##Generan Bordes Respecto a XY
            hiperboloid_1h.push_edge(carry_ref, ref_point, object_color)

            ##Generan Bordes respecto a Z
            hiperboloid_1h.push_edge(carry_ref, last_edge[index], object_color)

            carry_ref = ref_point
            index += 1

        last_edge = carry_edge


    return hiperboloid_1h


def hiperboloid_2h(a, b, c, dom, step = 0.5, object_color = None):
    if object_color is None:
        object_color = gs.Color(0.0, 0.2, 0.5)
    else:
        pass

    u_step = step
    v_step = step

    hiperboloid_2h = gs.GraphicalObject()
    hiperboloid_2h.set_name("hiperboloid")

    u_top = 2*math.pi
    u_down = 0

    v_top = dom
    v_down = -1*dom

    #hiperboloide de dos hojas x = a cos(u) senh(v) y = b sen(u) senh(v) z = c cosh(v), u = 0,2pi , v = R

    ### Lado +Z
    first_edge = []
    v = v_down
    o = c * math.cosh(v)
    for u in quat.frange(u_down, u_top, u_step):
        x_value = a * math.cos(u) * math.sinh(v)
        y_value = b * math.sin(u) * math.sinh(v)
        first_edge.append(gs.Point(x_value, y_value, o))

    carry_ref = first_edge[0]
    for ref_point in first_edge:
        hiperboloid_2h.push_edge(carry_ref, ref_point, object_color)

        carry_ref = ref_point

    last_edge = []
    last_edge = first_edge

    for v in quat.frange(v_down, v_top, v_step):
        carry_edge = []
        z_value = c * math.cosh(v)
        for u in quat.frange(u_down, u_top, u_step):
            x_value = a * math.cos(u) * math.sinh(v)
            y_value = b * math.sin(u) * math.sinh(v)
            carry_edge.append(gs.Point(x_value, y_value, z_value))

        ##SE EMPIEZA A GENERAR LOS BORDES
        carry_ref = carry_edge[0]
        index = 0
        for ref_point in carry_edge:
            ##Generan Bordes Respecto a XY
            hiperboloid_2h.push_edge(carry_ref, ref_point, object_color)

            ##Generan Bordes respecto a Z
            hiperboloid_2h.push_edge(carry_ref, last_edge[index], object_color)

            carry_ref = ref_point
            index += 1

        last_edge = carry_edge


    ### Lado -Z

    first_edge = []
    v = v_down
    o = -1*c * math.cosh(v)
    for u in quat.frange(u_down, u_top, u_step):
        x_value = a * math.cos(u) * math.sinh(v)
        y_value = b * math.sin(u) * math.sinh(v)
        first_edge.append(gs.Point(x_value, y_value, o))

    carry_ref = first_edge[0]
    for ref_point in first_edge:
        hiperboloid_2h.push_edge(carry_ref, ref_point, object_color)

        carry_ref = ref_point

    last_edge = []
    last_edge = first_edge

    for v in quat.frange(v_down, v_top, v_step):
        carry_edge = []
        z_value = -1 * c * math.cosh(v)
        for u in quat.frange(u_down, u_top, u_step):
            x_value = a * math.cos(u) * math.sinh(v)
            y_value = b * math.sin(u) * math.sinh(v)
            carry_edge.append(gs.Point(x_value, y_value, z_value))

        ##SE EMPIEZA A GENERAR LOS BORDES
        carry_ref = carry_edge[0]
        index = 0
        for ref_point in carry_edge:
            ##Generan Bordes Respecto a XY
            hiperboloid_2h.push_edge(carry_ref, ref_point, object_color)

            ##Generan Bordes respecto a Z
            hiperboloid_2h.push_edge(carry_ref, last_edge[index], object_color)

            carry_ref = ref_point
            index += 1

        last_edge = carry_edge


    return hiperboloid_2h

def elliptic_paraboloid(a, b, c, dom, step = 0.5, object_color = None):
    if object_color is None:
        object_color = gs.Color(0.0, 0.2, 0.5)
    else:
        pass

    u_step = step
    v_step = step

    elliptic_paraboloid = gs.GraphicalObject()
    elliptic_paraboloid.set_name("elliptic_paraboloid")

    u_top = 2*math.pi
    u_down = 0

    v_top = dom
    v_down = 0

    #paraboloide eliptico x = a v cos(u) y = b v sen(u) z = c v²

    first_edge = []
    v = v_down
    o = c * v**2
    for u in quat.frange(u_down, u_top, u_step):
        x_value = a * math.cos(u) * v
        y_value = b * math.sin(u) * v
        first_edge.append(gs.Point(x_value, y_value, o))

    carry_ref = first_edge[0]
    for ref_point in first_edge:
        elliptic_paraboloid.push_edge(carry_ref, ref_point, object_color)

        carry_ref = ref_point

    last_edge = []
    last_edge = first_edge

    for v in quat.frange(v_down, v_top, v_step):
        carry_edge = []
        z_value = c * v ** 2
        for u in quat.frange(u_down, u_top, u_step):
            x_value = a * math.cos(u) * math.sin(v)
            y_value = b * math.sin(u) * math.sin(v)
            carry_edge.append(gs.Point(x_value, y_value, z_value))

        ##SE EMPIEZA A GENERAR LOS BORDES
        carry_ref = carry_edge[0]
        index = 0
        for ref_point in carry_edge:
            ##Generan Bordes Respecto a XY
            elliptic_paraboloid.push_edge(carry_ref, ref_point, object_color)

            ##Generan Bordes respecto a Z
            elliptic_paraboloid.push_edge(carry_ref, last_edge[index], object_color)

            carry_ref = ref_point
            index += 1

        last_edge = carry_edge


    return elliptic_paraboloid


def hyperbolic_parabolid(a, b, c, dom, step = 0.5, object_color = None):
    if object_color is None:
        object_color = gs.Color(0.0, 0.2, 0.5)
    else:
        pass

    u_step = step
    v_step = step

    hyperbolic_parabolid = gs.GraphicalObject()
    hyperbolic_parabolid.set_name("hyperbolic_parabolid")

    u_top = dom
    u_down = -1*dom

    v_top = dom
    v_down = -1*dom

    #paraboloide hiperbolico  x = a (u+v) y =  b (u− v) z = 4c uv), con D = R²
    #a    u, b    v, c(u² − v²)

    first_edge = []
    v = v_down
    for u in quat.frange(u_down, u_top, u_step):
        x_value = a*u
        y_value = b *v
        z_value = c * (u ** 2 - v ** 2)
        first_edge.append(gs.Point(x_value, y_value, z_value))

    carry_ref = first_edge[0]
    for ref_point in first_edge:
        hyperbolic_parabolid.push_edge(carry_ref, ref_point, object_color)

        carry_ref = ref_point

    last_edge = []
    last_edge = first_edge

    for v in quat.frange(v_down, v_top, v_step):
        carry_edge = []
        for u in quat.frange(u_down, u_top, u_step):
            x_value = a * u
            y_value = b * v
            z_value = c * (u ** 2 - v ** 2)
            carry_edge.append(gs.Point(x_value, y_value, z_value))

        ##SE EMPIEZA A GENERAR LOS BORDES
        carry_ref = carry_edge[0]
        index = 0
        for ref_point in carry_edge:
            ##Generan Bordes Respecto a XY
            hyperbolic_parabolid.push_edge(carry_ref, ref_point, object_color)

            ##Generan Bordes respecto a Z
            hyperbolic_parabolid.push_edge(carry_ref, last_edge[index], object_color)

            carry_ref = ref_point
            index += 1

        last_edge = carry_edge


    return hyperbolic_parabolid


def elliptic_cylinder(a, b, dom, step = 0.5, object_color = None):
    if object_color is None:
        object_color = gs.Color(0.0, 0.2, 0.5)
    else:
        pass

    u_step = step
    v_step = step

    elliptic_cylinder = gs.GraphicalObject()
    elliptic_cylinder.set_name("elliptic_cylinder")

    u_top = 2*math.pi
    u_down = 0

    v_top = dom
    v_down = -dom

    #cilindro eliptico T(u, v) = (a cos(u), b sen(u), v)

    first_edge = []
    v = v_down
    o = v
    for u in quat.frange(u_down, u_top, u_step):
        x_value = a * math.cos(u)
        y_value = b * math.sin(u)
        first_edge.append(gs.Point(x_value, y_value, o))

    carry_ref = first_edge[0]
    for ref_point in first_edge:
        elliptic_cylinder.push_edge(carry_ref, ref_point, object_color)

        carry_ref = ref_point

    last_edge = []
    last_edge = first_edge

    for v in quat.frange(v_down, v_top, v_step):
        carry_edge = []
        z_value = v
        for u in quat.frange(u_down, u_top, u_step):
            x_value = a * math.cos(u)
            y_value = b * math.sin(u)
            carry_edge.append(gs.Point(x_value, y_value, z_value))

        ##SE EMPIEZA A GENERAR LOS BORDES
        carry_ref = carry_edge[0]
        index = 0
        for ref_point in carry_edge:
            ##Generan Bordes Respecto a XY
            elliptic_cylinder.push_edge(carry_ref, ref_point, object_color)

            ##Generan Bordes respecto a Z
            elliptic_cylinder.push_edge(carry_ref, last_edge[index], object_color)

            carry_ref = ref_point
            index += 1

        last_edge = carry_edge



    return elliptic_cylinder

def hyperbolic_cylinder(a, b, dom, step = 0.5, object_color = None):
    if object_color is None:
        object_color = gs.Color(0.0, 0.2, 0.5)
    else:
        pass

    u_step = step
    v_step = step

    hyperbolic_cylinder = gs.GraphicalObject()
    hyperbolic_cylinder.set_name("hyperbolic_cylinder")

    u_top = 2*math.pi
    u_down = 0

    v_top = dom
    v_down = -dom

    #cilindro hiperbolico (a sec(u), b tg(u), v)

    first_edge = []
    v = v_down
    o = v
    for u in quat.frange(u_down, u_top, u_step):
        x_value = a * (1/math.cos(u))
        y_value = b * math.tan(u)
        first_edge.append(gs.Point(x_value, y_value, o))

    carry_ref = first_edge[0]
    for ref_point in first_edge:
        hyperbolic_cylinder.push_edge(carry_ref, ref_point, object_color)

        carry_ref = ref_point

    last_edge = []
    last_edge = first_edge

    for v in quat.frange(v_down, v_top, v_step):
        carry_edge = []
        z_value = v
        for u in quat.frange(u_down, u_top, u_step):
            x_value = a * (1/math.cos(u))
            y_value = b * math.tan(u)
            carry_edge.append(gs.Point(x_value, y_value, z_value))

        ##SE EMPIEZA A GENERAR LOS BORDES
        carry_ref = carry_edge[0]
        index = 0
        for ref_point in carry_edge:
            ##Generan Bordes Respecto a XY
            hyperbolic_cylinder.push_edge(carry_ref, ref_point, object_color)

            ##Generan Bordes respecto a Z
            hyperbolic_cylinder.push_edge(carry_ref, last_edge[index], object_color)

            carry_ref = ref_point
            index += 1

        last_edge = carry_edge



    return hyperbolic_cylinder


def parabolic_cylinder(a, dom, step = 0.5, object_color = None):
    if object_color is None:
        object_color = gs.Color(0.0, 0.2, 0.5)
    else:
        pass

    u_step = step
    v_step = step

    parabolic_cylinder = gs.GraphicalObject()
    parabolic_cylinder.set_name("parabolic_cylinder")

    u_top = dom
    u_down = -dom

    v_top = dom
    v_down = -dom

    #cilindro parabolico T(u, v) = (u, a u², v)

    first_edge = []
    v = v_down
    o = v
    for u in quat.frange(u_down, u_top, u_step):
        x_value = u
        y_value = a * u ** 2
        first_edge.append(gs.Point(x_value, y_value, o))

    carry_ref = first_edge[0]
    for ref_point in first_edge:
        parabolic_cylinder.push_edge(carry_ref, ref_point, object_color)

        carry_ref = ref_point

    last_edge = []
    last_edge = first_edge

    for v in quat.frange(v_down, v_top, v_step):
        carry_edge = []
        z_value = v
        for u in quat.frange(u_down, u_top, u_step):
            x_value = u
            y_value = a * u ** 2
            carry_edge.append(gs.Point(x_value, y_value, z_value))

        ##SE EMPIEZA A GENERAR LOS BORDES
        carry_ref = carry_edge[0]
        index = 0
        for ref_point in carry_edge:
            ##Generan Bordes Respecto a XY
            parabolic_cylinder.push_edge(carry_ref, ref_point, object_color)

            ##Generan Bordes respecto a Z
            parabolic_cylinder.push_edge(carry_ref, last_edge[index], object_color)

            carry_ref = ref_point
            index += 1

        last_edge = carry_edge


    return parabolic_cylinder