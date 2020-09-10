#Here we get the array we will manipulate and create the labyrinth with
import numpy as np
import cell

def getSize():
	x = -1
	y = -1
	boolean = False
	while boolean == False:
		x= int(input("Introduce the grid size X: "))
		y= int(input("Introduce the grid size Y: "))
		boolean = checkSize(x, y)
	return x, y

#With this function we initialize an array size Size filled with cells
def getGrid(size):
	
	grid = np.empty((size), dtype = "object")

	for i in range(size[0]):
		for j in range(size[1]):
			grid[i][j] = cell.Cell(i, j, True, True, True, True, False)

	
	return grid
def checkSize(x, y):
	boolean = False
	if x == -1 and y == -1:
		pass
	elif (x % 5 != 0 or y % 5 != 0):
		print("Grid size must be multiple of 5")
		boolean = False
	else:
		boolean = True

	return boolean

