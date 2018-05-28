# TODO: Remove
# pylint: disable=unused-wildcard-import
# pylint: disable=wildcard-import
# pylint: disable=invalid-name

from PyQt5 import QtWidgets, QtCore

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *



toggleAnimation = True


class VisualizationWidget(QtWidgets.QOpenGLWidget):
    def __init__(self, *args):
        super(VisualizationWidget, self).__init__(*args)
        self.initializeGL()

        # Variables
        self.angle_x = 45
        self.angle_y = 45
        self.angle_z = 45
        self.translate_x = 0
        self.translate_y = 0
        self.translate_z = 0
        self.scale_x = 1
        self.scale_y = 1
        self.scale_z = 1
        self.projection_type = "Ortogonal"

    def rotate(self, theta_x, theta_y, theta_z):
        self.angle_x += theta_x
        self.angle_y += theta_y
        self.angle_z += theta_z
        self.update()

    def translate(self, inc_x, inc_y, inc_z):
        self.translate_x += inc_x
        self.translate_y += inc_y
        self.translate_z += inc_z
        self.update()

    def mirror(self, plane_xy, plane_yz, plane_zx):
        pass

    def scale(self, dx, dy, dz):
        if dx != 0:
            self.scale_x *= dx
        if dy != 0:
            self.scale_y *= dy
        if dz != 0:
            self.scale_z *= dz

    def change_projection(self, projection_type):
        self.projection_type = projection_type
        self.update()

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glMatrixMode(GL_MODELVIEW)

        if self.projection_type == 'Perspectiva':
            gluPerspective(5, 1, -2, 100)
        elif self.projection_type == "Ortogonal":
            glOrtho(-2, 2, -2, 2, -2, 100)
        else:
            print("ERROR, not a valid projection")

        # The operations are done from bottom to top
        glPushMatrix()

        glColor3f(1.0, 1.5, 0.0) # set colour

        # Scale
        glScale(self.scale_x, self.scale_y, self.scale_z)

        # Rotations
        glRotatef(self.angle_x, 1, 0, 0)
        glRotatef(self.angle_y, 0, 1, 0)
        glRotatef(self.angle_z, 0, 0, 1)

        # Translate
        glTranslate(self.translate_x, self.translate_y, self.translate_z)

        glutWireCube(1)
        glPopMatrix()

    def initializeGL(self):
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        glClearColor(0, 0, 1, 0)

        glOrtho(-2, 2, -2, 2, -2, 100)

        # TODO: choose correct values
        #gluPerspective(45.0,1.33,0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

        # Define posicao inicial da janela na tela
        glEnable(GL_DEPTH_TEST)

        glutInit()

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Define a matriz de projeção ortogonal
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(0, 1, -2, 100)
        #glOrtho(-2, 2, -2, 2, -2, 100)

        # Define que irá trabalhar com a matriz de modelo/visão
        glMatrixMode(GL_MODELVIEW)

        # Para cada porta de visão, configura as propriedades do
        # material e desenha o objeto
        glViewport(0, 0, 400, 400)
        glLoadIdentity()

    def init(self):
        # Function for correct integration with PyQt5
        self.makeCurrent()

        # Agora temos que cuidar também o buffer de profundidade.
        # Trocamos para utilizar dois buffers, deve-se
        # trocar o glFlush() no método display() para glutSwapBuffers()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)

        # Check depth buffer
        glEnable(GL_DEPTH_TEST)

        glClearColor(0, 0, 1, 0)
        gluLookAt(0, 0, 2, 0, 0, 0, 0, 1, 0)
        glutDisplayFunc(self.display)
