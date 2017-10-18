import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton,QMessageBox

app = QApplication(sys.argv)
widget = QPushButton('Do something!')
message = QMessageBox()
message.setText("Lalala")
widget.clicked.connect(message.exec)
widget.show()
app.exec_()