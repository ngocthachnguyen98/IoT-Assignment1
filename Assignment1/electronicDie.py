from sense_hat import SenseHat
import random
from random import seed
from random import random
from datetime import datetime
import time

seed(datetime.now())
sense = SenseHat()

class Die:

	def __init__(self, sides):
		self.sides = sides

	def waitForShake(self):
		while True:
			acceleration = sense.get_accelerometer_raw()
			x = acceleration['x']
			y = acceleration['y']

			overallAccel = x + y
			threshold = 1
			if overallAccel > threshold:
				return

	def roll(self):
		#gets a random int between 1 and {sides}
		return int(round((random() * (self.sides-1)) + 1, 0))



