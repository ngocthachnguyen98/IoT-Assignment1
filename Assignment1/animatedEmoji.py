import logging
from sense_hat import SenseHat
from time import sleep

# Config logging
logging.basicConfig(level=logging.DEBUG)

# Declaring varibables 
sense = SenseHat()

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

smiley_face = [
    black, black, black, black, black, black, black, black,
    black, black, red, black, black, red, black, black,
    black, black, red, black, black, red, black, black,
    black, black, black, black, black, black, black, black,
    black, red, black, black, black, black, red, black,
    black, black, red, black, black, red, black, black,
    black, black, black, red, red, black, black, black,
    black, black, black, black, black, black, black, black
]

sad_face = [
    black, black, black, black, black, black, black, black,
    black, black, green, black, black, green, black, black,
    black, black, green, black, black, green, black, black,
    black, black, black, black, black, black, black, black,
    black, black, black, green, green, black, black, black,
    black, black, green, black, black, green, black, black,
    black, green, black, black, black, black, green, black,
    black, black, black, black, black, black, black, black
]

winky_face = [
    black, black, black, black, black, black, black, black,
    black, black, blue, black, black, black, blue, black,
    black, black, blue, black, black, blue, blue, blue,
    black, black, black, black, black, black, black, black,
    black, blue, black, black, black, black, blue, black,
    black, black, blue, black, black, blue, black, black,
    black, black, black, blue, blue, black, black, black,
    black, black, black, black, black, black, black, black
]

# Animating emojis (smiley -> sad -> winky)
while True:
    sense.set_pixels(smiley_face)
    sleep(3)
    logging.debug("Animating Smiley Face")

    sense.set_pixels(sad_face)
    sleep(3)
    logging.debug("Animating Sad Face")
    
    sense.set_pixels(winky_face)
    sleep(3)
    logging.debug("Animating Winky Face")
