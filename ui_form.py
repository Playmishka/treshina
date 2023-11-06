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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QRadioButton, QSizePolicy,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1109, 686)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setContextMenuPolicy(Qt.DefaultContextMenu)
        Widget.setAcceptDrops(False)
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Widget.setWindowIcon(icon)
        Widget.setStyleSheet(u"background-color: rgb(120, 120, 120);\n"
"")
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.DownloadVideoButton = QPushButton(Widget)
        self.DownloadVideoButton.setObjectName(u"DownloadVideoButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.DownloadVideoButton.sizePolicy().hasHeightForWidth())
        self.DownloadVideoButton.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Segoe UI Variable Small Semilig"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.DownloadVideoButton.setFont(font)
        self.DownloadVideoButton.setMouseTracking(False)
        self.DownloadVideoButton.setStyleSheet(u"background-color: rgb(72, 72, 72);\n"
"font: 350 12pt \"Segoe UI Variable Small Semilig\";\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.DownloadVideoButton)

        self.listWidget = QListWidget(Widget)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy2)
        self.listWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"\n"
"font: 9pt \"PT Bold Heading\";\n"
"border-radius: 3px;\n"
"gridline-color: rgb(93, 31, 104);")

        self.verticalLayout.addWidget(self.listWidget)

        self.DeleteButton = QPushButton(Widget)
        self.DeleteButton.setObjectName(u"DeleteButton")
        sizePolicy1.setHeightForWidth(self.DeleteButton.sizePolicy().hasHeightForWidth())
        self.DeleteButton.setSizePolicy(sizePolicy1)
        self.DeleteButton.setStyleSheet(u"background-color: rgb(72, 72, 72);\n"
"font: 350 12pt \"Segoe UI Variable Small Semilig\";\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.DeleteButton)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.groupBox_2 = QGroupBox(Widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.groupBox_2.setStyleSheet(u"background-color: rgb(72, 72, 72);\n"
"font: 350 12pt \"Segoe UI Variable Small Semilig\";\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);")
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.isImage = QRadioButton(self.groupBox_2)
        self.isImage.setObjectName(u"isImage")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.isImage.sizePolicy().hasHeightForWidth())
        self.isImage.setSizePolicy(sizePolicy3)
        self.isImage.setChecked(True)

        self.horizontalLayout.addWidget(self.isImage)

        self.isVideo = QRadioButton(self.groupBox_2)
        self.isVideo.setObjectName(u"isVideo")
        self.isVideo.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.isVideo.sizePolicy().hasHeightForWidth())
        self.isVideo.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.isVideo)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.Text = QLabel(Widget)
        self.Text.setObjectName(u"Text")
        sizePolicy1.setHeightForWidth(self.Text.sizePolicy().hasHeightForWidth())
        self.Text.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Variable Small Semibol"])
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(False)
        self.Text.setFont(font1)
        self.Text.setLayoutDirection(Qt.LeftToRight)
        self.Text.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"font: 600 10pt \"Segoe UI Variable Small Semibol\";\n"
"")

        self.verticalLayout_3.addWidget(self.Text)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.doubleSpinBox = QDoubleSpinBox(Widget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox.setSizePolicy(sizePolicy4)
        self.doubleSpinBox.setStyleSheet(u"background-color: rgb(72, 72, 72);\n"
"font: 350 12pt \"Segoe UI Variable Small Semilig\";\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);")
        self.doubleSpinBox.setMaximum(1.000000000000000)
        self.doubleSpinBox.setSingleStep(0.100000000000000)

        self.verticalLayout_2.addWidget(self.doubleSpinBox)

        self.ProcessingButton = QPushButton(Widget)
        self.ProcessingButton.setObjectName(u"ProcessingButton")
        sizePolicy1.setHeightForWidth(self.ProcessingButton.sizePolicy().hasHeightForWidth())
        self.ProcessingButton.setSizePolicy(sizePolicy1)
        self.ProcessingButton.setStyleSheet(u"background-color: rgb(72, 72, 72);\n"
"font: 350 12pt \"Segoe UI Variable Small Semilig\";\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.ProcessingButton)

        self.HelpHelp = QPushButton(Widget)
        self.HelpHelp.setObjectName(u"HelpHelp")
        sizePolicy1.setHeightForWidth(self.HelpHelp.sizePolicy().hasHeightForWidth())
        self.HelpHelp.setSizePolicy(sizePolicy1)
        self.HelpHelp.setStyleSheet(u"background-color: rgb(72, 72, 72);\n"
"font: 350 12pt \"Segoe UI Variable Small Semilig\";\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.HelpHelp)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy5)
        self.label.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"font: 600 13pt \"Segoe UI Variable Small Semibol\";\n"
"")

        self.verticalLayout_4.addWidget(self.label)

        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy6)
        self.tabWidget.setStyleSheet(u"background-color: rgb(83, 83, 83);\n"
"font: 350 12pt \"Segoe UI Variable Small Semilig\";\n"
"border-radius: 5px;\n"
"color: rgb(72, 72, 72);\n"
"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.ImageFile = QLabel(self.tab)
        self.ImageFile.setObjectName(u"ImageFile")
        self.ImageFile.setGeometry(QRect(0, 0, 791, 541))
        sizePolicy7 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.ImageFile.sizePolicy().hasHeightForWidth())
        self.ImageFile.setSizePolicy(sizePolicy7)
        self.ImageFile.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ImageFile.setStyleSheet(u"background-color: rgb(83, 83, 83);")
        self.ImageFile.setScaledContents(False)
        self.ImageFile.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.ImageAfterProc = QLabel(self.tab_2)
        self.ImageAfterProc.setObjectName(u"ImageAfterProc")
        self.ImageAfterProc.setGeometry(QRect(0, 0, 791, 541))
        sizePolicy6.setHeightForWidth(self.ImageAfterProc.sizePolicy().hasHeightForWidth())
        self.ImageAfterProc.setSizePolicy(sizePolicy6)
        self.ImageAfterProc.setLayoutDirection(Qt.LeftToRight)
        self.ImageAfterProc.setStyleSheet(u"background-color: rgb(83, 83, 83);")
        self.ImageAfterProc.setFrameShape(QFrame.NoFrame)
        self.ImageAfterProc.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_4.addWidget(self.tabWidget)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 1, 1, 1)


        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u044b\u0439 \u043a\u043e\u043c\u043f\u043b\u0435\u043a\u0441 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u044f \u0434\u0435\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0439 \u0441\u043e\u043e\u0440\u0443\u0436\u0435\u043d\u0438\u0439 ", None))
        self.DownloadVideoButton.setText(QCoreApplication.translate("Widget", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.DeleteButton.setText(QCoreApplication.translate("Widget", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0444\u0430\u0439\u043b", None))
#if QT_CONFIG(statustip)
        self.groupBox_2.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.groupBox_2.setTitle("")
        self.isImage.setText(QCoreApplication.translate("Widget", u"\u0424\u043e\u0442\u043e ", None))
        self.isVideo.setText(QCoreApplication.translate("Widget", u"\u0412\u0438\u0434\u0435\u043e", None))
        self.Text.setText(QCoreApplication.translate("Widget", u"\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438:", None))
        self.ProcessingButton.setText(QCoreApplication.translate("Widget", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c", None))
        self.HelpHelp.setText(QCoreApplication.translate("Widget", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u044b\u0439 \u043a\u043e\u043c\u043f\u043b\u0435\u043a\u0441 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u044f \u0434\u0435\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0439 \u0441\u043e\u043e\u0440\u0443\u0436\u0435\u043d\u0438\u0439 ", None))
        self.ImageFile.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"\u0424\u0430\u0439\u043b \u0434\u043e \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438", None))
        self.ImageAfterProc.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"\u0424\u0430\u0439\u043b \u043f\u043e\u0441\u043b\u0435 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438", None))
    # retranslateUi

