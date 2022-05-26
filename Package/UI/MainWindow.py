# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow_kwic(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow_kwic")
        MainWindow.setEnabled(True)
        MainWindow.resize(774, 456)
        MainWindow.setMinimumSize(QSize(774, 456))
        MainWindow.setMaximumSize(QSize(774, 456))
        #MainWindow.setCursor(QCursor(Qt.UpArrowCursor))
        self.action_search = QAction(MainWindow)
        self.action_search.setObjectName(u"action_search")
        self.action_inputfile = QAction(MainWindow)
        self.action_inputfile.setObjectName(u"action_inputfile")
        self.action_outputfile = QAction(MainWindow)
        self.action_outputfile.setObjectName(u"action_outputfile")
        self.action1_2 = QAction(MainWindow)
        self.action1_2.setObjectName(u"action1_2")
        self.action_setting = QAction(MainWindow)
        self.action_setting.setObjectName(u"action_setting")
        self.action_help = QAction(MainWindow)
        self.action_help.setObjectName(u"action_help")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit_keywords = QLineEdit(self.centralwidget)
        self.lineEdit_keywords.setObjectName(u"lineEdit_keywords")
        self.lineEdit_keywords.setGeometry(QRect(300, 301, 151, 21))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 24, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(460, 20, 24, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(300, 280, 48, 16))
        self.plainTextEdit_input = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_input.setObjectName(u"plainTextEdit_input")
        self.plainTextEdit_input.setGeometry(QRect(20, 40, 271, 361))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(340, 100, 81, 161))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_cyclicshift = QPushButton(self.layoutWidget)
        self.pushButton_cyclicshift.setObjectName(u"pushButton_cyclicshift")

        self.verticalLayout.addWidget(self.pushButton_cyclicshift)

        self.pushButton_sort = QPushButton(self.layoutWidget)
        self.pushButton_sort.setObjectName(u"pushButton_sort")

        self.verticalLayout.addWidget(self.pushButton_sort)

        self.pushButton_search = QPushButton(self.layoutWidget)
        self.pushButton_search.setObjectName(u"pushButton_search")

        self.verticalLayout.addWidget(self.pushButton_search)

        self.plainTextEdit_output = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_output.setObjectName(u"plainTextEdit_output")
        self.plainTextEdit_output.setGeometry(QRect(460, 40, 271, 361))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 774, 22))
        self.menu_F = QMenu(self.menubar)
        self.menu_F.setObjectName(u"menu_F")
        self.menu_S = QMenu(self.menubar)
        self.menu_S.setObjectName(u"menu_S")
        self.menu_E = QMenu(self.menubar)
        self.menu_E.setObjectName(u"menu_E")
        self.menu_H = QMenu(self.menubar)
        self.menu_H.setObjectName(u"menu_H")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_F.menuAction())
        self.menubar.addAction(self.menu_E.menuAction())
        self.menubar.addAction(self.menu_S.menuAction())
        self.menubar.addAction(self.menu_H.menuAction())
        self.menu_F.addAction(self.action_inputfile)
        self.menu_F.addAction(self.action_outputfile)
        self.menu_F.addSeparator()
        self.menu_S.addAction(self.action_setting)
        self.menu_E.addAction(self.action_search)
        self.menu_H.addAction(self.action_help)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Kwic", None))
        self.action_search.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u627e(&F)", None))
        self.action_inputfile.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165", None))
        self.action_outputfile.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
        self.action1_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.action_setting.setText(QCoreApplication.translate("MainWindow", u"\u7b97\u6cd5\u8bbe\u7f6e", None))
        self.action_help.setText(QCoreApplication.translate("MainWindow", u"\u9879\u76ee\u6587\u6863", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5173\u952e\u8bcd\uff1a", None))
        self.plainTextEdit_input.setPlainText("")
        self.plainTextEdit_input.setPlaceholderText("")
        self.pushButton_cyclicshift.setText(QCoreApplication.translate("MainWindow", u"\u5faa\u73af\u79fb\u4f4d", None))
        self.pushButton_sort.setText(QCoreApplication.translate("MainWindow", u"\u6392\u5e8f", None))
        self.pushButton_search.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u627e", None))
        self.menu_F.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6(&F)", None))
        self.menu_S.setTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e(&S)", None))
        self.menu_E.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91(&E)", None))
        self.menu_H.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9(&H)", None))
    # retranslateUi

