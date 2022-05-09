# Delete a Table

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql ="DROP TABLE customers"

mycursor.execute(sql)

# Drop Only if Exit this code of delete is same with the code of "DROP"