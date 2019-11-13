#!/usr/bin/python3

import sys
import Adafruit_DHT
import time
import http.client as http
import urllib
import json

deviceid="Dbod01o0"
deviceKey="5xO9OGH0eZafS6Zp"
def post_to_mcs(payload):
	headers={"Content-type":"application/json","deviceKey":deviceKey}
	not_connected=1
	while(not_connected):
		try:
			conn=http.HTTPConnection("api.mediatek.com:80")
			conn.connect()
			not_connect = 0
		except(http.HTTPException,scoket.error)as ex:
			print("Error:%s"%ex)
			time.sleep(10)
			#sleep 10 seconds
	conn.request("POST","/mcs/v2/devices/" + deviced + "/datapoints",json.dumps(payload),headers)
	response = conn.getresponse()
	print(response.status, response.reason, json.dumps(payload), time.strftime("%c"))
	data = response.read()
	conn.close()



# Parse command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
else:
    print('Usage: sudo ./Adafruit_DHT.py [11|22|2302] <GPIO pin number>')
    print('Example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO pin #4')
    sys.exit(1)

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry)

# Un-comment the line below to convert the temperature to Fahrenheit.
# temperature = temperature * 9/5.0 + 32

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
#if humidity is not None and temperature is not None:
#    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
#else:
#    print('Failed to get reading. Try again!')
#    sys.exit(1)
while True:
	h0,t0=Adafruit_DHT.read_retry(sensor,pin)
	if h0 is not None and t0 is not None:
		print('Temp={0:0.1f}* Humi={1:0.1f}%'.format(t0, h0))
		payload={"datapoints":[{"dataChnld":"Humidity","values":{"values":ho}},{"dataChnld":"Temperature","values":{"values":to}}]}
		post_to_mcs(payload)
		time.sleep(10)
	else:
		print('Failed to get reading, Try again!')
		sys.exit(1)
