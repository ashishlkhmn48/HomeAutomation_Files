import sys
import RPi.GPIO as G
import time
G.cleanup()
G.setmode(G.BOARD)
trig=3
echo=7
buzz=10
count=0
G.setup(trig,G.OUT)
G.setup(echo,G.IN)
G.setup(buzz,G.OUT)
type = sys.argv[1]

if(type == "on") :
	while (1):
        	G.output(trig,False)
        	time.sleep(0.5)
    	    	G.output(trig,True)
       		time.sleep(0.00001)
       	 	G.output(trig,False)
		while G.input(echo)==0:
                	pulse_start=time.time()
      		while G.input(echo)==1:
                	pulse_end=time.time()
        	duration=pulse_end-pulse_start
        	distance=34300*duration/2
        	#print "Distance = ",distance," cm    "
		#print count
		if (distance<=30 and distance>3):
			count=count+1
			if (count>=8):
				count=0
				G.output(buzz,True)
				time.sleep(5)
				G.output(buzz,False)
		
		else:
			count=0
	
else : 
	sys.exit()