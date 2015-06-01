from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtSql
import sys
import sqlData

import mainWindow_ui
import checkoutWindow_ctrl

class MainWindow(QMainWindow, mainWindow_ui.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.action_newCheckout.triggered.connect(self.checkoutWinOpen)


        self.searchLine = QLineEdit()
        self.toolBar.addWidget(self.searchLine)

        self.model = sqlData.CheckoutModel()
        self.checkout_table.setModel(self.model)
        # self.tableView.resizeColumnsToContents()

    def checkoutWinOpen(self):

        # self.model.insertRows(self.model.rowCount(), 1)
        # self.model.insertRow(self.model.rowCount())
        # self.model.setData(self.model.index(self.model.rowCount(), 0), "123123")

        # query = QtSql.QSqlQuery()
        # query.prepare("insert into table1 (first, second) values (:one, :two)")
        # # query.addBindValue("5656")
        # query.bindValue(":one", "one")
        # query.bindValue(":two", "two")
        # query.exec_()
        sqlData.CheckoutModel.addCheckout()
        self.model.select()



        #
        # self.checkoutWin = checkoutWindow_ctrl.CheckoutWindow()
        # self.checkoutWin.show()

