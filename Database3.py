#Database3

import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
)
mycursor =mydb.cursor()
mycursor.execute("Create Database mydatabase")
