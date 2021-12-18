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
from ui import shop_windows as sw
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Account_Database import Database
from Admin import AdminWindow
import sys
import pandas as pd
import sqlite3


_translate = QtCore.QCoreApplication.translate
class main_window(QMainWindow):
    def __init__(self, parent=None):
        super(main_window, self).__init__(parent)
        self.ui = mw.Ui_BMT_client_main_windows()
        self.ui.setupUi(self)

        # 显示时间
        timer = QTimer(self)
        timer.timeout.connect(self.show_current_time)
        timer.start()

        # 未登录时注销、购买记录、去购买按钮无法触发
        self.ui.log_out.setEnabled(False)
        self.ui.purchase_history.setEnabled(False)
        self.ui.buy.setEnabled(False)
        self.log_in = log_in()

        # 登录跳转
        self.ui.welcome_log_in.clicked.connect(self.close)
        self.ui.welcome_log_in.clicked.connect(self.log_in.show)

        # 注册跳转
        self.register_to = register_to()
        self.ui.welcome_register.clicked.connect(self.close)
        self.ui.welcome_register.clicked.connect(self.register_to.show)
        self.ui.log_out.clicked.connect(self.log_out)

        # 设置定时器定时更换书籍图片
        self.time1 = QTimer(self)
        self.time1.timeout.connect(self.timer_TimeOut)
        self.time1.start(1000)

        # 读取书籍名字进行循环播放
        self.books_info = pd.read_csv(r"./books_info.csv", header=0)
        self.n = 0
        self.books = self.books_info.loc[self.n, "books_name"]
        self.pic = _translate("BMT_client_main_windows", "<html><head/><body><p><img src=\":/books/resource/books_picture/{}.jpg\"/></p></body></html>".format(self.books))
        self.ui.books_recommend_pic.setText(self.pic)
        self.ui.books_on_sale_pic.setText(self.pic)
        self.ui.books_for_you_pic.setText(self.pic)

        # 联系客服
        self.ui.call_for_help.clicked.connect(self.call_for_help)
        # 使用手册
        self.ui.manual.clicked.connect(self.manual)
        # 展示表格
        self.show_table()

    def show_table(self):
        # 添加表格对象
        self.ui.table = QTableWidget(self)
        # 保存所有的选择框
        self.ui.check_list = []

        self.ui.table.setFixedWidth(760)  # 设置宽度
        self.ui.table.setFixedHeight(290)  # 设置高度
        self.ui.table.move(20, 190)  # 设置显示的位置
        #self.ui.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 自动填充
        self.ui.table.setSelectionBehavior(QAbstractItemView.SelectRows)  # 只能选择整行
        self.ui.table.setColumnCount(5)  # 设置列数
        self.ui.table.setHorizontalHeaderLabels(["购买意向", "书籍类别", "书籍名称", "近期销量", "售价"])  # 设置首行
        self.ui.table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 表格中的内容设置为无法修改
        self.ui.table.verticalHeader().hide()  # 把序号隐藏
        self.ui.table.setSortingEnabled(False)  # 自动排序
        self.ui.database = './books_info.db'
        data = self.read_table()
        for books_info in data:
            self.add_row(books_info[2], books_info[3], books_info[7],books_info[6])

    def read_table(self):
        """读取数据库中的所有元素"""
        connect = sqlite3.connect(self.ui.database)
        cursor = connect.cursor()
        sql = 'SELECT * FROM database ORDER BY [books_name]'
        result = cursor.execute(sql)
        data = result.fetchall()
        connect.commit()
        connect.close()
        return data

    def add_row(self, books_type, books_name, sales_this_week, current_selling_price):
        """在表格上添加一行新的内容"""
        row = self.ui.table.rowCount()  # 表格的行数
        self.ui.table.setRowCount(row + 1)  # 添加一行表格
        self.ui.table.setItem(row, 1, QTableWidgetItem(str(books_type)))  # 将书籍信息插入到表格中
        self.ui.table.setItem(row, 2, QTableWidgetItem(str(books_name)))
        self.ui.table.setItem(row, 3, QTableWidgetItem(str(sales_this_week)))
        self.ui.table.setItem(row, 4, QTableWidgetItem(str(current_selling_price)))

        # 设置复选框
        widget = QWidget()
        check = QCheckBox()
        self.ui.check_list.append(check)  # 添加到复选框列表中
        check_lay = QHBoxLayout()
        check_lay.addWidget(check)
        check_lay.setAlignment(Qt.AlignCenter)
        widget.setLayout(check_lay)
        self.ui.table.setCellWidget(row, 0, widget)

    def manual(self):
        QDesktopServices.openUrl(QUrl("https://github.com/hyBio/BMT/blob/master/README.md"))

    def show_current_time(self):
        datetime = QDateTime.currentDateTime()
        text = datetime.toString("yyyy年MM月dd日 hh:mm:ss ddd")
        self.ui.date_time.setText(text)
        self.ui.date_time.setFont(QFont("Roman times", 12, QFont.Bold))

    def timer_TimeOut(self):
        self.n += 1
        self.books = self.books_info.loc[self.n, "books_name"]
        if self.n >= 99:
            self.n = 0
        self.pic = _translate("BMT_client_main_windows", "<html><head/><body><p><img src=\":/books/resource/books_picture/{}.jpg\"/></p></body></html>".format(self.books))
        self.ui.books_recommend_pic.setText(self.pic)
        self.ui.books_on_sale_pic.setText(self.pic)
        self.ui.books_for_you_pic.setText(self.pic)

    def log_out(self):
        self.ui.welcome_log_in.setText(_translate("BMT_client_main_windows", "您好，请登录"))
        self.ui.welcome_log_in.setEnabled(True)

    def call_for_help(self):
        clipboard = QGuiApplication.clipboard()
        clipboard.setText("huyan35@mail2.sysu.edu.cn")
        self.ui.call_for_help.setText(_translate("BMT_client_main_windows", "已复制到剪切板"))
        self.time1 = QTimer(self)
        self.time1.singleShot(1000,self.timer_TimeOut1)

    def timer_TimeOut1(self):
        self.ui.call_for_help.setText(_translate("BMT_client_main_windows", "联系客服(点我复制)"))

class log_in(QMainWindow):
    def __init__(self, parent=None):
        super(log_in, self).__init__(parent)
        self.ui = li.Ui_BMT_client_log_in()
        self.ui.setupUi(self)

        # 连接管理员账户
        self.admin_win = AdminWindow()
        self.database = Database("./account_info.db")
        # 返回主页
        self.ui.back.clicked.connect(self.back)
        # 密码显示按钮
        self.ui.checkBox.stateChanged.connect(self.checkBox)
        # 登录
        self.ui.log_in.clicked.connect(self.log_in)
        # 忘记密码
        self.ui.password_forget.clicked.connect(self.passwordforget)
        # 注册
        self.ui.register_to.clicked.connect(self.register_to)
        # 联系客服
        self.ui.call_for_help.clicked.connect(self.call_for_help)

    def log_in(self):
        # 登录功能实现
        # 获取账户和密码
        username = self.ui.account.text()
        password = self.ui.password.text()
        # 在数据库中查找数据
        data = self.database.find_password_by_username(username)
        # 如果两个输入框都不为空
        if username and password:
            if data:
                if str(data[0][0]) == password:
                    QMessageBox.information(self, '成功', '欢迎加入BMT:\n{}'.format(username),
                                            QMessageBox.Yes)
                    # 登录成功，将之前的用户信息清除
                    self.ui.account.setText('')
                    self.ui.password.setText('')
                    self.close()
                    self.main_window = main_window()
                    self.main_window.show()
                    # 如果是管理员，进入管理界面
                    if username == 'admin':
                        self.admin_win.show()
                    # 如果是书店用户，则进入书店主页
                    elif username == 'shop':
                        self.shop_window = shop_window()
                        self.shop_window.show()
                    # 如果是普通用户，则进入个人主页，并取消登录按钮的功能
                    else:
                        self.main_window.ui.welcome_log_in.setText(_translate("BMT_client_main_windows", "{}".format(username)))
                        self.main_window.ui.welcome_log_in.setEnabled(False)
                        self.main_window.ui.log_out.setEnabled(True)
                        self.main_window.ui.purchase_history.setEnabled(True)
                        self.main_window.ui.buy.setEnabled(True)

                else:
                    QMessageBox.information(self, '失败', '密码错误，请确认后重试',
                                            QMessageBox.Yes)
            else:
                QMessageBox.information(self, '错误', '无该账户', QMessageBox.Yes)
        # 如果用户名写了
        elif username:
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
        QMessageBox.information(self, '提示', '请发送邮件联系管理员，单击登录页面右下角\"联系客服\"按钮复制管理员邮箱！', QMessageBox.Yes)

    def register_to(self):
        self.register_to = register_to()
        self.close()
        self.register_to.show()

    def call_for_help(self):
        clipboard = QGuiApplication.clipboard()
        clipboard.setText("huyan35@mail2.sysu.edu.cn")
        self.ui.call_for_help.setText(_translate("BMT_client_main_windows", "已复制到剪切板"))
        self.time1 = QTimer(self)
        self.time1.singleShot(1000,self.timer_TimeOut1)

    def timer_TimeOut1(self):
        self.ui.call_for_help.setText(_translate("BMT_client_main_windows", "联系客服(点我复制)"))


class register_to(QMainWindow):
    def __init__(self, parent=None):
        super(register_to, self).__init__(parent)
        self.ui = rt.Ui_BMT_client_register_to()
        self.ui.setupUi(self)
        self.database = Database('./account_info.db')
        # 返回主页
        self.ui.back.clicked.connect(self.back)
        # 已有帐号前往登录
        self.ui.log_in.clicked.connect(self.log_in)
        # 注册
        self.ui.register_to.clicked.connect(self.register_to)
        # 显示密码
        self.ui.checkBox.stateChanged.connect(self.checkBox)
        # 联系客服
        self.ui.call_for_help.clicked.connect(self.call_for_help)

    def call_for_help(self):
        clipboard = QGuiApplication.clipboard()
        clipboard.setText("huyan35@mail2.sysu.edu.cn")
        self.ui.call_for_help.setText(_translate("BMT_client_main_windows", "已复制到剪切板"))
        self.time1 = QTimer(self)
        self.time1.singleShot(1000,self.timer_TimeOut1)

    def timer_TimeOut1(self):
        self.ui.call_for_help.setText(_translate("BMT_client_main_windows", "联系客服(点我复制)"))

    def back(self):
        self.main_window = main_window()
        self.close()
        self.main_window.show()

    def log_in(self):
        self.log_in = log_in()
        self.close()
        self.log_in.show()

    def register_to(self):
        # 实现注册功能
        username = self.ui.account.text()
        password = self.ui.password.text()
        confirm = self.ui.password_2.text()
        # 如果有一个密码或者密码确认框为空
        if not password or not confirm:
            QMessageBox.information(self, 'Error', '密码为空',
                                    QMessageBox.Yes)
        # 如果用户名已经存在
        elif self.database.is_has(username):
            QMessageBox.information(self, '错误',
                                    '用户已经存在',
                                    QMessageBox.Yes)
        else:
            # 如果两次密码一致，并且不为空
            if password == confirm and password:
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
                    # 将用户信息写入数据库
                    self.database.insert_table(username, password)
                    QMessageBox.information(self, '成功',
                                            '注册成功'.format(username),
                                            QMessageBox.Yes)
                    # 注册完毕之后关闭窗口
                    self.close()
            else:
                QMessageBox.information(self, '错误',
                                        '两次输入的密码不一致，请确认后重新输入',
                                        QMessageBox.Yes)
            self.register_success = register_success()
            self.register_success.show()

    def checkBox(self):
        if self.ui.checkBox.isChecked() is True:
            self.ui.password.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.password.setEchoMode(QLineEdit.Password)


class register_success(QMainWindow):
    def __init__(self, parent=None):
        super(register_success, self).__init__(parent)
        self.ui = rs.Ui_BMT_client_register()
        self.ui.setupUi(self)
        # 返回主页
        self.ui.back.clicked.connect(self.back)
        # 登录
        self.ui.log_in.clicked.connect(self.log_in)
        # 退出
        self.ui.exit.clicked.connect(self.close)
        # 联系客服
        self.ui.call_for_help.clicked.connect(self.call_for_help)

    def call_for_help(self):
        clipboard = QGuiApplication.clipboard()
        clipboard.setText("huyan35@mail2.sysu.edu.cn")
        self.ui.call_for_help.setText(_translate("BMT_client_main_windows", "已复制到剪切板"))
        self.time1 = QTimer(self)
        self.time1.singleShot(1000,self.timer_TimeOut1)

    def timer_TimeOut1(self):
        self.ui.call_for_help.setText(_translate("BMT_client_main_windows", "联系客服(点我复制)"))

    def back(self):
        self.main_window = main_window()
        self.close()
        self.main_window.show()

    def log_in(self):
        self.log_in = log_in()
        self.close()
        self.log_in.show()

class shop_window(QMainWindow):
    def __init__(self, parent=None):
        super(shop_window, self).__init__(parent)
        self.ui = sw.Ui_BMT_client_main_windows()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = main_window()
    win.show()
    sys.exit(app.exec())
