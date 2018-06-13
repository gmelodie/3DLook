# pylint: skip-file
from PyQt5 import QtWidgets, QtGui

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

curObject = 0
curShading = 0
lightTypes = [["Diffuse reflection only","No ambient or specular"],
            ["Diffuse and specular reflection", "Low shininess; no ambient"],
            ["Diffuse and specular reflection", "high shininess; no ambient"],
            ["Diffuse refl.; emission", "no ambient or specular reflection"]]


class VisualizationWidget(QtWidgets.QOpenGLWidget):
    def __init__(self, *args):
        super(VisualizationWidget, self).__init__(*args)
        self.makeCurrent()  # Necessary for integration with PyQt5
        glutInit()
        self.init()
        self.initLighting()

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
        self.shading = "FLAT"

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
        if plane_xy:
            self.scale_z *= -1
        if plane_yz:
            self.scale_x *= -1
        if plane_zx:
            self.scale_y *= -1
        self.update()

    def scale(self, dx, dy, dz):
        if dx != 0:
            self.scale_x *= dx
        if dy != 0:
            self.scale_y *= dy
        if dz != 0:
            self.scale_z *= dz
        self.update()

    def change_projection(self, projection_type):
        self.projection_type = projection_type
        self.update()


    # Função utilizada para definir as propriedades do material
    def setMaterial(self):
        print("Setting material")
        no_mat = [ 0.0, 0.0, 0.0, 1.0 ]
        mat_ambient = [ 0.7, 0.7, 0.7, 1.0 ]
        mat_ambient_color = [ 0.8, 0.8, 0.2, 1.0 ]
        mat_diffuse = [ 0.1, 0.5, 0.8, 1.0 ]
        mat_specular = [ 1.0, 1.0, 1.0, 1.0 ]
        no_shininess = [ 0.0 ] 
        low_shininess = [ 5.0 ] 
        high_shininess = [ 100.0 ]
        mat_emission = [0.3, 0.2, 0.2, 0.0]
 
        # Diffuse reflection only; no ambient or specular  
        glMaterialfv(GL_FRONT, GL_AMBIENT, no_mat)
        glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
        glMaterialfv(GL_FRONT, GL_SPECULAR, no_mat)
        glMaterialfv(GL_FRONT, GL_SHININESS, no_shininess)
        glMaterialfv(GL_FRONT, GL_EMISSION, no_mat)
    
    def changeShading(self):
        print("Changing shading")
        glShadeModel(GL_SMOOTH)
        """
        if self.shading == "FLAT":
            glShadeModel(GL_SMOOTH)
        else:
            glShadeModel(GL_FLAT)
        """

    def drawObject(self):
        self.setMaterial()
        glColor3f(1,1,0)
        glutSolidCube(1)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        if self.projection_type == 'Perspectiva':
            glFrustum(-2.0, 2.0, -2.0, 2.0, 2.0, 100.0)
            gluPerspective(45, 1, 1.7, 20)
        else:
            glOrtho(-2, 2, -2, 2, -2, 100)

        glMatrixMode(GL_MODELVIEW)

        # ADDED
        self.setLight()
        self.setShading()

        #glViewport(0,0, 400, 400)
        glLoadIdentity()
        glRotatef(60, 1, 1, 1)
        self.drawObject()

        # Uncomment when working
        """
        # The operations are done from bottom to top
        #glPushMatrix()

        #glColor3f(1.0, 1.5, 0.0) # set colour

        # Scale
        glScale(self.scale_x, self.scale_y, self.scale_z)

        # Rotations
        glRotatef(self.angle_x, 1, 0, 0)
        glRotatef(self.angle_y, 0, 1, 0)
        glRotatef(self.angle_z, 0, 0, 1)

        # Translate
        glTranslate(self.translate_x, self.translate_y, self.translate_z)

        #glutWireCube(1)
        #glPopMatrix()
        self.drawObject()
        glFlush()
        """
        glFlush()
        #glutSwapBuffers() # DOES NOT WORK since we dont have a window
        


    # TODO: Convert to english
    def initLighting(self) :
        print("Rodando init lighting")
        # Informa que irá utilizar iluminação
        glEnable(GL_LIGHTING)
        # Liga a luz0
        glEnable(GL_LIGHT0)
        # Informa que irá utilizar as cores do material
        glEnable(GL_COLOR_MATERIAL)


    # Define a posição da luz 0
    # TODO: English
    def setLight(self):
        print("Rodando set light")
        light_position = [10.0, 10.0, -20.0, 1.0]
        glLightfv(GL_LIGHT0, GL_POSITION, light_position);

    # temo
    def setShading(self):
        print("Rodando set Shading")
        glShadeModel(GL_SMOOTH)
        #glShadeModel(GL_FLAT)

    def init(self):
        # Function for correct integration with PyQt5
        #self.makeCurrent()

        # Initiation
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)

        # Check depth buffer
        glEnable(GL_DEPTH_TEST)

        glClearColor(0, 0, 1, 0)
        gluLookAt(0, 0, 2, 0, 0, 0, 0, 1, 0)
