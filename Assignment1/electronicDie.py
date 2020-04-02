from sense_hat import SenseHat
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

    def roll(self, displayRoll):
        #gets a random int between 1 and {sides}
        rand = int(round((random() * (self.sides-1)) + 1, 0));
        if(displayRoll):
            self.displayRoll(rand)
        else:
            sense.show_message(num)
        return rand

    def displayRoll(self, num):
        if num <= 6:
            sense.set_pixels(dieFaces[num-1])
        else:
            sense.show_message(
            str(player.points),
            scroll_speed = 0.05
        )
        time.sleep(2)
        sense.clear()



b = (0, 0, 0)
w = (255, 255, 255)

dieFaces = [
    [
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, w, w, b, b, b,
    b, b, b, w, w, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b
    ],
    [
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, w, w, b,
    b, b, b, b, b, w, w, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, w, w, b, b, b, b, b,
    b, w, w, b, b, b, b, b,
    b, b, b, b, b, b, b, b
    ],
    [
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, w, w, b,
    b, b, b, b, b, w, w, b,
    b, b, b, w, w, b, b, b,
    b, b, b, w, w, b, b, b,
    b, w, w, b, b, b, b, b,
    b, w, w, b, b, b, b, b,
    b, b, b, b, b, b, b, b
    ],
    [
    b, b, b, b, b, b, b, b,
    b, w, w, b, b, w, w, b,
    b, w, w, b, b, w, w, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, w, w, b, b, w, w, b,
    b, w, w, b, b, w, w, b,
    b, b, b, b, b, b, b, b
    ],
    [
    b, b, b, b, b, b, b, b,
    b, w, w, b, b, w, w, b,
    b, w, w, b, b, w, w, b,
    b, b, b, w, w, b, b, b,
    b, b, b, w, w, b, b, b,
    b, w, w, b, b, w, w, b,
    b, w, w, b, b, w, w, b,
    b, b, b, b, b, b, b, b
    ],
    [
    b, w, w, b, b, w, w, b,
    b, w, w, b, b, w, w, b,
    b, b, b, b, b, b, b, b,
    b, w, w, b, b, w, w, b,
    b, w, w, b, b, w, w, b,
    b, b, b, b, b, b, b, b,
    b, w, w, b, b, w, w, b,
    b, w, w, b, b, w, w, b
    ],
]
