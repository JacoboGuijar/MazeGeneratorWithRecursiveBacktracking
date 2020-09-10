#Cells
import random
import pygame

class Cell:
	def __init__(self, positionX, positionY, wallN, wallS, wallW, wallE, visited):

		self.positionX = positionX
		self.positionY = positionY

		#The state indicates if it is wall or path
		self.wallN = wallN
		self.wallS = wallS
		self.wallW = wallW
		self.wallE = wallE

		#Has it been visited?
		self.visited = visited





