import sys
from PyQt5.QtWidgets import QApplication, QLabel

"""
All PyQt applications share a basic, four-line structure:
    - Define the application
    - Define the main widget
    - Show the main widget
    - Execute the app (that's the event loop)
"""
app = QApplication(sys.argv)
widget = QLabel('<font size=14>Hello World</font>')
widget.show()
app.exec_()