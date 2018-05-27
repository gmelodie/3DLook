# pylint: disable=unused-wildcard-import
# pylint: disable=wildcard-import
# pylint: disable=invalid-name

from PyQt5 import QtWidgets, QtCore

#from OpenGL import GL as gl
#from OpenGL import GLU as glu
#from OpenGL import GLUT as glut
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


# Variaveis globais para transformações de rotação.
increment = 1
curAngle = 45
repetitions = 100

# Variáveis auxiliares
toggleAnimation = True
curObject = 0
curShading = 0


class VisualizationWidget(QtWidgets.QOpenGLWidget):
    def __init__(self, *args):
        super(VisualizationWidget, self).__init__(*args)
        self.initializeGL()
        self.timer = None

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

        self.reps = 0
        self.continuos = True

    def rotate(self, theta_x, theta_y, theta_z):
        if not self.continuos:
            self.angle_x += theta_x
            self.angle_y += theta_y
            self.angle_z += theta_z
            self.update()
        else:
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(
                lambda: self.rotate_fun(theta_x, theta_y, theta_z))
            self.reps = 0
            self.timer.start(10)

    def rotate_fun(self, theta_x, theta_y, theta_z):
        self.angle_x += (theta_x) / repetitions
        self.angle_y += (theta_y) / repetitions
        self.angle_z += (theta_z) / repetitions
        self.reps += 1
        if self.reps >= repetitions:
            self.timer.stop()
        else:
            self.update()


    def translate(self, inc_x, inc_y, inc_z):
        if not self.continuos:
            self.translate_x += inc_x
            self.translate_y += inc_y
            self.translate_z += inc_z
            self.update()

        else:
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(
                lambda: self.translate_fun(inc_x, inc_y, inc_z))
            self.reps = 0
            self.timer.start(10)


    def translate_fun(self, inc_x, inc_y, inc_z):
        self.translate_x += (inc_x) / repetitions
        self.translate_y += (inc_y) / repetitions
        self.translate_z += (inc_z) / repetitions
        self.reps += 1
        if self.reps >= repetitions:
            self.timer.stop()
        else:
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
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        if (projection_type == 'Perspectiva'):
            gluPerspective(45, 2, -2, 100)
        else:
            glOrtho(-2, 2, -2, 2, -2, 100)
        self.update()

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glMatrixMode(GL_MODELVIEW)

        glPushMatrix() # The operations are done from bottom to top
        # set color
        glColor3f(1.0, 1.5, 0.0)

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
        self.makeCurrent()
        # Agora temos que cuidar também o buffer de profundidade.
        # Trocamos para utilizar dois buffers, deve-se
        # trocar o glFlush() no método display() para glutSwapBuffers()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        # Pedimos para o OpenGL verificar o buffer de
        # profundidade na hora de renderizar. Precisa ser depois
        # de criada a janela!
        glEnable(GL_DEPTH_TEST)

        glClearColor(0, 0, 1, 0)
        gluLookAt(0, 0, 2, 0, 0, 0, 0, 1, 0)
        glutDisplayFunc(self.display)
