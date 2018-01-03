import copy
import math
import os

import numpy as np
from OpenGL import GL
from OpenGL import GLU

import libg2f.Morphing as MO
import libg2f.Quaternion as QUAT


def to_seg(value, precision=4):
    seg_value = (360 / (2 * math.pi)) * value
    hour = int(seg_value)
    min_value = (seg_value - hour) * 60
    min = int(min_value)
    sec = round((min_value - min) * 60, precision)

    return [hour, min, sec]


def float_to_hex(value):
    return value * 255


def plot_list(list_of_objects):
    os.system("clear")

    do = True
    while do:
        print("LISTA DE OBJETOS DIBUJADOS\n\n")
        index = 0
        for graph_object in list_of_objects:
            print(graph_object.get_color_name(), " \t Indice[", index, "]\n")
            index += 1
        print("\n\n[-1] Omitir\t")
        index = input("""
        \n Si el Objeto es Visible , se oculta
        Si esta  oculto, se hace visible
        Opcion >>>:\t

        """)

        try:
            index = int(index)

            if index >= len(list_of_objects):
                return None
            else:
                pass
        except:
            return None

        if index == -1:
            do = False
            pass
        else:
            who_object = list_of_objects[index]

            if who_object.is_visible():
                who_object.hide()
            else:
                who_object.show()

    for ref_object in list_of_objects:
        ref_object.plot()


def control(list_of_objects, glu_context=GLU):
    os.system("clear")

    print("LISTA DE OBJETOS DIBUJADOS\n\n")
    index = 0
    exist = False
    for graph_object in list_of_objects:
        if graph_object.is_visible():
            print(graph_object.get_color_name(), " \t Indice[", index, "]\n")
            exist = True
        else:
            pass
        index += 1

    index = input("Opcion >>>:\t")

    if exist:
        pass
    else:
        return None

    try:
        index = int(index)

        if index >= len(list_of_objects):
            return None
        else:
            pass
    except:
        return None

    who_object = list_of_objects[index]

    option = input("""
        [1]Rotar - Sobre si mismo
        [2]Rotar - Respecto a un Vector
        [3]Escalar
        [4]Trasladar
        [9]CAMARA
        """)

    try:
        option = int(option)
    except:
        return None

    if option == 1:
        option = input("""
            [1]X
            [2]Y
            [3]Z
            """)
        try:
            option = int(option)
        except:
            return None

        who_object.update_center()
        ref_center = copy.copy(who_object.get_center())

        angle = input("Angulo >>>:\t")

        try:
            angle = float(angle)
        except:
            return None

        if option == 1:
            who_object.translate()
            who_object.rotate(angle, "x", True)
            who_object.translate(ref_center)
        elif option == 2:
            who_object.translate()
            who_object.rotate(angle, "y", True)
            who_object.translate(ref_center)
        elif option == 3:
            who_object.translate()
            who_object.rotate(angle, "z", True)
            who_object.translate(ref_center)
        else:
            return None

    elif option == 2:
        option = input("""
            [1]X
            [2]Y
            [3]Z
            [4]Otro
            """)
        try:
            option = int(option)
        except:
            return None

        angle = input("Angulo >>>:\t")

        try:
            angle = float(angle)
        except:
            return None

        if option == 1:
            who_object.rotate(angle, "x", True)
        elif option == 2:
            who_object.rotate(angle, "y", True)
        elif option == 3:
            who_object.rotate(angle, "z", True)
        elif option == 4:
            vector = eval(input("Vector >>>:\t"))
            try:
                vector[0]
            except:
                return None

            who_object.rotate(angle, vector)

        else:
            return None

    elif option == 3:
        escala = eval(input("Escala >>>:\t"))
        try:
            escala = list(escala)
        except:
            return None

        who_object.scale(None, escala)
    elif option == 4:
        to_point = eval(input("Punto >>>:\t"))
        try:
            to_point == list(to_point)
        except:
            return None

        who_object.translate(Point(to_point[0], to_point[1], to_point[2]))

    else:
        return None
    """
        elif option == 9:
            to_point = eval(input("Punto >>>:\t"))
            try:
                to_point == list(to_point)
            except:
                return None

            glu_context.gluLookAt(to_point[0], to_point[1], to_point[2], 0, 0, 0, 0, 1, 0)
        """


class Color:
    r = 0.0
    g = 0.0
    b = 0.0
    color_name = ""

    def __init__(self, r=0.0, g=0.0, b=0.0):
        self.r = r
        self.g = g
        self.b = b

        self.color_name = ""

    def get_rgb(self):
        return [self.r, self.g, self.b]

    def get_r(self):
        return self.r

    def get_g(self):
        return self.g

    def get_b(self):
        return self.b

    def set_color(self, color):
        self.r = color[0]
        self.g = color[1]
        self.b = color[2]

    def set_color_name(self, name):
        self.color_name = name

    def get_color_name(self):
        return self.color_name

    def set_entity_color(self, gl_context=GL):
        gl_context.glColor3f(self.r, self.g, self.b)

    def color_mode(self, color_mode=None):
        if color_mode is None:
            color_mode = 'rgb'
        else:
            pass

        if color_mode == 'rgb':
            pass
        elif color_mode == 'cmyk':
            self.convert_cmyk()
        elif color_mode == 'yuv':
            self.convert_yuv()
        elif color_mode == 'hsl':
            self.convert_hsl()
        elif color_mode == 'hsv':
            self.convert_hsv()
        else:
            print("ERROR - Invalid Color Mode")
            pass

    def convert_cmyk(self):
        r_p = float_to_hex(self.r) / 255
        g_p = float_to_hex(self.g) / 255
        b_p = float_to_hex(self.b) / 255

        k = 1 - max([r_p, g_p, b_p])

        if k == 1:
            c = m = y = 0
        else:
            c = (1 - r_p - k) / (1 - k)
            m = (1 - g_p - k) / (1 - k)
            y = (1 - b_p - k) / (1 - k)

        self.r = c
        self.g = m
        self.b = y

        """#SI SE DESEA VOLVER A RGB
        self.R = (1-c)*(1-k)
        self.G = (1-m)*(1-k)
        self.B = (1-y)*(1-k)
        """

    def convert_yuv(self):
        yuv_matrix = [[0.299, 0.587, 0.114],
                      [-0.147, -0.289, 0.436],
                      [0.615, -0.515, -0.100]]
        rgb_vector = [self.r, self.g, self.b]

        yuv_matrix = np.matrix(yuv_matrix)
        rgb_vector = np.matrix(rgb_vector)

        yuv_vector = yuv_matrix * rgb_vector.T

        yuv_vector = yuv_vector.T
        yuv_vector = yuv_vector.tolist()
        self.r = yuv_vector[0][0]
        self.g = yuv_vector[0][1]
        self.b = yuv_vector[0][2]

        """#SI SE DESEA VOLVER A RGB
        rgb_matrix = [[1, 0, 1.14],
                      [1, -0.396, -0.581],
                      [1, 2.029, 0]]
        rgb_matrix = np.matrix(rgb_matrix)
        yuv_vector = np.matrix(yuv_vector[0])
        yuv_vector = yuv_vector.T

        rgb_vector = rgb_matrix*yuv_vector
        rgb_vector = rgb_vector.T
        rgb_vector = rgb_vector.tolist()

        self.R = rgb_vector[0][0]
        self.G = rgb_vector[0][1]
        self.B = rgb_vector[0][2]
        """

    def convert_hsl(self):
        r_p = float_to_hex(self.r) / 255
        g_p = float_to_hex(self.g) / 255
        b_p = float_to_hex(self.b) / 255

        max_value = max([r_p, g_p, b_p])
        min_value = min([r_p, g_p, b_p])

        if max_value == min_value:
            H = 0
        elif max_value == r_p:
            H = (60 * ((g_p - b_p) / (max_value - min_value)) + 360) % 360
        elif max_value == g_p:
            H = 60 * ((b_p - r_p) / (max_value - min_value)) + 120
        elif max_value == b_p:
            H = 60 * ((r_p - g_p) / (max_value - min_value)) + 240

        L = (max_value + min_value) / 2

        if max_value == min_value:
            S = 0
        elif L <= 0.5:
            S = (max_value - min_value) / (2 * L)
        elif L > 0.5:
            S = (max_value - min_value) / (2 - (2 * L))

        self.r = H
        self.g = S
        self.b = L

        """#SI SE DESEA VOLVER A RGB
        C = (1 - math.fabs(2*L - 1)) * S
        X = C*(1 - math.fabs((H / 60) % 2 - 1))
        m = L - C / 2

        if 0 <= H and H < 60:
            self.R = C + m
            self.G = X + m
            self.B = 0 + m
        elif 60 <= H and H < 120:
            self.R = X + m
            self.G = C + m
            self.B = 0 + m
        elif 120 <= H and H < 180:
            self.R = 0 + m
            self.G = C + m
            self.B = X + m
        elif 180 <= H and H < 240:
            self.R = 0 + m
            self.G = X + m
            self.B = C + m
        elif 240 <= H and H < 300:
            self.R = X + m
            self.G = 0 + m
            self.B = C + m
        elif 300 <= H and H < 360:
            self.R = C + m
            self.G = 0 + m
            self.B = X + m
        """

    def convert_hsv(self):
        r_p = float_to_hex(self.r) / 255
        g_p = float_to_hex(self.g) / 255
        b_p = float_to_hex(self.b) / 255

        max_value = max([r_p, g_p, b_p])
        min_value = min([r_p, g_p, b_p])

        if max_value == min_value:
            H = 0
        elif max_value == r_p:
            H = 60 * (((g_p - b_p) / (max_value - min_value)) % 6)
        elif max_value == g_p:
            H = 60 * (((b_p - r_p) / (max_value - min_value)) + 2)
        elif max_value == b_p:
            H = 60 * (((r_p - g_p) / (max_value - min_value)) + 4)

        if max_value == 0:
            S = 0
        else:
            S = (max_value - min_value) / max_value

        V = max_value

        self.r = H
        self.g = S
        self.b = V

        """#SI SE DESEA VOLVER A RGB
        C = V * S
        X = C*(1 - math.fabs((H / 60) % 2 - 1))
        m = V - C

        if 0 <= H and H < 60:
            self.R = C + m
            self.G = X + m
            self.B = 0 + m
        elif 60 <= H and H < 120:
            self.R = X + m
            self.G = C + m
            self.B = 0 + m
        elif 120 <= H and H < 180:
            self.R = 0 + m
            self.G = C + m
            self.B = X + m
        elif 180 <= H and H < 240:
            self.R = 0 + m
            self.G = X + m
            self.B = C + m
        elif 240 <= H and H < 300:
            self.R = X + m
            self.G = 0 + m
            self.B = C + m
        elif 300 <= H and H < 360:
            self.R = C + m
            self.G = 0 + m
            self.B = X + m
        """

    def __hash__(self):
        return hash(str(self.r) + str(self.g) + str(self.b) + str(self.color_name))

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __str__(self):
        carry = "\nColor Name\t" + str(self.color_name) + "\tR\t" + str(self.r) + "\tG\t" +\
                str(self.g) + "\tB\t" + str(self.b)
        return carry


class ColorSet:
    def __init__(self):
        self.internal_set = set([])

    def push(self, ref_color):
        try:
            ref_color.get_color_name()

            if ref_color in self.internal_set:
                carry = list(self.internal_set)
                return carry[carry.index(ref_color)]
            else:
                self.internal_set.add(ref_color)
                return ref_color
        except:
            return None

    def get_set(self):
        return self.internal_set

    def get_set_list(self):
        return list(self.internal_set)

    def __str__(self):
        carry = ""
        for i in self:
            carry += i

        return carry


class Point:
    x_component = 0
    y_component = 0
    z_component = 0

    point_name = ""
    queried_state = False

    def __init__(self, x=0, y=0, z=0):
        self.x_component = x
        self.y_component = y
        self.z_component = z

        self.queried_state = False
        self.point_name = None

    def get_x(self):
        return self.x_component

    def get_y(self):
        return self.y_component

    def get_z(self):
        return self.z_component

    def get_queried_state(self):
        return self.queried_state

    def set_queried_state(self, flag):
        self.queried_state = flag

    def get_coord(self):
        return [self.x_component, self.y_component, self.z_component]

    def get_unitary(self, ref_point=None):
        if ref_point is None:
            ref_point = Point()
        else:
            pass

        norm = self.norm(ref_point)

        if norm != 0:
            return [self.distance_x(ref_point) / norm,
                    self.distance_y(ref_point) / norm,
                    self.distance_z(ref_point) / norm]
        else:
            return [0, 0, 0]

    def conjugate(self):
        self.x_component = -1 * self.x_component
        self.y_component = -1 * self.y_component
        self.z_component = -1 * self.z_component

    def set_coord(self, coord):
        self.x_component = coord[0]
        self.y_component = coord[1]
        self.z_component = coord[2]

    def set_point_name(self, name=None):
        if name is None:
            print("No Label Name Changed")
        else:
            self.point_name = name

    def get_point_name(self, mode=0):
        if self.point_name is None:
            return False
        else:
            if mode == 0:
                return int(self.point_name)
            else:
                return self.point_name

    def norm(self, ref_point=None):
        if ref_point is None:
            ref_point = Point()
        else:
            pass

        return math.sqrt(self.distance_x(ref_point) ** 2 +
                         self.distance_y(ref_point) ** 2 +
                         self.distance_z(ref_point) ** 2)

    def distance_x(self, reference_point=None):
        return reference_point.get_x() - self.x_component

    def distance_y(self, reference_point=None):
        return reference_point.get_y() - self.y_component

    def distance_z(self, reference_point=None):
        return reference_point.get_z() - self.z_component

    def angle_x(self, reference_point=None):
        if reference_point is None:
            reference_point = Point()
        else:
            pass

        return math.acos(self.distance_x(reference_point) / self.norm(reference_point))

    def angle_y(self, reference_point=None):
        if reference_point is None:
            reference_point = Point()
        else:
            pass

        return math.acos(self.distance_y(reference_point) / self.norm(reference_point))

    def angle_z(self, reference_point=None):
        if reference_point is None:
            reference_point = Point()
        else:
            pass

        return math.acos(self.distance_z(reference_point) / self.norm(reference_point))

    def step_to_point(self, reference_point, step):
        self.step_x = self.x_component
        self.step_y = self.y_component
        self.step_z = self.z_component

        self.x_component = self.x_component + step * self.distance_x(reference_point)
        self.y_component = self.y_component + step * self.distance_y(reference_point)
        self.z_component = self.z_component + step * self.distance_z(reference_point)

    def step_return(self):
        self.x_component = self.step_x
        self.y_component = self.step_y
        self.z_component = self.step_z

    def set_entity_vertex(self, gl_context=GL):
        gl_context.glVertex3f(self.x_component, self.y_component, self.z_component)

    def get_relative_normal(self, point0, pointf):
        carry_coords = np.cross(self.get_unitary(point0), pointf.get_unitary(pointf))
        carry_point = Point()
        carry_point.set_coord(carry_coords)
        return carry_point.get_unitary()


    def __hash__(self):
        return hash(str(self.x_component) + str(self.y_component) + str(self.z_component) + str(self.point_name))

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __str__(self):
        carry = "\nPoint Name\t" + str(self.point_name) + "\tX\t" + str(self.x_component) +\
                "\tY\t" + str(self.y_component) + "\tZ\t" + str(self.z_component)
        return carry


class PointSet:
    def __init__(self):
        self.internal_set = set([])
        #self.internal_set = []

    def push(self, ref_point):
        if ref_point in self.internal_set:
            carry = list(self.internal_set)
            return carry[carry.index(ref_point)]
        else:
            self.internal_set.add(ref_point)
            return ref_point
        """
        self.internal_set.append(ref_point)
        return ref_point
        """
    def get_set(self):
        return self.internal_set

    def get_set_list(self):
        return list(self.internal_set)

    def __str__(self):
        carry = ""
        for i in self:
            carry += i
        return carry


class Edge:
    point_A = None
    point_B = None
    edge_norm = 0
    color = None

    edge_name = ""

    def __init__(self, p_a=None, p_b=None, color=None, name=None):
        if p_a is None:
            p_a = Point(0, 0, 0)
        else:
            pass
        if p_b is None:
            p_b = Point(0, 0, 0)
        else:
            pass
        if color is None:
            color = Color()
        else:
            pass

        self.point_A = p_a
        self.point_B = p_b

        self.color = color

        self.edge_name = name

        self.edge_norm = 0

        self.norm()

    def set_edge_name(self, name=None):
        if name is None:
            print("No Label Name Changed")
        else:
            self.edge_name = name

    def get_edge_name(self):
        if self.edge_name is None:
            return False
        else:
            return self.edge_name

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def dist_x(self):
        return self.point_B.distance_x(self.point_A)

    def dist_y(self):
        return self.point_B.distance_y(self.point_A)

    def dist_z(self):
        return self.point_B.distance_z(self.point_A)

    def norm(self):
        self.edge_norm = self.point_B.norm(self.point_A)

    def get_norm(self):
        return self.edge_norm

    def unitary(self):
        return self.point_B.get_unitary(self.point_A)

    def angle_x(self):
        return self.point_B.angle_x(self.point_A)

    def angle_y(self):
        return self.point_B.angle_y(self.point_A)

    def angle_z(self):
        return self.point_B.angle_z(self.point_A)

    def get_point_a(self):
        return self.point_A

    def get_point_b(self):
        return self.point_B

    def __hash__(self):
        return hash(str(self.point_A) + str(self.point_B) + str(self.edge_norm) + str(self.color) + str(self.edge_name))

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __str__(self):
        carry = "\nName\t" + str(self.edge_name) + "\tPoint A\t" + str(self.point_A) + "\tPoint B\t" +\
                str(self.point_B) + "\tColor\t" + str(self.color)
        return carry


class EdgeSet:
    def __init__(self):
        self.internal_set = set([])
        #self.internal_set = []

    def push(self, ref_edge):
        if ref_edge in self.internal_set:
            carry = list(self.internal_set)
            return carry[carry.index(ref_edge)]
        else:
            self.internal_set.add(ref_edge)
            return ref_edge
        """
        self.internal_set.append(ref_edge)
        return ref_edge
        """
    def get_set(self):
        return self.internal_set

    def get_set_list(self):
        return list(self.internal_set)

    def __str__(self):
        carry = ""
        for i in self:
            carry += i

        return carry


class GraphicalObject:
    point_set_collection = []
    edge_set_collection = []
    faces_set_collection = []

    center = None

    precision = 3

    graphical_object_name = ""

    visible = False

    def __init__(self):
        self.center = Point()

        self.point_set_collection = []
        self.edge_set_collection = []
        self.precision = 3

        self.graphical_object_name = ""
        self.visible = False

        self.faces_set_collection = []

    def set_precision(self, precision):
        self.precision = precision

    def get_precision(self):
        return self.precision

    def set_name(self, new_name):
        self.graphical_object_name = new_name

    def get_name(self):
        return self.graphical_object_name

    def show(self):
        self.visible = True

    def hide(self):
        self.visible = False

    def is_visible(self):
        return self.visible

    def __update_center(self):
        auxiliary_list = self.point_set_collection

        num_of_points = len(auxiliary_list)

        x_carry = 0
        y_carry = 0
        z_carry = 0

        for point_ref in auxiliary_list:
            x_carry += point_ref.get_x()
            y_carry += point_ref.get_y()
            z_carry += point_ref.get_z()

        x_carry = round(x_carry / num_of_points, self.precision)
        y_carry = round(y_carry / num_of_points, self.precision)
        z_carry = round(z_carry / num_of_points, self.precision)

        self.center.set_coord([x_carry, y_carry, z_carry])

    def get_center(self):
        self.__update_center()
        return self.center

    def push_point(self, coords, index):
        carry = Point(coords[0], coords[1], coords[2])
        carry.set_point_name(str(index))
        self.point_set_collection.append(carry)

    def push_edge(self, ref_point_1, ref_point_2, color=None, name=None, verbose=False):
        self.edge_set_collection.append(Edge(self.point_set_collection[ref_point_1],
                                           self.point_set_collection[ref_point_2],
                                           color,
                                           name))
        if verbose:
            print("\nEdge\n\tPuntos")
            print("\t", self.point_set_collection.push(point_1))
            print("\t", self.point_set_collection.push(point_2))

    def init(self):
        pass

    def plot(self, gl_context=GL):
        if self.visible:
            pass
        else:
            return None

        if len(self.faces_set_collection) is not 0:
            self.plot_faces(None, gl_context)
        else:
            pass

        gl_context.glBegin(GL.GL_LINES)

        for edge_ref in self.edge_set_collection:
            color = edge_ref.get_color()

            gl_context.glColor3f(color.get_r(), color.get_g(), color.get_b())

            gl_context.glVertex3f(edge_ref.get_point_a().get_x(), edge_ref.get_point_a().get_y(),
                                  edge_ref.get_point_a().get_z())
            gl_context.glVertex3f(edge_ref.get_point_b().get_x(), edge_ref.get_point_b().get_y(),
                                  edge_ref.get_point_b().get_z())

        gl_context.glEnd()

    def rotate(self, angle=0, vector=None, its_unitary=False, sign="+", verbose=False):
        if vector is None:
            vector = self.get_center()
        else:
            pass

        for point_ref in self.point_set_collection:
            carry_coord = QUAT.rotate(point_ref.get_coord(), vector, angle, sign, its_unitary, verbose)
            point_ref.set_coord(carry_coord)

    def scale(self, gen_fact=1, fact_vector=[1, 1, 1]):
        if gen_fact is None:
            pass
        else:
            fact_vector = [gen_fact, gen_fact, gen_fact]

        for point_ref in self.point_set_collection:
            point_ref.set_coord([point_ref.get_x() * fact_vector[0],
                                 point_ref.get_y() * fact_vector[1],
                                 point_ref.get_z() * fact_vector[2]])

    def translate(self, move_point=None):
        if move_point is None:
            move_point = self.get_center()
            move_point.conjugate()
        else:
            pass

        for point_ref in self.point_set_collection:
            point_ref.set_coord([point_ref.get_x() + move_point.get_x(),
                                 point_ref.get_y() + move_point.get_y(),
                                 point_ref.get_z() + move_point.get_z()])

    def show_points(self,mode=0):
        if mode==0:
            print("Number of Points\t", len(self.point_set_collection))
        else:
            print("Number of Points\t", len(self.point_set_collection))
            for point_ref in self.point_set_collection:
                print(point_ref)

    def show_edges(self, mode=0):
        if mode==0:
            print("Number of Edges\t", len(self.edge_set_collection))
        else:
            print("Number of Edges\t", len(self.edge_set_collection))
            for edge_ref in self.edge_set_collection:
                print(edge_ref)

    def get_edge_collection(self):
        return self.edge_set_collection

    def on_self_rotate_x(self, step, sign):
        ref_center = copy.copy(self.get_center())
        self.translate()
        self.rotate(step, "x", True, sign)
        self.translate(ref_center)

    def on_self_rotate_y(self, step, sign):
        ref_center = copy.copy(self.get_center())
        self.translate()
        self.rotate(step, "y", True, sign)
        self.translate(ref_center)

    def on_self_rotate_z(self, step, sign):
        ref_center = copy.copy(self.get_center())
        self.translate()
        self.rotate(step, "z", True, sign)
        self.translate(ref_center)

    def get_point_by_index(self, index):
        return self.point_set_collection[index]

    def relate_objects(self, objective_object):
        self.relational_index_list = MO.Relate_Objects(self, objective_object)

    def morph(self, objective_object, step, precs=2, start=False):
        if start:
            self.relate_objects(objective_object)
            self.indicator_step = 0
            return None
        else:
            if self.indicator_step == 1:
                self.indicator_step = 0
            else:
                self.indicator_step = round(self.indicator_step + step, precs)

        print(self.indicator_step)
        for morph_pair in self.relational_index_list:
            self.point_set_collection[morph_pair[0]].step_to_point(objective_object.get_point_by_index(morph_pair[1]),
                                                                   self.indicator_step)

        self.plot()

        for point_ref in self.point_set_collection:
            point_ref.step_return()

    def push_face(self, index_list):
        self.faces_set_collection.append(index_list)

    def plot_faces(self, color=None, gl_context=GL):
        if color is None:
            color = Color(248/255, 150/225, 92/225)
        else:
            pass
        for face in self.faces_set_collection:

            #gl_context.glEnable(gl_context.GL_COLOR_MATERIAL)

            #gl_context.glColorMaterial(gl_context.GL_FRONT_AND_BACK, gl_context.GL_AMBIENT_AND_DIFFUSE)

            #gl_context.glMaterial(gl_context.GL_FRONT_AND_BACK, gl_context.GL_AMBIENT_AND_DIFFUSE, 0.7)

            gl_context.glPolygonMode(gl_context.GL_FRONT_AND_BACK, gl_context.GL_FILL)

            gl_context.glBegin(gl_context.GL_POLYGON)
            color.set_entity_color(gl_context)

            for vertex in face:

                self.get_point_by_index(vertex).set_entity_vertex(gl_context)

            gl_context.glEnd()

            #gl_context.glDisable(gl_context.GL_COLOR_MATERIAL)

    def __str__(self):
        return self.graphical_object_name