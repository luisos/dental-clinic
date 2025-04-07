import sqlite3

db = sqlite3.connect("test.db")
cursor = db.cursor()
cursor.execute("delete from patient")
cursor.execute("select * from patients")
patients = cursor.fetchall()
for p in patients:
    code, fullname, birthday, address = p
    #print code, fullname, birthday, address
    nameparts = fullname.split(" ",2)
    nameparts.extend([""]*(3-len(nameparts)))
    surname, name, patronymic = nameparts
    cursor.execute("insert into patient (code, surname, name, patronymic, birthday, address) values(?,?,?,?,?,?)", [code,surname,name,patronymic,birthday,address])
db.commit()
