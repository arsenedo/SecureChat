import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("src/securechat.ui", self)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec())
