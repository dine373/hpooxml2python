import untangle

obj = untangle.parse('files.xml')

print obj.steps
print obj.foo.bar.type['foobar']
print obj.foo.bar
