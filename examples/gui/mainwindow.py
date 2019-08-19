from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QDialog, \
                             QVBoxLayout, QAction, QMessageBox, QWidget, \
                             QFileDialog
from PyQt5.QtCore import QT_VERSION_STR, PYQT_VERSION_STR
import platform

import sys

class MainWindow(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        
        # Create the File menu
        self.menuFile = self.menuBar().addMenu("&File")
        self.actionSaveAs = QAction("&Save As", self)
        self.actionSaveAs.triggered.connect(self.saveas)
        self.actionQuit = QAction("&Quit", self)
        self.actionQuit.triggered.connect(self.close)
        self.menuFile.addActions([self.actionSaveAs, self.actionQuit])
        
        # Create the Help menu
        self.menuHelp = self.menuBar().addMenu("&Help")
        self.actionAbout = QAction("&About",self)
        self.actionAbout.triggered.connect(self.about)
        self.menuHelp.addActions([self.actionAbout])
        
        # Setup main widget
        widget = QWidget()
        self.edit1 = QLineEdit("widget 1")
        self.edit2 = QLineEdit("widget 2")
        self.edit2.returnPressed.connect(self.update_edit_2)

        layout = QVBoxLayout()
        layout.addWidget(self.edit1)
        layout.addWidget(self.edit2)  
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)

    def update_edit_2(self):
        text = str(self.edit1.text()).upper()
        self.edit2.setText(text)
        
    def saveas(self) :
        
        fname = QFileDialog.getSaveFileName(self, 'Save File')[0]
        f = open(fname, 'w')
        s = self.edit1.text()
        f.write(s)
        f.close()
                
    def about(self) :
        QMessageBox.about(self, 
            "About Function Evaluator",
            """<b>Function Evaluator</b>
               <p>Copyright &copy; 2017 Jeremy Roberts, All Rights Reserved.
               <p>Python %s -- Qt %s -- PyQt %s on %s""" %
            (platform.python_version(),
             QT_VERSION_STR, PYQT_VERSION_STR, platform.system()))
        
app = QApplication(sys.argv)
widget = MainWindow()
widget.show()
app.exec_()