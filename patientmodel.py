# -*- coding: utf-8 -*-

import db
import ua
from operator import itemgetter
import locale
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class PatientModel(QAbstractTableModel):

    """Patient model for QTableView"""

    def __init__(self, dbconf, parent=None):
        super(PatientModel, self).__init__(parent)
        self.headers = (u"Код", u"Ім\'я", u"Дата народження", u"Адреса")

        locale.setlocale(locale.LC_ALL, "")
        self.db = db.SQLite(dbconf)
        self.patients = []
        self.query("")

    def rowCount(self, parent):
        return len(self.patients)

    def columnCount(self, parent):
        return len(self.headers)

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        col = index.column()
        row = index.row()
        if role == Qt.DisplayRole:
            value = self.patients[row][col]
            if not value:
                return QVariant()
            if col == 1:
                value = ' '.join(map(ua.namelize, value.split(' ')))
            if col == 2:
                value = '.'.join(reversed(value.split('-')))
            return QVariant(value)
        if role == Qt.TextAlignmentRole:
            if col == 0:
                return QVariant(Qt.AlignRight | Qt.AlignVCenter)
            elif col == 2:
                return QVariant(Qt.AlignRight | Qt.AlignVCenter)
            else:
                return QVariant(Qt.AlignLeft | Qt.AlignVCenter)
        return QVariant()

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.headers[section])
        return QVariant()

    def query(self, query):
        name = lambda x: locale.strxfrm(x.name)
        self.patients = self.db.select(query)
        if not query.lstrip().startswith("?"):
            self.patients.sort(key=name)
        self.dataChanged.emit(QModelIndex(), QModelIndex())
