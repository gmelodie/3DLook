from PyQt5 import QtWidgets

from OpenGL import GL as gl
from OpenGL import GLU as glu
from OpenGL import GLUT as glut

class VisualizationWidget(QtWidgets.QOpenGLWidget):

    def __init__(self, *args):
        super(VisualizationWidget, self).__init__(*args)
        self.element_array = None
        self.vertex_array = None
        self.initializeGL()

    def rotate(self, theta_x, theta_y, theta_z):
        pass

    def translate(self, inc_x, inc_y, inc_z):
        print(inc_x, inc_y, inc_z)

    def mirror(self, plane_xy, plane_yz, plane_zx):
        pass

    def scale(self, dx, dy, dz):
        pass

    def change_projection(self, projection_type):
    # set projection to projection_type
        pass

    def create_cube(self, edge):
        pass

    # Test fucntion for now
    def paintGL(self):
        """
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        gl.glColor3f(1, 0, 0)
        gl.glBegin(gl.GL_TRIANGLES)
        gl.glVertex3f(-0.5, -0.5, 0)
        gl.glVertex3f(0.5, -0.5, 0)
        gl.glVertex3f(0.0, 0.5, 0)
        glut.glutWireCube(1)
        gl.glEnd()

        glu.gluPerspective(45, 651/551, 0.1, 50.0)
        gl.glTranslatef(0.0, 0.0, -5)
        """
