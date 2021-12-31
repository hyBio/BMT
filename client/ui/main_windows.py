# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_windows.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BMT_client_main_windows(object):
    def setupUi(self, BMT_client_main_windows):
        BMT_client_main_windows.setObjectName("BMT_client_main_windows")
        BMT_client_main_windows.resize(800, 794)
        BMT_client_main_windows.setMaximumSize(QtCore.QSize(800, 800))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        BMT_client_main_windows.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/resource/BMT_64.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BMT_client_main_windows.setWindowIcon(icon)
        BMT_client_main_windows.setStyleSheet("background-color: rgb(238, 255, 243);")
        self.centralwidget = QtWidgets.QWidget(BMT_client_main_windows)
        self.centralwidget.setObjectName("centralwidget")
        self.welcome_log_in = QtWidgets.QPushButton(self.centralwidget)
        self.welcome_log_in.setGeometry(QtCore.QRect(170, 10, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.welcome_log_in.setFont(font)
        self.welcome_log_in.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.welcome_log_in.setObjectName("welcome_log_in")
        self.welcome_register = QtWidgets.QPushButton(self.centralwidget)
        self.welcome_register.setGeometry(QtCore.QRect(340, 10, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.welcome_register.setFont(font)
        self.welcome_register.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.welcome_register.setObjectName("welcome_register")
        self.call_for_help = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.call_for_help.setGeometry(QtCore.QRect(610, 10, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.call_for_help.setFont(font)
        self.call_for_help.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.call_for_help.setToolTipDuration(0)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ico/resource/BMT_32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.call_for_help.setIcon(icon1)
        self.call_for_help.setObjectName("call_for_help")
        self.search_input = QtWidgets.QLineEdit(self.centralwidget)
        self.search_input.setGeometry(QtCore.QRect(210, 80, 471, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.search_input.setFont(font)
        self.search_input.setText("")
        self.search_input.setMaxLength(30)
        self.search_input.setObjectName("search_input")
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(690, 80, 75, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.search.setFont(font)
        self.search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search.setObjectName("search")
        self.client_name = QtWidgets.QLabel(self.centralwidget)
        self.client_name.setGeometry(QtCore.QRect(60, 10, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.client_name.setFont(font)
        self.client_name.setAlignment(QtCore.Qt.AlignCenter)
        self.client_name.setObjectName("client_name")
        self.client_logo = QtWidgets.QLabel(self.centralwidget)
        self.client_logo.setGeometry(QtCore.QRect(55, 55, 128, 128))
        self.client_logo.setObjectName("client_logo")
        self.books_recommend = QtWidgets.QPushButton(self.centralwidget)
        self.books_recommend.setGeometry(QtCore.QRect(60, 540, 80, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.books_recommend.setFont(font)
        self.books_recommend.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.books_recommend.setObjectName("books_recommend")
        self.books_on_sale = QtWidgets.QPushButton(self.centralwidget)
        self.books_on_sale.setGeometry(QtCore.QRect(300, 540, 80, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.books_on_sale.setFont(font)
        self.books_on_sale.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.books_on_sale.setObjectName("books_on_sale")
        self.books_recommend_pic = QtWidgets.QLabel(self.centralwidget)
        self.books_recommend_pic.setGeometry(QtCore.QRect(60, 580, 200, 200))
        self.books_recommend_pic.setObjectName("books_recommend_pic")
        self.books_on_sale_pic = QtWidgets.QLabel(self.centralwidget)
        self.books_on_sale_pic.setGeometry(QtCore.QRect(300, 580, 200, 200))
        self.books_on_sale_pic.setObjectName("books_on_sale_pic")
        self.manual = QtWidgets.QPushButton(self.centralwidget)
        self.manual.setGeometry(QtCore.QRect(440, 10, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.manual.setFont(font)
        self.manual.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.manual.setObjectName("manual")
        self.books_for_you = QtWidgets.QPushButton(self.centralwidget)
        self.books_for_you.setGeometry(QtCore.QRect(540, 540, 80, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.books_for_you.setFont(font)
        self.books_for_you.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.books_for_you.setObjectName("books_for_you")
        self.books_for_you_pic = QtWidgets.QLabel(self.centralwidget)
        self.books_for_you_pic.setGeometry(QtCore.QRect(540, 580, 200, 200))
        self.books_for_you_pic.setObjectName("books_for_you_pic")
        self.novel = QtWidgets.QPushButton(self.centralwidget)
        self.novel.setGeometry(QtCore.QRect(190, 130, 80, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.novel.setFont(font)
        self.novel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.novel.setToolTip("")
        self.novel.setObjectName("novel")
        self.music = QtWidgets.QPushButton(self.centralwidget)
        self.music.setGeometry(QtCore.QRect(620, 130, 80, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.music.setFont(font)
        self.music.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.music.setToolTip("")
        self.music.setObjectName("music")
        self.political = QtWidgets.QPushButton(self.centralwidget)
        self.political.setGeometry(QtCore.QRect(400, 130, 80, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.political.setFont(font)
        self.political.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.political.setToolTip("")
        self.political.setObjectName("political")
        self.education = QtWidgets.QPushButton(self.centralwidget)
        self.education.setGeometry(QtCore.QRect(290, 130, 80, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.education.setFont(font)
        self.education.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.education.setToolTip("")
        self.education.setObjectName("education")
        self.cooking = QtWidgets.QPushButton(self.centralwidget)
        self.cooking.setGeometry(QtCore.QRect(510, 130, 80, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cooking.setFont(font)
        self.cooking.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cooking.setToolTip("")
        self.cooking.setObjectName("cooking")
        self.buy = QtWidgets.QPushButton(self.centralwidget)
        self.buy.setGeometry(QtCore.QRect(680, 485, 100, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.buy.setFont(font)
        self.buy.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buy.setObjectName("buy")
        self.date_time = QtWidgets.QLabel(self.centralwidget)
        self.date_time.setGeometry(QtCore.QRect(350, 50, 411, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.date_time.setFont(font)
        self.date_time.setText("")
        self.date_time.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.date_time.setObjectName("date_time")
        self.buy_log = QtWidgets.QLabel(self.centralwidget)
        self.buy_log.setGeometry(QtCore.QRect(20, 490, 530, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.buy_log.setFont(font)
        self.buy_log.setText("")
        self.buy_log.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.buy_log.setObjectName("buy_log")
        self.purchase_history = QtWidgets.QPushButton(self.centralwidget)
        self.purchase_history.setGeometry(QtCore.QRect(570, 485, 100, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.purchase_history.setFont(font)
        self.purchase_history.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.purchase_history.setObjectName("purchase_history")
        self.log_out = QtWidgets.QPushButton(self.centralwidget)
        self.log_out.setGeometry(QtCore.QRect(540, 10, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.log_out.setFont(font)
        self.log_out.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.log_out.setObjectName("log_out")
        self.biography = QtWidgets.QPushButton(self.centralwidget)
        self.biography.setGeometry(QtCore.QRect(290, 153, 80, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.biography.setFont(font)
        self.biography.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.biography.setToolTip("")
        self.biography.setObjectName("biography")
        self.architecture = QtWidgets.QPushButton(self.centralwidget)
        self.architecture.setGeometry(QtCore.QRect(400, 153, 80, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.architecture.setFont(font)
        self.architecture.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.architecture.setToolTip("")
        self.architecture.setObjectName("architecture")
        self.comics = QtWidgets.QPushButton(self.centralwidget)
        self.comics.setGeometry(QtCore.QRect(510, 153, 80, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comics.setFont(font)
        self.comics.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comics.setToolTip("")
        self.comics.setObjectName("comics")
        self.psychology = QtWidgets.QPushButton(self.centralwidget)
        self.psychology.setGeometry(QtCore.QRect(620, 153, 80, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.psychology.setFont(font)
        self.psychology.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.psychology.setToolTip("")
        self.psychology.setObjectName("psychology")
        self.history = QtWidgets.QPushButton(self.centralwidget)
        self.history.setGeometry(QtCore.QRect(190, 153, 80, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.history.setFont(font)
        self.history.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.history.setToolTip("")
        self.history.setObjectName("history")
        self.total_books = QtWidgets.QPushButton(self.centralwidget)
        self.total_books.setGeometry(QtCore.QRect(720, 130, 60, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.total_books.setFont(font)
        self.total_books.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.total_books.setToolTip("")
        self.total_books.setObjectName("total_books")
        self.client_logo.raise_()
        self.search_input.raise_()
        self.welcome_log_in.raise_()
        self.welcome_register.raise_()
        self.call_for_help.raise_()
        self.search.raise_()
        self.client_name.raise_()
        self.books_recommend.raise_()
        self.books_on_sale.raise_()
        self.books_recommend_pic.raise_()
        self.books_on_sale_pic.raise_()
        self.manual.raise_()
        self.books_for_you.raise_()
        self.books_for_you_pic.raise_()
        self.novel.raise_()
        self.music.raise_()
        self.political.raise_()
        self.education.raise_()
        self.cooking.raise_()
        self.buy.raise_()
        self.date_time.raise_()
        self.buy_log.raise_()
        self.purchase_history.raise_()
        self.log_out.raise_()
        self.biography.raise_()
        self.architecture.raise_()
        self.comics.raise_()
        self.psychology.raise_()
        self.history.raise_()
        self.total_books.raise_()
        BMT_client_main_windows.setCentralWidget(self.centralwidget)

        self.retranslateUi(BMT_client_main_windows)
        QtCore.QMetaObject.connectSlotsByName(BMT_client_main_windows)
        BMT_client_main_windows.setTabOrder(self.welcome_log_in, self.welcome_register)
        BMT_client_main_windows.setTabOrder(self.welcome_register, self.manual)
        BMT_client_main_windows.setTabOrder(self.manual, self.log_out)
        BMT_client_main_windows.setTabOrder(self.log_out, self.call_for_help)
        BMT_client_main_windows.setTabOrder(self.call_for_help, self.search_input)
        BMT_client_main_windows.setTabOrder(self.search_input, self.search)
        BMT_client_main_windows.setTabOrder(self.search, self.novel)
        BMT_client_main_windows.setTabOrder(self.novel, self.education)
        BMT_client_main_windows.setTabOrder(self.education, self.political)
        BMT_client_main_windows.setTabOrder(self.political, self.cooking)
        BMT_client_main_windows.setTabOrder(self.cooking, self.music)
        BMT_client_main_windows.setTabOrder(self.music, self.books_recommend)
        BMT_client_main_windows.setTabOrder(self.books_recommend, self.books_on_sale)
        BMT_client_main_windows.setTabOrder(self.books_on_sale, self.books_for_you)
        BMT_client_main_windows.setTabOrder(self.books_for_you, self.purchase_history)
        BMT_client_main_windows.setTabOrder(self.purchase_history, self.buy)

    def retranslateUi(self, BMT_client_main_windows):
        _translate = QtCore.QCoreApplication.translate
        BMT_client_main_windows.setWindowTitle(_translate("BMT_client_main_windows", "BMT_client"))
        self.welcome_log_in.setText(_translate("BMT_client_main_windows", "您好，请登录"))
        self.welcome_register.setText(_translate("BMT_client_main_windows", "免费注册"))
        self.call_for_help.setToolTip(_translate("BMT_client_main_windows", "<html><head/><body><p><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">huyan35@mail2.sysu.edu.cn</span></p></body></html>"))
        self.call_for_help.setText(_translate("BMT_client_main_windows", "联系客服(点我复制)"))
        self.search_input.setPlaceholderText(_translate("BMT_client_main_windows", "搜一下吧，准有你喜欢的"))
        self.search.setText(_translate("BMT_client_main_windows", "检索"))
        self.client_name.setText(_translate("BMT_client_main_windows", "<html><head/><body><p><span style=\" font-size:28pt; font-style:italic;\">BMT</span></p></body></html>"))
        self.client_logo.setText(_translate("BMT_client_main_windows", "<html><head/><body><p><img src=\":/logo/resource/BMT_128.ico\"/></p></body></html>"))
        self.books_recommend.setText(_translate("BMT_client_main_windows", "书店推荐"))
        self.books_on_sale.setText(_translate("BMT_client_main_windows", "特价书籍"))
        self.books_recommend_pic.setText(_translate("BMT_client_main_windows", "<html><head/><body><p><img src=\":/books/resource/books_picture/罪与罚.jpg\"/></p></body></html>"))
        self.books_on_sale_pic.setText(_translate("BMT_client_main_windows", "<html><head/><body><p><img src=\":/books/resource/books_picture/中南海人物春秋.jpg\"/></p></body></html>"))
        self.manual.setText(_translate("BMT_client_main_windows", "使用手册"))
        self.books_for_you.setText(_translate("BMT_client_main_windows", "专属推荐"))
        self.books_for_you_pic.setText(_translate("BMT_client_main_windows", "<html><head/><body><p><img src=\":/books/resource/books_picture/音乐理论基础.jpg\"/></p></body></html>"))
        self.novel.setText(_translate("BMT_client_main_windows", "小说"))
        self.music.setText(_translate("BMT_client_main_windows", "音乐"))
        self.political.setText(_translate("BMT_client_main_windows", "军政"))
        self.education.setText(_translate("BMT_client_main_windows", "教材"))
        self.cooking.setText(_translate("BMT_client_main_windows", "烹饪"))
        self.buy.setText(_translate("BMT_client_main_windows", "购买"))
        self.purchase_history.setText(_translate("BMT_client_main_windows", "购买记录"))
        self.log_out.setText(_translate("BMT_client_main_windows", "注销"))
        self.biography.setText(_translate("BMT_client_main_windows", "传记"))
        self.architecture.setText(_translate("BMT_client_main_windows", "建筑"))
        self.comics.setText(_translate("BMT_client_main_windows", "漫画"))
        self.psychology.setText(_translate("BMT_client_main_windows", "心理"))
        self.history.setText(_translate("BMT_client_main_windows", "历史"))
        self.total_books.setText(_translate("BMT_client_main_windows", "全部"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BMT_client_main_windows = QtWidgets.QMainWindow()
    ui = Ui_BMT_client_main_windows()
    ui.setupUi(BMT_client_main_windows)
    BMT_client_main_windows.show()
    sys.exit(app.exec_())
