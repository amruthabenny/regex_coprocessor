import re2compiler
import sys
import os


fp = None
input_re = sys.argv[1]
if os.path.isfile(input_re):
    fp = open(input_re, "r")
    regex = fp.readline()
    #print(regex)
    machine_code = re2compiler.compile(data=regex)
    print("Resultant code:\n",machine_code)
else:
    print(f"{input_re} does not exist")
    sys.exit(1)
