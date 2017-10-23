# Visit 2.12.3 log file
ScriptVersion = "2.12.3"
if ScriptVersion != Version():
    print "This script is for VisIt %s. It may not work with version %s" % (ScriptVersion, Version())
visit.ShowAllWindows()
visit.ShowAllWindows()
visit.OpenDatabase("test.vtk", 0)
# The UpdateDBPluginInfo RPC is not supported in the VisIt module so it will not be logged.
visit.AddPlot("Pseudocolor", "scalars", 1, 1)
visit.DrawPlots()
SaveWindowAtts = visit.SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 1
SaveWindowAtts.outputDirectory = "."
SaveWindowAtts.fileName = "visit"
SaveWindowAtts.family = 1
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SaveWindowAtts.width = 1024
SaveWindowAtts.height = 1024
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.ScreenProportions  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.advancedMultiWindowSave = 0
visit.SetSaveWindowAttributes(SaveWindowAtts)
visit.SaveWindow()
# Begin spontaneous state
View3DAtts = visit.View3DAttributes()
View3DAtts.viewNormal = (0.264045, 0.220135, 0.939053)
View3DAtts.focus = (1, 1, 1)
View3DAtts.viewUp = (0.100817, 0.961974, -0.253856)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 1.73205
View3DAtts.nearPlane = -3.4641
View3DAtts.farPlane = 3.4641
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (1, 1, 1)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
visit.SetView3D(View3DAtts)
# End spontaneous state

