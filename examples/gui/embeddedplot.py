import sys
import platform
import numpy as np

#import matplotlib
#matplotlib.use('Qt5Agg')

from PyQt5.QtWidgets import (QMainWindow, QApplication, QDialog, QLineEdit, 
                             QVBoxLayout, QAction, QMessageBox,QFileDialog,
                             QSizePolicy)
from PyQt5.QtCore import QT_VERSION_STR, PYQT_VERSION_STR

from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure

class MainWindow(QMainWindow) :
    
    def __init__(self, parent=None) :
        super(MainWindow, self).__init__(parent)

        ########################################################################
        # ADD MENU ITEMS
        ########################################################################
        
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
        
        ########################################################################
        # CREATE CENTRAL WIDGET
        ########################################################################

        self.widget = QDialog()
        self.plot = MatplotlibCanvas()
        self.edit1 = QLineEdit("enter the plot title here!")
        self.edit2 = QLineEdit("ignore me for now")
        
        # signals + slots ()
        self.edit1.returnPressed.connect(self.update)
        
        layout = QVBoxLayout()
        layout.addWidget(self.plot)
        layout.addWidget(self.edit1)
        layout.addWidget(self.edit2)  
        self.widget.setLayout(layout)        
        self.setCentralWidget(self.widget) 

    def saveas(self):
        """Save something
        
        Hint: look up QFileDialog.getSaveFileName.
        """
        pass
                
    def about(self):
        QMessageBox.about(self, 
            "About Function Evaluator",
            """<b>Function Evaluator</b>
               <p>Copyright &copy; 2016 Jeremy Roberts, All Rights Reserved.
               <p>Python %s -- Qt %s -- PyQt %s on %s""" %
            (platform.python_version(),
             QT_VERSION_STR, PYQT_VERSION_STR, platform.system()))

    def update(self):
        """Update the figure title.
        
        Of course, this is trivial(ish), but it serves as a guid for how
        to update other parts of the figure (see the reference for more).
        """
        title = str(self.edit1.text())
        self.plot.axes.set_title(title)
        self.plot.draw()
        
        
class Form(QDialog) :

    def __init__(self, parent=None) :
        super(Form, self).__init__(parent)
        self.function_edit = QLineEdit("x**2")
        self.function_edit.selectAll()
        self.parameter_edit = QLineEdit("np.linspace(0,1,4)")
        self.parameter_edit.selectAll()
        self.output_edit = QLineEdit(" ")
        self.output_edit.selectAll()
        self.plot = MatplotlibCanvas()
        layout = QVBoxLayout()
        layout.addWidget(self.plot)
        layout.addWidget(self.function_edit)
        layout.addWidget(self.parameter_edit)     
        layout.addWidget(self.output_edit)  
        self.setLayout(layout)
        self.function_edit.setFocus()
        self.output_edit.returnPressed.connect(self.updateUi)
        self.setWindowTitle("Function Evaluator")
        self.x = None
        self.f = None

    def updateUi(self) :
        #try : 
            self.x = str(self.parameter_edit.text())
            x = eval(self.x) 
            if len(x) > 1 :
                x = np.array(x)
            # Is there a cleaner way?
            f = eval(str(self.function_edit.text()))
            self.f = str(f)
            self.f = self.f.replace("[","").replace("]","")
            self.f = ",".join(self.f.split())
            self.output_edit.setText(self.f)
            self.plot.redraw(x, f)
            #self.plot.axes.plot(x, f)
            #self.plot.draw()
        #except :
        #    self.output_edit.setText("error! check function or parameter.")
                

class MatplotlibCanvas(FigureCanvas) :
    """ This is borrowed heavily from the matplotlib documentation;
        specifically, see:
        http://matplotlib.org/examples/user_interfaces/embedding_in_qt5.html
    """
    def __init__(self):
        
        # Initialize the figure and axes
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        
        # Give it some default plot (if desired).  
        x = np.arange(0.0, 3.0, 0.01)
        y = np.sin(2*np.pi*x)
        self.axes.plot(x, y)
        self.axes.set_xlabel('x')
        self.axes.set_ylabel('y(x)')   
        
        # Now do the initialization of the super class
        FigureCanvas.__init__(self, self.fig)
        #self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
         
        
    def redraw(self, x, y) :
        """ Redraw the figure with new x and y values.
        """
        # clear the old image (axes.hold is deprecated)
        self.axes.clear()
        self.axes.plot(x, y)
        self.draw()    
        
        
app = QApplication(sys.argv)
form = MainWindow()
form.show()
app.exec_()
