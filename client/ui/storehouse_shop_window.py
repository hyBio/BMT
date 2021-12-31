# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'storehouse_shop_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_shop_window(object):
    def setupUi(self, shop_window):
        shop_window.setObjectName("shop_window")
        shop_window.resize(850, 930)
        shop_window.setMaximumSize(QtCore.QSize(850, 930))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        shop_window.setFont(font)
        shop_window.setWindowTitle("采购单")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/resource/BMT_64.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        shop_window.setWindowIcon(icon)
        shop_window.setStyleSheet("background-color: rgb(193, 200, 187);")
        self.centralwidget = QtWidgets.QWidget(shop_window)
        self.centralwidget.setObjectName("centralwidget")
        self.client_name = QtWidgets.QLabel(self.centralwidget)
        self.client_name.setGeometry(QtCore.QRect(140, 30, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.client_name.setFont(font)
        self.client_name.setAlignment(QtCore.Qt.AlignCenter)
        self.client_name.setObjectName("client_name")
        self.generate = QtWidgets.QPushButton(self.centralwidget)
        self.generate.setGeometry(QtCore.QRect(700, 60, 121, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.generate.setFont(font)
        self.generate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.generate.setObjectName("generate")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 110, 800, 800))
        self.tableWidget.setMinimumSize(QtCore.QSize(800, 800))
        self.tableWidget.setMaximumSize(QtCore.QSize(800, 800))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(252)
        self.tableWidget.verticalHeader().setDefaultSectionSize(36)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 0, 131, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.client_logo = QtWidgets.QLabel(self.centralwidget)
        self.client_logo.setGeometry(QtCore.QRect(30, -10, 128, 128))
        self.client_logo.setObjectName("client_logo")
        self.client_name.raise_()
        self.client_logo.raise_()
        self.generate.raise_()
        self.tableWidget.raise_()
        self.label.raise_()
        shop_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(shop_window)
        QtCore.QMetaObject.connectSlotsByName(shop_window)

    def retranslateUi(self, shop_window):
        _translate = QtCore.QCoreApplication.translate
        self.client_name.setText(_translate("shop_window", "<html><head/><body><p><span style=\" font-size:28pt; font-style:italic;\">BMT</span></p></body></html>"))
        self.generate.setText(_translate("shop_window", "导出采购单"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("shop_window", "书目类别"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("shop_window", "书籍名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("shop_window", "采购数量"))
        self.label.setText(_translate("shop_window", "采购单"))
        self.client_logo.setText(_translate("shop_window", "<html><head/><body><p><img src=\":/logo/resource/BMT_128.ico\"/></p></body></html>"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    shop_window = QtWidgets.QMainWindow()
    ui = Ui_shop_window()
    ui.setupUi(shop_window)
    shop_window.show()
    sys.exit(app.exec_())
