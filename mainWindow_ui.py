# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Fri May 29 15:54:47 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1072, 821)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.checkout_table = QtGui.QTableView(self.tab)
        self.checkout_table.setAlternatingRowColors(True)
        self.checkout_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.checkout_table.setObjectName(_fromUtf8("checkout_table"))
        self.gridLayout.addWidget(self.checkout_table, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.dictors_table = QtGui.QTableView(self.tab_2)
        self.dictors_table.setObjectName(_fromUtf8("dictors_table"))
        self.gridLayout_3.addWidget(self.dictors_table, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.customers_table = QtGui.QTableView(self.tab_3)
        self.customers_table.setObjectName(_fromUtf8("customers_table"))
        self.gridLayout_4.addWidget(self.customers_table, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1072, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menu = QtGui.QMenu(self.menuBar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_2 = QtGui.QMenu(self.menuBar)
        self.menu_2.setObjectName(_fromUtf8("menu_2"))
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_newCheckout = QtGui.QAction(MainWindow)
        self.action_newCheckout.setObjectName(_fromUtf8("action_newCheckout"))
        self.menu_2.addAction(self.action_newCheckout)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())
        self.toolBar.addAction(self.action_newCheckout)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "SFManager", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Заказы", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Дикторы", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Заказчики", None))
        self.menu.setTitle(_translate("MainWindow", "Файл", None))
        self.menu_2.setTitle(_translate("MainWindow", "Заказы", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.action_newCheckout.setText(_translate("MainWindow", "Новый заказ", None))

