import bresenham3d as br
import quaternion as qd
import graph_data_struct as gs
import grid as gr

import OpenGL.GL as GL
import OpenGL.GLU as GLU
import OpenGL.GLUT as GLUT

import sys
import numpy as np


def matrix_90_rotate(matrix):
    pass



class RubikCube:

    def __init__(self, down_vertex, edge_length):
        self.ref_vertex = down_vertex
        self.length = edge_length
        self.list_of_points = []

        self.generate()

        self.cloud_of_points = []

        self.cube = gs.GraphicalObject()

        self.black = gs.Color()
        self.white = gs.Color(1.0, 1.0, 1.0)
        self.red = gs.Color(1.0, 0.0, 0.0)
        self.green = gs.Color(0.0, 1.0, 0.0)
        self.blue = gs.Color(0.0, 0.0, 1.0)
        self.orange = gs.Color(1.0, 0.27, 0.0)
        self.yellow = gs.Color(1.0, 1.0, 0.0)

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
            print(m[0].get_coord(), m[1].get_coord(), m[2].get_coord(), m[3].get_coord())

            m = ref[1]
            print(m[0].get_coord(), m[1].get_coord(), m[2].get_coord(), m[3].get_coord())

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

        index_i = -1
        for i in self.matrix_of_cubes:
            index_i += 1
            index_j = -1
            for j in i:
                index_j += 1
                index_k = -1
                for k in j:
                    index_k += 1
                    print(index_i, index_j, index_k, "\t")
                    for face in k:
                        m = face
                        print(m[0].get_coord(), m[1].get_coord(), m[2].get_coord(), m[3].get_coord())
                    print("********************")

    """
    def rotate_size(self, id = "i2+"):
        if id[0] == "i":
            if id[1] == "0":
                if id[2] == "+":

                elif id[2] == "-":

                else:
                    pass

            elif id[1] == "1":
                if id[2] == "+":

                elif id[2] == "-":

                else:
                    pass

            elif id[2] == "2":
                if id[2] == "+":
                    carry_matrix = [[[],[],[]],
                                    [[], [], []],
                                    [[], [], []]]
                    for k in range(0,3):
                        for j in range(0,3):
                            if k == 0:
                                carry_matrix[2][j]=self.matrix_of_cubes[2][j][k]
                            elif k == 1:
                                carry_matrix[k][j] = self.matrix_of_cubes[2][j][k]
                            elif k == 2:
                                carry_matrix[0][j] = self.matrix_of_cubes[2][j][k]
                            else:
                                pass
                elif id[2] == "-":

                else:
                    pass

            else:
                pass
        elif id[0] == "j":
            if id[1] == "0":
                if id[2] == "+":

                elif id[2] == "-":

                else:
                    pass

            elif id[1] == "1":
                if id[2] == "+":

                elif id[2] == "-":

                else:
                    pass

            elif id[2] == "2":
                if id[2] == "+":

                elif id[2] == "-":

                else:
                    pass

            else:
                pass

        elif id[0] == "k":
            if id[1] == "0":
                if id[2] == "+":

                elif id[2] == "-":

                else:
                    pass

            elif id[1] == "1":
                if id[2] == "+":

                elif id[2] == "-":

                else:
                    pass

            elif id[2] == "2":
                if id[2] == "+":

                elif id[2] == "-":

                else:
                    pass

            else:
                pass

        else:
            pass
    """


rubik = RubikCube([0, 0, 0], 3)
rubik.standard_cube()

print(rubik.get_vertex_ref())

rubik.generate_matrix_of_cubes()

test_cloud = rubik.get_cloud()


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

    while True:
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
            #first_time = False

        rubik.get_cube().plot()
        rubik.plot_sub_faces()

        ########################################

        GL.glFlush()
        GLUT.glutPostRedisplay()

    GLUT.glutMainLoop()

main(test_cloud)