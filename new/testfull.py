import subprocess as sp
import os
import xml.etree.ElementTree as ET
filename='copyunzip_resource.xml'
tree = ET.parse(filename)
root = tree.getroot()
global startstep 
i = 0; r =0; s = {}; p ={}; 

print "FileName Used\t\t\t:\t " , filename
startstep = root.find('startSteps').text
print "Starting Step id of the process : \t",startstep
print "----------------------------------------------------------------------------"


# Print No of Steps and Return steps in the Process

for steps in root.iter('steps'):
 print "SNo",'\t'," StepName",'\t', "ID"
 for step in steps.iter('step'):
  i = i+1;
  print i,'\t',step.find('name').text,'\t',step.get('id')
 print "\nTotal No of Steps :" , i
 print "---------------------------------------------------------------------------- "
 print "SNo", '\t', "ReturnStepName", '\t',"ID"
 for returnstep in steps.iter('returnStep'):
  r = r+1 
  print r,'\t',returnstep.find('returnStepType').text,'\t', returnstep.get('id')
 print "\nTotal No of ReturnSteps :" , r
print "-----------------------------------------------------------------------------\n\n"


#Collect All Id's in a dict
for steps in root.iter('steps'):
 for step in steps.iter('step'):
  id = step.get('id')
  fun = id[:4]
  s[fun] = id
 for returnstep in steps.iter('returnStep'):
  id = returnstep.get('id')
  fun = id[:4]
  s[fun] = id


#Defining all functions for each step and return step with function name as first four characters of their id

def d7e7():
 for returnstep in steps.iter('returnStep'):
  if(returnstep.find('returnStepType').text == 'RESOLVED'):
    successid = returnstep.get('id')
    print "Success Step"
    dest = returnstep.find('transitions').find('transition').find('destination').find('refId').text
    source = returnstep.find('transitions').find('transition').find('source').find('refId').text
    if ( source == dest):
      print "Process done"

def d299():
 for returnstep in steps.iter('returnStep'):
  if(returnstep.find('returnStepType').text == 'ERROR'):
   failureid = returnstep.get('id')
   print "Failure Step"
   dest = returnstep.find('transitions').find('transition').find('destination').find('refId').text
   source = returnstep.find('transitions').find('transition').find('source').find('refId').text
   if (source == dest):
     print "Process Failed"

def fdaf():
 for step in steps.iter('step'):
  if (step.find('name').text == 'FS Copy'):
   print "Step No 1 - FS Copy : \n"
   # Getting Property from Steps
   for property in step.iter('bindings'):
    for staticinput in property.iter('staticBinding'):
     var = staticinput.find('inputSymbol').text
     val = staticinput.find('value').text
     p[var] = val
    for userinput in property.iter('userInputBinding'):
     var = userinput.find('inputSymbol').text
     val = raw_input("Enter value for "+var+ " : ")
     p[var] = val
    print "-----------------------------------------------------------------"
    print "Total properties in "+ step.find('name').text ,":"
    for j in p:
     print j , " " , p[j]
    print "-----------------------------------------------------------------\n"
   if p.values()[2] in ('true','yes','y'): 
    p[p.keys()[2]] = ' -r'
   if p.values()[2] in ('false','no', 'n'):
    p[p.keys()[2]] = ' -n'
   #cmd = 'cp'+p.values()[2]+' '+p.values()[0]+' '+p.values()[1]
   cmd = 'cp ' + (' '.join(p.values())) 
   #print (' '.join(p.values()))
   print "command to execute : ", cmd
   try :
    sp.check_output(cmd, shell=True)
    ret = 0
   except sp.CalledProcessError as e:
    ret = e.returncode
   # print ret
   for tran in step.iter('transition'):
 #   tran = step.find('transitions').find('transition')
    if((tran.find('name').text == 'success') and not ret):
     nextprocess = tran.find('destination').find('refId').text
     for j in s:
      if(s[j] == nextprocess):
       eval(s[j][:4]+'()')
       #fdaf()
    if((tran.find('name').text == 'failure') and ret):
     nextprocess = tran.find('destination').find('refId').text
     for j in s:
      if(s[j] == nextprocess):
       eval(s[j][:4]+'()')


def seco():
 for step in steps.iter('step'):
  if (step.find('name').text == 'Copy2'):
   print "Step No 2 - COPY2 : \n"
   # Getting Property from Steps
   for property in step.iter('bindings'):
    for staticinput in property.iter('staticBinding'):
     var = staticinput.find('inputSymbol').text
     val = staticinput.find('value').text
     p[var] = val
    for userinput in property.iter('userInputBinding'):
     var = userinput.find('inputSymbol').text
     val = raw_input("Enter value for "+var+ " : ")
     p[var] = val
    print "-----------------------------------------------------------------"
    print "Total properties in "+ step.find('name').text ,":"
    for j in p:
     print j , " " , p[j]
    print "-----------------------------------------------------------------\n"
   if p.values()[2] in ('true','yes','y'):
    p[p.keys()[2]] = ' -r'
   if p.values()[2] in ('false','no', 'n'):
    p[p.keys()[2]] = ' -n'
   #cmd = 'cp'+p.values()[2]+' '+p.values()[0]+' '+p.values()[1]
   cmd = 'unzip ' + (' '.join(p.values()))+' -d'
   #print (' '.join(p.values()))
   print "command to execute : ", cmd
   try :
    sp.check_output(cmd, shell=True)
    ret = 0
   except sp.CalledProcessError as e:
    ret = e.returncode
   # print ret
   for tran in step.iter('transition'):
 #   tran = step.find('transitions').find('transition')
    if((tran.find('name').text == 'success') and not ret):
     nextprocess = tran.find('destination').find('refId').text
     for j in s:
      if(s[j] == nextprocess):
       eval(s[j][:4]+'()')
       #fdaf()
    if((tran.find('name').text == 'failure') and ret):
     nextprocess = tran.find('destination').find('refId').text
     for j in s:
      if(s[j] == nextprocess):
       eval(s[j][:4]+'()')



# Starting the Main process 

for j in s:
 if(s[j] == startstep):
  eval(s[j][:4]+'()')


