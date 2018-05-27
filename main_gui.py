import sys

from PyQt5 import QtWidgets

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
        self.ui.choose_projection.currentTextChanged.connect(
            self.handle_choose_projection)

    def handle_choose_projection(self):
        self.widget.change_projection(str(self.ui.choose_projection.currentText()))


    def handle_apply(self):
        translate_nums = [self.ui.choose_translate_x, self.ui.choose_translate_y,
                          self.ui.choose_translate_z]
        self.widget.translate(*[convert_combo_str_to_float(var.text()) for var in translate_nums])

        scale_nums = [self.ui.choose_scale_x, self.ui.choose_scale_y,
                      self.ui.choose_scale_z]
        self.widget.scale(*[convert_combo_str_to_float(var.text()) for var in scale_nums])

        rotate_nums = [self.ui.choose_rotate_x, self.ui.choose_rotate_y,
                       self.ui.choose_rotate_z]
        self.widget.rotate(*[convert_combo_str_to_float(var.text()) for var in rotate_nums])

        planes = [self.ui.choose_plane_xy, self.ui.choose_plane_yz,
                  self.ui.choose_plane_zx]
        self.widget.mirror(*[var.isChecked() for var in planes])

def convert_combo_str_to_float(num):
    return float(num.replace(",", "."))

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
