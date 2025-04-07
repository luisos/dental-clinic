# -*- coding: utf-8 -*-

PATTERN = u'^моч\\w'
import sqlite3


db = sqlite3.connect('data.sqlite')
sql = u'select * from patient where regexp \'{}\''.format(PATTERN)
patients = db.execute(sql).fetchall()
for patient in patients:
    print u'{0} {2} {3} {4}'.format(*patient)