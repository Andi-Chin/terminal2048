import random
from random import randint as rd
import subprocess as sbp



class Block():
	def __init__(self, value):#0 means empty, 69 means put in random

		self.value = value
		self.canCombine = True

	def __repr__(self):
		return 'value: %s' % (self.value)




size = int(input('size: '))


class Matrix():


	matrix = [[Block(0) for x in range(size)] for y in range(size)]
	
	# matrix = 	[[Block(0), Block(0), Block(0), Block(0)],
	# 			[Block(0) , Block(0), Block(0), Block(0)],
	# 			[Block(0) , Block(0) , Block(0) , Block(0)],
	# 			[Block(0) , Block(0) , Block(0) , Block(0)],
	# 			[Block(0) , Block(0) , Block(0), Block(0)]]


	def pMatrix():
		biggest = Matrix.matrix[0][0].value
		for y in range(size):
			for x in range(size):
				if Matrix.matrix[y][x].value > biggest:
					biggest = Matrix.matrix[y][x].value

		

		for y in range(size):
			for x in range(size):

				num = Matrix.matrix[y][x].value
				padding = (len(str(biggest)) - len(str(num))) * ' '
				if num == 0:
					print('.', end = padding + ' ')
				else:
					
					print(num, end = padding + ' ')
					
				if (x + 1) % size == 0:
					print('\n')
		print()

	def lose():		
		print('you lose!')
		exit()
	def availableSquares():
		result = []
		for y in range(size):
			for x in range(size):
				if Matrix.matrix[y][x].value == 0:
					result.append([x, y])
		if len(result) == 0:
			Matrix.lose()
		return result

	def spawnBlock():
		available = Matrix.availableSquares()
		chosenOne = available[rd(0, len(available)-1)]
		chosenX = chosenOne[0]
		chosenY = chosenOne[1]
		Matrix.matrix[chosenY][chosenX].value = 4 if rd(0, 5) == 0 else 2

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
			for y in range(size):
				for x in range(1, size):
					if Matrix.matrix[y][x].value != 0: #a block lol
						# try:

						# 	if Matrix.matrix[y][x].value == Matrix.matrix[y][x-2].value == Matrix.matrix[y][x-1].value:
						# 		Matrix.collision(x - 1, y, x - 2, y)


						# except IndexError:
						# 	pass


						
						Matrix.collision(x, y, x - 1, y)

		#have to do this cuz the loop searchs left to right and 
		#might not take care of some
		for lolo in range(size * 2):
			moveOnce()

	def moveRight():
		def moveOnce():
			for y in range(size):
				for x in range(0, size-1):
					if Matrix.matrix[y][x].value != 0: #a block lol
						try:
							try: #four in a row
								first = Matrix.matrix[y][x].value
								second = Matrix.matrix[y][x+1].value
								third = Matrix.matrix[y][x+2].value
								fourth = Matrix.matrix[y][x+3].value

								if first == second == third == fourth:
									Matrix.collision(x, y, x + 1, y)
									Matrix.collision(x + 2, y, x + 3, y)
									continue
								
							except IndexError: #not four in a row
								pass




							if Matrix.matrix[y][x].value == Matrix.matrix[y][x+2].value == Matrix.matrix[y][x+1].value:
								Matrix.collision(x + 1, y, x + 2, y)


						except IndexError:
							pass


						
						Matrix.collision(x, y, x+1, y)


		for lolo in range(size * 2):
			moveOnce()

	def moveUp():
		def moveOnce():
			for y in range(1, size):
				for x in range(size):
					if Matrix.matrix[y][x].value != 0:

						# try:
						# 	if Matrix.matrix[y][x].value == Matrix.matrix[y - 1][x].value == Matrix.matrix[y - 2][x].value:
						# 		Matrix.collision(x, y - 1, x, y - 2)

						# except IndexError:
						# 	pass

						#a block
						Matrix.collision(x, y, x, y-1)

		for lolo in range(size * 2):
			moveOnce()

	def moveDown():
		def moveOnce():
			for y in range(0, size-1):
				for x in range(size):

					if Matrix.matrix[y][x].value != 0:
						try:
							try: #four in a row
								first = Matrix.matrix[y][x].value
								second = Matrix.matrix[y+1][x].value
								third = Matrix.matrix[y+2][x].value
								fourth = Matrix.matrix[y+3][x].value

								if first == second == third == fourth:
									Matrix.collision(x, y, x, y + 1)
									Matrix.collision(x, y + 2, x, y + 3)
									continue
								
							except IndexError: #not four in a row
								pass

							if Matrix.matrix[y][x].value == Matrix.matrix[y + 1][x].value == Matrix.matrix[y + 2][x].value:
								Matrix.collision(x, y + 1, x, y + 2)							
						except IndexError:
							pass

						#a block
						Matrix.collision(x, y, x, y + 1)

		for lolo in range(size * 2):
			moveOnce()

	def setCombine(value):
		for y in range(size):
			for x in range(size):
				Matrix.matrix[y][x].canCombine = value


def play():

	Matrix.spawnBlock()
	Matrix.spawnBlock()
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
		# sbp.call('clear', shell=True)
		Matrix.pMatrix()

		Matrix.setCombine(True)



#auto play
def autoPlay():

	Matrix.spawnBlock()
	Matrix.spawnBlock()
	Matrix.pMatrix()
	
	while True:

		direction = random.choice(['a', 'd', 'w', 's'])

		if direction == 'a':
			Matrix.moveLeft()
		elif direction == 'd':
			Matrix.moveRight()
		elif direction == 'w':
			Matrix.moveUp()
		elif direction == 's':
			Matrix.moveDown()

		Matrix.spawnBlock()
		# sbp.call('clear', shell=True)
		Matrix.pMatrix()

		Matrix.setCombine(True)
autoPlay()


