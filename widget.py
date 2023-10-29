# This Python file uses the following encoding: utf-8
import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import *


# класс, предоставляемый Qt и PySide6 для работы с изображениями
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

from ultralytics import YOLO, settings

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget


class Widget(QWidget):
	listPath: list = []
	model = YOLO("model/best.pt")

	# Конструктор класса окна приложения.
	def __init__(self, parent=None):
		super().__init__(parent)
		self.ui = Ui_Widget()
		self.ui.setupUi(self)
		self.ui.DownloadVideoButton.clicked.connect(self.getMaterialVP)
		self.ui.DeleteButton.clicked.connect(self.deleteSelectedItem)
		self.ui.HelpHelp.clicked.connect(self.showHelp)
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

		# for obj in directory[0]:
		#     self.ui.listWidget.addItem(os.path.basename(obj))
		#     self.listPath.append(directory[0])
		for obj in directory[0]:
			self.ui.listWidget.addItem(obj)
			self.listPath.append(obj)

	# Удаление объектов.

	def deleteSelectedItem(self):
		selectitem = self.ui.listWidget.currentItem()
		print(self.listPath)
		if selectitem:
			self.ui.listWidget.takeItem(self.ui.listWidget.row(selectitem))
			print("Файл удален!")
			self.listPath.remove(selectitem.text())
		print(self.listPath)

	# Получение доп. информации.
	def showHelp(self):
		msg = QMessageBox()
		msg.setIcon(QMessageBox.Icon.Information)
		msg.setText("You look pretty")
		msg.setDetailedText(
			"Здесь будет отображаться подсказка для пользователя.")
		msg.setWindowTitle("Помощь")
		msg.exec_()

	# Отображение изображений
	def ViewImage(self):
		selected_item = self.ui.listWidget.currentItem()
		if selected_item:
			# Загружаем изображение из пути, хранящегося в тексте элемента
			pixmap = QPixmap(selected_item.text())
			self.ui.ImageFile.setFixedSize(300, 300)
			ImageFile_width = self.ui.ImageFile.width()  # Получаем ширину label_2
			ImageFile_height = self.ui.ImageFile.height()  # Получаем высоту label_2
			# Масштабируем изображение
			pixmap = pixmap.scaled(
				ImageFile_width, ImageFile_height, aspectMode=Qt.KeepAspectRatio)
			# В этой строке мы устанавливаем загруженное изображение (pixmap) в label_2
			
			self.ui.ImageFile.setPixmap(pixmap)

	def process(self):
		print(len(self.listPath))
		if len(self.listPath) == 0:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Icon.Critical)
			msg.setText("Отсутствуют файлы для обработки")
			msg.setWindowTitle("Ошибка")
			msg.exec_()
		else:
			settings.update(save_dir="/")
			self.model.predict(self.listPath, show=False, save=True, conf=0.1)


# Точка выполнения программы.
if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = Widget()
	widget.show()
	sys.exit(app.exec())
