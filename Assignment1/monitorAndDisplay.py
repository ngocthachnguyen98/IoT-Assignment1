from time import sleep
from sense_hat import SenseHat
import json

# Declare varibles
sense = SenseHat()

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


# Read and declare variables from config.json file
with open("config.json", "r") as read_file:
    data = json.load(read_file)

cold_max = data["cold_max"]
comfortable_min = data["comfortable_min"]
comfortable_max = data["comfortable_max"]
hot_min = data["hot_min"]


# Get temperature from Sense Hat
temp = sense.get_temperature()
temp = round(temp, 1) # Round up to one decimal point


# Display message on Sense Hat
while True:
    if temp <= cold_max: background = blue
    elif comfortable_min < temp < comfortable_max: background = green
    elif temp >= hot_min: background = red

    sense.show_message(
        "Temperature: " + str(temp) + "*C",
        scroll_speed = 0.1,
        back_colour =  background
    )

    # Delay 10s and refresh the display
    sleep(10) 