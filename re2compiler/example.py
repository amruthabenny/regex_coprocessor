import re2compiler

data 	= '(a|a_b)*'
output	= re2compiler.compile(data=data)
print(output)
