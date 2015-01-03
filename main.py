# Game
import random

keepPlaying = True
while keepPlaying:
	print("""
1. Rock
2. Paper
3. Scissors
""")

	ai = random.randint(1,3)

	choice = int(input())
	
	print(ai)
	
	if ai == choice:
		print("Draw!")
	elif choice > ai and not (ai == 1 and choice == 3):
		print("You win!")
	else:
		print("You lose!")