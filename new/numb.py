import collections
import os
a = [1,2,3,4,5]
for i in a: print i 
d = collections.OrderedDict()
d = {'s':'s'}
x = {'x' : 'x'}

d.update(x)

print d

v = 'v'
d[v] = v
x = {'is': 'x'}
d.update(x)
print d


print d['is']
