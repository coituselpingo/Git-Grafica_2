import bresenham3d as br
import quaternion as qd
import graph_data_struct as gs
import grid as gr
import quaternion as QUAT
import OpenGL.GL as GL
import OpenGL.GLU as GLU
import OpenGL.GLUT as GLUT

import sys
import copy
import numpy as np


def set_color(data_color):
    GL.glColor(data_color[0], data_color[1], data_color[2])


def set_vertex(data_array):
    GL.glVertex3f(data_array[0], data_array[1], data_array[2])


def plot_face(data_face):
    for ref in data_face:
        GL.glBegin(GL.GL_LINES)
        set_vertex(ref[0])
        set_vertex(ref[1])
        set_vertex(ref[2])
        set_vertex(ref[3])
        GL.glEnd()

        GL.glPolygonMode(GL.GL_FRONT_AND_BACK, GL.GL_FILL)
        set_color(ref[4])
        GL.glBegin(GL.GL_POLYGON)
        set_vertex(ref[0])
        set_vertex(ref[1])
        set_vertex(ref[2])
        set_vertex(ref[3])
        GL.glEnd()


def plot_matrix_of_cubes(data):
    for i in range(0, 3):
        for j in range(0, 3):
            for k in range(0, 3):
                plot_face(data[i][j][k])


def inspect_matrix_of_cubes(data):
    for i in range(0, 3):
        for j in range(0, 3):
            for k in range(0, 3):
                print(i, j, k, "\t")
                for face in data[i][j][k]:
                    m = face
                    print(m[0], m[1], m[2], m[3], m[4])
                print("********************")


def get_side_center(side_format, len):

    center = [0, 0, 0]

    for index in range(0, 3):
        if side_format[index] == 0:
            center[index] += (len**2)/2
        else:
            center[index] += len*side_format[index] + len/2

    print(center)
    return center


def translate_side(data_side, point, inverse=True):
    if inverse:
        point = [-1*point[0], -1*point[1], -1*point[2]]
    else:
        pass

    for i in range(0, 3):
        for j in range(0, 3):
            for face in data_side[i][j]:
                for vertex in face[0:4]:
                    vertex[0] += point[0]

                    vertex[1] += point[1]

                    vertex[2] += point[2]


def rotate_side(side, angle, eje):
    for i in range(0, 3):
        for j in range(0, 3):
            for face in side[i][j]:
                index = 0
                for vertex in face[0:4]:
                    face[index] = QUAT.rotate(vertex, eje, angle)
                    index += 1


def cube_side_rotate(side, ref, giro, format, len):

    if ref == "i":
        if giro == "+":
            carry_center = get_side_center(format, len)
            translate_side(side, carry_center)
            rotate_side(side, 90, "x")
            translate_side(side, carry_center, inverse=False)
        elif giro == "-":
            carry_center = get_side_center(format, len)
            translate_side(side, carry_center)
            rotate_side(side, -90, "x")
            translate_side(side, carry_center, inverse=False)
        else:
            pass

    if ref == "j":
        if giro == "+":
            carry_center = get_side_center(format, len)
            translate_side(side, carry_center)
            rotate_side(side, 90, "z")
            translate_side(side, carry_center, inverse=False)
        elif giro == "-":
            carry_center = get_side_center(format, len)
            translate_side(side, carry_center)
            rotate_side(side, -90, "z")
            translate_side(side, carry_center, inverse=False)
        else:
            pass

    if ref == "k":
        if giro == "+":
            carry_center = get_side_center(format, len)
            translate_side(side, carry_center)
            rotate_side(side, 90, "z")
            translate_side(side, carry_center, inverse=False)
        elif giro == "-":
            carry_center = get_side_center(format, len)
            translate_side(side, carry_center)
            rotate_side(side, -90, "z")
            translate_side(side, carry_center, inverse=False)
        else:
            pass


def matrix_90_rotate(matrix, giro):
    if giro == "+":
        carry_matrix = [[[], [], []],
                        [[], [], []],
                        [[], [], []]]
        for j in range(0, 3):
            for i in range(0, 3):
                carry_matrix[2-j][i]= matrix[i][j]

        for i in range(0, 3):
            for j in range(0, 3):
                matrix[i][j] = carry_matrix[i][j]

    elif giro == "-":
        carry_matrix = [[[], [], []],
                        [[], [], []],
                        [[], [], []]]
        for j in range(0, 3):
            for i in range(0, 3):
                carry_matrix[j][2-i] = matrix[i][j]

        for i in range(0, 3):
            for j in range(0, 3):
                matrix[i][j] = carry_matrix[i][j]

    else:
        pass


class FunctionalRubik:

    def __init__(self, matrix_of_cubes, len):
        self.matrix_of_cubes = [[[[], [], []], [[], [], []], [[], [], []]],
                                [[[], [], []], [[], [], []], [[], [], []]],
                                [[[], [], []], [[], [], []], [[], [], []]]]
        self.clone_and_steal(matrix_of_cubes)
        self.constructor_len = len

    def clone_and_steal(self, matrix_of_cubes):
        for i in range(0, 3):
            for j in range(0, 3):
                for k in range(0, 3):
                    for face in matrix_of_cubes[i][j][k]:
                        carry = []
                        for ref in face[0:4]:
                            carry.append(ref.get_coord())
                        carry.append(face[4].get_rgb())
                        self.matrix_of_cubes[i][j][k].append(carry)

    def get_matrix_of_cubes(self):
        return self.matrix_of_cubes

    def plot(self):
        plot_matrix_of_cubes(self.matrix_of_cubes)

    def rotate_side(self, id="j2+"):
        if id[0] == "i":
            cube_side_rotate(self.matrix_of_cubes[int(id[1])][:][:], id[0], id[2], [int(id[1]), 0, 0], self.constructor_len)
            matrix_90_rotate(self.matrix_of_cubes[int(id[1])][:][:], id[2])
        elif id[0] == "j":
            cube_side_rotate(self.matrix_of_cubes[:][int(id[1])][:], id[0], id[2], [0, int(id[1]), 0], self.constructor_len)
            matrix_90_rotate(self.matrix_of_cubes[:][int(id[1])][:], id[2])
        elif id[0] == "k":
            cube_side_rotate(self.matrix_of_cubes[:][:][int(id[1])], id[0], id[2], [0, 0, int(id[1])], self.constructor_len)
            matrix_90_rotate(self.matrix_of_cubes[:][:][int(id[1])], id[2])




class RubikCube:

    def __init__(self, down_vertex, edge_length):
        self.ref_vertex = down_vertex
        self.length = edge_length
        self.list_of_points = []

        self.generate()

        self.cloud_of_points = []

        self.cube = gs.GraphicalObject()

        self.black = gs.Color()
        self.black.set_name("black")
        self.white = gs.Color(1.0, 1.0, 1.0)
        self.white.set_name("white")
        self.red = gs.Color(1.0, 0.0, 0.0)
        self.red.set_name("red")
        self.green = gs.Color(0.0, 1.0, 0.0)
        self.green.set_name("green")
        self.blue = gs.Color(0.0, 0.0, 1.0)
        self.blue.set_name("blue")
        self.orange = gs.Color(1.0, 0.27, 0.0)
        self.orange.set_name("orange")
        self.yellow = gs.Color(1.0, 1.0, 0.0)
        self.yellow.set_name("yellow")

        self.list_of_faces = []
        self.list_of_sub_faces = []
        self.matrix_of_cubes = [[[[], [], []], [[], [], []], [[], [], []]],
                                [[[], [], []], [[], [], []], [[], [], []]],
                                [[[], [], []], [[], [], []], [[], [], []]]]
        self.create_refs_vertex()
        self.generate_cloud()

    def generate(self):
        pass

    def create_refs_vertex(self):

        down_carry_list = []
        for j in qd.frange(self.ref_vertex[1], self.ref_vertex[1] + self.length * 4, self.length):
            for k in qd.frange(self.ref_vertex[2], self.ref_vertex[2] + self.length * 4, self.length):
                for i in qd.frange(self.ref_vertex[0], self.ref_vertex[0] + self.length * 4, self.length):
                    carry = gs.Point(i, j, k)
                    self.list_of_points.append(carry)
                    self.cube.push_point(carry)
                    down_carry_list.append(carry)

        front_carry_list = []
        for k in qd.frange(self.ref_vertex[2], self.ref_vertex[2] + self.length * 4, self.length):
            for i in qd.frange(self.ref_vertex[0], self.ref_vertex[0] + self.length * 4, self.length):
                for j in qd.frange(self.ref_vertex[1], self.ref_vertex[1] + self.length * 4, self.length):
                    carry = gs.Point(i, j, k)
                    self.list_of_points.append(carry)
                    self.cube.push_point(carry)
                    front_carry_list.append(carry)

        right_carry_list = []
        for i in qd.frange(self.ref_vertex[0], self.ref_vertex[0] + self.length * 4, self.length):
            for j in qd.frange(self.ref_vertex[1], self.ref_vertex[1] + self.length * 4, self.length):
                for k in qd.frange(self.ref_vertex[2], self.ref_vertex[2] + self.length * 4, self.length):
                    carry = gs.Point(i, j, k)
                    self.list_of_points.append(carry)
                    self.cube.push_point(carry)
                    right_carry_list.append(carry)

        ###################################

        index = 0
        color_counter = 0
        color = self.blue
        suspend_flag = False
        while index < len(front_carry_list):

            if index % 16 == 0:
                if color_counter == 0:
                    color = self.blue
                elif color_counter == 3:
                    color = self.green
                else:
                    color = self.black

                color_counter += 1
                suspend_flag = False

            if (index - 11) % 16 == 0 and index != 0:
                suspend_flag = True

            if (index - 3) % 4 == 0 or suspend_flag:
                pass
            else:
                self.list_of_sub_faces.append([front_carry_list[index], front_carry_list[index + 1],
                                               front_carry_list[index + 5], front_carry_list[index + 4], color])

            index += 1

        index = 0
        color_counter = 0
        color = self.orange
        suspend_flag = False
        while index < len(right_carry_list):

            if index % 16 == 0:
                if color_counter == 0:
                    color = self.orange
                elif color_counter == 3:
                    color = self.red
                else:
                    color = self.black

                color_counter += 1
                suspend_flag = False

            if (index - 11) % 16 == 0 and index != 0:
                suspend_flag = True

            if (index - 3)%4 == 0 or suspend_flag:
                pass
            else:
                self.list_of_sub_faces.append([right_carry_list[index], right_carry_list[index + 1],
                                               right_carry_list[index + 5], right_carry_list[index + 4], color])

            index += 1

        index = 0
        color_counter = 0
        color = self.yellow
        suspend_flag = False
        while index < len(down_carry_list):

            if index % 16 == 0:
                if color_counter == 0:
                    color = self.yellow
                elif color_counter == 3:
                    color = self.white
                else:
                    color = self.black

                color_counter += 1
                suspend_flag = False

            if (index - 11) % 16 == 0 and index != 0:
                suspend_flag = True

            if (index - 3)%4 == 0 or suspend_flag:
                pass
            else:
                self.list_of_sub_faces.append([down_carry_list[index], down_carry_list[index + 1],
                                               down_carry_list[index + 5], down_carry_list[index + 4], color])

            index += 1

        ###################################

        id = 0
        for m in self.list_of_sub_faces:
            print(id, "\t", m[0].get_coord(), m[1].get_coord(), m[2].get_coord(), m[3].get_coord())
            id += 1

    def get_vertex_ref(self):
        carry = []

        for ref in self.list_of_points:
            carry.append(ref.get_coord())
        return carry

    def generate_cloud(self):

        counter = 0
        for ref in self.list_of_points:

            if counter%4 == 0:
                p0 = ref
            else:
                p1 = ref

                self.cloud_of_points = self.cloud_of_points + br.bresenham_3d(p0.get_coord(), p1.get_coord())
                p0 = p1

            counter = counter + 1

    def get_cloud(self):
        return self.cloud_of_points

    def standard_cube(self):

        counter = 0
        for ref in self.list_of_points:
            if counter % 4 == 0:
                p0 = ref
            else:
                p1 = ref

                self.cube.push_edge(p0, p1, gs.Color(0, 0, 0))

                p0 = p1
            counter = counter + 1

        self.cube.show()

    def get_cube(self):
        return self.cube

    def plot_sub_faces(self):

        for sub_face in self.list_of_sub_faces:
            GL.glPolygonMode(GL.GL_FRONT_AND_BACK, GL.GL_FILL)
            GL.glColor(sub_face[4].get_rgb()[0], sub_face[4].get_rgb()[1], sub_face[4].get_rgb()[2])
            GL.glBegin(GL.GL_POLYGON)
            GL.glVertex3f(sub_face[0].get_coord()[0], sub_face[0].get_coord()[1], sub_face[0].get_coord()[2])
            GL.glVertex3f(sub_face[1].get_coord()[0], sub_face[1].get_coord()[1], sub_face[1].get_coord()[2])
            GL.glVertex3f(sub_face[2].get_coord()[0], sub_face[2].get_coord()[1], sub_face[2].get_coord()[2])
            GL.glVertex3f(sub_face[3].get_coord()[0], sub_face[3].get_coord()[1], sub_face[3].get_coord()[2])
            GL.glVertex3f(sub_face[0].get_coord()[0], sub_face[0].get_coord()[1], sub_face[0].get_coord()[2])
            GL.glEnd()

    def generate_matrix_of_cubes(self):
        f_list = self.list_of_sub_faces[72:]
        r_list = self.list_of_sub_faces[36:72]
        d_list = self.list_of_sub_faces[:36]

        f_cubes = []
        index = 0
        while index < 27:
            f_cubes.append([f_list[index], f_list[index + 9]])
            index += 1

        for ref in f_cubes:
            m = ref[0]
            print(m[0].get_coord(), m[1].get_coord(), m[2].get_coord(), m[3].get_coord(), m[4].get_name())

            m = ref[1]
            print(m[0].get_coord(), m[1].get_coord(), m[2].get_coord(), m[3].get_coord(), m[4].get_name())

            print("****")

        index = 0
        y_index = -1
        z_index = -1
        x_index = 0
        while index < 27:
            if index % 9 == 0:
                y_index += 1
                z_index = -1
            if index % 3 == 0:
                z_index += 1
                x_index = 0

            print(index, x_index, y_index, z_index)

            self.matrix_of_cubes[x_index][y_index][z_index] += f_cubes[index]

            x_index += 1
            index += 1

        r_cubes = []
        index = 0
        while index < 27:
            r_cubes.append([r_list[index], r_list[index + 9]])
            index += 1

        for ref in f_cubes:
            m = ref[0]
            print(m[0].get_coord(), m[1].get_coord(), m[2].get_coord(), m[3].get_coord(), m[4].get_name())

            m = ref[1]
            print(m[0].get_coord(), m[1].get_coord(), m[2].get_coord(), m[3].get_coord(), m[4].get_name())

            print("****")

        index = 0
        x_index = -1
        y_index = -1
        z_index = 0
        while index < 27:
            if index % 9 == 0:
                x_index += 1
                y_index = -1
            if index % 3 == 0:
                y_index += 1
                z_index = 0

            print(index, x_index, y_index, z_index)

            self.matrix_of_cubes[x_index][y_index][z_index] += r_cubes[index]

            z_index += 1
            index += 1

        d_cubes = []
        index = 0
        while index < 27:
            d_cubes.append([d_list[index], d_list[index + 9]])
            index += 1

        for ref in f_cubes:
            m = ref[0]
            print(m[0].get_coord(), m[1].get_coord(), m[2].get_coord(), m[3].get_coord(), m[4].get_name())

            m = ref[1]
            print(m[0].get_coord(), m[1].get_coord(), m[2].get_coord(), m[3].get_coord(), m[4].get_name())

            print("****")

        index = 0
        x_index = -1
        z_index = -1
        y_index = 0
        while index < 27:
            if index % 9 == 0:
                x_index += 1
                z_index = -1
            if index % 3 == 0:
                z_index += 1
                y_index = 0

            print(index, x_index, y_index, z_index)

            self.matrix_of_cubes[x_index][y_index][z_index] += d_cubes[index]

            y_index += 1
            index += 1

        return self.matrix_of_cubes

    def rotate_side(self, id="j2+"):
        if id[0] == "i":
            matrix_90_rotate(self.matrix_of_cubes[int(id[1])][:][:], id[2])
            cube_side_rotate(self.matrix_of_cubes[int(id[1])][:][:], id[0], id[2])
        elif id[0] == "j":
            matrix_90_rotate(self.matrix_of_cubes[:][int(id[1])][:], id[2])
            cube_side_rotate(self.matrix_of_cubes[:][int(id[1])][:], id[0], id[2])
        elif id[0] == "k":
            matrix_90_rotate(self.matrix_of_cubes[:][:][int(id[1])], id[2])
            cube_side_rotate(self.matrix_of_cubes[:][:][int(id[1])], id[0], id[2])



rubik = RubikCube([0, 0, 0], 3)
rubik.standard_cube()
test_cloud = rubik.get_cloud()
print(rubik.get_vertex_ref())


functional_rubik = rubik.generate_matrix_of_cubes()

final_rubik = FunctionalRubik(functional_rubik, 3)

del functional_rubik

inspect_matrix_of_cubes(final_rubik.get_matrix_of_cubes())


################################################################


def main(points):
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
    GLU.gluLookAt(15, 15, 15, 0, 0, 0, 0, 1, 0)

    first_time = True
    grid = gr.grid_gen(250, gs.Color(25 / 255, 150 / 250, 25 / 255))
    grid.show()

    do = True
    while do:
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        grid.plot()

        ########################################

        if first_time:
            GL.glPointSize(2)
            GL.glColor3f(1.0, 0.0, 0.0)
            #GL.glBegin(GL.GL_LINES)
            GL.glBegin(GL.GL_POINTS)
            #carry_ref = points[0]
            for ref_point in points:
                #coordinates = ref_point
                #GL.glVertex3f(carry_ref[0], carry_ref[1], carry_ref[2])
                GL.glVertex3f(ref_point[0], ref_point[1], ref_point[2])
                #carry_ref = ref_point
            GL.glEnd()
            first_time = False

        """
        rubik.rotate_side("i1+")
        rubik.get_cube().plot()
        rubik.plot_sub_faces()
        """

        #final_rubik.rotate_side()
        final_rubik.plot()

        ########################################

        GL.glFlush()
        GLUT.glutPostRedisplay()

        do = False

    GLUT.glutMainLoop()

main(test_cloud)