# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGridLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_Dialog_setting(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(384, 266)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.comboBox_sort = QComboBox(Dialog)
        self.comboBox_sort.addItem("")
        self.comboBox_sort.setObjectName(u"comboBox_sort")

        self.gridLayout.addWidget(self.comboBox_sort, 0, 1, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.comboBox_search = QComboBox(Dialog)
        self.comboBox_search.addItem("")
        self.comboBox_search.addItem("")
        self.comboBox_search.addItem("")
        self.comboBox_search.setObjectName(u"comboBox_search")

        self.gridLayout.addWidget(self.comboBox_search, 1, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Setting", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u6392\u5e8f\u7b97\u6cd5\uff1a   ", None))
        self.comboBox_sort.setItemText(0, QCoreApplication.translate("Dialog", u"SpaceAdvance", None))

        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u641c\u7d22\u7b97\u6cd5\uff1a    ", None))
        self.comboBox_search.setItemText(0, QCoreApplication.translate("Dialog", u"LsSearch_notin", None))
        self.comboBox_search.setItemText(1, QCoreApplication.translate("Dialog", u"LsSearch_re", None))
        self.comboBox_search.setItemText(2, QCoreApplication.translate("Dialog", u"LsSearch_kmp", None))

    # retranslateUi

