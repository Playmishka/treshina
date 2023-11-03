# This Python file uses the following encoding: utf-8
import os.path
import sys

from PySide6 import QtWidgets

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, QSize
from ultralytics import YOLO

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget


def showHelp():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Information)
    msg.setText("You look pretty")
    msg.setDetailedText(
        "Здесь будет отображаться подсказка для пользователя.")
    msg.setWindowTitle("Помощь")
    msg.exec_()


class Widget(QWidget):
    listImage: list = []
    listVideo: list = []
    VideoExtensions: list = [".asf", ".avi", ".gif", ".m4v", ".mkv", ".mov", ".mp4", ".mpeg", ".mpg", ".ts", ".wmv",
                                                     ".webm"]
    imageExtensions: list = [".dmp", ".dng", ".jpeg", ".jpg",
                             ".mpo", ".png", ".tif", ".tiff", ".webp", ".pfm"]

    model = YOLO("model/best.pt")
    path_save: str = None
    is_proccess: bool = False

    # Конструктор класса окна приложения.
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.DownloadVideoButton.clicked.connect(self.getMaterialVP)
        self.ui.DeleteButton.clicked.connect(self.deleteSelectedItem)
        self.ui.HelpHelp.clicked.connect(showHelp)
        self.ui.listWidget.itemDoubleClicked.connect(self.ViewImage)
        self.ui.ProcessingButton.clicked.connect(self.process)

    # loader = QUiLoader()
    # ui_file = QFile("form.ui")
    # ui_file.open(QFile.ReadOnly)
    # self.ui = loader.load(ui_file)
    # ui_file.close()

    # Получение материалов для обработки.
    def getMaterialVP(self):
        directory = QtWidgets.QFileDialog.getOpenFileNames(self, filter="AVI JPG JPEG MP4 PNG (*.avi *.jpg *.jpeg "
                                                           "*.mp4 *.png) ;; AVI (*.avi) ;; MP4 (*.mp4);;"
                                                           "PNG (*.png);; JPEG (*.jpeg);; JPG (*.jpg)")
        for obj in directory[0]:
            filename, file_extension = os.path.splitext(obj)
            self.ui.listWidget.addItem(os.path.basename(obj))
            if file_extension in self.imageExtensions:
                self.listImage.append(obj)
            else:
                self.listVideo.append(obj)

    # Удаление объектов.
    def deleteSelectedItem(self):
        select_item = self.ui.listWidget.currentItem()
        if select_item:
            self.ui.listWidget.takeItem(self.ui.listWidget.row(select_item))

            name, extention = os.path.splitext(select_item.text())
            if extention in self.imageExtensions:
                for item_list in self.listImage:
                    if item_list.find(select_item.text()) != -1:
                        self.listImage.remove(item_list)
            else:
                for item_list in self.listVideo:
                    if item_list.find(select_item.text()) != -1:
                        self.listVideo.remove(item_list)

        print(self.listVideo, self.listImage)

    # Отображение изображений
    def ViewImage(self):
        path_file: str

        select_item = self.ui.listWidget.currentItem()
        name, extention = os.path.splitext(select_item.text())

        if extention in self.imageExtensions:
            for item_list in self.listImage:
                if item_list.find(select_item.text()) != -1:
                    path_file = item_list
        else:
            for item_list in self.listVideo:
                if item_list.find(select_item.text()) != -1:
                    path_file = item_list

        if path_file:
            # Загружаем изображение из пути, хранящегося в тексте элемента
            pixmap = QPixmap(path_file)
            ImageFile_width = self.ui.ImageFile.width()  # Получаем ширину label_2
            ImageFile_height = self.ui.ImageFile.height()  # Получаем высоту label_2
            # Масштабируем изображение

            pixmap = pixmap.scaled(QSize(ImageFile_width, ImageFile_height),
                                   Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.FastTransformation)
            self.ui.ImageFile.setPixmap(pixmap)

        if self.path_save:
            for root, dirs, files in os.walk(self.path_save):
                if select_item.text() in files:
                    path = os.path.join(root, select_item.text())

                    pixmap = QPixmap(path)
                    ImageFile_width = self.ui.ImageAfterProc.width()  # Получаем ширину label_2
                    ImageFile_height = self.ui.ImageAfterProc.height()  # Получаем высоту label_2
            # Масштабируем изображение

                    pixmap = pixmap.scaled(QSize(ImageFile_width, ImageFile_height),
                                           Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.FastTransformation)
                    self.ui.ImageAfterProc.setPixmap(pixmap)

    def process(self):
        self.path_save = QFileDialog.getExistingDirectory(
            None, "папка для сохранения")

        if self.path_save:
            if self.ui.isImage.isChecked() & len(self.listImage) != 0:
                self.model.predict(source=self.listImage, save=True,
                                   conf=self.ui.doubleSpinBox.value(), project=self.path_save)
                self.is_proccess = True
            elif self.ui.isVideo.isChecked() & len(self.listVideo) != 0:
                self.model.predict(source=self.listVideo, stream=True,
                                   save=True, conf=self.ui.doubleSpinBox.value(), project=self.path_save)
                self.is_proccess = True
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Critical)
                msg.setText("Отсутствуют файлы для обработки")
                msg.setWindowTitle("Ошибка")
                msg.exec_()


# Точка выполнения программы.
if __name__ == "__main__":
    app = QApplication()
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
