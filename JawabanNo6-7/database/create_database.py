import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    port=23306,
    user="root",
    password="p455w0rd",
)

db = mydb.cursor()

db.execute("SHOW DATABASES")

try:
    for i in db:
        print(i)
except:
    print("Gagal!")