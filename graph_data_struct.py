import math
import sys
import copy
import numpy as np
import os

from OpenGL import GL
from OpenGL import GLU
from OpenGL import GLUT

import quaternion as QUAT


def to_seg(value,precs = 4):
    seg_value = (360/(2*math.pi))*value
    hour = int(seg_value)
    min_value = (seg_value - hour)*60
    min = int(min_value)
    sec = round((min_value - min)*60 , precs)

    return [hour, min, sec]

def float_to_hex(value):
    return value*255

def plot_list(list_of_objects):
    os.system("clear")

    do = True
    while do:
        print("LISTA DE OBJETOS DIBUJADOS\n\n")
        index = 0
        for graph_object in list_of_objects:
            print(graph_object.get_name(), " \t Indice[", index, "]\n")
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
            print(graph_object.get_name(), " \t Indice[", index, "]\n")
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
    R = 0.0
    G = 0.0
    B = 0.0
    id_name = ""

    def __init__(self, r=0.0, g=0.0, b=0.0):
        self.R = r
        self.G = g
        self.B = b

        self.id_name = "Void"

    def get_rgb(self):
        return [self.R, self.G, self.B]

    def get_r(self):
        return self.R

    def get_g(self):
        return self.G

    def get_b(self):
        return self.B

    def set_name(self, name):
        self.id_name = name

    def get_name(self):
        return self.id_name

    def set_entity_color(self):
        GL.glColor3f(self.R, self.G, self.B)

    def color_mode(self,type=None):
        if type is None:
            type = 'rgb'
        else:
            pass

        if type == 'rgb':
            pass

        elif type == 'cmyk':
            self.convert_cmyk()
        elif type == 'yuv':
            self.convert_yuv()
        elif type == 'hsl':
            self.convert_hsl()
        elif type == 'hsv':
            self.convert_hsv()
        else:
            print("ERROR - Modo de Color Invalido")
            pass

    def convert_cmyk(self):
        r_p = float_to_hex(self.R)/255
        g_p = float_to_hex(self.G)/255
        b_p = float_to_hex(self.B)/255

        k = 1 - max([r_p, g_p, b_p])

        if k == 1:
            c = m = y = 0
        else:
            c = (1 - r_p - k) / (1 - k)
            m = (1 - g_p - k) / (1 - k)
            y = (1 - b_p - k) / (1 - k)

        self.R = c
        self.G = m
        self.B = y

        """#SI SE DESEA VOLVER A RGB
        self.R = (1-c)*(1-k)
        self.G = (1-m)*(1-k)
        self.B = (1-y)*(1-k)
        """

    def convert_yuv(self):
        yuv_matrix = [[0.299, 0.587, 0.114],
                      [-0.147, -0.289, 0.436],
                      [0.615, -0.515, -0.100]]
        rgb_vector = [self.R, self.G, self.B]

        yuv_matrix = np.matrix(yuv_matrix)
        rgb_vector = np.matrix(rgb_vector)

        yuv_vector = yuv_matrix*rgb_vector.T

        yuv_vector = yuv_vector.T
        yuv_vector = yuv_vector.tolist()
        self.R = yuv_vector[0][0]
        self.G = yuv_vector[0][1]
        self.B = yuv_vector[0][2]

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
        r_p = float_to_hex(self.R) / 255
        g_p = float_to_hex(self.G) / 255
        b_p = float_to_hex(self.B) / 255

        max_value = max([r_p, g_p, b_p])
        min_value = min([r_p, g_p, b_p])

        if max_value == min_value:
            H = 0
        elif max_value == r_p:
            H = (60 * ((g_p - b_p)/(max_value - min_value)) +360) % 360
        elif max_value == g_p:
            H = 60 * ((b_p - r_p)/(max_value - min_value)) + 120
        elif max_value == b_p:
            H = 60 * ((r_p - g_p)/(max_value - min_value)) +240

        L = (max_value + min_value)/2

        if max_value == min_value:
            S = 0
        elif L <= 0.5:
            S = (max_value - min_value)/(2*L)
        elif L > 0.5:
            S = (max_value - min_value) / (2 - (2 * L))

        self.R = H
        self.G = S
        self.B = L

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
        r_p = float_to_hex(self.R) / 255
        g_p = float_to_hex(self.G) / 255
        b_p = float_to_hex(self.B) / 255

        max_value = max([r_p, g_p, b_p])
        min_value = min([r_p, g_p, b_p])

        if max_value == min_value:
            H = 0
        elif max_value == r_p:
            H = 60 *(((g_p - b_p) / (max_value - min_value)) % 6)
        elif max_value == g_p:
            H = 60 * (((b_p - r_p) / (max_value - min_value)) + 2)
        elif max_value == b_p:
            H = 60 * (((r_p - g_p) / (max_value - min_value)) + 4)

        if max_value == 0:
            S = 0
        else:
            S = (max_value-min_value)/max_value

        V = max_value

        self.R = H
        self.G = S
        self.B = V

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


class Point:
    x_component = 0
    y_component = 0
    z_component = 0

    it_self_name = ""

    def __init__(self, x=0, y=0, z=0):
        self.x_component = x
        self.y_component = y
        self.z_component = z

        self.it_self_name = None

    def comp_x(self):
        return self.x_component

    def comp_y(self):
        return self.y_component

    def comp_z(self):
        return self.z_component

    def get_coord(self):
        return [self.x_component, self.y_component, self.z_component]

    def get_unitary(self):
        return [self.x_component/self.norm(), self.y_component/self.norm(), self.z_component/self.norm()]

    def conjugate(self):
        self.x_component = -1 * self.x_component
        self.y_component = -1 * self.y_component
        self.z_component = -1 * self.z_component

    def set_point_name(self, name=None):
        if name is None:
            print("No Label Name Changed")
        else:
            self.it_self_name = name

    def get_point_name(self):
        if self.it_self_name is None:
            return False
        else:
            return  self.it_self_name

    def norm(self):
        return math.sqrt(self.x_component**2 + self.y_component**2 + self.z_component**2)

    def angle_x(self, reference_point = None):
        if reference_point is None:
            reference_point = Point(0, 0, 0)
        else:
            pass

        a_x = self.x_component - reference_point.comp_x()
        b_y = self.y_component - reference_point.comp_y()
        c_z = self.z_component - reference_point.comp_z()

        norm  = math.sqrt(a_x**2 + b_y**2 + c_z**2)

        return math.acos(a_x/norm)

    def angle_y(self, reference_point=None):
        if reference_point is None:
            reference_point = Point(0, 0, 0)
        else:
            pass

        a_x = self.x_component - reference_point.comp_x()
        b_y = self.y_component - reference_point.comp_y()
        c_z = self.z_component - reference_point.comp_z()

        norm = math.sqrt(a_x**2 + b_y**2 + c_z**2)

        return math.acos(b_y/norm)

    def angle_z(self, reference_point = None):
        if reference_point is None:
            reference_point = Point(0, 0, 0)
        else:
            pass

        a_x = self.x_component - reference_point.comp_x()
        b_y = self.y_component - reference_point.comp_y()
        c_z = self.z_component - reference_point.comp_z()

        norm  = math.sqrt(a_x**2 + b_y**2 + c_z**2)

        return math.acos(c_z/norm)

    def update(self, x=0, y=0, z=0):
        self.x_component = x
        self.y_component = y
        self.z_component = z


class Edge:

    point_A = None
    point_B = None
    edge_norm = 0
    color = None

    it_self_name = ""

    def __init__(self,p_a=None, p_b=None, color=None):
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

        self.it_self_name = None

        self.edge_norm = 0

    def set_edge_name(self, name=None):
        if name is None:
            print("No Label Name Changed")
        else:
            self.it_self_name = name

    def get_edge_name(self):
        if self.it_self_name is None:
            return False
        else:
            return self.it_self_name

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def dist_x(self):
        return self.point_B.comp_x() - self.point_A.comp_x()

    def dist_y(self):
        return self.point_B.comp_y() - self.point_A.comp_y()

    def dist_z(self):
        return self.point_B.comp_z() - self.point_A.comp_z()

    def norm(self):

        self.edge_norm = math.sqrt(self.dist_x()**2 + self.dist_y()**2 + self.dist_z()**2)

        return self.edge_norm

    def angle_x(self):
        return math.acos(self.dist_x()/self.norm())

    def angle_y(self):
        return math.acos(self.dist_y() / self.norm())

    def angle_z(self):
        return math.acos(self.dist_z() / self.norm())

    def get_point_a(self):
        return self.point_A

    def get_point_b(self):
        return self.point_B

class GraphicalObject:

    point_collection = {}
    edge_collection = {}

    point_set = []

    last_point_index = 0
    last_edge_index = 0

    center = None

    precs = 3

    name = ""

    visible = False

    def __init__(self):
        self.point_set = set(self.point_set)
        self.last_point_index = 0
        self.last_edge_index = 0
        self.center = Point(0, 0, 0)

        self.point_collection = {}
        self.edge_collection = {}

        self.precs = 3

        self.name = "Void"
        self.visible = False
################################################################

    def set_precs(self, precs):
        self.precs = precs

    def get_precs(self):
        return self.precs

################################################################

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

################################################################
    def update_last_point_index(self):
        self.last_point_index += 1

    def last_point_name(self):
        self.update_last_point_index()
        return "p_" + str(self.last_point_index - 1)

###*********************************************************###

    def update_last_edge_index(self):
        self.last_edge_index += 1

    def last_edge_name(self):
        self.update_last_edge_index()
        return "e_" + str(self.last_edge_index - 1)

################################################################

    def show(self):
        self.visible = True

    def hide(self):
        self.visible = False

    def is_visible(self):
        return self.visible

################################################################

    def update_center(self):
        auxiliar_list = list(self.point_set)

        num_of_points = len(auxiliar_list)

        x_carry = 0
        y_carry = 0
        z_carry = 0

        for point_ref in auxiliar_list:
            x_carry += point_ref.comp_x()
            y_carry += point_ref.comp_y()
            z_carry += point_ref.comp_z()

        x_carry = round(x_carry / num_of_points, self.precs)
        y_carry = round(y_carry / num_of_points, self.precs)
        z_carry = round(z_carry / num_of_points, self.precs)

        self.center.update(x_carry, y_carry, z_carry)

    def get_center(self):
        return self.center

################################################################

    def push_point(self, ref_point = Point(0,0,0),name = None):
        if name is None:
            name = self.last_point_name()
        else:
            pass

        if ref_point.get_point_name() is None:
            name = self.last_edge_name()
        else:
            name = ref_point.get_point_name()

        ref_point.set_point_name(name)

        self.point_collection[name] = ref_point
        self.point_set.add(ref_point)

        print("\nPoint:\t(", ref_point.comp_x(), ",", ref_point.comp_y(), ",", ref_point.comp_z(), ") Add-ed /=/ Name:\t", name, "\n")

################################################################

    def get_point(self,name):
        return self.point_collection[name]

################################################################

    def push_edge(self, point_1, point_2, color=None, name=None, verbose=False):

        try:
            self.point_collection[point_1.get_point_name()]
        except:
            if verbose:
                print("\nError - No Point with name ", point_1.get_point_name())

            point_1.set_point_name(self.last_point_name())
            self.point_collection[point_1.get_point_name()] = point_1
            self.point_set.add(point_1)

            if verbose:
                print("\nCreate Point ", point_1.get_point_name())

            if verbose:
                print(self.last_point_index)

        try:
            self.point_collection[point_2.get_point_name()]
        except:
            if verbose:
                print("\nError - No Point with name ", point_2.get_point_name())

            point_2.set_point_name(self.last_point_name())
            self.point_collection[point_2.get_point_name()] = point_2
            self.point_set.add(point_2)

            if verbose:
                print("\n Create Point ", point_2.get_point_name())
                print(self.last_point_index)

        if name is None:
            name = self.last_edge_name()
        else:
            pass

        ref_edge = Edge(point_1, point_2, color)
        ref_edge.set_edge_name(name)
        self.edge_collection[name] = ref_edge

################################################################

    def init(self):
        pass

    def plot(self, gl_context=GL):
        if self.visible:
            pass
        else:
            return None

        gl_context.glBegin(GL.GL_LINES)
        for edge_name, edge_ref in self.edge_collection.items():

            color = edge_ref.get_color()

            gl_context.glColor3f(color.get_r(), color.get_g(), color.get_b())

            gl_context.glVertex3f(edge_ref.get_point_a().comp_x(), edge_ref.get_point_a().comp_y(), edge_ref.get_point_a().comp_z())
            gl_context.glVertex3f(edge_ref.get_point_b().comp_x(), edge_ref.get_point_b().comp_y(), edge_ref.get_point_b().comp_z())

        gl_context.glEnd()

################################################################

    def rotate(self, angle=0, vector=None, its_unitary=False, sign="+", verbose=False):
        if vector is None:
            self.update_center()
            vector = self.center.get_coord()
        else:
            pass

        for point_ref in list(self.point_set):
            carry_coord = QUAT.rotate(point_ref.get_coord(), vector, angle, sign, its_unitary, verbose)
            point_ref.update(carry_coord[0], carry_coord[1], carry_coord[2])

    def scale(self, gen_fact=1, fact_vector=[1, 1, 1]):
        if gen_fact is None:
            pass
        else:
            fact_vector = [gen_fact, gen_fact, gen_fact]

        for label_ref, point_ref in self.point_collection.items():
            carry_coord = point_ref.get_coord()
            point_ref.update(carry_coord[0]*fact_vector[0], carry_coord[1]*fact_vector[1], carry_coord[2]*fact_vector[2])

    def translate(self, move_point=None):
        if move_point is None:
            self.update_center()
            move_point_vector = self.get_center().get_coord()

            move_point_vector[0] = -1 * move_point_vector[0]
            move_point_vector[1] = -1 * move_point_vector[1]
            move_point_vector[2] = -1 * move_point_vector[2]

        else:
            move_point_vector = move_point.get_coord()

        for point_ref in list(self.point_set):
            carry_coord = point_ref.get_coord()
            point_ref.update(carry_coord[0]+move_point_vector[0], carry_coord[1]+move_point_vector[1],
                             carry_coord[2]+move_point_vector[2])


################################################################

    def show_points(self):
        for point_ref in list(self.point_set):
            print("\tPoint:\t",point_ref.get_point_name()," at (", point_ref.comp_x(), " ,",
                  point_ref.comp_y(), " ,", point_ref.comp_z(), ")")


    def show_edges(self):
        sorted(self.edge_collection)
        for edge_name, edge_ref in self.edge_collection.items():
            print("\tEdge:\t", edge_ref.get_edge_name(), " between ", edge_ref.get_point_a().get_point_name(),
                  " and ", edge_ref.get_point_b().get_point_name() + " , Color: ", edge_ref.color.get_rgb())

#################################################################

    def get_edge_collection(self):
        return self.edge_collection
