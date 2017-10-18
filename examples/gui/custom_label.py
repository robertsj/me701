from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QDialog, QVBoxLayout
import sys

class CustomLabel(QLabel):
    
    def __init__(self, msg):
        # easy way to skip super!
        QLabel.__init__(self, msg)
        edit1 = QLineEdit("widget 1")
        edit2 = QLineEdit("widget 2")
        layout = QVBoxLayout()
        layout.addWidget(edit1)
        layout.addWidget(edit2) 
        self.setLayout(layout)
        
class CustomDialog(QDialog):
    
    def __init__(self):
        # easy way to skip super!
        QDialog.__init__(self)
        edit1 = QLineEdit("widget 1")
        edit2 = QLineEdit("widget 2")
        layout = QVBoxLayout()
        layout.addWidget(edit1)
        layout.addWidget(edit2)  
        self.setLayout(layout)
        
app = QApplication(sys.argv)
#widget = CustomLabel('')
#widget = CustomDialog()
widget = QDialog()
edit1 = QLineEdit("widget 1")
edit2 = QLineEdit("widget 2")
layout = QVBoxLayout()
layout.addWidget(edit1)
layout.addWidget(edit2)  
widget.setLayout(layout)
widget.show()
app.exec_()