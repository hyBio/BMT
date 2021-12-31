# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shop_windows.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BMT_client_main_windows(object):
    def setupUi(self, BMT_client_main_windows):
        BMT_client_main_windows.setObjectName("BMT_client_main_windows")
        BMT_client_main_windows.resize(1560, 990)
        BMT_client_main_windows.setMaximumSize(QtCore.QSize(1560, 990))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        BMT_client_main_windows.setFont(font)
        BMT_client_main_windows.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        BMT_client_main_windows.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/resource/BMT_64.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BMT_client_main_windows.setWindowIcon(icon)
        BMT_client_main_windows.setStyleSheet("background-color: rgb(255, 245, 220);")
        self.centralwidget = QtWidgets.QWidget(BMT_client_main_windows)
        self.centralwidget.setObjectName("centralwidget")
        self.client_name = QtWidgets.QLabel(self.centralwidget)
        self.client_name.setGeometry(QtCore.QRect(170, 30, 91, 50))
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.client_name.setFont(font)
        self.client_name.setAlignment(QtCore.Qt.AlignCenter)
        self.client_name.setObjectName("client_name")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(49, 130, 861, 801))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.table.setFont(font)
        self.table.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.table.setGridStyle(QtCore.Qt.DashLine)
        self.table.setObjectName("table")
        self.table.setColumnCount(5)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(4, item)
        self.table.horizontalHeader().setDefaultSectionSize(170)
        self.date_time = QtWidgets.QLabel(self.centralwidget)
        self.date_time.setGeometry(QtCore.QRect(1100, 10, 411, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.date_time.setFont(font)
        self.date_time.setText("")
        self.date_time.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.date_time.setObjectName("date_time")
        self.today_sales = QtWidgets.QLabel(self.centralwidget)
        self.today_sales.setGeometry(QtCore.QRect(970, 40, 250, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.today_sales.setFont(font)
        self.today_sales.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.today_sales.setObjectName("today_sales")
        self.today_pay = QtWidgets.QLabel(self.centralwidget)
        self.today_pay.setGeometry(QtCore.QRect(970, 350, 250, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.today_pay.setFont(font)
        self.today_pay.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.today_pay.setObjectName("today_pay")
        self.today_profit = QtWidgets.QLabel(self.centralwidget)
        self.today_profit.setGeometry(QtCore.QRect(970, 670, 250, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.today_profit.setFont(font)
        self.today_profit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.today_profit.setObjectName("today_profit")
        self.total_profit = QtWidgets.QLabel(self.centralwidget)
        self.total_profit.setGeometry(QtCore.QRect(1260, 670, 250, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.total_profit.setFont(font)
        self.total_profit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.total_profit.setObjectName("total_profit")
        self.total_sales = QtWidgets.QLabel(self.centralwidget)
        self.total_sales.setGeometry(QtCore.QRect(1260, 40, 250, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.total_sales.setFont(font)
        self.total_sales.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.total_sales.setObjectName("total_sales")
        self.total_pay = QtWidgets.QLabel(self.centralwidget)
        self.total_pay.setGeometry(QtCore.QRect(1260, 350, 250, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.total_pay.setFont(font)
        self.total_pay.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.total_pay.setObjectName("total_pay")
        self.today_sales_plot = QtWidgets.QLabel(self.centralwidget)
        self.today_sales_plot.setGeometry(QtCore.QRect(970, 90, 250, 250))
        self.today_sales_plot.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.today_sales_plot.setFrameShape(QtWidgets.QFrame.Box)
        self.today_sales_plot.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.today_sales_plot.setAlignment(QtCore.Qt.AlignCenter)
        self.today_sales_plot.setObjectName("today_sales_plot")
        self.total_sales_plot = QtWidgets.QLabel(self.centralwidget)
        self.total_sales_plot.setGeometry(QtCore.QRect(1260, 90, 250, 250))
        self.total_sales_plot.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.total_sales_plot.setFrameShape(QtWidgets.QFrame.Box)
        self.total_sales_plot.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.total_sales_plot.setAlignment(QtCore.Qt.AlignCenter)
        self.total_sales_plot.setObjectName("total_sales_plot")
        self.today_pay_plot = QtWidgets.QLabel(self.centralwidget)
        self.today_pay_plot.setGeometry(QtCore.QRect(970, 400, 250, 250))
        self.today_pay_plot.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.today_pay_plot.setFrameShape(QtWidgets.QFrame.Box)
        self.today_pay_plot.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.today_pay_plot.setAlignment(QtCore.Qt.AlignCenter)
        self.today_pay_plot.setObjectName("today_pay_plot")
        self.total_pay_plot = QtWidgets.QLabel(self.centralwidget)
        self.total_pay_plot.setGeometry(QtCore.QRect(1260, 400, 250, 250))
        self.total_pay_plot.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.total_pay_plot.setFrameShape(QtWidgets.QFrame.Box)
        self.total_pay_plot.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.total_pay_plot.setAlignment(QtCore.Qt.AlignCenter)
        self.total_pay_plot.setObjectName("total_pay_plot")
        self.time_from = QtWidgets.QPushButton(self.centralwidget)
        self.time_from.setGeometry(QtCore.QRect(270, 30, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.time_from.setFont(font)
        self.time_from.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.time_from.setObjectName("time_from")
        self.time_to = QtWidgets.QPushButton(self.centralwidget)
        self.time_to.setGeometry(QtCore.QRect(270, 70, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.time_to.setFont(font)
        self.time_to.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.time_to.setObjectName("time_to")
        self.refresh = QtWidgets.QPushButton(self.centralwidget)
        self.refresh.setGeometry(QtCore.QRect(590, 70, 75, 30))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.refresh.setFont(font)
        self.refresh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.refresh.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.refresh.setObjectName("refresh")
        self.sales_trend_plot = QtWidgets.QLabel(self.centralwidget)
        self.sales_trend_plot.setGeometry(QtCore.QRect(970, 710, 540, 250))
        self.sales_trend_plot.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sales_trend_plot.setFrameShape(QtWidgets.QFrame.Box)
        self.sales_trend_plot.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.sales_trend_plot.setAlignment(QtCore.Qt.AlignCenter)
        self.sales_trend_plot.setObjectName("sales_trend_plot")
        self.Increase_inventory = QtWidgets.QPushButton(self.centralwidget)
        self.Increase_inventory.setGeometry(QtCore.QRect(680, 70, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.Increase_inventory.setFont(font)
        self.Increase_inventory.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Increase_inventory.setObjectName("Increase_inventory")
        self.call_for_help = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.call_for_help.setGeometry(QtCore.QRect(680, 10, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.call_for_help.setFont(font)
        self.call_for_help.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.call_for_help.setToolTipDuration(0)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ico/resource/BMT_32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.call_for_help.setIcon(icon1)
        self.call_for_help.setObjectName("call_for_help")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(820, 940, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.client_logo = QtWidgets.QLabel(self.centralwidget)
        self.client_logo.setGeometry(QtCore.QRect(60, 10, 128, 128))
        self.client_logo.setObjectName("client_logo")
        self.client_name.raise_()
        self.client_logo.raise_()
        self.table.raise_()
        self.date_time.raise_()
        self.today_sales_plot.raise_()
        self.total_sales_plot.raise_()
        self.today_pay_plot.raise_()
        self.total_pay_plot.raise_()
        self.time_from.raise_()
        self.time_to.raise_()
        self.refresh.raise_()
        self.sales_trend_plot.raise_()
        self.Increase_inventory.raise_()
        self.call_for_help.raise_()
        self.back.raise_()
        self.today_pay.raise_()
        self.total_sales.raise_()
        self.total_pay.raise_()
        self.today_profit.raise_()
        self.total_profit.raise_()
        self.today_sales.raise_()
        BMT_client_main_windows.setCentralWidget(self.centralwidget)

        self.retranslateUi(BMT_client_main_windows)
        QtCore.QMetaObject.connectSlotsByName(BMT_client_main_windows)

    def retranslateUi(self, BMT_client_main_windows):
        _translate = QtCore.QCoreApplication.translate
        BMT_client_main_windows.setWindowTitle(_translate("BMT_client_main_windows", "BMT_client"))
        self.client_name.setText(_translate("BMT_client_main_windows", "<html><head/><body><p><span style=\" font-size:28pt; font-style:italic;\">BMT</span></p></body></html>"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("BMT_client_main_windows", "书籍类别"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("BMT_client_main_windows", "书籍名称"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("BMT_client_main_windows", "销量"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("BMT_client_main_windows", "销售额"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("BMT_client_main_windows", "利润"))
        self.today_sales.setText(_translate("BMT_client_main_windows", "今日销售额："))
        self.today_pay.setText(_translate("BMT_client_main_windows", "今日支出："))
        self.today_profit.setText(_translate("BMT_client_main_windows", "今日利润："))
        self.total_profit.setText(_translate("BMT_client_main_windows", "累计利润："))
        self.total_sales.setText(_translate("BMT_client_main_windows", "累计销售额："))
        self.total_pay.setText(_translate("BMT_client_main_windows", "累计支出："))
        self.today_sales_plot.setText(_translate("BMT_client_main_windows", "today_sales_plot"))
        self.total_sales_plot.setText(_translate("BMT_client_main_windows", "total_sales_plot"))
        self.today_pay_plot.setText(_translate("BMT_client_main_windows", "today_pay_plot"))
        self.total_pay_plot.setText(_translate("BMT_client_main_windows", "total_pay_plot"))
        self.time_from.setText(_translate("BMT_client_main_windows", "从"))
        self.time_to.setText(_translate("BMT_client_main_windows", "到"))
        self.refresh.setText(_translate("BMT_client_main_windows", "刷新"))
        self.sales_trend_plot.setText(_translate("BMT_client_main_windows", "sales_trend_plot"))
        self.Increase_inventory.setText(_translate("BMT_client_main_windows", "增加库存"))
        self.call_for_help.setToolTip(_translate("BMT_client_main_windows", "<html><head/><body><p><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">huyan35@mail2.sysu.edu.cn</span></p></body></html>"))
        self.call_for_help.setText(_translate("BMT_client_main_windows", "联系客服(点我复制)"))
        self.back.setText(_translate("BMT_client_main_windows", "回到主页>"))
        self.client_logo.setText(_translate("BMT_client_main_windows", "<html><head/><body><p><img src=\":/logo/resource/BMT_128.ico\"/></p></body></html>"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BMT_client_main_windows = QtWidgets.QMainWindow()
    ui = Ui_BMT_client_main_windows()
    ui.setupUi(BMT_client_main_windows)
    BMT_client_main_windows.show()
    sys.exit(app.exec_())
