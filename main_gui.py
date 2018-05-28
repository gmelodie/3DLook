import sys

from PyQt5 import QtWidgets, QtCore

from autoMainWindow import Ui_MainWindow
import visualization

REPETITIONS = 100

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args):
        super(MainWindow, self).__init__(*args)
        self.ui = Ui_MainWindow()

        # Set up OpenGL
        self.ui.setupUi(self)
        self.widget = visualization.VisualizationWidget()
        self.ui.father_layout.addWidget(self.widget)

        # Helper variables
        self.timer = None
        self.updating = False
        self.reps = 0

        # Connect buttons
        self.ui.button_apply.clicked.connect(self.handle_apply)
        self.ui.choose_projection.currentTextChanged.connect(
            self.handle_choose_projection)

    def handle_choose_projection(self):
        self.widget.change_projection(str(self.ui.choose_projection.currentText()))

    def handle_apply(self):
        if self.updating:
            self.warning("Atualizacao ja em progresso!")
            return

        # Read input from user
        translate_nums = [self.ui.choose_translate_x, self.ui.choose_translate_y,
                          self.ui.choose_translate_z]
        scale_nums = [self.ui.choose_scale_x, self.ui.choose_scale_y,
                      self.ui.choose_scale_z]
        rotate_nums = [self.ui.choose_rotate_x, self.ui.choose_rotate_y,
                       self.ui.choose_rotate_z]
        planes = [self.ui.choose_plane_xy, self.ui.choose_plane_yz,
                  self.ui.choose_plane_zx]

        # Create timers and set mode to updating
        self.updating = True
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(
            lambda: self.continuos_updates(translate_nums, scale_nums, rotate_nums, planes))
        self.timer.start(10)

    def continuos_updates(self, translate_nums, scale_nums, rotate_nums, planes):
        self.reps += 1

        # First perform continously translate
        if self.reps < REPETITIONS:
            self.widget.translate(*[convert_combo_str_to_float(var.text()) / REPETITIONS
                                    for var in translate_nums])

        # Then perform continously rotate
        elif REPETITIONS <= self.reps <= 2*REPETITIONS:
            self.widget.rotate(*[convert_combo_str_to_float(var.text()) / REPETITIONS
                                 for var in rotate_nums])

        # If done, stop timer and do non-continuos updates
        else:
            self.timer.stop()
            self.widget.scale(*[convert_combo_str_to_float(var.text()) for var in scale_nums])
            self.widget.mirror(*[var.isChecked() for var in planes])
            self.updating = False
            self.reps = 0

    def warning(self, message):
        box = QtWidgets.QMessageBox()
        box.setIcon(QtWidgets.QMessageBox.Question)
        box.setWindowTitle('Atenção!')
        box.setText(message)
        box.setStandardButtons(QtWidgets.QMessageBox.Yes)
        button_yes = box.button(QtWidgets.QMessageBox.Yes)
        button_yes.setText('Ok')
        box.exec_()

        if box.clickedButton() == button_yes:  # Yes pressed
            box.close()

    # Overloading close window function
    def closeEvent(self, event):
        # Verifies if the user wants to exit the window
        box = QtWidgets.QMessageBox()
        box.setIcon(QtWidgets.QMessageBox.Question)
        box.setWindowTitle('Saindo!')
        box.setText('Tem certeza que quer sair?')
        box.setStandardButtons(QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        button_yes = box.button(QtWidgets.QMessageBox.Yes)
        button_yes.setText('Sim')
        button_no = box.button(QtWidgets.QMessageBox.No)
        button_no.setText('Não')
        box.exec_()

        if box.clickedButton() == button_yes:  # Yes pressed
            event.accept()
        elif box.clickedButton() == button_no:
            event.ignore()


def convert_combo_str_to_float(num):
    return float(num.replace(",", "."))

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
