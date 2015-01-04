# Game
import random
rps = {1: "Rock",
       2: "Paper",
       3: "Scissors"}
       
keepPlaying = True
while keepPlaying:
	print("""
1. Rock
2. Paper
3. Scissors
""")

	ai = random.randint(1,3)
	choice = int(input())
	print("You picked", rps[choice])
	print("The AI picked", rps[ai])
	
	if ai == choice:
		print("Draw!")
	elif choice > ai and not (ai == 1 and choice == 3):
		print("You win!")
	else:
		print("You lose!")