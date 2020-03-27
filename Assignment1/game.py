import time
from datetime import datetime
import electronicDie
from electronicDie import Die

class Game:

	def __init__(self, players):
		self.die = Die(6)
		self.players = players


	def start(self):
		print("Shake the dice (the pi) to score points equal to the number rolled.")
		print("First one to 30 points wins.")
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
		time.sleep(1)
		rand = self.die.roll()
		player.addPoints(rand)
		self.showScore()
		print()
		time.sleep(1)
		if player.points > 30:
			return player


	def showScore(self):
		for player in self.players:
			print("%s: %d" % (player.name, player.points))


	def announceWinner(self, player):
		print("%s Won!" % (player.name))
		f = open("scores.txt", "a")
		f.write("%s - %s - %d points\n" % (datetime.now(), player.name, player.points))
		f.close()


class Player:
	def __init__(self, name):
		self.name = name
		self.points = 0
		pass

	def addPoints(self, points):
		print("%s scored %d points!"% (self.name, points))
		self.points += points



def main():
	player1Name = input("Player 1, Enter your name: ")
	player1 = Player(player1Name)
	player2Name = input("Player 2, Enter your name: ")
	player2 = Player(player2Name)
	players = [player1, player2]
	game = Game(players)
	game.start()
	print("Goodbye")

main()