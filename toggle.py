#!/usr/bin/env python
import sys
import RPi.GPIO as g
state=sys.argv[1]
g.setmode(g.BOARD)
led = 3
g.setup(led,g.OUT)
if state=="on":
	g.output(led,True)
else:
	g.output(led,False)
