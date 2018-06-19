# pylint: disable=unused-wildcard-import
# pylint: disable=wildcard-import
# pylint: disable=invalid-name
# coding=utf-8

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

# Variables
projection_type = "Ortogonal"
shading = "FLAT"
ortho_project = True

X, Y, Z = 0, 1, 2
ESC = b'\x1b'

# Defines the various types of transformations
TRANSLATE = b"t"
SCALE = b"s"
ROTATE = b"r"
MIRROR = b"m"

KEY_NAME = {
    TRANSLATE: "Translate",
    SCALE: "Scale",
    ROTATE: "Rotate",
    MIRROR: "Mirror"
}

BYTE_KEY = {
    b'x': X,
    b'y': Y,
    b'z': Z
}

KEY_MAP = {
    TRANSLATE: [0, 0, 0],
    SCALE: [1, 1, 1],
    ROTATE: [0, 0, 0],
    MIRROR: [False, False, False]
}

current_key_type = ROTATE

# Window variables
WIDTH = HEIGHT = 800

def keyPressEvent(key, x, y):
    """
    Capture and process the keystrokes
    """
    global increment, toggleAnimation, curObject, curShading, project_type,\
           ortho_project, current_key_type

    if key == ESC:
        exit(0)

    # Higer/lower increment
    elif key == b'.':
        increment += 1
    elif key == b',':
        increment += -1

    # Turn animation on/off
    elif key == b'a':
        toggleAnimation = not toggleAnimation

    # Change the projection type
    elif key == b'p':
        ortho_project = not ortho_project

    # Swap object
    elif key == b'q':
        curObject += 1
        curObject %= 4

    # Change shading
    elif key == b'k':
        curShading += 1
        curShading %= 2

    # Change the current settings
    elif key in [TRANSLATE, ROTATE, SCALE, MIRROR]:
        current_key_type = key

    elif key in [b'x', b'y', b'z']:
        if current_key_type == TRANSLATE:
            KEY_MAP[TRANSLATE][BYTE_KEY[key]] += increment/10
        elif current_key_type == ROTATE:
            KEY_MAP[ROTATE][BYTE_KEY[key]] += increment
        elif current_key_type == SCALE:
            KEY_MAP[SCALE][BYTE_KEY[key]] *= increment*1.1
        elif current_key_type == MIRROR:
            KEY_MAP[MIRROR][BYTE_KEY[key]] = not KEY_MAP[MIRROR][BYTE_KEY[key]]


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Change projection type
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if ortho_project:
        glFrustum(-2.0, 2.0, -2.0, 2.0, 2.0, 100.0)
        gluPerspective(45, 1, 1.7, 20)
    else:
        glOrtho(-2, 2, -2, 2, -2, 100)

    # Changes to modelview
    glMatrixMode(GL_MODELVIEW)
    setLight()
    setShading(curShading)

    # Define the material and draw the object
    glViewport(0, 0, WIDTH, HEIGHT)
    glLoadIdentity()

    # Updates in scales, rotation and translation
    glScale(KEY_MAP[SCALE][X], KEY_MAP[SCALE][Y], KEY_MAP[SCALE][Z])

    glRotatef(KEY_MAP[ROTATE][X], 1, 0, 0)
    glRotatef(KEY_MAP[ROTATE][Y], 0, 1, 0)
    glRotatef(KEY_MAP[ROTATE][Z], 0, 0, 1)

    glTranslate(KEY_MAP[TRANSLATE][X], KEY_MAP[TRANSLATE][Y], KEY_MAP[TRANSLATE][Z])

    # Draw object
    drawObject(curObject, 1)

    glFlush
    glutSwapBuffers()


def drawObject(oType, currentMaterial):
    """
    Draw the given material wanted by the user
    """
    setMaterial(currentMaterial)

    glColor3f(1,1,0)
    if oType == 0:
        glutWireCube(1)
    elif oType == 1:
        glutSolidCube(1)
    elif oType == 2:
        glutSolidSphere(1, 100, 100)
    elif oType == 3:
        glutSolidTeapot(1)


def setShading(sType):
    """
    Change the shading type
    """
    if sType == 0:
        glShadeModel(GL_SMOOTH)
    elif sType == 1:
        glShadeModel(GL_FLAT)


def init():
    """
    Initialize need atributes and checks for the window
    """
    # Use two buffers for depth
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutInitWindowPosition(100, -500) # Initial window position

    glutCreateWindow("OpenGL eh super legal!")

    # Check the depth buffer when rendering
    glEnable(GL_DEPTH_TEST)

    glClearColor(0, 0, 1, 0)
    gluLookAt(0, 0, 2, 0, 0, 0, 0, 1, 0)


def initLighting():
    """
    Starts the light for the scene
    """
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    # use material coloursl
    glEnable(GL_COLOR_MATERIAL)


def setLight():
    """
    Defines the zeroth light caracteristics
    """
    light_position = [10.0, 10.0, -20.0, 0.0]
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)


def setMaterial(currentMaterial):
    """
    Defines the proprierties of the material
    """
    no_mat = [0.0, 0.0, 0.0, 1.0]
    mat_ambient = [0.7, 0.7, 0.7, 1.0]
    mat_ambient_color = [0.8, 0.8, 0.2, 1.0]
    mat_diffuse = [0.1, 0.5, 0.8, 1.0]
    mat_specular = [1.0, 1.0, 1.0, 1.0]
    no_shininess = [0.0]
    low_shininess = [5.0]
    high_shininess = [100.0]
    mat_emission = [0.3, 0.2, 0.2, 0.0]

    # Diffuse refl.; emission; no ambient or specular reflection
    glMaterialfv(GL_FRONT, GL_AMBIENT, no_mat)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, no_mat)
    glMaterialfv(GL_FRONT, GL_SHININESS, no_shininess)
    glMaterialfv(GL_FRONT, GL_EMISSION, mat_emission)


def timer(value):
    """
    Callback function for our timer
    """
    if toggleAnimation:
        global curAngle
        curAngle += increment
        display()   # Update the screen

    # Restart the timer
    glutTimerFunc(30, timer, 0)

   
if __name__ == '__main__':
    # Intialize needed function
    glutInit()
    init()
    initLighting()
    
    # Set our display and keypress functions
    glutDisplayFunc(display)
    glutKeyboardFunc(keyPressEvent)
    timer(0)

    glutMainLoop()
