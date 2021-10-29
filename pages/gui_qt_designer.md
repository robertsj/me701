# Qt Designer and PyQt

## Summary

For some applications, it *may* be easier to sketch out designs using 
a "what you see is what you get" interface like Qt Designer.  Windows,
layouts, widgets, and more can be dragged and dropped, and the starter
code (in C++ or, for us, in Python) is automatically generated.  Of course,
slots and signals are largely left to the user to define (as might be 
expected).

## Resources

[https://doc.qt.io/qt-5/qtdesigner-manual.html](https://doc.qt.io/qt-5/qtdesigner-manual.html)

[https://realpython.com/qt-designer-python/](https://realpython.com/qt-designer-python/)


##  Evidence of Student Learning

  - Students will complete a WYSIWYG exercise to construct a main-window application.

## Learning Plan


### Before Lecture

  - Skim this [tutorial](https://realpython.com/qt-designer-python/) on Qt Designer.    

### During Lecture
 
  For this lecture, you will follow along step by step with [this tutorial video](https://youtu.be/xvUKkulRcHc).  

  - Install Qt Designer.  On WSL, this requires:

    ```bash
    conda create -n qt5dev python=3.8 # enter "yes"
    conda activate qt5dev
    pip install pyqt5-tools
    ```

    Try `qt5-tools designer`.  If you get an error related to Qt and a package
    that cannot be loaded, then execute the following:

    ```bash
    sudo apt install libxcb-xinerama0
    ```

    (I needed this on one Windows machine but not the other, but I might already 
    have needed this library for another application!)

  - Example 1: A scroll bar with status bar indicator.
  - Example 2: The Guessing Game

### After Lecture

   The final `.ui` and `.py` files are [here](https://github.com/me701/gui_designer.git).


### Jeremy's Notes

  Camtasia is painfully slow to render.

