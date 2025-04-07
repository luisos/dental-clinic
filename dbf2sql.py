#!/usr/bin/env python
# -*- coding: utf-8 -*-

import db
import ydbf
import sys
import logging
from datetime import datetime

DBF_FILE = "SC21.DBF"

def dbf2sql(dentalbase, dbf):
    today = datetime.now().date()
    empty_dates = 0
    none_dates = 0
    skipped_patients = 0
    invalid_years = 0

    for p in dbf.records():
        code = int(p['CODE'])
        name = " ".join((p['DESCR'], p['SP23'], p['SP24']))
        birthday = p['SP25']
        try:
            if birthday.year > today.year:
                invalid_years += 1
                birthday = datetime(birthday.year-100, birthday.month, birthday.day).date()
        except AttributeError:
            empty_dates += 1
        address = "%(SP36)s %(SP37)s, %(SP38)s" % p

        dentalbase.insert(db.Patient(code, name, birthday, address), False)

    dentalbase.commit()

    print "Patient(s) with too big year fixed:", invalid_years
    print "Patient(s) with empty birthday:", empty_dates

def main():
    dbf = ydbf.open(DBF_FILE, use_unicode=True, encoding='windows-1251')
    dentalbase = db.SQLite('data.sqlite')
    dentalbase.create_table(True)
    print "Start converting..."
    dbf2sql(dentalbase, dbf)

if __name__ == "__main__":
    main()
