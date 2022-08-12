#!/usr/bin/python3
from convert import convert
import sys
from PyQt5.QtWidgets import QAction, QApplication, QPushButton, QWidget, QMainWindow, QFileDialog,QInputDialog, QLineEdit, QFileDialog

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'open file'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.openFileNameDialog()
                
        self.show()
    
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
    
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())
