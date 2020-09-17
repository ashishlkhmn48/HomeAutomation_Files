#!/usr/bin/python
import httplib
import urllib
import Adafruit_DHT
import time
# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
sensor = Adafruit_DHT.DHT11


pin = 17
# BCM pin is 17 , pin according to board is 11

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).

while (1):
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	localtime = time.asctime( time.localtime(time.time()) )

        if humidity is not None and temperature is not None:
#code to send data to server
                conn = httplib.HTTPConnection("lakhmanianita.000webhostapp.com")
                params = urllib.urlencode({"temperature":int(temperature),"humidity":humidity,"date_time":localtime})
                headers = {"Content-type":"application/x-www-form-urlencoded"}
                conn.request("POST", "/notification_home_automation.php",params,headers)
                r1 = conn.getresponse()
		print "Formatted time :", localtime
                print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
                print r1.read()
                time.sleep(3)

	else:

		print('Failed to get reading. Try again!')

