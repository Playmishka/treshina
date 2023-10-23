# This Python file uses the following encoding: utf-8
import sys
import os

from PySide6 import QtWidgets
from PySide6.QtWidgets import *

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.DownloadVideoButton.clicked.connect(self.getMaterialVP)
        self.ui.DeleteButton.clicked.connect(self.deleteSelectedItem)
        self.ui.HelpHelp.clicked.connect(self.showHelp)
        # loader = QUiLoader()
        # ui_file = QFile("form.ui")
        # ui_file.open(QFile.ReadOnly)
        # self.ui = loader.load(ui_file)
        # ui_file.close()

    def getMaterialVP(self):
        directory = QtWidgets.QFileDialog.getOpenFileNames(self, filter="AVI JPG JPEG MP4 PNG (*.avi *.jpg *.jpeg "
                                                                        "*.mp4 *.png) ;; MP4 (*.mp4);; PNG (*.png);; "
                                                                        "JPEG (*.jpeg);; JPG (*.jpg)")
        print(directory)

        for obj in directory[0]:
            self.ui.listWidget.addItem(os.path.basename(obj))

    def deleteSelectedItem(self):
        selectitem = self.ui.listWidget.currentItem()
        if selectitem:
            self.ui.listWidget.takeItem(self.ui.listWidget.row(selectitem))

    def showHelp(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("You look pretty")
        msg.setDetailedText("Здесь будет отображаться подсказка для пользователя.")
        msg.setWindowTitle("Помощь")
        msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
