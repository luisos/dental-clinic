#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from mainwindow import MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setOrganizationName("Skiff")
    app.setOrganizationDomain("Skiff")
    app.setApplicationName("Dental Clinic")
    mw = MainWindow()
    mw.show()
    app.exec_()
