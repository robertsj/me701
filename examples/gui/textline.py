import sys
from PyQt5.QtWidgets import QApplication, QLineEdit

"""
All PyQt applications share a basic, four-line structure:
    - Define the application
    - Define the main widget
    - Show the main widget
    - Execute the app (that's the event loop)
"""
app = QApplication(sys.argv)
widget = QLineEdit('some default text')
widget.returnPressed.connect(widget.selectAll)
widget.show()
app.exec_()