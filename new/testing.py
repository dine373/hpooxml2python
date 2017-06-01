#import numpy as np
from collections import defaultdict
from shutil import copyfile
import xml.etree.ElementTree as ET
filename='copyresource.xml'
tree = ET.parse(filename)
root = tree.getroot()
"""a = [ ]
b = [] 
c = [] 
for step in root.findall("step"):
# print step.find('name').text + "," +  step.get('id')
 a = step.find('name').text + "," + step.get('id')
# print a
for returnstep in root.findall("returnStep"):
# print returnstep.find('name').text + "," + returnstep.get('id')
 b.append((returnstep.find('name').text) + ":")
 b.append(returnstep.get('id'))
 c = returnstep.find('name').text + ":" + returnstep.get('id')
 print "....."
 print b[1]
 print c[1]
 print b
 print c
"working .... 
"""
def success(x, y):
 name = x
 ids = y
 #print "success inside loop"
 print name
 #print ids 

def failure(x, y):
 name = x
 ids = y
 print "failure"
 #print ids

def copy():
 copyfile("testing.py", "/tmp/testing.py")
 print "file copyied"
 for trans in steps.iter('transition'):
  transname = trans.find('name').text # failure, succesS
  if( transname == 'failure'):
    for dest in trans.iter('destination'):
     destid = dest.find('refId').text
     #print destid
     if (destid == faid):
      failure(transname , destid)
  if( transname == 'success'):
    for dest in trans.iter('destination'):
      destid = dest.find('refId').text
      if (destid == suid):
       success(transname, destid)
 #copyfile(x, y)
 #print "File is copied"

for steps in root.iter('returnStep'):
 name = steps.find('name').text
 if (name == "Resolved : success"):
  global suid 
  suid = steps.get('id')
  success(name, suid) 
 if (name == "Error : failure"):
  global faid
  faid = steps.get('id')
  success(name, faid) 
  #print "testing"

print "-------------------------------------------------------------------------"
print "Id's of sucsss and failure......"
print suid
print faid
print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"


for steps in root.iter('step'):
 id = steps.get('id')
 name = steps.find('name').text
 print name
 if (name == 'FS Copy'):
  copy()
  #trans = steps.find('transitions')
 # for trans in steps.iter('transition'):
 #  transname = trans.find('name').text # failure, succesS
 #  if( transname == 'failure'):
 #   for dest in trans.iter('destination'):
 #    destid = dest.find('refId').text
 #    print destid
 #    if (destid == faid):
 #     failure(transname , destid)
       
 #if (name == 'FS Copy'):
 # success(name, id)


#
# d = defaultdict(list)
# for k,v in b:
#  d[k].append(v)

#print d.items()

"""

print "+++++++++++++++++++++++++++++"

import untangle

obj = untangle.parse('copyresource.xml')

#print obj.steps.step['id']
#print obj.steps.attrib
#print obj.steps.name

import xmltodict

with open('copyresource.xml') as fd:
 doc = xmltodict.parse(fd.read())
 returnstepname = (doc['steps']['returnStep'][0]['name'])
 returnstepid = (doc['steps']['returnStep'][0]['@id'])
 returnstep = (doc['steps']['returnStep'])
 #print returnstepid
 for returnsteps in returnstep
  print returnsteps
 


def fail( x, y):
 name = x 
 ids = y 
 print "failure"

def success(x, y):
 name = d
 ids = y
 print "success"

"""


