# -*- coding: utf-8 -*-

import collections

Patient = collections.namedtuple("Patient", "code name birthday address")


class SQLite(object):
    """SQLite engine for Patient table"""

    def __init__(self, filename="test.db"):
        import sqlite3
        self.db = sqlite3.connect(filename)

    def select(self, query=""):
        sql = "SELECT code, surname||' '||name||' '||patronymic AS name, birthday, address FROM patient"
        args = []
        query = query.strip()
        if query.startswith("?"):
            sql += " ORDER BY RANDOM()"
            if query[1:].isdigit():
                sql += " LIMIT %d" % int(query[1:])
        elif query:
            fields = ["surname", "name", "patronymic"]
            args = [a.strip() + "%" for a in query.lower().split(" ", len(fields)-1)]
            sql += " WHERE " + " AND ".join([f+" LIKE ?" for f in fields[:len(args)]])
        print(sql)
        cursor = self.db.cursor()
        cursor.execute(sql, args)
        return list(map(Patient._make, cursor.fetchall()))

    def create_table(self, drop=False):
        query = """
            CREATE TABLE IF NOT EXISTS patient (
                id INTEGER PRIMARY KEY,
                code INTEGER,
                surname TEXT,
                name TEXT,
                patronymic TEXT,
                birthday DATE,
                address TEXT
                )
            """
        cursor = self.db.cursor()
        if drop:
            cursor.execute("DROP TABLE IF EXISTS patient")
        cursor.execute(query)

    def insert(self, patient, commit=True):

        # query = "INSERT INTO patients (%s) VALUES (%s)" % (
        #     ",".join(Patient._fields),
        #     ",".join("?"*len(Patient._fields))
        #     )
        surname, name, patronymic = patient.name.split(' ', 2)
        query =\
            '''
            INSERT INTO patient (code, surname, name, patronymic, birthday, address)
            VALUES (?, ?, ?, ?, ?, ?)
            '''
        cursor = self.db.cursor()
        cursor.execute(query,
                       [patient.code, surname, name, patronymic,
                        patient.birthday, patient.address])
        if commit:
            self.commit()

    def commit(self):
        self.db.commit()



if __name__ == "__main__":
    db = SQLite("data.sqlite")
    patients=db.select()
    print(len(patients))
