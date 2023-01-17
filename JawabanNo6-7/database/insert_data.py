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

sql = "INSERT INTO Anggrek (name,beri_air,beri_pupuk, status) VALUES (%s, %s, %s, %s)"
value = ("anggrek", "3", "1", "benih")
db.execute(sql, value)
mydb.commit()
print(db.rowcount, "BERHASIL INSERT")

sql = "INSERT INTO Anggrek (name,beri_air,beri_pupuk, status) VALUES (%s, %s, %s, %s)"
value = ("anggrek", "3", "1", "tunas")
db.execute(sql, value)
mydb.commit()
print(db.rowcount, "BERHASIL INSERT")

sql = "INSERT INTO Anggrek (name,beri_air,beri_pupuk, status) VALUES (%s, %s, %s, %s)"
value = ("anggrek", "3", "1", "tanaman kecil")
db.execute(sql, value)
mydb.commit()
print(db.rowcount, "BERHASIL INSERT")

sql = "INSERT INTO Anggrek (name,beri_air,beri_pupuk, status) VALUES (%s, %s, %s, %s)"
value = ("anggrek", "3", "1", "tanaman besar")
db.execute(sql, value)
mydb.commit()
print(db.rowcount, "BERHASIL INSERT")

sql = "INSERT INTO Anggrek (name,beri_air,beri_pupuk, status) VALUES (%s, %s, %s, %s)"
value = ("anggrek", "3", "1", "berbunga")
db.execute(sql, value)
mydb.commit()
print(db.rowcount, "BERHASIL INSERT")

sql = "INSERT INTO Mawar (name,beri_air,beri_pupuk, status) VALUES (%s, %s, %s, %s)"
value = ("mawar", "1", "1", "benih")
db.execute(sql, value)
mydb.commit()
print(db.rowcount, "BERHASIL INSERT")

sql = "INSERT INTO Mawar (name,beri_air,beri_pupuk, status) VALUES (%s, %s, %s, %s)"
value = ("mawar", "2", "1", "tunas")
db.execute(sql, value)
mydb.commit()
print(db.rowcount, "BERHASIL INSERT")

sql = "INSERT INTO Mawar (name,beri_air,beri_pupuk, status) VALUES (%s, %s, %s, %s)"
value = ("mawar", "2", "1", "tanaman kecil")
db.execute(sql, value)
mydb.commit()
print(db.rowcount, "BERHASIL INSERT")

sql = "INSERT INTO Mawar (name,beri_air,beri_pupuk, status) VALUES (%s, %s, %s, %s)"
value = ("mawar", "3", "1", "tanaman besar")
db.execute(sql, value)
mydb.commit()
print(db.rowcount, "BERHASIL INSERT")

sql = "INSERT INTO Mawar (name,beri_air,beri_pupuk, status) VALUES (%s, %s, %s, %s)"
value = ("mawar", "4", "1", "berbunga")
db.execute(sql, value)
mydb.commit()
print(db.rowcount, "BERHASIL INSERT")

sql = "INSERT INTO Melati (name,beri_air,beri_pupuk, status) VALUES (%s, %s, %s, %s)"
value = ("melati", "1", "1", "benih")
db.execute(sql, value)
mydb.commit()
print(db.rowcount, "BERHASIL INSERT")

sql = "INSERT INTO Melati (name,beri_air,beri_pupuk, status) VALUES (%s, %s, %s, %s)"
value = ("melati", "2", "1", "tunas")
db.execute(sql, value)
mydb.commit()
print(db.rowcount, "BERHASIL INSERT")

sql = "INSERT INTO Melati (name,beri_air,beri_pupuk, status) VALUES (%s, %s, %s, %s)"
value = ("melati", "3", "1", "tanaman kecil")
db.execute(sql, value)
mydb.commit()
print(db.rowcount, "BERHASIL INSERT")

sql = "INSERT INTO Melati (name,beri_air,beri_pupuk, status) VALUES (%s, %s, %s, %s)"
value = ("melati", "3", "1", "tanaman besar")
db.execute(sql, value)
mydb.commit()
print(db.rowcount, "BERHASIL INSERT")

sql = "INSERT INTO Melati (name,beri_air,beri_pupuk, status) VALUES (%s, %s, %s, %s)"
value = ("melati", "4", "1", "berbunga")
db.execute(sql, value)
mydb.commit()
print(db.rowcount, "BERHASIL INSERT")