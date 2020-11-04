import mayavi
from mayavi import mlab
f = mlab.figure()      # Returns the current scene.
engine = mlab.get_engine() # Returns the running mayavi engine.
source = engine.open("rectlin.vtk")
engine.add_source(source)
surface = mayavi.modules.api.Surface()
engine.add_module(surface)
mlab.show() # Opens up interactive GUI.  You can also script
f.scene.save_png("mayavi.png") # views and save the scene

