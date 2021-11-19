# Getting Set up for OpenGL with PyQt5

## Summary

Students will establish a computational environment that supports use of
of OpenGL within PyQt5 applications.  This environment may require installation
of alternative X servers and Python modules.

## Resources

Alan Moore, *Mastering GUI programming with Python*. 

[http://www.opengl-tutorial.org/](http://www.opengl-tutorial.org/)

[https://sourceforge.net/projects/vcxsrv/](https://sourceforge.net/projects/vcxsrv/)

##  Evidence of Student Learning

  - Students will demonstrate a working environment by running an example.

## Learning Plan


### Before Lecture

  1. Skim AM Chapter 13.
  2. Clone the [sample code](https://github.com/me701/gui_3d_graphics.git) for this lesson.

### During Lecture

The instructions below are for the WSL folks.  Instructions for Mac OS and Ubuntu 
will follow.

0.  Update the [sample code](https://github.com/me701/gui_3d_graphics.git) for this lesson.

1.  For those developing in WSL (the majority), we are living at the "bleeding 
    edge."  In other words, some things work as expected, but many things take
    some debugging.  That is a theme we've had all semester, and I'm optimistic that
    the direction WSL is going will yield a much more stable environment for the
    future.  

    In order to drive OpenGL applications on WSL, we need to be able to disable 
    "indirect" rendering.  With GWSL as our X Server, we *should* have the ability 
    to turn this off, but it *seems* there is a bug in the current GWSL such that
    the option can be disabled.  The solution for now is to install the tool
    that GWSL is actually based on: VcXsrv. 

    Then, open VcXsrv and:
        0. Quit any instances of Ubuntu and GWSL.  
        1. Head [here](https://sourceforge.net/projects/vcxsrv/) and install VcXsrv.
        2. Open VxXsrv to prepare the X server.
        3. Keep the defaults and click Next.
        4. Keep the defaults and click Next.
        5. **Unselect** "Native opengl," **select** "Disable access control," and click Next.
        6. Click Finish.
        7. Open WSL as usual run `xclock` to verify the X server is running.
        8. In the terminal, run `export LIBGL_ALWAYS_INDIRECT=0`.

    You will need to repeat steps 2-6 before running WSL with this X server.  
    
    (*Note that GWSL does build on VcXsrv, but it doesn't seem to allow us to unselect the 
    "Native opengl" option, which blocks our OpenGL access.  With Windows 11 and some tweaks to 
    Ubuntu coming, all of this X server nonsense should be eliminated within the year!*)

2.  **Verify your OpenGL Version**

    First, to use that disabled "Native opengl" option, in the terminal, execute

        `export LIBGL_ALWAYS_INDIRECT=0`

    Then, check your OpenGL version by running

        `glxinfo | grep OpenGL version`
    
    Your output should say something like `OpenGL version string: 3.1 Mesa 21.0.3`.

    If it says `OpenGL version string: 1.4 ...`, you have a problem.  Either you 
    did not perform the export above *or* your X server is not allowing this export
    to have an effect (which is seemingly what GWSL was doing.)  If you see the proper 
    string, you should have a virtual hardware setup that works.


3.  In addition, the `(base)` Anaconda environment (with Qt 5.9) appears to be insufficient
    for everything we'd like to do.  For instance, if you head to `gui_3d_graphics/triangle`
    and run `python main.py` while in the `(base)` environment, you might see
    that the line `self.gl.glEnable(self.gl.GL_DEPTH_TEST)` fails with the error 
    `No module named 'PyQt5._QOpenGLFunctions_2_1'` even though we have `PyQt5` installed
    and have verified the OpenGL version.

    I'm *not sure* why the `(base)` versions of everything fail, but I've seen some accounts
    of the Anaconda version of `PyQt5` not being GL-enabled in past versions.

    The fix is an environment nearly identical (I think) to the one I suggested for Qt Designer:

    ```
    conda create -n testgl Python=3.9
    conda activate testgl
    pip install pyqt5 
    pip install pyopengl #  needed for the "hello example"
    ```
    
    (Sadly, there are no `conda`-only environments that work)

    Now, try the `gui_3d_graphics/triangle/main.py` again.  You should see a nice, purple and gray triangle.

4. Now, head to the `gui_3d_graphics/hello` folder and run `main.py`.  You should see the `Qt` logo. 


### After Lecture

Videos from all week:

   - [Video, Lecture, 11/15/2021](https://mediasite.k-state.edu/mediasite/Play/31edd4b4fee24a879379ace8ae6989331d)  

   - [Video, Lecture, 11/17/2021](https://mediasite.k-state.edu/mediasite/Play/1abc1732811c4f86bd97e2b5021939fc1d)  

   - [Video, Lecture, 11/19/2021](https://mediasite.k-state.edu/mediasite/Play/7ace6356ec974369bdb3acd2b4daf6fd1d)  

### Jeremy's Notes

  - Holy hell, this was a tough week.  It's been awhile since I was so ineffective at getting
    something to work out in time.  Hopefully, this sets up those of you interested in OpenGL
    to explore a bit more using either the `QtOpenGL` widget or the `pyopengl` module.

  - Next time I do this, I hope to organize it as day (1) on set up and test, (2) on dissecting
    and understanding the "triangle" or similar, and (3) a more real-world application that
    includes known vertices from, e.g., an STL file or other CAD-driven format.  Maybe this
    is too much to ask from one week!



