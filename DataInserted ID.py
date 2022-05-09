# You can get id of the row you just inserted byasking the cursor object.
# If you insert more than one row ,the id of the last inserted row is returned.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user ="root",
    password ="",
    database ="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val =("Nicholas","Blue Village")
mycursor.execute(sql,val)

mydb.commit()

print("1 record inserted, ID:",mycursor.lastrowid)
