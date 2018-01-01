import sys

import graph_data_struct as gs
import grid as gr
import l_system as ls
from OpenGL import GL
from OpenGL import GLU
from OpenGL import GLUT

from prototype import grammar_interpreter as gm

myGrammar = gm.Grammar("++++F")
myGrammar.set_rule("F:F[+F]F[-F]F")
myGrammar.setType(0)


myTree = ls.LSystem(myGrammar, [0, 0, 0], 90, 22.5, 5)
myTree.getGraficalObject().scale(0.1)

def main():
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
    GLU.gluLookAt(10, 10, 10, 0, 0, 0, 0, 1, 0)

    grid = gr.grid_gen(100,gs.Color(0.5, 1, 1))

    while True:

        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

        grid.show()
        grid.plot()

        ########################################

        myTree.plotAge(5)

        ########################################

        GL.glFlush()
        GLUT.glutPostRedisplay()

    GLUT.glutMainLoop()

main()