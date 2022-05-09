# Jion Two or More Tables
# Jion users and products to see the name of the users favorite product:

import mysql.connector

mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database ="mydatabase"
)

mycursor =mydb.cursor()

sql ="SELECT \"
     users.name As user,\
     products.name As favorite\
     FROM users \
     INNER JION products ON users.fav=products.id"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)