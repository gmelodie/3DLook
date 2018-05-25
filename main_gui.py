import sys

from PyQt5 import QtWidgets, QtCore, uic


from autoMainWindow import Ui_MainWindow
import visulization

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args):
        super(MainWindow, self).__init__(*args)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.widget = visulization.VisualizationWidget()
        self.ui.father_layout.addWidget(self.widget)

        # Connect buttons
        self.ui.button_apply.clicked.connect(self.handle_apply)

    def handle_apply(self):
        translate_nums = [self.ui.choose_translate_x, self.ui.choose_translate_y,
                          self.ui.choose_translate_z]
        self.widget.translate(*[float(x.text()) for x in translate_nums])
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
