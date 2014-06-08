'''
Easy integration of DataFrame into pyqt framework

@author: Jev Kuznetsov
'''
try:
    from PyQt4.QtCore import QAbstractTableModel, Qt, QVariant, QModelIndex
    from PyQt4.QtGui import (QApplication, QDialog, QVBoxLayout, QTableView, QWidget)
except ImportError:
    from PySide.QtCore import QAbstractTableModel, Qt, QModelIndex
    from PySide.QtGui import (QApplication, QDialog, QVBoxLayout, QTableView, QWidget)
    QVariant = lambda value=None: value

from pandas import DataFrame, Index
import sys
import numpy as np
from PyQt4.QtCore import QRect
import pyodbc
import pandas.io.sql as psql
class DataFrameModel(QAbstractTableModel):
    ''' data model for a DataFrame class '''
    def __init__(self):
        super(DataFrameModel, self).__init__()
        self.df = DataFrame()

    def setDataFrame(self, dataFrame):
        self.df = dataFrame

    def signalUpdate(self):
        ''' tell viewers to update their data (this is full update, not
        efficient)'''
        self.layoutChanged.emit()

    #------------- table display functions -----------------
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return QVariant()

        if orientation == Qt.Horizontal:
            try:
                return self.df.columns.tolist()[section]
            except (IndexError, ):
                return QVariant()
        elif orientation == Qt.Vertical:
            try:
                # return self.df.index.tolist()
                return self.df.index.tolist()[section]
            except (IndexError, ):
                return QVariant()

    def data(self, index, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return QVariant()

        if not index.isValid():
            return QVariant()

        return QVariant(unicode(self.df.ix[index.row(), index.column()]).encode("utf-8").decode("utf-8"))

    def flags(self, index):
            flags = super(DataFrameModel, self).flags(index)
            flags |= Qt.ItemIsEditable
            return flags

    def setData(self, index, value, role):
        row = self.df.index[index.row()]
        col = self.df.columns[index.column()]
        if hasattr(value, 'toPyObject'):
            # PyQt4 gets a QVariant
            value = value.toPyObject()
        else:
            # PySide gets an unicode
            dtype = self.df[col].dtype
            if dtype != object:
                value = None if value == '' else dtype.type(value)
        self.df.set_value(row, col, value)
        return True

    def rowCount(self, index=QModelIndex()):
        return self.df.shape[0]

    def columnCount(self, index=QModelIndex()):
        return self.df.shape[1]


class DataFrameWidget(QWidget):
    ''' a simple widget for using DataFrames in a gui '''
    def __init__(self, dataFrame, parent=None):
        super(DataFrameWidget, self).__init__(parent)

        self.dataModel = DataFrameModel()
        self.dataTable = QTableView()
        self.dataTable.setModel(self.dataModel)

        layout = QVBoxLayout()
        layout.addWidget(self.dataTable)

        self.setLayout(layout)
        # Set DataFrame
        self.setDataFrame(dataFrame)

    def setDataFrame(self, dataFrame):
        self.dataModel.setDataFrame(dataFrame)
        self.dataModel.signalUpdate()
        self.dataTable.resizeColumnsToContents()

#-----------------stand alone test code


def testDf():
    ''' creates test dataframe '''
    #data = {'int': [1, 2, 3], 'float': [1.5, 2.5, 3.5],'string': ['a', 'b', 'c'], 'nan': [np.nan, np.nan, np.nan]}
    #return DataFrame(data, index=Index(['AAA', 'BBB', 'CCC']),columns=['int', 'float', 'string', 'nan'])
    connection_info="DRIVER={SQL Server};SERVER=127.0.0.1\MSSQLSERVERCM;DATABASE=ImageDB;UID=sa;PWD=111"
    cnxn = pyodbc.connect(connection_info) 
    cursor = cnxn.cursor()
    sql = "SELECT * FROM JDMCL Where ID<3000"
    df = psql.frame_query(sql, cnxn)
    #cnxn.close()
    print type(df.head())
    print df
    return df

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        df = testDf()  # make up some data
        self.widget = DataFrameWidget(df)
#        self.widget.resizeEvent()

        layout = QVBoxLayout()
        layout.addWidget(self.widget)
        #layout.setGeometry(QRect(1, 1, 1, 1))
        self.setLayout(layout)

if __name__ == '__main__':


    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()
