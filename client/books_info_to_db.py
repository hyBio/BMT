# -*- coding: utf-8 -*-

# @Time : 2021/12/16 11:50 下午

# @Author : huyan

# @FileName: books_info_to_db.py

# @Software: BMT

import pandas as pd
import sqlite3


class df_to_db(object):
    def __init__(self):
        database = "/Users/huyan/PycharmProjects/BMT/BMT/client/books_info.db"
        connect = sqlite3.connect(database)
        books_info = pd.read_csv("/Users/huyan/PycharmProjects/BMT/BMT/client/books_info.csv", header=0, encoding='utf-8')
        books_info.to_sql("database", connect, if_exists="append")
        connect.commit()

if __name__ == "__main__":
    df_to_db()





