import libg2f.GraphData as GD

def grid_gen(ref_value=200, xz_color=None, y_color=None):
    if xz_color is None:
        xz_color = GD.Color(204 / 255, 0, 0)
    else:
        pass

    if y_color is None:
        y_color = GD.Color(0, 0, 153 / 255)
    else:
        pass

    top_z = ref_value
    down_z = -1*ref_value

    top_x = ref_value
    down_x = -1*ref_value

    steps = 2

    grid = GD.GraphicalObject()
    grid.set_name("Grid")

    top_y = ref_value
    down_y = -1*ref_value

    for z in range(down_z, top_z, steps):
        p_1 = GD.Point(down_x, 0, z)
        p_2 = GD.Point(top_x, 0, z)
        grid.push_edge(p_1, p_2, xz_color)

    for x in range(down_x, top_x, steps):
        p_1 = GD.Point(x, 0, down_z)
        p_2 = GD.Point(x, 0, top_z)
        grid.push_edge(p_1, p_2, xz_color)

    grid.push_edge(GD.Point(0, down_y, 0), GD.Point(0, top_y, 0), y_color)

    return grid

"""
def main():
    GLUT.glutInit(sys.argv)
    GLUT.glutInitDisplayMode(GLUT.GLUT_SINGLE | GLUT.GLUT_RGBA | GLUT.GLUT_DEPTH)
    GLUT.glutInitWindowSize(400, 400)
    GLUT.glutInitWindowPosition(200, 200)

    GLUT.glutCreateWindow("Grafica 2")

    GL.glDepthFunc(GL.GL_LEQUAL)
    GL.glEnable(GL.GL_DEPTH_TEST)
    GL.glClearDepth(1.0)
    GL.glClearColor(0.0, 0.0, 0.0, 0.0)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
    GL.glMatrixMode(GL.GL_PROJECTION)
    GL.glLoadIdentity()
    #GL.glOrtho(-20, 20, -20, 20, -20, 20)
    GL.glMatrixMode(GL.GL_MODELVIEW)

    GLU.gluPerspective(100, 1.0, 1.0, 100.0)
    GL.glTranslatef(-0.0, -5.0, -8.0)

    grid = grid_gen()

    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

    ########################################

    grid.plot()

    ########################################

    GL.glFlush()

    GLUT.glutMainLoop()

main()
"""