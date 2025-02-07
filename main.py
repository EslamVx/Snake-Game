# main.py
import sys
from PyQt5 import QtWidgets, QtGui
from snake_game import SnakeGameDialog
from config import APP_ICON_PATH

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(APP_ICON_PATH))
    window = SnakeGameDialog()
    window.show()
    sys.exit(app.exec_())
