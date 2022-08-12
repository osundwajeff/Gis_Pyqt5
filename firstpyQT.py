#!/usr/bin/python3
import sys
from PyQt5.QtWidgets import QApplication, QWidget
app = QApplication(sys.argv)
gui = QWidget()
gui.setWindowTitle("PY GUI")
gui.show()
sys.exit(app.exec_())