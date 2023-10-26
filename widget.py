# This Python file uses the following encoding: utf-8
import sys
import os

from PySide6 import QtWidgets
from PySide6.QtWidgets import *

# класс, предоставляемый Qt и PySide6 для работы с изображениями
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget


class Widget(QWidget):
    listPath: list = []

    # Конструктор класса окна приложения.
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.DownloadVideoButton.clicked.connect(self.getMaterialVP)
        self.ui.DeleteButton.clicked.connect(self.deleteSelectedItem)
        self.ui.HelpHelp.clicked.connect(self.showHelp)
        self.ui.ProcessingButton.clicked.connect(self.robo)
        self.ui.listWidget.itemDoubleClicked.connect(self.ViewImage)

        # loader = QUiLoader()
        # ui_file = QFile("form.ui")
        # ui_file.open(QFile.ReadOnly)
        # self.ui = loader.load(ui_file)
        # ui_file.close()

    # Получение материалов для обработки.
    def getMaterialVP(self):
        directory = QtWidgets.QFileDialog.getOpenFileNames(self, filter="AVI JPG JPEG MP4 PNG (*.avi *.jpg *.jpeg "
                                                                        "*.mp4 *.png) ;; AVI (*.avi) ;; MP4 (*.mp4);; PNG (*.png);; "
                                                                        "JPEG (*.jpeg);; JPG (*.jpg)")

        # for obj in directory[0]:
        #     self.ui.listWidget.addItem(os.path.basename(obj))
        #     self.listPath.append(directory[0])
        for obj in directory[0]:
            self.ui.listWidget.addItem(obj)

    # Удаление объектов.

    def deleteSelectedItem(self):
        selectitem = self.ui.listWidget.currentItem()
        if selectitem:
            self.ui.listWidget.takeItem(self.ui.listWidget.row(selectitem))

    # Получение доп. информации.
    def showHelp(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("You look pretty")
        msg.setDetailedText(
            "Здесь будет отображаться подсказка для пользователя.")
        msg.setWindowTitle("Помощь")
        msg.exec_()

    # Отображение изображений
    def ViewImage(self, item):
        selected_item = self.ui.listWidget.currentItem()
        if selected_item:
            # Загружаем изображение из пути, хранящегося в тексте элемента
            pixmap = QPixmap(selected_item.text())
            self.ui.label_2.setFixedSize(300, 300)
            label_2_width = self.ui.label_2.width()  # Получаем ширину label_2
            label_2_height = self.ui.label_2.height()  # Получаем высоту label_2
            # Масштабируем изображение
            pixmap = pixmap.scaled(
                label_2_width, label_2_height, aspectMode=Qt.KeepAspectRatio)
            # В этой строке мы устанавливаем загруженное изображение (pixmap) в label_2
            self.ui.label_2.setPixmap(pixmap)


# Точка выполнения программы.
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
