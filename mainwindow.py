# -*- coding: utf-8 -*-

import os
from patientmodel import PatientModel
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


SETTINGS_FILE = "settings.ini"
SQLITE_FILE = "data.sqlite"
TABLE_ROW_HEIGHT = 23


class MainWindow(QMainWindow):

    """Main window for patient table view and search"""

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle(u"Паціенти")

        work_path = os.path.dirname(os.path.abspath(__file__))

        self.settings_file = os.path.join(work_path, SETTINGS_FILE)
        settings = QSettings(self.settings_file, QSettings.IniFormat)
        self.restoreGeometry(settings.value("Geometry"))

        # table view
        self.tableView = QTableView()
        self.patientModel = PatientModel(
            os.path.join(work_path, SQLITE_FILE), self.tableView)
        self.tableView.setModel(self.patientModel)
        self.tableView.verticalHeader().hide()
        self.tableView.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.tableView.verticalHeader().setDefaultSectionSize(TABLE_ROW_HEIGHT)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        # restore column sizes
        for col in range(self.patientModel.columnCount(self.tableView)):
            width = int(settings.value("Column%s" % col))
            self.tableView.setColumnWidth(col, width)

        # the search widget
        self.searchWidget = QLineEdit()
        self.searchWidget.returnPressed.connect(self.onSearch)
        self.setFocus()

        self.showRowCount()

        toolbox = QHBoxLayout()
        toolbox.addWidget(self.searchWidget)

        vbox = QVBoxLayout()
        vbox.addLayout(toolbox)
        vbox.addWidget(self.tableView)
        vbox.setContentsMargins(0, 0, 0, 0)

        central = QWidget()
        central.setLayout(vbox)
        self.setCentralWidget(central)

        self.searchWidget.setFocus()

    def showRowCount(self):
        self.statusBar().showMessage(
            str(self.patientModel.rowCount(self.tableView)))

    def onSearch(self):
        self.patientModel.query(self.searchWidget.text())
        self.showRowCount()

    def closeEvent(self, event):
        settings = QSettings(self.settings_file, QSettings.IniFormat)
        # save column sizes
        settings.setValue("Geometry", QVariant(self.saveGeometry()))
        for col in range(self.patientModel.columnCount(self.tableView)):
            settings.setValue("Column%s" % col,
                              QVariant(self.tableView.columnWidth(col)))

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.searchWidget.clear()
            self.searchWidget.setFocus()
