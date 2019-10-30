# need to run with Python 2  (e.g., python2)
#export PATH=$PATH:/home/robertsj/opt/visit/visit3_0_2.linux-x86_64/bin
#export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/robertsj/opt/visit/visit3_0_2.linux-x86_64/3.0.2/linux-x86_64/lib
import sys
sys.path.append("/home/robertsj/opt/visit/visit3_0_2.linux-x86_64/3.0.2/linux-x86_64/lib/site-packages/visit")
import visit
visit.Launch()
visit.ShowAllWindows()
visit.OpenDatabase("/home/robertsj/opt/visit/visit_data_files/CThead_mid.silo")
visit.AddPlot("Pseudocolor", "head")

visit.AddOperator("Slice")
s = visit.SliceAttributes()
s.originType = s.Intercept
s.axisType = s.ZAxis
s.originIntercept = 60.0
visit.SetOperatorOptions(s)
visit.DrawPlots()


#visit.SaveWindow()
