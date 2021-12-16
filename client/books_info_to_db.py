# -*- coding: utf-8 -*-

# @Time : 2021/12/16 11:50 下午

# @Author : huyan

# @FileName: books_info_to_db.py

# @Software: BMT

import pandas as pd
import sqlite3


class df_to_db(object):
    def __init__(self):
        self.database = "./books_info.db"
        self.connect = sqlite3.connect(self.database)
        self.books_info = pd.read_csv("./books_info.csv", header=0, encoding='utf-8')
        self.books_info.to_sql(self.database, self.connect, if_exists="append",index=False)
        self.connect.commit()

if __name__ == "__main__":
    df_to_db()





