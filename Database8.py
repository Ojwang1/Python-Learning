#Insert Into Table

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql ="INSERT INTO custormers (name,address)     VALUES (%s,%s)"
val = ("Nicholas","Mathare 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount,"record inserted.")
#Notice the statement:mydb.commit().It is required to make the changes,otherwise no change are made to the table.

