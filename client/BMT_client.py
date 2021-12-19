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
import time
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
        self.ui.books_for_you.setEnabled(False)
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
        self.time1.timeout.connect(self.print_books_pic)
        self.time1.start(1000)
        self.n = 0

        # 联系客服
        self.ui.call_for_help.clicked.connect(self.call_for_help)
        # 使用手册
        self.ui.manual.clicked.connect(self.manual)
        # 展示表格
        self.show_table()
        # 根据书籍类型切换输出的信息
        self.ui.novel.clicked.connect(lambda :self.type_change("小说"))
        self.ui.education.clicked.connect(lambda :self.type_change("教材"))
        self.ui.political.clicked.connect(lambda :self.type_change("军政"))
        self.ui.cooking.clicked.connect(lambda :self.type_change("烹饪"))
        self.ui.music.clicked.connect(lambda :self.type_change("音乐"))
        self.ui.history.clicked.connect(lambda :self.type_change("历史"))
        self.ui.biography.clicked.connect(lambda :self.type_change("传记"))
        self.ui.architecture.clicked.connect(lambda :self.type_change("建筑"))
        self.ui.comics.clicked.connect(lambda :self.type_change("漫画"))
        self.ui.psychology.clicked.connect(lambda :self.type_change("心理"))
        self.ui.total_books.clicked.connect(lambda :self.type_change("total"))
        self.ui.search.clicked.connect(self.search)
        self.ui.buy.clicked.connect(self.buy)

    def buy(self):
        choose_list = []
        for i in self.ui.check_list:
            if i.isChecked():
                books_name = self.ui.table.item(self.ui.check_list.index(i), 2).text()
                sales_this_week = int(self.ui.table.item(self.ui.check_list.index(i),3).text())+1
                inventory = int(self.ui.table.item(self.ui.check_list.index(i),5).text())-1
                self.ui.table.setItem(self.ui.check_list.index(i), 3, QTableWidgetItem(str(sales_this_week)))
                self.ui.table.setItem(self.ui.check_list.index(i), 5, QTableWidgetItem(str(inventory)))
                choose_list.append(books_name)

        for book in choose_list:
            # 在原先基础之上减去购买的一本
            connect = sqlite3.connect(self.database)
            cursor = connect.cursor()
            sql = 'SELECT * FROM database WHERE [books_name]=?'
            result = cursor.execute(sql, (book,))
            data = result.fetchall()[0]
            sales_this_week = data[7]
            cumulative_sales = data[8]
            inventory = data[9]
            sql = 'UPDATE database SET [inventory]="%s" WHERE [books_name]="%s"' % (inventory-1, book)
            cursor.execute(sql)
            sql = 'UPDATE database SET [sales_this_week]="%s" WHERE [books_name]="%s"' % (sales_this_week+1, book)
            cursor.execute(sql)
            sql = 'UPDATE database SET [cumulative_sales]="%s" WHERE [books_name]="%s"' % (cumulative_sales+1, book)
            cursor.execute(sql)
            connect.commit()
            connect.close()

            # 构造购买记录（销售记录）数据库
            date = time.localtime()
            created_time = "{}-{}-{}-{}:{}:{}".format(date.tm_year,
                                                      date.tm_mon,
                                                      date.tm_mday,
                                                      date.tm_hour,
                                                      date.tm_min,
                                                      date.tm_sec)
            username = self.ui.welcome_log_in.text()
            books_type = data[2]
            books_name = data[3]
            selling_price = data[6]
            connect = sqlite3.connect("./purchase_history.db")
            cursor = connect.cursor()
            sql = "CREATE TABLE IF NOT EXISTS database(u TEXT, bt TEXT, bn TEXT, sp TEXT, ct TEXT)"
            cursor.execute(sql)
            cursor = connect.cursor()
            sql = "INSERT INTO database VALUES (?,?,?,?,?)"
            cursor.execute(sql, (username, books_type, books_name, selling_price, created_time,))
            connect.commit()
            connect.close()

    def search(self):
        search_input = self.ui.search_input.text()
        if search_input == None:
            self.show_table()
        else:
            self.ui.table.setRowCount(0)
            self.ui.table.clearContents()
            connect = sqlite3.connect(self.database)
            cursor = connect.cursor()
            sql = 'SELECT * FROM database WHERE [books_name] LIKE "%s" ORDER BY [sales_this_week] DESC' % ('%%%s%%' % search_input)
            result = cursor.execute(sql)
            data = result.fetchall()
            connect.commit()
            connect.close()
            for books_info in data:
                self.add_row(books_info[2], books_info[3], books_info[7], books_info[6], books_info[9])

    def type_change(self, books_type):
        self.ui.table.setRowCount(0)
        self.ui.table.clearContents()
        data = self.read_table("total", books_type)
        for books_info in data:
            self.add_row(books_info[2], books_info[3], books_info[7], books_info[6], books_info[9])

    def show_table(self):
        # 添加表格对象
        self.ui.table = QTableWidget(self)
        # 保存所有的选择框
        self.ui.check_list = []

        self.ui.table.setFixedWidth(720)  # 设置宽度
        self.ui.table.setFixedHeight(290)  # 设置高度
        self.ui.table.move(40, 180)  # 设置显示的位置
        self.ui.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 自动填充
        self.ui.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  # 自动填充
        self.ui.table.setSelectionBehavior(QAbstractItemView.SelectRows)  # 只能选择整行
        self.ui.table.setColumnCount(6)  # 设置列数
        self.ui.table.setHorizontalHeaderLabels(["购买意向", "书籍类别", "书籍名称", "近期销量", "售价", "库存"])  # 设置首行
        # self.ui.table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 表格中的内容设置为无法修改
        self.database = './books_info.db'
        data = self.read_table()
        for books_info in data:
            self.add_row(books_info[2], books_info[3], books_info[7], books_info[6], books_info[9])

    def read_table(self, pic_type="total", books_type="total"):
        """读取数据库中的所有元素"""
        connect = sqlite3.connect(self.database)
        cursor = connect.cursor()
        if books_type == "total":
            sql = 'SELECT * FROM database ORDER BY [sales_this_week] DESC'
            result = cursor.execute(sql)
        else:
            sql = 'SELECT * FROM database WHERE [books_type]=? ORDER BY [sales_this_week] DESC'
            result = cursor.execute(sql, (books_type,))
        if pic_type == "total":
            data = result.fetchall()
        elif pic_type == "books_recommend":
            data = result.fetchall()[0:10]
        elif pic_type == "books_on_sale":
            data = result.fetchall()[190:200]
        else:
            data = result.fetchall()
        connect.commit()
        connect.close()
        return data

    def add_row(self, books_type, books_name, sales_this_week, current_selling_price, inventory):
        """在表格上添加一行新的内容"""
        row = self.ui.table.rowCount()  # 表格的行数
        self.ui.table.setRowCount(row + 1)  # 添加一行表格
        self.ui.table.setItem(row, 1, QTableWidgetItem(str(books_type)))  # 将书籍信息插入到表格中
        self.ui.table.setItem(row, 2, QTableWidgetItem(str(books_name)))
        self.ui.table.setItem(row, 3, QTableWidgetItem(str(sales_this_week)))
        self.ui.table.setItem(row, 4, QTableWidgetItem(str(current_selling_price)))
        self.ui.table.setItem(row, 5, QTableWidgetItem(str(inventory)))

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

    def print_books_pic(self):
        self.n += 1
        books_recommend = self.read_table("books_recommend")
        books_recommend_pic = books_recommend[self.n-1][3]
        books_on_sale = self.read_table("books_on_sale")
        books_on_sale_pic = books_on_sale[self.n-1][3]
        books_for_you = self.read_table("books_for_you")
        books_for_you_pic = books_for_you[self.n-1][3]
        if self.n >= 9:
            self.n = 0
        self.ui.books_recommend_pic.setText(_translate("BMT_client_main_windows", "<html><head/><body><p><img src=\":/books/resource/books_picture/{}.jpg\"/></p></body></html>".format(books_recommend_pic)))
        self.ui.books_on_sale_pic.setText(_translate("BMT_client_main_windows", "<html><head/><body><p><img src=\":/books/resource/books_picture/{}.jpg\"/></p></body></html>".format(books_on_sale_pic)))
        self.ui.books_for_you_pic.setText(_translate("BMT_client_main_windows", "<html><head/><body><p><img src=\":/books/resource/books_picture/{}.jpg\"/></p></body></html>".format(books_for_you_pic)))

    def log_out(self):
        self.ui.welcome_log_in.setText(_translate("BMT_client_main_windows", "您好，请登录"))
        self.ui.welcome_log_in.setEnabled(True)

    def call_for_help(self):
        clipboard = QGuiApplication.clipboard()
        clipboard.setText("huyan35@mail2.sysu.edu.cn")
        self.ui.call_for_help.setText(_translate("BMT_client_main_windows", "已复制到剪切板"))
        self.time1 = QTimer(self)
        self.time1.singleShot(1000, self.timer_TimeOut1)

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
                        self.main_window.ui.books_for_you.setEnabled(True)

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
