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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QGroupBox,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QRadioButton, QSizePolicy, QTabWidget, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 598)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setContextMenuPolicy(Qt.DefaultContextMenu)
        Widget.setAcceptDrops(False)
        Widget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"background-color: rgb(212, 212, 212);")
        self.DeleteButton = QPushButton(Widget)
        self.DeleteButton.setObjectName(u"DeleteButton")
        self.DeleteButton.setGeometry(QRect(10, 340, 171, 24))
        self.DeleteButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 700 10pt \"Perpetua Titling MT\";\n"
"border-radius: 7px;\n"
"")
        self.groupBox_2 = QGroupBox(Widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 370, 171, 61))
        self.groupBox_2.setStyleSheet(u"background-color: rgb(231, 231, 231);\n"
"border-radius: 7px;\n"
"font: 700 10pt \"Perpetua Titling MT\";")
        self.isImage = QRadioButton(self.groupBox_2)
        self.isImage.setObjectName(u"isImage")
        self.isImage.setGeometry(QRect(10, 20, 89, 20))
        self.isImage.setChecked(True)
        self.isVideo = QRadioButton(self.groupBox_2)
        self.isVideo.setObjectName(u"isVideo")
        self.isVideo.setGeometry(QRect(10, 40, 89, 20))
        self.ProcessingButton = QPushButton(Widget)
        self.ProcessingButton.setObjectName(u"ProcessingButton")
        self.ProcessingButton.setGeometry(QRect(10, 510, 171, 24))
        self.ProcessingButton.setStyleSheet(u"border-radius: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 700 10pt \"Perpetua Titling MT\";")
        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(190, 40, 601, 551))
        self.tabWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 700 10pt \"Perpetua Titling MT\";\n"
"background-color: rgb(194, 194, 194);\n"
"border-radius: 10px;")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.ImageFile = QLabel(self.tab)
        self.ImageFile.setObjectName(u"ImageFile")
        self.ImageFile.setGeometry(QRect(18, 15, 551, 491))
        self.ImageFile.setScaledContents(True)
        self.ImageFile.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.ImageAfterProc = QLabel(self.tab_2)
        self.ImageAfterProc.setObjectName(u"ImageAfterProc")
        self.ImageAfterProc.setGeometry(QRect(18, 20, 561, 491))
        self.ImageAfterProc.setLayoutDirection(Qt.LeftToRight)
        self.ImageAfterProc.setFrameShape(QFrame.NoFrame)
        self.ImageAfterProc.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.tab_2, "")
        self.HelpHelp = QPushButton(Widget)
        self.HelpHelp.setObjectName(u"HelpHelp")
        self.HelpHelp.setGeometry(QRect(10, 570, 171, 24))
        self.HelpHelp.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 700 10pt \"Perpetua Titling MT\";\n"
"border-radius: 7px;\n"
"\n"
"")
        self.SaveButton = QPushButton(Widget)
        self.SaveButton.setObjectName(u"SaveButton")
        self.SaveButton.setGeometry(QRect(10, 540, 171, 24))
        self.SaveButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 700 10pt \"Perpetua Titling MT\";\n"
"border-radius: 7px;\n"
"")
        self.listWidget = QListWidget(Widget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 70, 171, 261))
        self.listWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 9pt \"PT Bold Heading\";\n"
"border-radius: 3px;")
        self.DownloadVideoButton = QPushButton(Widget)
        self.DownloadVideoButton.setObjectName(u"DownloadVideoButton")
        self.DownloadVideoButton.setGeometry(QRect(10, 40, 171, 24))
        self.DownloadVideoButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 700 10pt \"Perpetua Titling MT\";\n"
"border-radius: 7px;")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 501, 16))
        self.label.setStyleSheet(u"font: 700 10pt \"Perpetua Titling MT\";\n"
"font-weight: bold;\n"
"Front-size: 40pt;\n"
"")
        self.doubleSpinBox = QDoubleSpinBox(Widget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setGeometry(QRect(10, 480, 171, 25))
        self.doubleSpinBox.setMaximum(1.000000000000000)
        self.doubleSpinBox.setSingleStep(0.100000000000000)
        self.Text = QLabel(Widget)
        self.Text.setObjectName(u"Text")
        self.Text.setGeometry(QRect(10, 440, 171, 31))
        self.Text.setStyleSheet(u"background-color: rgb(194, 194, 194);\n"
"font: 700 10pt \"Perpetua Titling MT\";\n"
"border-radius: 7px;\n"
"")

        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"\u0421\u0438\u0431\u0438\u0440\u0441\u043a\u0438\u0439 \u0433\u043e\u0441\u0443\u0434\u0430\u0440\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439 \u0443\u043d\u0438\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442 \u0433\u0435\u043e\u0441\u0438\u0441\u0442\u0435\u043c \u0438 \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0439 ", None))
        self.DeleteButton.setText(QCoreApplication.translate("Widget", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c", None))
        self.isImage.setText(QCoreApplication.translate("Widget", u"\u0424\u043e\u0442\u043e ", None))
        self.isVideo.setText(QCoreApplication.translate("Widget", u"\u0412\u0438\u0434\u0435\u043e", None))
        self.ProcessingButton.setText(QCoreApplication.translate("Widget", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c", None))
        self.ImageFile.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"\u0424\u0430\u0439\u043b \u0434\u043e \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438", None))
        self.ImageAfterProc.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"\u0424\u0430\u0439\u043b \u043f\u043e\u0441\u043b\u0435 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438", None))
        self.HelpHelp.setText(QCoreApplication.translate("Widget", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
        self.SaveButton.setText(QCoreApplication.translate("Widget", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.DownloadVideoButton.setText(QCoreApplication.translate("Widget", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u044b\u0439 \u043a\u043e\u043c\u043f\u043b\u0435\u043a\u0441 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u044f \u0434\u0435\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0439 \u0437\u0434\u0430\u043d\u0438\u0439 \u0438 \u0441\u043e\u043e\u0440\u0443\u0436\u0435\u043d\u0438\u0439 ", None))
        self.Text.setText(QCoreApplication.translate("Widget", u"\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438:", None))
    # retranslateUi

