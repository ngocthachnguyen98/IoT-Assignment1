import time
from datetime import datetime
import electronicDie
from electronicDie import Die
import csv
from sense_hat import SenseHat

sense = SenseHat()

class Game:

	def __init__(self, players):
		sense.clear()
		self.scoreBoard = ScoreBoard(players)
		self.die = Die(6)
		self.players = players


	def start(self):
		self.showMessage("Shake the dice (the pi) to score points equal to the number rolled.")
		self.showMessage("First one to 30 points wins.")
		currentPlayerIndex = 0
		while True:
			winningPlayer = self.playTurn(self.players[currentPlayerIndex])
			if winningPlayer is not None:
				self.announceWinner(winningPlayer)
				break
			currentPlayerIndex = 1-currentPlayerIndex #convert 0 to 1 or vice versa


	def playTurn(self, player):
		print("%s, it is your turn to roll." % (player.name))
		self.die.waitForShake()

		print("Rolling...")
		rand = self.die.roll(True)
		player.addPoints(rand)
		self.showScore()
		self.scoreBoard.showScore(player)

		self.scoreBoard.display()

		if player.points > 30:
			return player


	def showScore(self):
		for player in self.players:
			print(str(player.name) + ": " + str(player.points))


	def announceWinner(self, player):
		self.showMessage(player.name + " Won!")

		# Write record to a .csv file
		try:
			with open("winner.csv", "a") as file:
				writer = csv.writer(file, delimiter = "\t")
				writer.writerow([datetime.now(), player.name, player.points])
				file.close()
		except FileNotFoundError: # Catch exception if file is not found
			print("ERROR: winner.csv doesn't exist")


	def showMessage(self, message):
		print(message)
		sense.show_message(message, 
            scroll_speed = 0.05,
            back_colour =  b
		)




class Player:
	def __init__(self, name, color1, color2):
		self.name = name
		self.color1 = color1
		self.color2 = color2
		self.points = 0


	def addPoints(self, points):
		print("%s scored %d points!"% (self.name, points))
		self.points += points




class ScoreBoard:
	def __init__(self, players):
		self.players = players

	def display(self):
		board = scoreBoardTemplate

		p1TileCount = int(self.players[0].points / 5) + 1
		p2TileCount = int(self.players[1].points / 5) + 1

		print(p1TileCount)
		print(p2TileCount)
		rowLength = 8;

		for x in range(0, p1TileCount):
			board[x] = self.players[0].color1

		for x in range(p1TileCount, 7):
			board[x] =self.players[0].color2

		for x in range(rowLength, rowLength + p2TileCount):
			board[x] = self.players[1].color1

		for x in range(rowLength + p2TileCount, rowLength + 7):
			board[x] = self.players[1].color2

			
		sense.set_pixels(board)

	def showScore(self, player):
		sense.show_message(
            str(player.points),
            scroll_speed = 0.05,
            text_colour = player.color1
        )





b = (0, 0, 0)
w = (255, 255, 255)

B = (0, 0, 255)
dB = (0, 0, 50)

r = (255, 0, 0)
dr = (50, 0, 0)

y = (255, 255, 0)

clear = [
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b
]

scoreBoardTemplate = [
    B, b, b, b, b, b, b, y,
    r, b, b, b, b, b, b, y,
    b, b, b, b, b, b, b, b,
    b, B, b, b, b, r, r, b,
    b, B, b, b, b, b, r, b,
    b, B, b, b, b, r, r, b,
    b, B, b, b, b, r, b, b,
    b, B, b, b, b, r, r, b
]


def main():
	player1Name = input("Player 1, Enter your name: ")
	player1 = Player(player1Name, B, dB)
	player2Name = input("Player 2, Enter your name: ")
	player2 = Player(player2Name, r, dr)
	players = [player1, player2]
	game = Game(players)
	game.start()
	print("Goodbye")

main()