import xml.etree.ElementTree as ET
filename='copy1.xml'
tree = ET.parse(filename)
root = tree.getroot()
#steps=[]
#returnsteps=[]
#values=[]
#print root.tag

#for x in root.findall('step'):
# steps.append(x.find('name').text)
 #steps.append(x.attrib)
 #values.append(x.attrib)
# values.append(x.items())
# print list(x)
# print x.itertext()
#for x in root.findall('returnStep'):
# returnsteps.append(x.find('name').text)

#print steps[1]
#print values[0]
#print(returnsteps)


print "------------"

#test = ET.Element(steps)
#print test

#import subprocess
#import os

#os.putenv('Steps', ''.join(steps))
#subprocess.call["./test.sh"]

#content = ET.iterparse('copy1.xml', events=('end',))
#for event, elem in content:
# if elem.tag == 'name':
#  print elem.text
#  print steps

#for step in steps:
# print step



for step in root:
 #print step
 for transitions in step:
  for transition in transitions:
   print transition.tag
   step_name = transition.find('destination').find('refId')
   print step_name
#  print name.text
# step_destinations = step.find('transitions').find('transition').find('destination').find('refId')
# print  step_name.tag
# z = step_name.find('transition')
# x = z.find('destination')
# y = x.find('refId')
# print y.text
# print step_destinations.text
 
