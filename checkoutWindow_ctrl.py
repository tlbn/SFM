from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

import checkoutWindow_ui

class CheckoutWindow(QDialog, checkoutWindow_ui.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)