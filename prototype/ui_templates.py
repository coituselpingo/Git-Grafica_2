import math
import sys

from OpenGL import GL
from OpenGL import GLU
from OpenGL import GLUT
from PyQt5.QtCore import pyqtSignal, QPoint, QSize, Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import *

from prototype import graph_data_struct as GD


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.glWidget = GLWidget()

        self.start_menu_bar()

        self.setCentralWidget(self.glWidget)

        self.setGeometry(640, 480, 640, 480)
        self.setWindowTitle('Grafica 2')
        self.show()

    def start_menu_bar(self):
        self.statusBar().showMessage('Ready')

        ##########################################################################

        menubar = self.menuBar()

        file = menubar.addMenu('File')

        edit = menubar.addMenu('Edit')

        ##########################################################################

        create_object_menu = QMenu('Create Object', self)

        create_by_points = QAction('Add by Points', self)
        create_object_menu.addAction(create_by_points)

        create_by_file = QAction('Add from File', self)
        create_object_menu.addAction(create_by_file)

        edit.addMenu(create_object_menu)

        ##########################################################################

        modify_object = QMenu('Modify Object', self)

        scale_object = QAction('Scale Object', self)
        modify_object.addAction(scale_object)

        rotate_object = QAction('Rotate Object', self)
        modify_object.addAction(rotate_object)

        translate_object = QAction('Translate Object', self)
        modify_object.addAction(translate_object)

        delete_object = QAction('Delete Object', self)
        modify_object.addAction(delete_object)

        edit.addMenu(modify_object)

        ##########################################################################

        options = menubar.addMenu('Options')

        exit_option = menubar.addMenu('Exit')

        ##########################################################################

    def createSlider(self):
        slider = QSlider(Qt.Vertical)

        slider.setRange(0, 360 * 16)
        slider.setSingleStep(16)
        slider.setPageStep(15 * 16)
        slider.setTickInterval(15 * 16)
        slider.setTickPosition(QSlider.TicksRight)

        return slider


class GLWidget(QOpenGLWidget):
    xRotationChanged = pyqtSignal(int)
    yRotationChanged = pyqtSignal(int)
    zRotationChanged = pyqtSignal(int)

    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)

        self.object = 0
        self.xRot = 0
        self.yRot = 0
        self.zRot = 0

        self.lastPos = QPoint()

        self.trolltechGreen = QColor.fromCmykF(0.40, 0.0, 1.0, 0.0)
        self.trolltechPurple = QColor.fromCmykF(0.39, 0.39, 0.0, 0.0)

    def minimumSizeHint(self):
        return QSize(50, 50)

    def sizeHint(self):
        return QSize(400, 400)

    def setXRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.xRot:
            self.xRot = angle
            self.xRotationChanged.emit(angle)
            self.update()

    def setYRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.yRot:
            self.yRot = angle
            self.yRotationChanged.emit(angle)
            self.update()

    def setZRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.zRot:
            self.zRot = angle
            self.zRotationChanged.emit(angle)
            self.update()

    def initializeGL(self):
        #self.gl = self.context().versionFunctions()
        self.gl = GL
        self.glu = GLU
        self.glut = GLUT
        #self.gl.initializeOpenGLFunctions()

        self.gl.glDepthFunc(self.gl.GL_LEQUAL)
        self.gl.glEnable(self.gl.GL_DEPTH_TEST)
        self.gl.glClearDepth(1.0)
        self.gl.glClearColor(0.0, 0.0, 0.0, 0.0)
        self.gl.glClear(self.gl.GL_COLOR_BUFFER_BIT | self.gl.GL_DEPTH_BUFFER_BIT)
        self.gl.glMatrixMode(self.gl.GL_PROJECTION)
        self.gl.glLoadIdentity()
        self.gl.glMatrixMode(self.gl.GL_MODELVIEW)
        self.glu.gluPerspective(100, 1.0, 1.0, 100.0)
        self.gl.glTranslatef(0.0, 0.0, -8.0)

        self.gl.glFlush()

        self.gl.glClear(
            self.gl.GL_COLOR_BUFFER_BIT | self.gl.GL_DEPTH_BUFFER_BIT)

        self.gl.glBegin(self.gl.GL_LINES)
        self.gl.glColor(0, 0, 1)
        self.gl.glVertex(0, 0, 0)
        self.gl.glVertex(3, 3, 4)
        self.gl.glEnd()

        self.gl.glFlush()


    def paintGL(self):
        self.gl.glClear(
            self.gl.GL_COLOR_BUFFER_BIT | self.gl.GL_DEPTH_BUFFER_BIT)
        self.gl.glLoadIdentity()

        ref_value = 4.0
        rojo = GD.Color(1.0, 0.0, 0.0)
        verde = GD.Color(0.0, 1.0, 0.0)
        azul = GD.Color(0.0, 0.0, 1.0)

        p1 = GD.Point(ref_value, ref_value, ref_value)
        p2 = GD.Point(0.0, 0.0, 0.0)
        p3 = GD.Point(0.0, ref_value, 0.0)
        p4 = GD.Point(0.0, ref_value, ref_value)

        tetraedro = GD.GraphicalObject()

        tetraedro.push_edge(p1, p2, rojo)
        tetraedro.push_edge(p1, p3, rojo)
        tetraedro.push_edge(p1, p4, rojo)
        tetraedro.push_edge(p2, p3, verde)
        tetraedro.push_edge(p2, p4, verde)
        tetraedro.push_edge(p3, p4, verde)

        tetraedro.show_points()
        tetraedro.show_edges()

        # ____________________-----------------------____________-#

        t1 = GD.Point(ref_value, ref_value, 0)
        t2 = GD.Point(ref_value, 0, 0)
        t3 = GD.Point(0, ref_value, 0)

        triangle = GD.GraphicalObject()

        triangle.push_edge(t1, t2, rojo)
        triangle.push_edge(t1, t3, verde)
        triangle.push_edge(t2, t3, azul)

        triangle.show_points()
        triangle.show_edges()

        self.gl.glClear(
            self.gl.GL_COLOR_BUFFER_BIT | self.gl.GL_DEPTH_BUFFER_BIT)

        self.gl.glBegin(self.gl.GL_LINES)
        self.gl.glColor(0, 0, 1)
        self.gl.glVertex(0, 0, 0)
        self.gl.glVertex(3, 3, 4)
        self.gl.glEnd()

        tetraedro.plot(self.gl)
        triangle.plot(self.gl)

        self.gl.glFlush()

    def resizeGL(self, width, height):
        side = min(width, height)
        if side < 0:
            return

        self.gl.glViewport((width - side) // 2, (height - side) // 2, side,
                side)

        self.gl.glMatrixMode(self.gl.GL_PROJECTION)
        self.gl.glLoadIdentity()
        self.gl.glOrtho(-0.5, +0.5, +0.5, -0.5, 4.0, 15.0)
        self.gl.glMatrixMode(self.gl.GL_MODELVIEW)

    def mousePressEvent(self, event):
        self.lastPos = event.pos()

    def mouseMoveEvent(self, event):
        dx = event.x() - self.lastPos.x()
        dy = event.y() - self.lastPos.y()

        if event.buttons() & Qt.LeftButton:
            self.setXRotation(self.xRot + 8 * dy)
            self.setYRotation(self.yRot + 8 * dx)
        elif event.buttons() & Qt.RightButton:
            self.setXRotation(self.xRot + 8 * dy)
            self.setZRotation(self.zRot + 8 * dx)

        self.lastPos = event.pos()

    def makeObject(self):
        genList = self.gl.glGenLists(1)
        self.gl.glNewList(genList, self.gl.GL_COMPILE)

        self.gl.glBegin(self.gl.GL_QUADS)

        x1 = +0.06
        y1 = -0.14
        x2 = +0.14
        y2 = -0.06
        x3 = +0.08
        y3 = +0.00
        x4 = +0.30
        y4 = +0.22

        self.quad(x1, y1, x2, y2, y2, x2, y1, x1)
        self.quad(x3, y3, x4, y4, y4, x4, y3, x3)

        self.extrude(x1, y1, x2, y2)
        self.extrude(x2, y2, y2, x2)
        self.extrude(y2, x2, y1, x1)
        self.extrude(y1, x1, x1, y1)
        self.extrude(x3, y3, x4, y4)
        self.extrude(x4, y4, y4, x4)
        self.extrude(y4, x4, y3, x3)

        NumSectors = 50

        for i in range(NumSectors):
            angle1 = (i * 2 * math.pi) / NumSectors
            x5 = 0.30 * math.sin(angle1)
            y5 = 0.30 * math.cos(angle1)
            x6 = 0.20 * math.sin(angle1)
            y6 = 0.20 * math.cos(angle1)

            angle2 = ((i + 1) * 2 * math.pi) / NumSectors
            x7 = 0.20 * math.sin(angle2)
            y7 = 0.20 * math.cos(angle2)
            x8 = 0.30 * math.sin(angle2)
            y8 = 0.30 * math.cos(angle2)

            self.quad(x5, y5, x6, y6, x7, y7, x8, y8)

            self.extrude(x6, y6, x7, y7)
            self.extrude(x8, y8, x5, y5)

        self.gl.glEnd()
        self.gl.glEndList()

        return genList

    def quad(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.setColor(self.trolltechGreen)

        self.gl.glVertex3d(x1, y1, -0.05)
        self.gl.glVertex3d(x2, y2, -0.05)
        self.gl.glVertex3d(x3, y3, -0.05)
        self.gl.glVertex3d(x4, y4, -0.05)

        self.gl.glVertex3d(x4, y4, +0.05)
        self.gl.glVertex3d(x3, y3, +0.05)
        self.gl.glVertex3d(x2, y2, +0.05)
        self.gl.glVertex3d(x1, y1, +0.05)

    def extrude(self, x1, y1, x2, y2):
        self.setColor(self.trolltechGreen.darker(250 + int(100 * x1)))

        self.gl.glVertex3d(x1, y1, +0.05)
        self.gl.glVertex3d(x2, y2, +0.05)
        self.gl.glVertex3d(x2, y2, -0.05)
        self.gl.glVertex3d(x1, y1, -0.05)

    def normalizeAngle(self, angle):
        while angle < 0:
            angle += 360 * 16
        while angle > 360 * 16:
            angle -= 360 * 16
        return angle

    def setClearColor(self, c):
        self.gl.glClearColor(c.redF(), c.greenF(), c.blueF(), c.alphaF())

    def setColor(self, c):
        self.gl.glColor4f(c.redF(), c.greenF(), c.blueF(), c.alphaF())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
