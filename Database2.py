#Creating a Table

import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)
mycursor=mydb.cursor()
mycursor.execute("create table customer(name VARCHAR(255),address VARCHAR(255))")

#Check if the Table Exists

import  mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLE")

for x in mycursor:
    print(x)


