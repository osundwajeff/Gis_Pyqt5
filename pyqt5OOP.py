#!/usr/bin/python3
from convert import convert
import sys
from PyQt5.QtWidgets import QAction, QApplication, QPushButton, QWidget, QMainWindow

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        #initializes superclass which cretes new window
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PY GUI")
        self.resize(400, 300)
        self.add_widgets()

    def add_widgets(self):
        self.statusBar().showMessage("py file")

        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        newaction = QAction("new", self)
        file_menu.addAction(newaction)

        newaction.setStatusTip("New File")

       

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())
