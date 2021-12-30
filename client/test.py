# _*_ coding: utf-8 _*_
# @Time : 2021/12/30 10:36 
# @Author : 胡琰 
# @Version：V 0.1
# @File : test.py
# @Site :


import os
import sqlite3
import pandas as pd

storehouse_db = "./client/purchase_history.db"
connect = sqlite3.connect(storehouse_db)
cursor = connect.cursor()
sql = 'SELECT * FROM database'
result = cursor.execute(sql)
sh_data = result.fetchall()
ph_data = pd.DataFrame(sh_data)
connect.commit()
connect.close()




ph_data.columns = "user_name books_type books_name purchase_price current_selling_price inventory".split(sep=" ")
ph_data[["purchase_price","current_selling_price"]] = ph_data[["purchase_price","current_selling_price"]].astype(float)
ph_data["profit"] = ph_data["current_selling_price"]-ph_data["purchase_price"]

ph_data["sales_number"] = ph_data.groupby("books_name")["current_selling_price"].transform("count")
ph_data["sales_money"] = ph_data.groupby("books_name")["current_selling_price"].transform("sum")
ph_data["sales_profit"] = ph_data.groupby("books_name")["profit"].transform("sum")
