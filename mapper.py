#!/usr/bin/env python
import sys
for line in sys.stdin:
	line=line.strip()
	line=line.split(",")
	if len(line)>=2:
		gender=line[1]
		age=line[2]
		print'%s \t %s'%(gender,age)
