import sys
from PyQt5.QtWidgets import QApplication, QLineEdit

"""
All PyQt applications share a basic, four-line structure:
    - Define the application
    - Define the main widget
    - Show the main widget
    - Execute the app (that's the event loop)
"""
def print_stuff():
    print('lalalalalala')
    
app = QApplication(sys.argv)
widget = QLineEdit('some default text')
widget.setWindowTitle('Simple')
widget.returnPressed.connect(widget.selectAll)
#widget.mouseDoubleClickEvent.connect(print_stuff())
widget.show()

app.exec_()