from datetime import datetime as date
from dateutil.rrule import *

def get_dates(dates) :
  """ Return a list of dates on which classes could be held.
  """

  # base rule, e.g., available M, W, F's
  base = rrule(WEEKLY, dtstart=dates['start'], \
               until=dates['end'], byweekday=(dates['days']))

  # generate lecture dates
  lecturedates = rruleset()  
  lecturedates.rrule(base)
  for d in dates['holiday'] : 
    lecturedates.exdate(d[0])
  for exam in dates['exam'] : 
    lecturedates.exdate(exam[0])

  # generate all meaningful dates to list
  alldates = rruleset()
  alldates.rrule(base)
  for exam in dates['exam'] : 
    alldates.rdate(exam[0])
  for hw in dates['homework'] : 
    alldates.rdate(hw[0]) # given
    alldates.rdate(hw[1]) # due
  for exam in dates['other'] : 
    alldates.rdate(exam[0])
  return list(lecturedates), list(alldates)

class ClassDate() :

  def __init__(self, date) :
    self.reading = ""
    self.description = ""
    self.lecture = ""
    self.date = date.strftime("%a %m/%d")

  def display(self) :
    out = self.date + " & " + self.lecture +  " & " + self.description + " \\\\ \hline " 
    print out

def print_syllabus(dates, lectures) :

  d, ad = get_dates(dates)
  
  if (len(d) < len(lectures)) :
    exit('# lectures = ' + str(len(lectures)) + ' > # days = ' + str(len(d)))

  data = {}
  for i in ad :
    data[i] = ClassDate(i)

  # add lectures
  for i in range(0, len(lectures)) :
    data[d[i]].reading     = lectures[i][0]
    data[d[i]].description = lectures[i][1]
    data[d[i]].lecture     = str(i + 1)

  # add exams
  for exam in dates['exam'] :
    data[exam[0]].description = "{\\bf \\textcolor{red}{" + exam[1] + ".}}"


  # add holidays
  for h in dates['holiday'] :
    data[h[0]].description = "{\\bf \\textcolor{green}{NO CLASS: " + h[1] + ",}}"
  
  # add announcements
  for h in dates['announce'] :
    data[h[0]].description += " {\\bf \\textcolor{orange}{NOTICE: " + h[1] + ",}}"
  
  # add other
  for h in dates['other'] :
    data[h[0]].description += " {\\bf \\textcolor{red}{" + h[1] + "}}."
  
  # add homework
  for i in range(0, len(dates['homework'])) :
    data[dates['homework'][i][0]].description += " {\\bf \\textcolor{blue}{HW " + str(i+1) + " GIVEN}}."
    data[dates['homework'][i][1]].description += " {\\bf \\textcolor{red}{HW " + str(i+1) + " DUE}}."

  for i in ad :
    data[i].display()


