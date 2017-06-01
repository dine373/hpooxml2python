from shutil import copyfile
import inspect
import xml.etree.ElementTree as ET
filename='copy_fulladd.xml'
tree = ET.parse(filename)
root = tree.getroot()
global i
global successid
global failureid
global copyid
global copy2id
i = 0
r = 0
s = {}
print filename
print "------------------"
global startstep
startstep = root.find('startSteps').text
print "Start of Step : ", startstep
print "----------------------------------------------------\n"
#startstep = 'd72'

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

#print step.get('id')
def d7e7():
# print "success"
 for returnstep in steps.iter('returnStep'):
  if(returnstep.find('name').text == 'Resolved : success'):
    successid = returnstep.get('id')
    name = returnstep.find('name').text
    print "Return Step success id is (successid):", successid , "\n", inspect.stack()[0][3]

def d299():
# global failureid
# print "failure"
 for returnstep in steps.iter('returnStep'):
  if(returnstep.find('name').text == 'Error : failure'):
   failureid = returnstep.get('id')
   name = returnstep.find('name').text
   print "Failure Step failure id is (failureid):" , failureid , "\n", inspect.stack()[0][3]


def fdaf():

 for step in steps.iter('step'):
  if (step.find('name').text == 'FS Copy'):
 #  global copyid
   print "first step - copy"
   #copyid = step.get('id')
   copyid = step.find('name').text
   #s.append(copyid)
   name = step.find('name').text
   fun = inspect.stack()[0][3]
   #s[copyid] = fun
   print "Copy Step id is (copyid):", copyid, "\ntestttttttttttttt", inspect.stack()[0][3], name
  # for trans in step.iter('transitions'):
   for tran in step.iter('transition'):
    #print tran.find('name').text
    if(tran.find('name').text == 'success'):
     a=tran.find('destination')
     print a.find('refId').text
     t=a.find('refId').text
     nex = t[:4]
     print nex
     eval(nex+'()')
def d72():
 for step in steps.iter('step'):
  if(step.find('name').text == 'FSCopy2'):
  # global copy2id
   print "second step - copy"
   copy2id = step.get('id')
   #s.append(copy2id)
   name = step.find('name').text
   fun = inspect.stack()[0][3]
   #s[copy2id] = fun
   print "Copy 2 Step id is (copy2id): ", copy2id,  "\n", inspect.stack()[0][3]
   for tran in step.iter('transition'):
    if(tran.find('name').text == 'failure'):
      a=tran.find('destination')
      print a.find('refId').text


for steps in root.iter('steps'):
 for returnstep in steps.iter('returnStep'):
   name = returnstep.find('name').text
   if (name == 'Resolved : success'):
    #success()
    print name, returnstep.get('id')
   if (name == 'Error : failure'):
    print name, returnstep.get('id')
 print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
 for step in steps.iter('step'):
  name = step.find('name').text
  if(name == 'FS Copy'):
 #  copy()
   print name, step.get('id')
  if(name == 'FSCopy2'):
    print name, step.get('id')
 print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
"""
#print s
#j=0
#for j in range(len(s)):
 #print s[j]
# if(s[j] == startstep):
 # print s[j], name

#print list(s.values())

#print s.get("FS Copy")


for key, values in s.iteritems(): 
 # print key, values
 if(key == startstep):
   eval(values+'()')


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
 for stepa in steps.iter('step'):
  id = stepa.get('id')
  fun = id[:4]
  s[fun] = id
 for returnstep in steps.iter('returnStep'):
  id = returnstep.get('id')
  fun = id[:4]
  s[fun] = id
 for j in s:
  print j, s[j]
 print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

#for steps in root.iter('steps'):
# for step in steps.iter('step'):
for key,values in s.iteritems():
 if(values == startstep):
  eval(key+'()')
#  print values, key
#  eval(key+'()')
#  print "byyeep"


#print step.get('id')
# for j in s:
 #print j,s[j]
#   if(s[j] == startstep):
#    a = j
#a = 'd72'

#eval(a+'()') 

#for key, values in s.iteritems():
# print key, values
