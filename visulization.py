# pylint: disable=unused-wildcard-import
# pylint: disable=wildcard-import
# pylint: disable=invalid-name

from PyQt5 import QtWidgets

#from OpenGL import GL as gl
#from OpenGL import GLU as glu
#from OpenGL import GLUT as glut
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Variaveis globais para transformações de rotação.
increment = 1
curAngle = 45

# Variáveis auxiliares
toggleAnimation = True
curObject = 0
curShading = 0
lightTypes = [["Diffuse reflection only","No ambient or specular"],
            ["Diffuse and specular reflection", "Low shininess; no ambient"],
            ["Diffuse and specular reflection", "high shininess; no ambient"],
            ["Diffuse refl.; emission", "no ambient or specular reflection"]]



class VisualizationWidget(QtWidgets.QOpenGLWidget):
    def __init__(self, *args):
        super(VisualizationWidget, self).__init__(*args)
        glutInit()

    def rotate(self, theta_x, theta_y, theta_z):
        global curAngle
        curAngle += 15

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

    def initializeGL(self):
        glClearDepth(1.0)              
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()                    
        
        glOrtho(-2, 2, -2, 2, -2, 100)

        # TODO: choose correct values
        #gluPerspective(45.0,1.33,0.1, 100.0) 
        glMatrixMode(GL_MODELVIEW)

    def init(self):
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH) 

        # Define as dimensoes da janela.
        # Define posicao inicial da janela na tela
        glEnable(GL_DEPTH_TEST) 

        glClearColor(0, 0, 1, 0)
        gluLookAt(0, 0, 2, 0, 0, 0, 0, 1, 0)
        glutDisplayFunc(self.display)


    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glMatrixMode(GL_MODELVIEW)

        glPushMatrix()
        glColor3f( 1.0, 1.5, 0.0 );
        glRotatef(curAngle, 1, 1, 1)
        glutWireCube(2)
        glPopMatrix()

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Define a matriz de projeção ortogonal
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-2, 2, -2, 2, -2, 100)
        
        # Define que irá trabalhar com a matriz de modelo/visão
        glMatrixMode(GL_MODELVIEW)
        
        # Para cada porta de visão, configura as propriedades do material e desenha o objeto
        glViewport(0,0,400,400)
        glLoadIdentity()
