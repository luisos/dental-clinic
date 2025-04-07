# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *


class PatientForm(QDialog):

    "Patient add/edit form"

    def __init__(self, patient=None, parent=None):
        super(PatientForm, self).__init__(parent)

        self.surnameEdit = QLineEdit()
        self.nameEdit = QLineEdit()
        self.patronymicEdit = QLineEdit()
        self.birthdayEdit = QDateEdit()
        self.addressEdit = QLineEdit()

        if patient:
            self.surnameEdit.setText(patient.surname)
            self.nameEdit.setText(patient.name)
            self.patronymicEdit.setText(patient.patronymic)
            self.birthdayEdit.setDate(patient.birthday)
            self.addressEdit.setText(patient.address)

        buttonbox = QDialogButtonBox()
        buttonbox.addButton(u"Зберегти", QDialogButtonBox.AcceptRole)
        buttonbox.addButton(u"Скасувати", QDialogButtonBox.RejectRole)
        buttonbox.accepted.connect(self.accept)
        buttonbox.rejected.connect(self.reject)

        formLayout = QFormLayout()
        formLayout.addRow(u"Прізвище", self.surnameEdit)
        formLayout.addRow(u"Ім'я", self.nameEdit)
        formLayout.addRow(u"По-батькові", self.patronymicEdit)
        formLayout.addRow(u"Дата народження", self.birthdayEdit)
        formLayout.addRow(u"Адреса", self.addressEdit)
        vbox = QVBoxLayout()
        vbox.addLayout(formLayout)
        vbox.addWidget(buttonbox)
        self.setLayout(vbox)


    def accept(self):
        self.patient = Patient(
            surname = unicode(self.surnameEdit.text()),
            name = unicode(self.nameEdit.text()),
            patronymic = unicode(self.patronymicEdit.text()),
            birthday = unicode(self.birthdayEdit.date().toPyDate()),
            address = unicode(self.addressEdit.text())
            )
        QDialog.accept(self)
