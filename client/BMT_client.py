# _*_ coding: utf-8 _*_
# @Time : 2021/12/13 13:27
# @Author : 胡琰
# @Version：V 0.1
# @File : BMT_client.py
# @Site :
import os

import pandas as pd

from ui import main_windows as mw
from ui import log_in as li
from ui import register_success as rs
from ui import register_to as rt
from ui import shop_windows as sw
from ui import purchase_history as ph
from ui import storehouse_windows as shw
from ui import date_choose as dc
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
        self.ui.novel.clicked.connect(lambda :self.type_change("total","小说"))
        self.ui.education.clicked.connect(lambda :self.type_change("total","教材"))
        self.ui.political.clicked.connect(lambda :self.type_change("total","军政"))
        self.ui.cooking.clicked.connect(lambda :self.type_change("total","烹饪"))
        self.ui.music.clicked.connect(lambda :self.type_change("total","音乐"))
        self.ui.history.clicked.connect(lambda :self.type_change("total","历史"))
        self.ui.biography.clicked.connect(lambda :self.type_change("total","传记"))
        self.ui.architecture.clicked.connect(lambda :self.type_change("total","建筑"))
        self.ui.comics.clicked.connect(lambda :self.type_change("total","漫画"))
        self.ui.psychology.clicked.connect(lambda :self.type_change("total","心理"))
        self.ui.total_books.clicked.connect(lambda :self.type_change("total","total"))
        self.ui.books_recommend.clicked.connect(lambda :self.type_change("books_recommend"))
        self.ui.books_on_sale.clicked.connect(lambda :self.type_change("books_on_sale"))
        self.ui.search.clicked.connect(self.search)
        self.ui.buy.clicked.connect(self.buy)
        self.ui.purchase_history.clicked.connect(self.purchase_history)

    def purchase_history(self):
        self.purchase_history = purchase_history(self.ui.welcome_log_in.text())
        self.purchase_history.show()

    def buy(self):
        books_number = 0
        total_price = 0
        # 确认购买
        for i in self.ui.check_list:
            if i.isChecked():
                books_number += 1
                total_price += float(self.ui.table.item(self.ui.check_list.index(i), 4).text())
        rec_code = QMessageBox.question(self, "询问", "您选购了{}本书，共计{}元，确认购买？".format(books_number,total_price), QMessageBox.Yes | QMessageBox.No)
        # 65536代表选择否
        if rec_code == 65536:
            pass
        else:
            choose_list = []
            for i in self.ui.check_list:
                if i.isChecked():
                    books_name = self.ui.table.item(self.ui.check_list.index(i), 2).text()
                    # 在主页窗口实现实时更新销量和库存
                    sales_this_week = int(self.ui.table.item(self.ui.check_list.index(i),3).text())+1
                    inventory = int(self.ui.table.item(self.ui.check_list.index(i),5).text())-1
                    self.ui.table.setItem(self.ui.check_list.index(i), 3, QTableWidgetItem(str(sales_this_week)))
                    self.ui.table.setItem(self.ui.check_list.index(i), 5, QTableWidgetItem(str(inventory)))
                    choose_list.append(books_name)
                #取消复选框
                i.setCheckState(Qt.Unchecked)
            for book in choose_list:
                # 在原先基础之上减去购买的一本
                connect = sqlite3.connect(self.books_info_db)
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
                purchase_price = data[4]
                selling_price = data[6]
                connect = sqlite3.connect("./purchase_history.db")
                cursor = connect.cursor()
                sql = "CREATE TABLE IF NOT EXISTS database(u TEXT, bt TEXT, pp TEXT,bn TEXT, sp TEXT, ct TEXT)"
                cursor.execute(sql)
                cursor = connect.cursor()
                sql = "INSERT INTO database VALUES (?,?,?,?,?,?)"
                cursor.execute(sql, (username, books_type, books_name, purchase_price, selling_price, created_time,))
                connect.commit()
                connect.close()

    def search(self):
        search_input = self.ui.search_input.text()
        if search_input == None:
            pass
        else:
            self.ui.table.setRowCount(0)
            self.ui.table.clearContents()
            self.ui.check_list = []
            connect = sqlite3.connect(self.books_info_db)
            cursor = connect.cursor()
            sql = 'SELECT * FROM database WHERE [books_name] LIKE "%s" OR [books_type] LIKE "%s" ORDER BY [sales_this_week] DESC' % ('%%%s%%' % search_input,search_input)
            result = cursor.execute(sql)
            data = result.fetchall()
            connect.commit()
            connect.close()
            for books_info in data:
                self.add_row(books_info[2], books_info[3], books_info[7], books_info[6], books_info[9])

    def type_change(self, pic_type="total", books_type="total"):
        self.ui.table.setRowCount(0)
        self.ui.table.clearContents()
        self.ui.check_list = []
        data = self.read_table(pic_type, books_type)
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
        self.books_info_db = './books_info.db'
        data = self.read_table()
        for books_info in data:
            self.add_row(books_info[2], books_info[3], books_info[7], books_info[6], books_info[9])

    def read_table(self, pic_type="total", books_type="total"):
        """读取数据库中的所有元素"""
        connect = sqlite3.connect(self.books_info_db)
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
            data = result.fetchall()[-10:]
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
        self.account_info_db = Database("./account_info.db")
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
        self.username = self.ui.account.text()
        password = self.ui.password.text()
        # 在数据库中查找数据
        data = self.account_info_db.find_password_by_username(self.username)
        # 如果两个输入框都不为空
        if self.username and password:
            if data:
                if str(data[0][0]) == password:
                    QMessageBox.information(self, '成功', '欢迎加入BMT:\n{}'.format(self.username),
                                            QMessageBox.Yes)
                    # 登录成功，将之前的用户信息清除
                    self.ui.account.setText('')
                    self.ui.password.setText('')
                    self.close()
                    self.main_window = main_window()
                    self.main_window.show()
                    # 如果是管理员，进入管理界面
                    if self.username == 'admin':
                        self.admin_win.show()
                    # 如果是书店用户，则进入书店主页
                    elif self.username == 'shop':
                        self.shop_window = shop_window()
                        self.shop_window.show()
                    elif self.username == 'storehouse':
                        self.storehouse_window = storehouse_window()
                        self.storehouse_window.show()
                    # 如果是普通用户，则进入个人主页，并取消登录按钮的功能
                    else:
                        self.main_window.ui.welcome_log_in.setText(_translate("BMT_client_main_windows", "{}".format(self.username)))
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
        elif self.username:
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
        self.account_info_db = Database('./account_info.db')
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
        elif self.account_info_db.is_has(username):
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
                    self.account_info_db.insert_table(username, password)
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
        self.show_table()

        # 显示时间
        timer = QTimer(self)
        timer.timeout.connect(self.show_current_time)
        timer.start()

        self.ui.time_from.clicked.connect(self.time_from)
        self.ui.time_to.clicked.connect(self.time_to)

    def time_from(self):
        self.date_choose = date_choose("time_from")
        self.date_choose.show()
        self.date_choose.ui.pushButton.clicked.connect(lambda :self.ui.time_from.setText(self.date_choose.date_return("从")))
        self.date_choose.ui.pushButton.clicked.connect(self.date_choose.close)

    def time_to(self):
        self.date_choose = date_choose("time_to")
        self.date_choose.show()
        self.date_choose.ui.pushButton.clicked.connect(lambda :self.ui.time_to.setText(self.date_choose.date_return("到")))
        self.date_choose.ui.pushButton.clicked.connect(self.date_choose.close)

    def show_table(self):
        # 显示销售情况
        self.ui.table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 表格中的内容设置为无法修改
        self.ui.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 自动填充
        self.ui.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  # 自动填充
        self.purchase_history_db = "./purchase_history.db"
        connect = sqlite3.connect(self.purchase_history_db)
        cursor = connect.cursor()
        sql = 'SELECT * FROM database'
        result = cursor.execute(sql)
        self.ph_data = result.fetchall()
        connect.commit()
        connect.close()
        self.ph_data = pd.DataFrame(self.ph_data)
        self.ph_data.columns = "user_name books_type books_name purchase_price current_selling_price inventory".split(sep=" ")
        self.ph_data[["purchase_price","current_selling_price"]] = self.ph_data[["purchase_price","current_selling_price"]].astype(float)
        self.ph_data["profit"] = self.ph_data["current_selling_price"]-self.ph_data["purchase_price"]

        self.ph_data["sales_number"] = self.ph_data.groupby(["books_name"])["current_selling_price"].transform("count")
        self.ph_data["sales_money"] = self.ph_data.groupby(["books_name"])["current_selling_price"].transform("sum")
        self.ph_data["sales_profit"] = self.ph_data.groupby(["books_name"])["profit"].transform("sum")
        # 保留两位小数
        self.ph_data["sales_profit"] = self.ph_data["sales_profit"].round(2)
        # 排序
        self.ph_data = self.ph_data.sort_values(["sales_number","sales_profit"],ascending=False)
        # 去重
        self.ph_data = self.ph_data.drop_duplicates(subset=["books_name"])

        for books_info in self.ph_data.itertuples():
            self.add_row(getattr(books_info,"books_type"),getattr(books_info,"books_name"),getattr(books_info,"sales_number"),getattr(books_info,"sales_money"),getattr(books_info,"sales_profit"))

    def add_row(self, books_type, books_name, sales_number, sales_money, sales_profit):
        """在表格上添加一行新的内容"""
        row = self.ui.table.rowCount()  # 表格的行数
        self.ui.table.setRowCount(row + 1)  # 添加一行表格
        self.ui.table.setItem(row, 0, QTableWidgetItem(str(books_type)))# 将书籍信息插入到表格中
        self.ui.table.setItem(row, 1, QTableWidgetItem(str(books_name)))
        self.ui.table.setItem(row, 2, QTableWidgetItem(str(sales_number)))
        self.ui.table.setItem(row, 3, QTableWidgetItem(str(sales_money)))
        self.ui.table.setItem(row, 4, QTableWidgetItem(str(sales_profit)))

    def show_current_time(self):
        datetime = QDateTime.currentDateTime()
        text = datetime.toString("yyyy年MM月dd日 hh:mm:ss ddd")
        self.ui.date_time.setText(text)
        self.ui.date_time.setFont(QFont("Roman times", 12, QFont.Bold))


class purchase_history(QMainWindow):
    def __init__(self, username):
        # 获取顾客姓名
        self.username = username
        super(purchase_history, self).__init__()
        self.ui = ph.Ui_BMT_client_main_windows()
        self.ui.setupUi(self)
        self.ui.output.clicked.connect(self.output)

        #购买记录
        self.purchase_history_db = "./purchase_history.db"
        connect = sqlite3.connect(self.purchase_history_db)
        cursor = connect.cursor()
        sql = 'SELECT * FROM database WHERE [u]="%s" ORDER BY [ct]' % (self.username)
        result = cursor.execute(sql)
        self.ph_data = result.fetchall()
        connect.commit()
        connect.close()

        # 添加表格对象
        self.ui.table = QTableWidget(self)
        # 保存所有的选择框
        self.ui.check_list = []
        self.ui.table.setFixedWidth(720)  # 设置宽度
        self.ui.table.setFixedHeight(500)  # 设置高度
        self.ui.table.move(40, 180)  # 设置显示的位置
        self.ui.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 自动填充
        self.ui.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  # 自动填充
        self.ui.table.setSelectionBehavior(QAbstractItemView.SelectRows)  # 只能选择整行
        self.ui.table.setColumnCount(5)  # 设置列数
        self.ui.table.setHorizontalHeaderLabels([ "用户姓名", "书籍类别", "书籍名称", "成交价格", "交易时间"])  # 设置首行
        for purchase_history_info in self.ph_data:
            self.add_row(purchase_history_info[0], purchase_history_info[1], purchase_history_info[2], purchase_history_info[4], purchase_history_info[5])

    def add_row(self, user_name, books_type, books_name, current_selling_price, time):
        """在表格上添加一行新的内容"""
        row = self.ui.table.rowCount()  # 表格的行数
        self.ui.table.setRowCount(row + 1)  # 添加一行表格
        self.ui.table.setItem(row, 0, QTableWidgetItem(str(user_name)))# 将书籍信息插入到表格中
        self.ui.table.setItem(row, 1, QTableWidgetItem(str(books_type)))
        self.ui.table.setItem(row, 2, QTableWidgetItem(str(books_name)))
        self.ui.table.setItem(row, 3, QTableWidgetItem(str(current_selling_price)))
        self.ui.table.setItem(row, 4, QTableWidgetItem(str(time)))

    def output(self):
        file = pd.DataFrame(self.ph_data)
        file.columns = ["顾客姓名","书籍类型","书籍名称","购入价格","交易时间"]
        # 尝试保存，忽略由于用户取消抛出的FileNotFoundError
        try:
            file_save_path = QFileDialog.getSaveFileName(self, "选择保存路径", os.getcwd(), "txt files (*.txt);;all files(*.*)")
            file.to_csv(file_save_path[0],sep="\t",index=False)
        except FileNotFoundError:
            pass


class date_choose(QWidget):
    def __init__(self, action):
        self.action = action
        super(date_choose, self).__init__()
        self.ui = dc.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.date_return)

    def date_return(self,from_or_to):
        self.date = self.ui.calendarWidget.selectedDate()
        self.date = self.date.toString("yyyy年MM月dd日")
        return ("{} {}".format(from_or_to,self.date))


class storehouse_window(QMainWindow):
    def __init__(self, parent=None):
        super(storehouse_window, self).__init__(parent)
        self.ui = shw.Ui_storehouse_window()
        self.ui.setupUi(self)

        self.storehouse_db = "./books_info.db"
        connect = sqlite3.connect(self.storehouse_db)
        cursor = connect.cursor()
        sql = 'SELECT [books_type],[books_name],[purchase_price],[current_selling_price],[inventory] FROM database ORDER BY [inventory] DESC'
        result = cursor.execute(sql)
        self.sh_data = result.fetchall()
        connect.commit()
        connect.close()

        for books_info in self.sh_data:
            self.add_row(books_info[0], books_info[1], books_info[2], books_info[3], books_info[4])

    def add_row(self, books_type, books_name, purchase_price, current_selling_price, inventory):
        """在表格上添加一行新的内容"""
        row = self.ui.table.rowCount()  # 表格的行数
        self.ui.table.setRowCount(row + 1)  # 添加一行表格
        self.ui.table.setItem(row, 0, QTableWidgetItem(str(books_type)))# 将书籍信息插入到表格中
        self.ui.table.setItem(row, 1, QTableWidgetItem(str(books_name)))
        self.ui.table.setItem(row, 2, QTableWidgetItem(str(purchase_price)))
        self.ui.table.setItem(row, 3, QTableWidgetItem(str(current_selling_price)))
        self.ui.table.setItem(row, 4, QTableWidgetItem(str(inventory)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = main_window()
    win.show()
    sys.exit(app.exec())
