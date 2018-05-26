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
curAngle = 0
increment = 1

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
        self.init()
        self.initLighting()
        self.display()

        # Draw solid cube
        
    def init(self) :
        # Agora temos que cuidar também o buffer de profundidade.
        # Trocamos para utilizar dois buffers, deve-se trocar o glFlush() no método display() para glutSwapBuffers()
        # Define as dimensoes da janela.
        # Define posicao inicial da janela na tela
        # Pedimos para o OpenGL verificar o buffer de profundidade na hora de renderizar. Precisa ser depois de criada a janela!
        glEnable(GL_DEPTH_TEST) 
        glClearColor(0, 0, 1, 0)
        glutInit()


    # Inicializa a luz
    def initLighting(self) :
        # Informa que irá utilizar iluminação    
        glEnable(GL_LIGHTING)
        # Liga a luz0
        glEnable(GL_LIGHT0)
        # Informa que irá utilizar as cores do material
        glEnable(GL_COLOR_MATERIAL)

    # Define a posição da luz 0
    def setLight(self) :
        light_position = [10.0, 10.0, -20.0, 0.0]
        glLightfv(GL_LIGHT0, GL_POSITION, light_position);

    # Função para definir o tipo de tonalização
    def setShading(self, sType) :
        if sType == 0 :
            glShadeModel(GL_SMOOTH)
        elif sType == 1 :
            glShadeModel(GL_FLAT)


    def drawObject(self):
        print("drawing wire cube, there should only be 1 print")
        glColor3f(1,1,0)
        glutWireCube(1)

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Define a matriz de projeção ortogonal
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-2, 2, -2, 2, -2, 100)
        

        # Define que irá trabalhar com a matriz de modelo/visão
        glMatrixMode(GL_MODELVIEW)
        self.setLight()
        self.setShading(curShading)
        
        # Para cada porta de visão, configura as propriedades do material e desenha o objeto
        glViewport(0,0,400,400)
        glLoadIdentity()
        self.drawObject()

