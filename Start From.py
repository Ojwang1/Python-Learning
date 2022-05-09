# Start From Another Position.
# If you want to return five records,starting from the third record, you can use the "OFFSET" keyword:
# Start from position 3 and return 5 record.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)