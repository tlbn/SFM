from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import mainWindow_ctrl



app = QApplication(sys.argv)
mainWindow = mainWindow_ctrl.MainWindow()
mainWindow.show()
app.exec_()