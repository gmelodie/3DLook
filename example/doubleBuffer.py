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
lightTypes = [["Diffuse reflection only","No ambient or specular"],
            ["Diffuse and specular reflection", "Low shininess; no ambient"],
            ["Diffuse and specular reflection", "high shininess; no ambient"],
            ["Diffuse refl.; emission", "no ambient or specular reflection"]]


def init() :
    # Agora temos que cuidar também o buffer de profundidade.
    # Trocamos para utilizar dois buffers, deve-se trocar o glFlush() no método display() para glutSwapBuffers()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH) 
    # Define as dimensoes da janela.
    glutInitWindowSize(800, 800) 
    # Define posicao inicial da janela na tela
    glutInitWindowPosition(100, -500) 
    glutCreateWindow("Hello World!")
    # Pedimos para o OpenGL verificar o buffer de profundidade na hora de renderizar. Precisa ser depois de criada a janela!
    glEnable(GL_DEPTH_TEST) 


    glClearColor(0, 0, 1, 0)
    gluLookAt(0, 0, 2, 0, 0, 0, 0, 1, 0)

# Inicializa a luz
def initLighting() :
    # Informa que irá utilizar iluminação    
    glEnable(GL_LIGHTING)
    # Liga a luz0
    glEnable(GL_LIGHT0)
    # Informa que irá utilizar as cores do material
    glEnable(GL_COLOR_MATERIAL)

# Define a posição da luz 0
def setLight() :
    light_position = [10.0, 10.0, -20.0, 0.0]
    glLightfv(GL_LIGHT0, GL_POSITION, light_position);


# Função utilizada para definir as propriedades do material
def setMaterial(currentMaterial) :
    no_mat = [ 0.0, 0.0, 0.0, 1.0 ]
    mat_ambient = [ 0.7, 0.7, 0.7, 1.0 ]
    mat_ambient_color = [ 0.8, 0.8, 0.2, 1.0 ]
    mat_diffuse = [ 0.1, 0.5, 0.8, 1.0 ]
    mat_specular = [ 1.0, 1.0, 1.0, 1.0 ]
    no_shininess = [ 0.0 ]
    low_shininess = [ 5.0 ]
    high_shininess = [ 100.0 ]
    mat_emission = [0.3, 0.2, 0.2, 0.0]
    if currentMaterial ==  0:
        # Diffuse reflection only; no ambient or specular  
        glMaterialfv(GL_FRONT, GL_AMBIENT, no_mat);
        glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse);
        glMaterialfv(GL_FRONT, GL_SPECULAR, no_mat);
        glMaterialfv(GL_FRONT, GL_SHININESS, no_shininess);
        glMaterialfv(GL_FRONT, GL_EMISSION, no_mat);
    elif currentMaterial ==  1:
        # Diffuse and specular reflection; low shininess; no ambient
        glMaterialfv(GL_FRONT, GL_AMBIENT, no_mat);
        glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse);
        glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular);
        glMaterialfv(GL_FRONT, GL_SHININESS, low_shininess);
        glMaterialfv(GL_FRONT, GL_EMISSION, no_mat);
    elif currentMaterial ==  2:
        # Diffuse and specular reflection; high shininess; no ambient
        glMaterialfv(GL_FRONT, GL_AMBIENT, no_mat);
        glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse);
        glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular);
        glMaterialfv(GL_FRONT, GL_SHININESS, high_shininess);
        glMaterialfv(GL_FRONT, GL_EMISSION, no_mat);
    elif currentMaterial ==  3:
        # Diffuse refl.; emission; no ambient or specular reflection
        glMaterialfv(GL_FRONT, GL_AMBIENT, no_mat);
        glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse);
        glMaterialfv(GL_FRONT, GL_SPECULAR, no_mat);
        glMaterialfv(GL_FRONT, GL_SHININESS, no_shininess);
        glMaterialfv(GL_FRONT, GL_EMISSION, mat_emission);
          

# Função utizada na função de callback temporizada
def timer(value) :
    # Apenas realiza as operações de animação se estiver ligado
    if toggleAnimation :
        global curAngle
        curAngle += increment
        # Chama a função para desenhar a tela após a mudança
        display()

    # Define a função timer na função de callback temporizada
    glutTimerFunc(30, timer, 0)

# Função para capturar os eventos do teclado
def keyPressEvent(key, x, y) :
    global increment, toggleAnimation, curObject, curShading
    if key == '\x1b' :
         # Sai do programa se apertar ESC
        exit(0)
    elif key == '.' :
        # Aumenta o passo do incremento
        increment += 1
    elif key == ',' :
        # Diminui o passo do incremento
        increment += -1
    elif key == 'a' :
        # Liga ou desliga a animação
        toggleAnimation = not toggleAnimation
    elif key == 'q' :
        # Troca o objeto mostrado
        curObject += 1
        curObject %= 4
    elif key == 's' :
        curShading += 1
        curShading %= 2

# Função para definir o tipo de tonalização
def setShading(sType) :
    if sType == 0 :
        glShadeModel(GL_SMOOTH)
    elif sType == 1 :
        glShadeModel(GL_FLAT)


def drawObject(oType, currentMaterial) :
    setMaterial(currentMaterial)

    glColor3f(1,1,0)
    if oType == 0:
        glutWireCube(1)
    elif oType == 1 :
        glutSolidCube(1)
    elif oType == 2 :
        glutSolidSphere(1, 100, 100)
    elif oType == 3 :
        glutSolidTeapot(1)

# Função para desenhar a descrição de cada configuração de iluminação
def drawDescriptionText(currentMaterial) :
    glDisable(GL_LIGHTING)
    pos = 1.2
    for s in lightTypes[currentMaterial]:
        glut_print( -1.9 , pos , GLUT_BITMAP_9_BY_15 , s , 1.0 , 1.0 , 1.0 , 1.0 )
        pos -= 0.2
    glEnable(GL_LIGHTING)
    

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # Define a matriz de projeção ortogonal
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-2, 2, -2, 2, -2, 100)
    

    # Define que irá trabalhar com a matriz de modelo/visão
    glMatrixMode(GL_MODELVIEW)
    setLight()
    setShading(curShading)
    
    # Para cada porta de visão, configura as propriedades do material e desenha o objeto
    glViewport(0,0,400,400)
    glLoadIdentity()
    drawDescriptionText(0)
    glRotatef(curAngle, 1, 1, 1)
    drawObject(curObject, 0)


    glViewport(400,0,400,400)
    glLoadIdentity()
    drawDescriptionText(1)
    glRotatef(curAngle, 1, 1, 1)
    drawObject(curObject, 1)


    glViewport(0, 400 ,400,400)
    glLoadIdentity()
    drawDescriptionText(2)
    glRotatef(curAngle, 1, 1, 1)
    drawObject(curObject, 2)


    glViewport(400,400,400,400) 
    glLoadIdentity()
    drawDescriptionText(3)
    glRotatef(curAngle, 1, 1, 1)   
    drawObject(curObject, 3)

    glutSwapBuffers()

# Função utilizada para desenhar uma string na tela
def glut_print( x,  y,  font,  text, r,  g , b , a):
    blending = False 
    if glIsEnabled(GL_BLEND) :
        blending = True

    #glEnable(GL_BLEND)
    glColor3f(1,1,1)
    glRasterPos2f(x,y)
    for ch in text :
        glutBitmapCharacter( font , ctypes.c_int( ord(ch) ) )
    if not blending :
        glDisable(GL_BLEND) 


if __name__ == '__main__':
    
    glutInit()
    
    init()
    initLighting()

    glutDisplayFunc(display)
    glutKeyboardFunc(keyPressEvent)
    timer(0)
    
    glutMainLoop()