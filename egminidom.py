#!/usr/bin/python

from xml.dom.minidom import parse
import xml.dom.minidom

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("copy1.xml")
collection = DOMTree.documentElement

steps = collection.getElementsByTagName("step")

for step in steps:
 print "step"
 if step.hasAttribute("id"):
  print "Step id : %s" % step.getAttribute("id")
 name = step.getElementsByTagName('name')[0]
 print "name : %s" % name.childNodes[0].data
 print "name :%s" % name.childNodes[0]
