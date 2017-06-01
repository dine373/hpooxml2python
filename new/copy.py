from shutil import copyfile
import os
import sys
try :
 copyfile('testig.py' , '/tmp/copyreso.xml')
except EnvironmentError,e: 
 print "error happend %s " %e
else:
 print "ok"
#os.system("copyfile")
#if sys.exit() == '1':
# print "exit"
