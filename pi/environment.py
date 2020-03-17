from sense_hat import SenseHat
import firebase_admin
from firebase_admin import credentials, firestore
from math import floor, ceil
import time

# firebase
cred = credentials.Certificate("//")
firebase_admin.intialize_app(cred)

# db 
db = firestore.client()

# sensehat
sense = SenseHat()
sense.set_imu_config(False,False,False)
sense.clear()

#color defined
color_blue = (0, 0, 255)
color_black = (0, 0, 0)



while True: 
	#matrix
	pattern = ""
	matrix = []
	for r in range(0,8):
		temp = ""
		for c in range(0,4):
			temp = temp + str(round(random.random()))
		temp = temp + temp[::-1]
		pattern = pattern + temp

	#defined the bits wich wil display
	for p in range(0,64):
		bit = int(pattern[p])
		color = color_blue if bit  == 1 else color_black
		matrix.append(color)

	#data
	Setdata = {
			u'temperature':sense.get_temparture(),
			u'humidity':sense.get_humidity(),
	}
db.collection(u'raspcollection').document(u'sensor-data').set('Setdata')
sense.set_pixels(matrix)
time.sleep(60)

