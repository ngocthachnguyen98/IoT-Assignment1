class game:

	def __init__(self):
		pass










def main():
	die = Die(6)
	while True:
		die.waitForShake()
		rand = die.roll()
		print(rand)
		#time.sleep(2)
main()