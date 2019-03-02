from random import randint as rd
import time
import subprocess as sbp
class Block():
	def __init__(self, value):#0 means empty, 69 means put in random

		self.value = value
		self.canCombine = True

	def __repr__(self):
		return 'value: %s' % (self.value)


width = int(input('width: '))
height = width
class Matrix():

	
	matrix = [[Block(0) for x in range(width)] for y in range(height)]
	

	matrix[rd(0, len(matrix)-1)][rd(0, len(matrix)-1)].value = 2 if rd(0, 1) == 0 else 4


	def pMatrix():
		biggest = Matrix.matrix[0][0].value
		for y in range(height):
			for x in range(width):
				if Matrix.matrix[y][x].value > biggest:
					biggest = Matrix.matrix[y][x].value

		

		for y in range(height):
			for x in range(width):

				num = Matrix.matrix[y][x].value
				padding = (len(str(biggest)) - len(str(num))) * ' '
				if num == 0:
					print('.', end = padding + ' ')
				else:
					
					print(num, end = padding + ' ')
					
				if (x + 1) % width == 0:
					print('\n')
		print()

	def availableSquares():
		result = []
		for y in range(height):
			for x in range(width):
				if Matrix.matrix[y][x].value == 0:
					result.append([x, y])
		if len(result) == 0:
			print('you lose!')
			print(result)
			exit()
		return result

	def spawnBlock():
		available = Matrix.availableSquares()
		chosenOne = available[rd(0, len(available)-1)]
		chosenX = chosenOne[0]
		chosenY = chosenOne[1]
		Matrix.matrix[chosenY][chosenX].value = 4 if rd(0, 3) == 0 else 2


	def swap(x1, y1, x2, y2):

		temp = Matrix.matrix[y1][x1]

		Matrix.matrix[y1][x1] = Matrix.matrix[y2][x2]

		Matrix.matrix[y2][x2] = temp

	def collision(x1, y1, x2, y2):

		if Matrix.matrix[y2][x2].value == 0:
			# the second block is empty
			Matrix.swap(x1, y1, x2, y2)

			#two blocks combine***

		elif Matrix.matrix[y1][x1].value == Matrix.matrix[y2][x2].value:
			#makes sure the block can't combine a second time every round
			if Matrix.matrix[y1][x1].canCombine and Matrix.matrix[y2][x2].canCombine:
				Matrix.matrix[y2][x2].value *= 2 #second block absorbes first block
				Matrix.matrix[y1][x1].value = 0 #first block becomes empty

				Matrix.matrix[y1][x1].canCombine = False
				Matrix.matrix[y2][x2].canCombine = False


				
	def moveLeft():
		def moveOnce():
			for y in range(height):
				for x in range(1, width):
					
					if Matrix.matrix[y][x].value != 0: #a block
						Matrix.collision(x, y, x-1, y)

					else: #empty block
						pass

		#have to do this cuz the loop searchs left to right and 
		#might not take care of some
		for lolo in range(width * 2):
			moveOnce()

	def moveRight():
		def moveOnce():
			for y in range(height):
				for x in range(0, width-1):

					if Matrix.matrix[y][x].value != 0: #a block lol
						Matrix.collision(x, y, x+1, y)

					else: #empty block
						pass
		for lolo in range(width * 2):
			moveOnce()

	def moveUp():
		def moveOnce():
			for y in range(1, height):
				for x in range(width):

					if Matrix.matrix[y][x].value != 0: #a block
						Matrix.collision(x, y, x, y-1)

					else: #empty block
						pass
		for lolo in range(width * 2):
			moveOnce()

	def moveDown():
		def moveOnce():
			for y in range(0, height-1):
				for x in range(width):
					if Matrix.matrix[y][x].value != 0: #a block lul
						Matrix.collision(x, y, x, y+1)
					else: #empty block
						pass
		for lolo in range(width * 2):
			moveOnce()

	def setCombine(value):
		for y in range(height):
			for x in range(width):
				Matrix.matrix[y][x].canCombine = value


def play():
	Matrix.pMatrix()
	while True:
		properInput = False
		while not properInput:
			direction = input('please move: ')

			if direction == '':
				# print('plz give proper inputs "w, a, s, d" to move the blocks')
				continue

			if direction in 'adws':
				properInput = True
			else:
				# print('plz give proper inputs "w, a, s, d" to move the blocks')
				pass

		if direction == 'a':
			Matrix.moveLeft()
		elif direction == 'd':
			Matrix.moveRight()
		elif direction == 'w':
			Matrix.moveUp()
		elif direction == 's':
			Matrix.moveDown()


		Matrix.spawnBlock()
		sbp.call('clear', shell=True)
		Matrix.pMatrix()

		Matrix.setCombine(True)


play()

#auto play
# iterations = 0
# while True:
# 	rand = rd(0, 3)
# 	if rand == 0:
# 		Matrix.moveLeft()
# 	elif rand == 1:
# 		Matrix.moveRight()
# 	elif rand == 2:
# 		Matrix.moveDown()
# 	elif rand == 3:
# 		Matrix.moveUp()

# 	Matrix.spawnBlock()
	
# 	
# 	Matrix.pMatrix()
# 	print('******************************')
# 	print('iterations: %s' % (iterations))
#	time.sleep(0.5)

# 	iterations += 1


