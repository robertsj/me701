# need to run with Python 2  (e.g., python2)
import sys
sys.path.append("/home/robertsj/opt/visit2_12_3.linux-x86_64/2.12.3/linux-x86_64/lib/site-packages/")
import visit
visit.Launch()
visit.ShowAllWindows()
visit.OpenDatabase("test.vtk")
visit.AddPlot("Pseudocolor", "scalars")
visit.DrawPlots()
visit.SaveWindow()
