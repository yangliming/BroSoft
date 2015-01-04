# Snake.py

import os
import random
import time
import msvcrt

clear = lambda: os.system("cls")

Grid = [['#' for i in range(30)]] + [(['#'] + [' ' for i in range(28)] + ['#']) for i in range(18)] + [['#' for i in range(30)]]

Snake = []

def PrepareScreen():
	screen = []
	for row in Grid:
		screen.append(''.join(row))
	return '\n'.join(screen)
	
def Initialize():
	Grid[10][10] = 'O'
	Grid[10][9] = 'O'
	Grid[10][8] = 'O'
	Snake.append((10, 10))
	Snake.append((10, 9))
	Snake.append((10, 8))
	PlaceApple()

def PlaceApple():
	while True:
		x = random.randint(0, len(Grid) - 1)
		y = random.randint(0, len(Grid[0]) - 1)
		
		if Grid[x][y] == ' ':
			Grid[x][y] = '@'
			return

def Move(dir):
	head = Snake[0]
	tail = Snake[-1]
	
	newHead = (0,0)
	
	if (dir == 'up'):
		newHead = (head[0] - 1, head[1])
	elif (dir == 'down'):
		newHead = (head[0] + 1, head[1])
	elif (dir == 'left'):
		newHead = (head[0], head[1] - 1)
	elif (dir == 'right'):
		newHead = (head[0], head[1] + 1)
	
	global next
	next = Grid[newHead[0]][newHead[1]]
	if next == ' ' or next == '@':
		Grid[newHead[0]][newHead[1]] = 'O'
		Grid[tail[0]][tail[1]] = ' '
		Snake.insert(0, newHead)
		
	if next == ' ':
		Snake.pop()
		
	if next == '@':
		PlaceApple()
		
CurrDir = 'right'

Initialize()

while True:
	clear()
	print(PrepareScreen())
	time.sleep(0.25)
	Move(CurrDir)
	
	if next == '#' or next == 'O':
		print('Game Over')
		break
	
	if msvcrt.kbhit():
		key = msvcrt.getch()
		if (key == 'w'):
			CurrDir = 'up'
		if (key == 'a'):
			CurrDir = 'left'
		if (key == 's'):
			CurrDir = 'down'
		if (key == 'd'):
			CurrDir = 'right'
	