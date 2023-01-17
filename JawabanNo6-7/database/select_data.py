import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    port=23306,
    user="root",
    password="p455w0rd",
    database="kebun"
)

# print(mydb)

db = mydb.cursor()

db.execute("SELECT * from Anggrek ")
rest = db.fetchall()
for x in rest:
    print(x)

db.execute("SELECT * from Mawar ")
rest = db.fetchall()
for x in rest:
    print(x)

db.execute("SELECT * from Melati ")
rest = db.fetchall()
for x in rest:
    print(x)