# Prevent SQL Injection

#It is considered a good practice to escape the values of any query,also in update statements.
# This is to prevent SQL injections ,which is a common web hacking technique to destroy or misuse your database.

import mysql.connector

mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

mycursor =mydb.cursor()

sql = "UPDATE customers SET address =%s WHERE address =%"
val =("Valley 345","Canyon 123")

mycursor.execute(sql,val)

mydb.commit()
print(mycursor.rowcount,"record(s) affected")