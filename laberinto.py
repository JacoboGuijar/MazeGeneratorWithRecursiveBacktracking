import pygame
import numpy as np
import random
import time
import grid, cell

WHITE = [255, 255, 255]
GRAY = [100,100,100]
RED = [235, 107, 52]
BLACK = [0,0,0]
wallWidth = 1
pxSize = 5
pygame.init()
NONVISITEDCOLOR = GRAY
VISITEDCOLOR = WHITE
CURRENCELLCOLOR = [52, 232, 235]
pygame.display.set_caption("minimal")
size = grid.getSize()
window = pygame.display.set_mode((size[0]+20, size[1]+20))
canvas = pygame.Surface((size[0]+2, size[1]+2))


cellsGrid = grid.getGrid((int(size[0]/pxSize) , int(size[1]/pxSize)))


def main():
	running = True
	stack = []
	boolean = drawTheMaze()
 
	currentCell = cellsGrid[0][0]
	currentCell.visited = True
	drawCellsGrid(currentCell)
	
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running == False

		nextCell = chooseNextCell(currentCell)
		
		if nextCell != None:
			nextCell.visited = True
			stack.append(currentCell)
			if boolean == True:
				drawCellsGrid(nextCell)
				drawWalls()
			
			currentCell = nextCell

		elif len(stack) > 0:
			currentCell = stack.pop()
			if boolean == True:
				drawCellsGrid(currentCell)
				drawWalls()

		else:
			drawLastCellsGrid()
			drawWalls()
			window.blit(canvas, (10,10))
			pygame.display.update()
			print("se acabo")
			time.sleep(100)
			pygame.event.get()

		window.blit(canvas, (10,10))
		pygame.display.update()


def drawCellsGrid(cell):
	
	for i in range(len(cellsGrid)):
		for j in range(len(cellsGrid[i])):
			
			if cellsGrid[i][j].visited == False:
				pygame.draw.rect(canvas, NONVISITEDCOLOR,   (int(cellsGrid[i][j].positionX * pxSize), int(cellsGrid[i][j].positionY * pxSize), pxSize, pxSize))
			else:
				pygame.draw.rect(canvas, VISITEDCOLOR, (int(cellsGrid[i][j].positionX * pxSize), int(cellsGrid[i][j].positionY * pxSize), pxSize, pxSize))
			pygame.draw.rect(canvas, CURRENCELLCOLOR, (int(cell.positionX * pxSize), int(cell.positionY * pxSize), pxSize, pxSize))			
			#time.sleep(0.001)


def drawWalls():

	for i in range(len(cellsGrid)):
		for j in range(len(cellsGrid[i])):
			cell = cellsGrid[i][j]
			currentPosition = (int(cell.positionX * pxSize), int(cell.positionY * pxSize))

			if cell.wallN == True:
				pygame.draw.line(canvas, BLACK, (currentPosition[0], currentPosition[1]), (currentPosition[0] + pxSize, currentPosition[1]), wallWidth)
			else:
				pygame.draw.line(canvas, VISITEDCOLOR, (currentPosition[0] + wallWidth, currentPosition[1]), (currentPosition[0] + pxSize - wallWidth, currentPosition[1]), wallWidth)

			if cell.wallS == True:
				pygame.draw.line(canvas, BLACK, (currentPosition[0] + pxSize, currentPosition[1]), (currentPosition[0] + pxSize, currentPosition[1] + pxSize), wallWidth)
			else:
				pygame.draw.line(canvas, VISITEDCOLOR, (currentPosition[0] + pxSize, currentPosition[1] + wallWidth), (currentPosition[0] + pxSize - wallWidth, currentPosition[1] + pxSize), wallWidth)

			if cell.wallW == True:
				pygame.draw.line(canvas, BLACK, (currentPosition[0], currentPosition[1]), (currentPosition[0], currentPosition[1] + pxSize), wallWidth)
			else:
				pygame.draw.line(canvas, VISITEDCOLOR, (currentPosition[0], currentPosition[1] + wallWidth), (currentPosition[0], currentPosition[1] + pxSize - wallWidth), wallWidth)

			if cell.wallE:
				pygame.draw.line(canvas, BLACK, (currentPosition[0] + pxSize, currentPosition[1]), (currentPosition[0] + pxSize, currentPosition[1] + pxSize), wallWidth)
			else:
				pygame.draw.line(canvas, VISITEDCOLOR, (currentPosition[0] + pxSize, currentPosition[1]  + wallWidth), (currentPosition[0] + pxSize, currentPosition[1] + pxSize - wallWidth), wallWidth)

def chooseNextCell(cell):
	i = cell.positionX
	j = cell.positionY
	choices = []
	writtenChoices = []

	if ((j - 1 >= 0) and (cellsGrid[i][j - 1].visited == False)):
		choices.append(cellsGrid[i][j - 1])
		writtenChoices.append("Northwards")
	else:
		pass

	if ((j < len(cellsGrid[i]) - 1) and (cellsGrid[i][j + 1].visited == False)):
		choices.append(cellsGrid[i][j + 1])
		writtenChoices.append("Soutwards")
	else:
		pass

	if ((i - 1 >= 0) and (cellsGrid[i - 1][j].visited == False)):
		choices.append(cellsGrid[i - 1][j])
		writtenChoices.append("Westwards")
	else:
		pass

	if (i < len(cellsGrid) - 1) and (cellsGrid[i + 1][j].visited == False):
		choices.append(cellsGrid[i + 1][j])
		writtenChoices.append("Eastwards")
	else: 
		pass

	if len(choices) > 0:
		n = random.randint(0,len(choices) - 1)
		nextCell = choices[n]
		deleteWall(cell, nextCell, writtenChoices[n])
		#print("Choosed: " + str(writtenChoices[n]) + " from: " + str(writtenChoices))
		
	else:
		#print("No posibilities where found")
		nextCell = None
	
	return nextCell



def deleteWall(currentCell, nextCell, movement):
	currentPosition = (currentCell.positionX, currentCell.positionY)
	nextPosition = (nextCell.positionX, nextCell.positionY)

	if movement == "Northwards":
		currentCell.wallN = False
		nextCell.wallS = False
		# print("North wall from " + str(currentPosition) + " and South wall from " + str(nextPosition) + "has been removed")
		# print(currentCell.wallN, currentCell.wallS, currentCell.wallW, currentCell.wallE)
		# print(nextCell.wallN, nextCell.wallS, nextCell.wallW, nextCell.wallE)

	elif movement == "Soutwards":
		currentCell.wallS = False
		nextCell.wallN = False
		# print("South wall from " + str(currentPosition) + " and North wall from " + str(nextPosition) + "has been removed")
		# print(currentCell.wallN, currentCell.wallS, currentCell.wallW, currentCell.wallE)
		# print(nextCell.wallN, nextCell.wallS, nextCell.wallW, nextCell.wallE)

	elif movement == "Westwards":
		currentCell.wallW = False
		nextCell.wallE = False
		# print("West wall from " + str(currentPosition) + " and East wall from " + str(nextPosition) + "has been removed")
		# print(currentCell.wallN, currentCell.wallS, currentCell.wallW, currentCell.wallE)
		# print(nextCell.wallN, nextCell.wallS, nextCell.wallW, nextCell.wallE)

	elif movement == "Eastwards":
		currentCell.wallE = False
		nextCell.wallW = False
		# print("East wall from " + str(currentPosition) + " and West wall from " + str(nextPosition) + "has been removed")
		# print(currentCell.wallN, currentCell.wallS, currentCell.wallW, currentCell.wallE)
		# print(nextCell.wallN, nextCell.wallS, nextCell.wallW, nextCell.wallE)
	else:
		pass

def drawLastCellsGrid():
	for i in range(len(cellsGrid)):
		for j in range(len(cellsGrid[i])):
			
			if cellsGrid[i][j].visited == False:
				pygame.draw.rect(canvas, NONVISITEDCOLOR,   (int(cellsGrid[i][j].positionX * pxSize), int(cellsGrid[i][j].positionY * pxSize), pxSize, pxSize))
			else:
				pygame.draw.rect(canvas, VISITEDCOLOR, (int(cellsGrid[i][j].positionX * pxSize), int(cellsGrid[i][j].positionY * pxSize), pxSize, pxSize))
	pygame.draw.rect(canvas, CURRENCELLCOLOR, (int(cellsGrid[0][0].positionX * pxSize), int(cellsGrid[0][0].positionY * pxSize), pxSize, pxSize))
	pygame.draw.rect(canvas, RED, (int(cellsGrid[-1][-1].positionX * pxSize), int(cellsGrid[-1][-1].positionY * pxSize), pxSize, pxSize))

def drawTheMaze():
	boolean = bool(input("Do you want the maze to be drawn?"))
	return boolean

if __name__=="__main__":
    # call the main function
    main()

