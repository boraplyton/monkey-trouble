from PyQt5.QtWidgets import QApplication
import sys

from UI.MainWindow import MainWindow


def application():
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
