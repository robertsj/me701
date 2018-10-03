# need to run with Python 2  (e.g., python2)
import sys
sys.path.append("/home/robertsj/opt/visit/visit2_13_2.linux-x86_64/2.13.2/linux-x86_64/lib/site-packages/")
import visit
visit.Launch()
visit.ShowAllWindows()
visit.OpenDatabase("/home/robertsj/opt/visit/visit_data_files/CThead_mid.silo")
visit.AddPlot("Volume", "head")

visit.AddOperator("Slice")
s = visit.SliceAttributes()
s.originType = s.Intercept
s.axisType = s.ZAxis
s.originIntercept = 60.0
visit.SetOperatorOptions(s)
visit.DrawPlots()


visit.SaveWindow()
