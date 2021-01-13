from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from Controller import MainScreen

app = QtWidgets.QApplication(sys.argv)
myapp = MainScreen()
myapp.show()   
sys.exit(app.exec_())
