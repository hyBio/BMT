# _*_ coding: utf-8 _*_
# @Time : 2021/12/13 13:27 
# @Author : 胡琰 
# @Version：V 0.1
# @File : BMT_client.py
# @Site :
import pandas as pd

from ui import main_windows as mw
from ui import log_in as li
from ui import register_success as rs
from ui import register_to as rt
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Account_Database import Database
from Admin import AdminWindow
import sys
import pandas as pd


class main_window(QMainWindow):
    def __init__(self,parent = None):
        super(main_window, self).__init__(parent)
        self.ui = mw.Ui_BMT_client_main_windows()
        self.ui.setupUi(self)

        self.ui.log_out.setEnabled(False)
        self.log_in = log_in()
        self.ui.welcome_log_in.clicked.connect(self.close)
        self.ui.welcome_log_in.clicked.connect(self.log_in.show)

        self.register_to=register_to()
        self.ui.welcome_register.clicked.connect(self.close)
        self.ui.welcome_register.clicked.connect(self.register_to.show)
        self.ui.log_out.clicked.connect(self.log_out)

        self.time1=QTimer(self)
        self.time1.timeout.connect(self.timer_TimeOut)
        self.time1.start(2000)
        self.show()

        self.books_info=pd.read_csv(r"./books_info.csv",header=0)
        self.n=0
        self.books=self.books_info.loc[self.n,"books_name"]
        _translate = QtCore.QCoreApplication.translate
        self.pic = _translate("BMT_client_main_windows", "<html><head/><body><p><img src=\":/books/resource/books_picture/{}.jpg\"/></p></body></html>".format(self.books))
        self.ui.books_recommend_pic.setText(self.pic)
        self.ui.books_on_sale_pic.setText(self.pic)
        self.ui.books_for_you_pic.setText(self.pic)

    def timer_TimeOut(self):
        self.n+=1
        self.books=self.books_info.loc[self.n,"books_name"]
        if self.n>99:
            self.n=0
        _translate = QtCore.QCoreApplication.translate
        self.pic = _translate("BMT_client_main_windows", "<html><head/><body><p><img src=\":/books/resource/books_picture/{}.jpg\"/></p></body></html>".format(self.books))
        self.ui.books_recommend_pic.setText(self.pic)
        self.ui.books_on_sale_pic.setText(self.pic)
        self.ui.books_for_you_pic.setText(self.pic)

    def log_out(self):
        _translate = QtCore.QCoreApplication.translate
        self.ui.welcome_log_in.setText(_translate("BMT_client_main_windows", "您好，请登录"))
        self.ui.welcome_log_in.setEnabled(True)

class log_in(QMainWindow):
    def __init__(self,parent = None):
        super(log_in, self).__init__(parent)
        self.ui = li.Ui_BMT_client_log_in()
        self.ui.setupUi(self)
        self.admin_win=AdminWindow()
        self.database=Database("./account_info.db")

        self.ui.back.clicked.connect(self.back)
        self.ui.checkBox.stateChanged.connect(self.checkBox)
        self.ui.log_in.clicked.connect(self.log_in)
        self.ui.password_forget.clicked.connect(self.passwordforget)
        self.ui.register_to.clicked.connect(self.register_to)

    def log_in(self):
        """登录功能实现"""
        _translate = QtCore.QCoreApplication.translate
        username = self.ui.account.text()
        password = self.ui.password.text()
        data = self.database.find_password_by_username(username)  # 在数据库中查找数据
        if username and password:  # 如果两个输入框都不为空
            if data:
                if str(data[0][0]) == password:
                    QMessageBox.information(self, '成功', '欢迎加入BMT:\n{}'.format(username),
                                            QMessageBox.Yes)
                    self.ui.account.setText('') # 登录成功，将之前的用户信息清除
                    self.ui.password.setText('')
                    self.close()
                    self.main_window=main_window()
                    self.main_window.show()
                    if username == 'admin':  # 如果是管理员，进入管理界面
                        self.admin_win.show()
                    else:  # 如果是普通用户，则进入个人主页，并取消登录按钮的功能
                        self.main_window.ui.welcome_log_in.setText(_translate("BMT_client_main_windows", "{}".format(username)))
                        self.main_window.ui.welcome_log_in.setEnabled(False)
                        self.main_window.ui.log_out.setEnabled(True)

                else:
                    QMessageBox.information(self, '失败', '密码错误，请确认后重试',
                                            QMessageBox.Yes)
            else:
                QMessageBox.information(self, '错误', '无该账户', QMessageBox.Yes)
        elif username:  # 如果用户名写了
            QMessageBox.information(self, '错误', '请输入密码', QMessageBox.Yes)
        else:
            QMessageBox.information(self, '错误', '账户为空', QMessageBox.Yes)

    def back(self):
        self.main_window = main_window()
        self.close()
        self.main_window.show()

    def checkBox(self):
        if self.ui.checkBox.isChecked() is True:
            self.ui.password.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.password.setEchoMode(QLineEdit.Password)

    def passwordforget(self):
        QMessageBox.information(self, '提示', '请发送邮件联系管理员，单击登录页面\"联系客服\"按钮复制管理员邮箱！', QMessageBox.Yes)

    def register_to(self):
        self.register_to=register_to()
        self.close()
        self.register_to.show()


class register_to(QMainWindow):
    def __init__(self,parent = None):
        super(register_to, self).__init__(parent)
        self.ui = rt.Ui_BMT_client_register_to()
        self.ui.setupUi(self)
        self.database = Database('./account_info.db')

        self.ui.back.clicked.connect(self.back)
        self.ui.log_in.clicked.connect(self.log_in)
        self.ui.register_to.clicked.connect(self.register_to)
        self.ui.checkBox.stateChanged.connect(self.checkBox)

    def back(self):
        self.main_window = main_window()
        self.close()
        self.main_window.show()

    def log_in(self):
        self.log_in = log_in()
        self.close()
        self.log_in.show()

    def register_to(self):
        """实现注册功能"""
        username = self.ui.account.text()
        password = self.ui.password.text()
        confirm = self.ui.password_2.text()

        if not password or not confirm:  # 如果有一个密码或者密码确认框为空
            QMessageBox.information(self, 'Error', '密码为空',
                                    QMessageBox.Yes)
        elif self.database.is_has(username):  # 如果用户名已经存在
            QMessageBox.information(self, '错误',
                                    '用户已经存在',
                                    QMessageBox.Yes)
        else:
            if password == confirm and password:  # 如果两次密码一致，并且不为空
                if len(username) < 2:
                    QMessageBox.information(self, '错误',
                                            '用户名太短，请输入至少2个字符',
                                            QMessageBox.Yes)
                    return
                if len(password) < 6:
                    QMessageBox.information(self, '错误',
                                            '密码少于六位，请重新输入',
                                            QMessageBox.Yes)
                    return
                else:
                    self.database.insert_table(username,password)  # 将用户信息写入数据库
                    QMessageBox.information(self, '成功',
                                            '注册成功'.format(username),
                                            QMessageBox.Yes)
                    self.close()  # 注册完毕之后关闭窗口
            else:
                QMessageBox.information(self, '错误',
                                        '两次输入的密码不一致，请确认后重新输入',
                                        QMessageBox.Yes)
            self.register_success=register_success()
            self.register_success.show()

    def checkBox(self):
        if self.ui.checkBox.isChecked() is True:
            self.ui.password.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.password.setEchoMode(QLineEdit.Password)


class register_success(QMainWindow):
    def __init__(self,parent = None):
        super(register_success, self).__init__(parent)
        self.ui = rs.Ui_BMT_client_register()
        self.ui.setupUi(self)

        self.ui.back.clicked.connect(self.back)
        self.ui.log_in.clicked.connect(self.log_in)
        self.ui.exit.clicked.connect(self.close)

    def back(self):
        self.main_window=main_window()
        self.close()
        self.main_window.show()

    def log_in(self):
        self.log_in=log_in()
        self.close()
        self.log_in.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = main_window()
    win.show()
    sys.exit(app.exec())
