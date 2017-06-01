from shutil import copyfile
import inspect
import xml.etree.ElementTree as ET
filename='copy_fulladd.xml'
tree = ET.parse(filename)
root = tree.getroot()
global i
i = 0
r = 0
s = {}
print filename
print "------------------"
global startstep
startstep = root.find('startSteps').text
print "Start of Step : ", startstep
print "----------------------------------------------------\n"

for steps in root.iter('steps'):
 for step in steps.iter('step'):
  i = i+1;
  print i,'.  ' ,   step.find('name').text
 print "\nTotal No of Steps :" , i
 print "-------------------------------------------------------------------------- \n"
 for returnstep in steps.iter('returnStep'):
  r = r+1 
  print r , '.   ', returnstep.find('name').text
 print "\nTotal No of ReturnSteps :" , r
 print "--------------------------------------------------------------------------\n"


def d299():
 global successid
# print "success"
 successid = returnstep.get('id')
 name = returnstep.find('name').text
 print "Return Step success id is (successid):", successid , "\n", inspect.stack()[0][3]

def d7e7():
 global failureid
# print "failure"
 failureid = returnstep.get('id')
 name = returnstep.find('name').text
 print "Failure Step failure id is (failureid):" , failureid , "\n", inspect.stack()[0][3]

def fdaf():
 global copyid
 print "first step - copy"
 copyid = step.get('id')
  #s.append(copyid)
 name = step.find('name').text
 fun = inspect.stack()[0][3]
 #s[copyid] = fun
 print "Copy Step id is (copyid):", copyid, "\n", inspect.stack()[0][3]

def d72():
 global copy2id
 print "second step - copy"
 copy2id = step.get('id')
 #s.append(copy2id)
 name = step.find('name').text
 fun = inspect.stack()[0][3]
 #s[copy2id] = fun
 print "Copy 2 Step id is (copy2id): ", copy2id,  "\n", inspect.stack()[0][3]

"""

for steps in root.iter('steps'):
 for returnstep in steps.iter('returnStep'):
   name = returnstep.find('name').text
   if (name == 'Resolved : success'):
    success()
   if (name == 'Error : failure'):
    failure()
 print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
 for step in steps.iter('step'):
  name = step.find('name').text
  if(name == 'FS Copy'):
 #  copy()
   print 'bye'
  if(name == 'FSCopy2'):
   copy2()
 print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"

#print s
#j=0
#for j in range(len(s)):
 #print s[j]
# if(s[j] == startstep):
 # print s[j], name

#print list(s.values())

#print s.get("FS Copy")
"""
print s
for key, values in s.iteritems(): 
 # print key, values
 if(key == startstep):
   eval(values+'()')

"""
def fdaf():
 print "First step"
 a = 'd72'
 for key, values in s.iteritems():
  if (key == 'faf'):
    eval(a+'()')

def d72():
# print "asd"
 print ""

"""

for steps in root.iter('steps'):
 for step in steps.iter('step'):
  id = step.get('id')
  fun = id[:4]
  s[fun] = id
 for returnstep in steps.iter('returnStep'):
  id = returnstep.get('id')
  fun = id[:4]
  s[fun] = id
 for j in s:
  print j, s[j]
 for key,values in s.iteritems():
  if(values == startstep ):
   eval(key+'()')  

#for j in s:
# print j,s[j]

#for key, values in s.iteritems():
# print key, values
