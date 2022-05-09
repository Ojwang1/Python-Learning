# To insert multiple rows into a table,use the executemany()method.
#The second parameter of the executemany() method is a list of tuples,containing the data you want to inser:

import mysql.connector

mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "",
database = "mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO  customers (name, address) VALUES (%s, %s)"
val =[
    ( 'Nicholas','Lowstreet 4'),
    ('Arm','Apple st 652'),
    ('Hannah','Mountain'),
    ('Michael','Valley 345'),
    ('Sandy','Ocean blvd'),
    ('Betty','Green Grass 1'),
    ('Richard','Sky st 331'),
    ('Susan','One way 98'),
    ('Vicky','Yellow Garden 2'),
    ('Ben','Park Lane 38'),
    ('William','Central st 954'),
    ('Chuck','Main Road 989'),
    ('Viola','Sideway 1633')
]

mycursor.executemany(sql,val)

mydb.commit()

print(mycursor.rowcount,"was inserted.")

