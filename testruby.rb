#!/usr/bin/env ruby  -Ku 
require 'rexml/document' 
include REXML 
File.open("file.xml") do |doc| 
  xml = Document.new(doc) 
  xml.elements.each("steps") do |elem| 
    elem.elements.each {|x| print "->#{x}\n" } 
  end 
end
