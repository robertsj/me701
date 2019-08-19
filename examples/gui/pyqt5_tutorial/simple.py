#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In this example, we create a simple
window in PyQt5.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

def print_stuff():
    print('lalalalalalala')

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    w = QLineEdit()
    #w.resize(500, 500)
    #w.move(100, 300)
    w.setWindowTitle('Simple')
    w.returnPressed.connect(print_stuff)
    
    
    w.show()
    
    sys.exit(app.exec_())
