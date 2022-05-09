# Connecting to a specific database
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
    #database2="school" # Connected to two different database ,you can even connect to 3,4,5 by adding database3="test" etc.
)

mycursor =mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
