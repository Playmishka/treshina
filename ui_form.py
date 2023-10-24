# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGroupBox, QLabel,
    QListWidget, QListWidgetItem, QProgressBar, QPushButton,
    QRadioButton, QSizePolicy, QTabWidget, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        Widget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"background-color: rgb(212, 212, 212);")
        self.DeleteButton = QPushButton(Widget)
        self.DeleteButton.setObjectName(u"DeleteButton")
        self.DeleteButton.setGeometry(QRect(10, 320, 151, 24))
        self.DeleteButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 700 10pt \"Perpetua Titling MT\";")
        self.groupBox_2 = QGroupBox(Widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 360, 151, 71))
        self.groupBox_2.setStyleSheet(u"background-color: rgb(231, 231, 231);\n"
"\n"
"font: 700 10pt \"Perpetua Titling MT\";")
        self.radioButton = QRadioButton(self.groupBox_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(10, 20, 89, 20))
        self.radioButton_2 = QRadioButton(self.groupBox_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(10, 40, 89, 20))
        self.ProcessingButton = QPushButton(Widget)
        self.ProcessingButton.setObjectName(u"ProcessingButton")
        self.ProcessingButton.setGeometry(QRect(10, 440, 151, 24))
        self.ProcessingButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 700 10pt \"Perpetua Titling MT\";")
        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(166, 40, 621, 551))
        self.tabWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 700 10pt \"Perpetua Titling MT\";\n"
"background-color: rgb(171, 171, 171);")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.ImageWiget = QGraphicsView(self.tab)
        self.ImageWiget.setObjectName(u"ImageWiget")
        self.ImageWiget.setGeometry(QRect(15, 11, 571, 501))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.progressBar = QProgressBar(Widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 480, 151, 23))
        self.progressBar.setValue(24)
        self.HelpHelp = QPushButton(Widget)
        self.HelpHelp.setObjectName(u"HelpHelp")
        self.HelpHelp.setGeometry(QRect(10, 550, 151, 24))
        self.HelpHelp.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 700 10pt \"Perpetua Titling MT\";")
        self.SaveButton = QPushButton(Widget)
        self.SaveButton.setObjectName(u"SaveButton")
        self.SaveButton.setGeometry(QRect(10, 520, 151, 24))
        self.SaveButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 700 10pt \"Perpetua Titling MT\";")
        self.listWidget = QListWidget(Widget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 80, 151, 231))
        self.listWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 9pt \"PT Bold Heading\";")
        self.DownloadVideoButton = QPushButton(Widget)
        self.DownloadVideoButton.setObjectName(u"DownloadVideoButton")
        self.DownloadVideoButton.setGeometry(QRect(10, 40, 151, 24))
        self.DownloadVideoButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 700 10pt \"Perpetua Titling MT\";")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 481, 16))
        self.label.setStyleSheet(u"font: 600 12pt \"Bahnschrift SemiBold SemiConden\";")

        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"\u0421\u0438\u0431\u0438\u0440\u0441\u043a\u0438\u0439 \u0433\u043e\u0441\u0443\u0434\u0430\u0440\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439 \u0443\u043d\u0438\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442 \u0433\u0435\u043e\u0441\u0438\u0441\u0442\u0435\u043c \u0438 \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0439 ", None))
        self.DeleteButton.setText(QCoreApplication.translate("Widget", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c", None))
        self.radioButton.setText(QCoreApplication.translate("Widget", u"\u0424\u043e\u0442\u043e ", None))
        self.radioButton_2.setText(QCoreApplication.translate("Widget", u"\u0412\u0438\u0434\u0435\u043e", None))
        self.ProcessingButton.setText(QCoreApplication.translate("Widget", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"\u0424\u0430\u0439\u043b \u0434\u043e \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"\u0424\u0430\u0439\u043b \u043f\u043e\u0441\u043b\u0435 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438", None))
        self.HelpHelp.setText(QCoreApplication.translate("Widget", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
        self.SaveButton.setText(QCoreApplication.translate("Widget", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.DownloadVideoButton.setText(QCoreApplication.translate("Widget", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u044b\u0439 \u043a\u043e\u043c\u043f\u043b\u0435\u043a\u0441 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u044f \u0434\u0435\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0439 \u0437\u0434\u0430\u043d\u0438\u0439 \u0438 \u0441\u043e\u043e\u0440\u0443\u0436\u0435\u043d\u0438\u0439 ", None))
    # retranslateUi

