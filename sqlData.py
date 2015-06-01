import os, sys
from PyQt4 import QtSql
from PyQt4 import QtCore




class CheckoutModel(QtSql.QSqlTableModel):
    def __init__(self):
        self.dbConnect()
        QtSql.QSqlTableModel.__init__(self)
        # queryAll = QtSql.QSqlQuery()
        # queryAll.exec_("Select * from checkout")
        # self.setQuery(queryAll)
        self.setTable("CHECKOUT")
        self.setEditStrategy(QtSql.QSqlTableModel.OnRowChange)
        self.sort(0, 1)
        self.select()

    def flags(self, QModelIndex):
        flags = super(CheckoutModel, self).flags(QModelIndex)
        if QModelIndex.column() == 2:
            flags |= QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled
        return flags




        #self.setFilter()

    def makeDb(self):

        mydb = sqlite3.connect("silaDB.db")

        mydb.execute("CREATE TABLE IF NOT EXISTS CHECKOUT"
                     "(ID_CHECKOUT INTEGER PRIMARY KEY,"
                     "DATA TEXT,"
                     "TITLE TEXT,"
                     "TYPE TEXT,"
                     "CUSTOMER TEXT,"
                     "PAYVALUE TEXT,"
                     "PAYTYPE TEXT,"
                     "PAYSTATUS TEXT,"
                     "STATUS TEXT)")

        mydb.execute("CREATE TABLE IF NOT EXISTS DICTORS"
                     "(ID_DICTOR INTEGER PRIMARY KEY,"
                     "NAME TEXT,"
                     "CITY TEXT,"
                     "EMAIL TEXT,"
                     "ICQ TEXT,"
                     "CUSTOMER TEXT,"
                     "TELEPHONE TEXT)")

        mydb.execute("CREATE TABLE IF NOT EXISTS DICTORS_PAYTYPE"
                     "(ID_DICTOR INTEGER PRIMARY KEY,"
                     "TITLE TEXT,"
                     "NUMBER TEXT)")




    def dbConnect(self):
        if not os.path.exists("silaDB.db"):
            DbCreate.createDb()

        self.myDb = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.myDb.setDatabaseName("silaDB.db")
        if self.myDb.open():
            print("OPEN")

    @staticmethod
    def addCheckout():
        query = QtSql.QSqlQuery()
        query.prepare("insert into table1 (first, second) values (:one, :two)")
        # query.addBindValue("5656")
        query.bindValue(":one", "one")
        query.bindValue(":two", "two")
        query.exec_()


class DbCreate(object):
    @staticmethod
    def createDb():

        import sqlite3
        mydb = sqlite3.connect("silaDB.db")

        mydb.execute("CREATE TABLE IF NOT EXISTS CHECKOUT"
                     "(ID_CHECKOUT INTEGER PRIMARY KEY,"
                     "DATA TEXT,"
                     "TITLE TEXT,"
                     "TYPE TEXT,"
                     "CUSTOMER TEXT,"
                     "PAYVALUE TEXT,"
                     "PAYTYPE TEXT,"
                     "PAYSTATUS TEXT,"
                     "STATUS TEXT)")

        mydb.execute("CREATE TABLE IF NOT EXISTS DICTORS"
                     "(ID_DICTOR INTEGER PRIMARY KEY,"
                     "NAME TEXT,"
                     "CITY TEXT,"
                     "EMAIL TEXT,"
                     "ICQ TEXT,"
                     "CUSTOMER TEXT,"
                     "TELEPHONE TEXT)")

        mydb.execute("CREATE TABLE IF NOT EXISTS DICTORS_PAYTYPE"
                     "(ID_DICTOR INTEGER PRIMARY KEY,"
                     "TITLE TEXT,"
                     "NUMBER TEXT)")