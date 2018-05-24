import sys

from PyQt5 import QtWidgets, QtCore, uic

from OpenGL import GL as gl
from OpenGL import GLU as glu
# from OpenGL import GLUT

from autoMainWindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args):
        super(MainWindow, self).__init__(*args)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.openGLWidget.initializeGL()
        self.ui.openGLWidget.resizeGL(651, 551)
        self.ui.openGLWidget.paintGL = self.paintGL

        # Connect buttons
        self.ui.button_apply.clicked.connect(lambda x: print("mm"))

    def paintGL(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        gl.glColor3f(1, 0, 0)
        gl.glBegin(gl.GL_TRIANGLES)
        gl.glVertex3f(-0.5, -0.5, 0)
        gl.glVertex3f(0.5, -0.5, 0)
        gl.glVertex3f(0.0, 0.5, 0)
        gl.glEnd()

        glu.gluPerspective(45, 651/551, 0.1, 50.0)
        gl.glTranslatef(0.0, 0.0, -5)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
