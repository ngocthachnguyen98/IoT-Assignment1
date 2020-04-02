# ProgIoT - Assignment 1

This is Assignment 1 for Programming Internet of Things course at RMIT in Semester 1 2020.

This is assignment containing 3 tasks.

### Task A - [animatedEmoji.py](Assignment1/animatedEmoji.py)

This task involves display 3 Emoji faces in the LED matrix on Sense HAT with distinctive colors for each emoji.

The 3 emojis are smiley face, sad face and winky face which are displayed in the same order as named with 3-second intervals.

This task is handled by Thach Ngoc Nguyen

### Task B - [config.json](Assignment1/config.json), [monitorAndDisplay.py](Assignment1/monitorAndDisplay.py)

A pre-defined [config.js](Assignment1/config.json) file is provided with 3 levels of temperature. 

[monitorAndDisplay.py](Assignment1/monitorAndDisplay.py) which will read the temperature from the sensor and display current temperature in LED matrix on Sense HAT, refreshed every 10 seconds.

1. If the level of temperature is cold, display temperature with blue colour
2. If the level of temperature is comfortable, display temperature with green colour
3. If the level of temperature is hot, display temperature with red colour

This task is handled by Thach Ngoc Nguyen

### Task C - [electronicDie.py](Assignment1/electronicDie.py), [game.py](Assignment1/game.py)

A python file called [electronicDie.py](Assignment1/electronicDie.py) is programmed to trigger the roll of the die when shaking the Raspberry Pi. Shaking motion will be detected by IMU sensor and then display the die in random matter.

A python file called [game.py](Assignment1/game.py) will use the electronic die to play a game with two players. 
The players will shake the Raspberry Pi several times one by one until one player gets above 30 points. The player who gets above 30 points first is the winner.
Instruction and feedback messages will be prompted. 
At the end of the game, a record of the winner will be written to [winner.csv] file, including time and score.

This task is handled by Michael Hamilton