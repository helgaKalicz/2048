def printing():
	os.system('clear')

# colour part, 0 is invisible
	a0 = str(a[0])
	a1 = str(a[1])
	a2 = str(a[2])
	a3 = str(a[3])
	b0 = str(b[0])
	b1 = str(b[1])
	b2 = str(b[2])
	b3 = str(b[3])
	c0 = str(c[0])
	c1 = str(c[1])
	c2 = str(c[2])
	c3 = str(c[3])
	d0 = str(d[0])
	d1 = str(d[1])
	d2 = str(d[2])
	d3 = str(d[3])

	Color1a0= "\033[08m{}\033[0m" .format(a0)
	Color1a1= "\033[08m{}\033[0m" .format(a1)
	Color1a2= "\033[08m{}\033[0m" .format(a2)
	Color1a3= "\033[08m{}\033[0m" .format(a3)
	Color1b0= "\033[08m{}\033[0m" .format(b0)
	Color1b1= "\033[08m{}\033[0m" .format(b1)
	Color1b2= "\033[08m{}\033[0m" .format(b2)
	Color1b3= "\033[08m{}\033[0m" .format(b3)
	Color1c0= "\033[08m{}\033[0m" .format(c0)
	Color1c1= "\033[08m{}\033[0m" .format(c1)
	Color1c2= "\033[08m{}\033[0m" .format(c2)
	Color1c3= "\033[08m{}\033[0m" .format(c3)
	Color1d0= "\033[08m{}\033[0m" .format(d0)
	Color1d1= "\033[08m{}\033[0m" .format(d1)
	Color1d2= "\033[08m{}\033[0m" .format(d2)
	Color1d3= "\033[08m{}\033[0m" .format(d3)
	Color2a0= "\033[92m{}\033[0m" .format(a0)
	Color2a1= "\033[92m{}\033[0m" .format(a1)
	Color2a2= "\033[92m{}\033[0m" .format(a2)
	Color2a3= "\033[92m{}\033[0m" .format(a3)
	Color2b0= "\033[92m{}\033[0m" .format(b0)
	Color2b1= "\033[92m{}\033[0m" .format(b1)
	Color2b2= "\033[92m{}\033[0m" .format(b2)
	Color2b3= "\033[92m{}\033[0m" .format(b3)
	Color2c0= "\033[92m{}\033[0m" .format(c0)
	Color2c1= "\033[92m{}\033[0m" .format(c1)
	Color2c2= "\033[92m{}\033[0m" .format(c2)
	Color2c3= "\033[92m{}\033[0m" .format(c3)
	Color2d0= "\033[92m{}\033[0m" .format(d0)
	Color2d1= "\033[92m{}\033[0m" .format(d1)
	Color2d2= "\033[92m{}\033[0m" .format(d2)
	Color2d3= "\033[92m{}\033[0m" .format(d3)

	if a[0] == 0:
		a0 = Color1a0
	else:
		a0 = Color2a0
	if a[1] == 0:
		a1 = Color1a1
	else:
		a1 = Color2a1
	if a[2] == 0:
		a2 = Color1a2
	else:
		a2 = Color2a2
	if a[3] == 0:
		a3 = Color1a3
	else:
		a3 = Color2a3
	if b[0] == 0:
		b0 = Color1b0
	else:
		b0 = Color2b0
	if b[1] == 0:
		b1 = Color1b1
	else:
		b1 = Color2b1
	if b[2] == 0:
		b2 = Color1b2
	else:
		b2 = Color2b2
	if b[3] == 0:
		b3 = Color1b3
	else:
		b3 = Color2b3
	if c[0] == 0:
		c0 = Color1c0
	else:
		c0 = Color2c0
	if c[1] == 0:
		c1 = Color1c1
	else:
		c1 = Color2c1
	if c[2] == 0:
		c2 = Color1c2
	else:
		c2 = Color2c2
	if c[3] == 0:
		c3 = Color1c3
	else:
		c3 = Color2c3
	if d[0] == 0:
		d0 = Color1d0
	else:
		d0 = Color2d0
	if d[1] == 0:
		d1 = Color1d1
	else:
		d1 = Color2d1
	if d[2] == 0:
		d2 = Color1d2
	else:
		d2 = Color2d2
	if d[3] == 0:
		d3 = Color1d3
	else:
		d3 = Color2d3

# handling several digit numbers, first row
	if len(str(a[0])) == 1:
		partBetween1 = '   │  '
	elif len(str(a[0])) == 2:
		partBetween1 = '  │  '
	elif len(str(a[0])) == 3:
		partBetween1 = ' │  '
	elif len(str(a[0])) == 4:
		partBetween1 = '│  '

	if len(str(a[1])) == 1:
		partBetween2 = '   │  '
	elif len(str(a[1])) == 2:
		partBetween2 = '  │  '
	elif len(str(a[1])) == 3:
		partBetween2 = ' │  '
	elif len(str(a[1])) == 4:
		partBetween2 = '│  '

	if len(str(a[2])) == 1:
		partBetween3 = '   │  '
	elif len(str(a[2])) == 2:
		partBetween3 = '  │  '
	elif len(str(a[2])) == 3:
		partBetween3 = ' │  '
	elif len(str(a[2])) == 4:
		partBetween3 = '│  '
	
	if len(str(a[3])) == 1:
		partRight1 = '   │  '
	elif len(str(a[3])) == 2:
		partRight1 = '  │  '
	elif len(str(a[3])) == 3:
		partRight1 = ' │  '
	elif len(str(a[3])) == 4:
		partRight1 = '│  '

# digits: second row
	if len(str(b[0])) == 1:
		partBetween4 = '   │  '
	elif len(str(b[0])) == 2:
		partBetween4 = '  │  '
	elif len(str(b[0])) == 3:
		partBetween4 = ' │  '
	elif len(str(b[0])) == 4:
		partBetween4 = '│  '

	if len(str(b[1])) == 1:
		partBetween5 = '   │  '
	elif len(str(b[1])) == 2:
		partBetween5 = '  │  '
	elif len(str(b[1])) == 3:
		partBetween5 = ' │  '
	elif len(str(b[1])) == 4:
		partBetween5 = '│  '

	if len(str(b[2])) == 1:
		partBetween6 = '   │  '
	elif len(str(b[2])) == 2:
		partBetween6 = '  │  '
	elif len(str(b[2])) == 3:
		partBetween6 = ' │  '
	elif len(str(b[2])) == 4:
		partBetween6 = '│  '
	
	if len(str(b[3])) == 1:
		partRight2 = '   │  '
	elif len(str(b[3])) == 2:
		partRight2 = '  │  '
	elif len(str(b[3])) == 3:
		partRight2 = ' │  '
	elif len(str(b[3])) == 4:
		partRight2 = '│  '

# digits: third row
	if len(str(c[0])) == 1:
		partBetween7 = '   │  '
	elif len(str(c[0])) == 2:
		partBetween7 = '  │  '
	elif len(str(c[0])) == 3:
		partBetween7 = ' │  '
	elif len(str(c[0])) == 4:
		partBetween7 = '│  '

	if len(str(c[1])) == 1:
		partBetween8 = '   │  '
	elif len(str(c[1])) == 2:
		partBetween8 = '  │  '
	elif len(str(c[1])) == 3:
		partBetween8 = ' │  '
	elif len(str(c[1])) == 4:
		partBetween8 = '│  '

	if len(str(c[2])) == 1:
		partBetween9 = '   │  '
	elif len(str(c[2])) == 2:
		partBetween9 = '  │  '
	elif len(str(c[2])) == 3:
		partBetween9 = ' │  '
	elif len(str(c[2])) == 4:
		partBetween9 = '│  '
	
	if len(str(c[3])) == 1:
		partRight3 = '   │  '
	elif len(str(c[3])) == 2:
		partRight3 = '  │  '
	elif len(str(c[3])) == 3:
		partRight3 = ' │  '
	elif len(str(c[3])) == 4:
		partRight3 = '│  '

# digits: fourth row
	if len(str(d[0])) == 1:
		partBetween10 = '   │  '
	elif len(str(d[0])) == 2:
		partBetween10 = '  │  '
	elif len(str(d[0])) == 3:
		partBetween10 = ' │  '
	elif len(str(d[0])) == 4:
		partBetween10 = '│  '

	if len(str(d[1])) == 1:
		partBetween11 = '   │  '
	elif len(str(d[1])) == 2:
		partBetween11 = '  │  '
	elif len(str(d[1])) == 3:
		partBetween11 = ' │  '
	elif len(str(d[1])) == 4:
		partBetween11 = '│  '

	if len(str(d[2])) == 1:
		partBetween12 = '   │  '
	elif len(str(d[2])) == 2:
		partBetween12 = '  │  '
	elif len(str(d[2])) == 3:
		partBetween12 = ' │  '
	elif len(str(d[2])) == 4:
		partBetween12 = '│  '
	
	if len(str(d[3])) == 1:
		partRight4 = '   │  '
	elif len(str(d[3])) == 2:
		partRight4 = '  │  '
	elif len(str(d[3])) == 3:
		partRight4 = ' │  '
	elif len(str(d[3])) == 4:
		partRight4 = '│  '

# print part
	print("\033[92m" + "Score:" + "\033[0m" + "\033[96m" + " " + str(score) + "\033[0m")
	print()
	print('                                     \033[91m' + '┌──────┬──────┬──────┬──────┐' + '\033[0m')
	print('                                     \033[91m' + '│      │      │      │      │' + '\033[0m')
	print('                                     \033[91m' + '│  ' + '\033[0m' + a0 + '\033[91m' + partBetween1 + '\033[0m' + a1 + '\033[91m' + partBetween2 + '\033[0m' + a2 + '\033[91m' + partBetween3 + '\033[0m' + a3 + '\033[91m' + partRight1 + '\033[0m')
	print('                                     \033[91m' + '│      │      │      │      │' + '\033[0m')
	print('                                     \033[91m' + '├──────┼──────┼──────┼──────┤' + '\033[0m')
	print('                                     \033[91m' + '│      │      │      │      │' + '\033[0m')
	print('                                     \033[91m' + '│  ' + '\033[0m' + b0 + '\033[91m' + partBetween4 + '\033[0m' + b1 + '\033[91m' + partBetween5 + '\033[0m' + b2 + '\033[91m' + partBetween6 + '\033[0m' + b3 + '\033[91m' + partRight2 + '\033[0m')
	print('                                     \033[91m' + '│      │      │      │      │' + '\033[0m')
	print('                                     \033[91m' + '├──────┼──────┼──────┼──────┤' + '\033[0m')
	print('                                     \033[91m' + '│      │      │      │      │' + '\033[0m')
	print('                                     \033[91m' + '│  ' + '\033[0m' + c0 + '\033[91m' + partBetween7 + '\033[0m' + c1 + '\033[91m' + partBetween8 + '\033[0m' + c2 + '\033[91m' + partBetween9 + '\033[0m' + c3 + '\033[91m' + partRight3 + '\033[0m')
	print('                                     \033[91m' + '│      │      │      │      │' + '\033[0m')
	print('                                     \033[91m' + '├──────┼──────┼──────┼──────┤' + '\033[0m')
	print('                                     \033[91m' + '│      │      │      │      │' + '\033[0m')
	print('                                     \033[91m' + '│  ' + '\033[0m' + d0 + '\033[91m' + partBetween10 + '\033[0m' + d1 + '\033[91m' + partBetween11 + '\033[0m' + d2 + '\033[91m' + partBetween12 + '\033[0m' + d3 + '\033[91m' + partRight4 + '\033[0m')
	print('                                     \033[91m' + '│      │      │      │      │' + '\033[0m')
	print('                                     \033[91m' + '└──────┴──────┴──────┴──────┘' + '\033[0m')
	print()

# checking the end of the game, in case if you achive 2048 or you don't have more moves
def checking():
	if (2048 in a) or (2048 in b) or (2048 in c) or (2048 in d):
		print()
		print("\033[92m" + "You win!!!" + "\033[0m")
		print()
		quit()
	elif (a[0] == 0) or (a[1] == 0) or (a[2] == 0) or (a[3] == 0):
		pass
	elif (b[0] == 0) or (b[1] == 0) or (b[2] == 0) or (b[3] == 0):
		pass
	elif (c[0] == 0) or (c[1] == 0) or (c[2] == 0) or (c[3] == 0):
		pass
	elif (d[0] == 0) or (d[1] == 0) or (d[2] == 0) or (d[3] == 0):
		pass
	elif (a[0] == a[1]) or (a[0] == b[0]):
		pass
	elif (a[2] == a[1]) or (a[2] == a[3]) or (a[2] == b[2]):
		pass
	elif (b[1] == b[0]) or (b[1] == a[1]) or (b[1] == b[2]) or (b[1] == c[1]):
		pass
	elif (b[3] == b[2]) or (b[3] == a[3]) or (b[3] == c[3]):
		pass
	elif (c[0] == b[0]) or (c[0] == d[0]) or (c[0] == c[1]):
		pass
	elif (c[2] == c[1]) or (c[2] == c[3]) or (c[2] == b[2]) or (c[2] == d[2]):
		pass
	elif (d[1] == d[0]) or (d[1] == d[2]) or (d[1] == c[1]):
		pass
	elif (d[3] == c[3]) or (d[3] == d[2]):
		pass
	else:
		print()
		print("\033[92m" + "No more moves! Game over!" + "\033[92m")
		print()
		quit()

# Put 2 (90% of the cases) or 4 (10% of the cases) to an empty random place (if there is), if the board changed. 
def randNum():
	if dontMove == 1:
		randomList = list()
		randomItem = list()
		for i in range(len(a)):
			if a[i] == 0:
				randomItem.append(i)
				randomList.append("a")

		for i in range(len(b)):
			if b[i] == 0:
				randomItem.append(i)
				randomList.append("b")

		for i in range(len(c)):
			if c[i] == 0:
				randomItem.append(i)
				randomList.append("c")

		for i in range(len(d)):
			if d[i] == 0:
				randomItem.append(i)
				randomList.append("d")
# 2 or 4
		if len(randomList) != 0:
			import random
			chosen = random.randint(0,len(randomList)-1)
			row = randomList[chosen]
			column = randomItem[chosen]
			twoOrFourlot = random.randint(1,10)
			if twoOrFourlot == 1:
				twoOrFour = 4
			else:
				twoOrFour = 2

			if row == "a":
				a[column] = twoOrFour
			if row == "b":
				b[column] = twoOrFour
			if row == "c":
				c[column] = twoOrFour
			if row == "d":
				d[column] = twoOrFour

# First board printing
a = [0, 0, 0, 0]
b = [0, 0, 0, 0]
c = [0, 0, 0, 0]
d = [0, 0, 0, 0]

from functions2048 import coolStart
import os
game = 1
print()
print()
while game == 1:
	start = input("\033[92m" + "Press \'s\' to start the game! (or \'x\' to EXIT): " + "\033[0m")
	if start == "s":
		score = int()
		dontMove = 1
		randNum()
		randNum()
		printing()
		game = 0
	elif start == "x":
		quit()
	else:
		pass

# The game starts here:
while game < 1:
	key = input("\033[92m" + "Select a direction and press enter (use \'x\' to EXIT): " + "\033[0m")
# UP direction with 'w'
# Exclusion of false movements caused by zeros
	if key == "w":
		dontMove = 0
		for j in range(4):
			if a[j] == 0:
				if b[j] == 0:
					if c[j] == 0:
						if d[j] == 0:
							pass
						else:
							dontMove = 1
					else:
						dontMove = 1
				else:
					dontMove = 1
			else:
				if b[j] == 0:
					if c[j] == 0:
						if d[j] == 0:
							pass
						else:
							dontMove = 1
					else:
						dontMove = 1
				else:
					if c[j] == 0:
						if d[j] == 0:
							pass
						else:
							dontMove = 1
# UP sorting
		for j in range(4):
			for i in range(3):
				if a[j] == 0:
					a[j] = b[j]
					b[j] = c[j]
					c[j] = d[j]
					d[j] = 0
				else:
					for i in range(2):
						if b[j] == 0:
							b[j] = c[j]
							c[j] = d[j]
							d[j] = 0
						else:
							if c[j] == 0:
								c[j] = d[j]
								d[j] = 0
# UP to add up similar numbers
		for j in range(4):
			if a[j] != 0:
				if a[j] == b[j]:
					a[j] = a[j] + b[j]
					score = score + a[j]
					b[j] = c[j]
					c[j] = d[j]
					d[j] = 0
					dontMove = 1
			if b[j] != 0:
				if b[j] == c[j]:
					b[j] = b[j] + c[j]
					score = score + b[j]
					c[j] = d[j]
					d[j] = 0
					dontMove = 1
			if c[j] != 0:
				if c[j] == d[j]:
					c[j] = c[j] + d[j]
					score = score + c[j]
					d[j] = 0
					dontMove = 1
			j = j + 1
		randNum()
		printing()
		checking()

# DOWN direction with 's'
	elif key == "s":
		dontMove = 0
		for j in range(4):
			if d[j] == 0:
				if c[j] == 0:
					if b[j] == 0:
						if a[j] == 0:
							pass
						else:
							dontMove = 1
					else:
						dontMove = 1
				else:
					dontMove = 1
			else:
				if c[j] == 0:
					if b[j] == 0:
						if a[j] == 0:
							pass
						else:
							dontMove = 1
					else:
						dontMove = 1
				else:
					if b[j] == 0:
						if a[j] == 0:
							pass
						else:
							dontMove = 1
# DOWN sorting
		for j in range(4):
			for i in range(3):
				if d[j] == 0:
					d[j] = c[j]
					c[j] = b[j]
					b[j] = a[j]
					a[j] = 0
				else:
					for i in range(2):
						if c[j] == 0:
							c[j] = b[j]
							b[j] = a[j]
							a[j] = 0
						else:
							if b[j] == 0:
								b[j] = a[j]
								a[j] = 0
# DOWN to add up similar numbers
		j = 0
		while j < 4:
			if d[j] != 0:
				if d[j] == c[j]:
					d[j] = d[j] + c[j]
					score = score + d[j]
					c[j] = b[j]
					b[j] = a[j]
					a[j] = 0
					dontMove = 1
			if c[j] != 0:
				if c[j] == b[j]:
					c[j] = c[j] + b[j]
					score = score + c[j]
					b[j] = a[j]
					a[j] = 0
					dontMove = 1
			if b[j] != 0:
				if b[j] == a[j]:
					b[j] = b[j] + a[j]
					score = score + b[j]
					a[j] = 0           
					dontMove = 1
			j = j + 1
		randNum()
		printing()
		checking()

# LEFT direction with 'a'
	elif key == "a":
		dontMove = 0
# LEFT First row
		if a[0] == 0:
			if a[1] == 0:
				if a[2] == 0:
					if a[3] == 0:
						pass
					else:
						dontMove = 1
				else:
					dontMove = 1
			else:
				dontMove = 1
		else:
			if a[1] == 0:
				if a[2] == 0:
					if a[3] == 0:
						pass
					else:
						dontMove = 1
				else:
					dontMove = 1
			else:
				if a[2] == 0:
					if a[3] == 0:
						pass
					else:
						dontMove = 1
# LEFT Second row
		if b[0] == 0:
			if b[1] == 0:
				if b[2] == 0:
					if b[3] == 0:
						pass
					else:
						dontMove = 1
				else:
					dontMove = 1
			else:
				dontMove = 1
		else:
			if b[1] == 0:
				if b[2] == 0:
					if b[3] == 0:
						pass
					else:
						dontMove = 1
				else:
					dontMove = 1
			else:
				if b[2] == 0:
					if b[3] == 0:
						pass
					else:
						dontMove = 1
# LEFT Third row
		if c[0] == 0:
			if c[1] == 0:
				if c[2] == 0:
					if c[3] == 0:
						pass
					else:
						dontMove = 1
				else:
					dontMove = 1
			else:
				dontMove = 1
		else:
			if c[1] == 0:
				if c[2] == 0:
					if c[3] == 0:
						pass
					else:
						dontMove = 1
				else:
					dontMove = 1
			else:
				if c[2] == 0:
					if c[3] == 0:
						pass
					else:
						dontMove = 1
# LEFT Fourth row
		if d[0] == 0:
			if d[1] == 0:
				if d[2] == 0:
					if d[3] == 0:
						pass
					else:
						dontMove = 1
				else:
					dontMove = 1
			else:
				dontMove = 1
		else:
			if d[1] == 0:
				if d[2] == 0:
					if d[3] == 0:
						pass
					else:
						dontMove = 1
				else:
					dontMove = 1
			else:
				if d[2] == 0:
					if d[3] == 0:
						pass
					else:
						dontMove = 1
# LEFT sorting, first row
		for i in range(3):
			if a[0] == 0:
				a[0] = a[1]
				a[1] = a[2]
				a[2] = a[3]
				a[3] = 0
			else:
				for i in range(2):
					if a[1] == 0:
						a[1] = a[2]
						a[2] = a[3]
						a[3] = 0
					else:
						if a[2] == 0:
							a[2] = a[3]
							a[3] = 0
# LEFT sorting, second row
		for i in range(3):
			if b[0] == 0:
				b[0] = b[1]
				b[1] = b[2]
				b[2] = b[3]
				b[3] = 0
			else:
				for i in range(2):
					if b[1] == 0:
						b[1] = b[2]
						b[2] = b[3]
						b[3] = 0
					else:
						if b[2] == 0:
							b[2] = b[3]
							b[3] = 0
# LEFT sorting, third row
		for i in range(3):
			if c[0] == 0:
				c[0] = c[1]
				c[1] = c[2]
				c[2] = c[3]
				c[3] = 0
			else:
				for i in range(2):
					if c[1] == 0:
						c[1] = c[2]
						c[2] = c[3]
						c[3] = 0
					else:
						if c[2] == 0:
							c[2] = c[3]
							c[3] = 0
# LEFT sorting, fourth row
		for i in range(3):
			if d[0] == 0:
				d[0] = d[1]
				d[1] = d[2]
				d[2] = d[3]
				d[3] = 0
			else:
				for i in range(2):
					if d[1] == 0:
						d[1] = d[2]
						d[2] = d[3]
						d[3] = 0
					else:
						if d[2] == 0:
							d[2] = d[3]
							d[3] = 0
# LEFT to add up similar numbers, first row
		if a[0] != 0:
			if a[0] == a[1]:
				a[0] = a[0] + a[1]
				score = score + a[0]
				a[1] = a[2]
				a[2] = a[3]
				a[3] = 0
				dontMove = 1
		if a[1] != 0:
			if a[1] == a[2]:
				a[1] = a[1] + a[2]
				score = score + a[1]
				a[2] = a[3]
				a[3] = 0
				dontMove = 1
		if a[2] != 0:
			if a[2] == a[3]:
				a[2] = a[2] + a[3]
				score = score + a[2]
				a[3] = 0
				dontMove = 1
# LEFT to add up similar numbers, second row
		if b[0] != 0:
			if b[0] == b[1]:
				b[0] = b[0] + b[1]
				score = score + b[0]
				b[1] = b[2]
				b[2] = b[3]
				b[3] = 0
				dontMove = 1
		if b[1] != 0:
			if b[1] == b[2]:
				b[1] = b[1] + b[2]
				score = score + b[1]
				b[2] = b[3]
				b[3] = 0
				dontMove = 1
		if b[2] != 0:
			if b[2] == b[3]:
				b[2] = b[2] + b[3]
				score = score + b[2]
				b[3] = 0
				dontMove = 1
# LEFT to add up similar numbers, third row
		if c[0] != 0:
			if c[0] == c[1]:
				c[0] = c[0] + c[1]
				score = score + c[0]
				c[1] = c[2]
				c[2] = c[3]
				c[3] = 0
				dontMove = 1
		if c[1] != 0:
			if c[1] == c[2]:
				c[1] = c[1] + c[2]
				score = score + c[1]
				c[2] = c[3]
				c[3] = 0
				dontMove = 1
		if c[2] != 0:
			if c[2] == c[3]:
				c[2] = c[2] + c[3]
				score = score + c[2]
				c[3] = 0
				dontMove = 1
# LEFT to add up similar numbers, fourth row
		if d[0] != 0:
			if d[0] == d[1]:
				d[0] = d[0] + d[1]
				score = score + d[0]
				d[1] = d[2]
				d[2] = d[3]
				d[3] = 0
				dontMove = 1
		if d[1] != 0:
			if d[1] == d[2]:
				d[1] = d[1] + d[2]
				score = score + d[1]
				d[2] = d[3]
				d[3] = 0
				dontMove = 1
		if d[2] != 0:
			if d[2] == d[3]:
				d[2] = d[2] + d[3]
				score = score + d[2]
				d[3] = 0
				dontMove = 1
		randNum()
		printing()
		checking()

# RIGHT direction with 'd'
	elif key == "d":
		dontMove = 0
# RIGHT First row
		if a[3] == 0:
			if a[2] == 0:
				if a[1] == 0:
					if a[0] == 0:
						pass
					else:
						dontMove = 1
				else:
					dontMove = 1
			else:
				dontMove = 1
		else:
			if a[2] == 0:
				if a[1] == 0:
					if a[0] == 0:
						pass
					else:
						dontMove = 1
				else:
					dontMove = 1
			else:
				if a[1] == 0:
					if a[0] == 0:
						pass
					else:
						dontMove = 1
# RIGHT Second row
		if b[3] == 0:
			if b[2] == 0:
				if b[1] == 0:
					if b[0] == 0:
						pass
					else:
						dontMove = 1
				else:
					dontMove = 1
			else:
				dontMove = 1
		else:
			if b[2] == 0:
				if b[1] == 0:
					if b[0] == 0:
						pass
					else:
						dontMove = 1
				else:
					dontMove = 1
			else:
				if b[1] == 0:
					if b[0] == 0:
						pass
					else:
						dontMove = 1
# RIGHT Third row
		if c[3] == 0:
			if c[2] == 0:
				if c[1] == 0:
					if c[0] == 0:
						pass
					else:
						dontMove = 1
				else:
					dontMove = 1
			else:
				dontMove = 1
		else:
			if c[2] == 0:
				if c[1] == 0:
					if c[0] == 0:
						pass
					else:
						dontMove = 1
				else:
					dontMove = 1
			else:
				if c[1] == 0:
					if c[0] == 0:
						pass
					else:
						dontMove = 1
# RIGHT Fourth row
		if d[3] == 0:
			if d[2] == 0:
				if d[1] == 0:
					if d[0] == 0:
						pass
					else:
						dontMove = 1
				else:
					dontMove = 1
			else:
				dontMove = 1
		else:
			if d[2] == 0:
				if d[1] == 0:
					if d[0] == 0:
						pass
					else:
						dontMove = 1
				else:
					dontMove = 1
			else:
				if d[1] == 0:
					if d[0] == 0:
						pass
					else:
						dontMove = 1
# RIGHT sorting, first row
		for i in range(3):
			if a[3] == 0:
				a[3] = a[2]
				a[2] = a[1]
				a[1] = a[0]
				a[0] = 0
			else:
				for i in range(2):
					if a[2] == 0:
						a[2] = a[1]
						a[1] = a[0]
						a[0] = 0
					else:
						if a[1] == 0:
							a[1] = a[0]
							a[0] = 0
# RIGHT sorting, second row
		for i in range(3):
			if b[3] == 0:
				b[3] = b[2]
				b[2] = b[1]
				b[1] = b[0]
				b[0] = 0
			else:
				for i in range(2):
					if b[2] == 0:
						b[2] = b[1]
						b[1] = b[0]
						b[0] = 0
					else:
						if b[1] == 0:
							b[1] = b[0]
							b[0] = 0
# RIGHT sorting, third row
		for i in range(3):
			if c[3] == 0:
				c[3] = c[2]
				c[2] = c[1]
				c[1] = c[0]
				c[0] = 0
			else:
				for i in range(2):
					if c[2] == 0:
						c[2] = c[1]
						c[1] = c[0]
						c[0] = 0
					else:
						if c[1] == 0:
							c[1] = c[0]
							c[0] = 0
# RIGHT sorting, fourth row
		for i in range(3):
			if d[3] == 0:
				d[3] = d[2]
				d[2] = d[1]
				d[1] = d[0]
				d[0] = 0
			else:
				for i in range(2):
					if d[2] == 0:
						d[2] = d[1]
						d[1] = d[0]
						d[0] = 0
					else:
						if d[1] == 0:
							d[1] = d[0]
							d[0] = 0
# RIGHT to add up similar numbers, first row
		if a[3] != 0:
			if a[3] == a[2]:
				a[3] = a[3] + a[2]
				score = score + a[3]
				a[2] = a[1]
				a[1] = a[0]
				a[0] = 0
				dontMove = 1
		if a[2] != 0:
			if a[2] == a[1]:
				a[2] = a[2] + a[1]
				score = score + a[2]
				a[1] = a[0]
				a[0] = 0
				dontMove = 1
		if a[1] != 0:
			if a[1] == a[0]:
				a[1] = a[1] + a[0]
				score = score + a[1]
				a[0] = 0
				dontMove = 1
# RIGHT to add up similar numbers, second row
		if b[3] != 0:
			if b[3] == b[2]:
				b[3] = b[3] + b[2]
				score = score + b[3]
				b[2] = b[1]
				b[1] = b[0]
				b[0] = 0
				dontMove = 1
		if b[2] != 0:
			if b[2] == b[1]:
				b[2] = b[2] + b[1]
				score = score + b[2]
				b[1] = b[0]
				b[0] = 0
				dontMove = 1
		if b[1] != 0:
			if b[1] == b[0]:
				b[1] = b[1] + b[0]
				score = score + b[1]
				b[0] = 0
				dontMove = 1
# RIGHT to add up similar numbers, third row
		if c[3] != 0:
			if c[3] == c[2]:
				c[3] = c[3] + c[2]
				score = score + c[3]
				c[2] = c[1]
				c[1] = c[0]
				c[0] = 0
				dontMove = 1
		if c[2] != 0:
			if c[2] == c[1]:
				c[2] = c[2] + c[1]
				score = score + c[2]
				c[1] = c[0]
				c[0] = 0
				dontMove = 1
		if c[1] != 0:
			if c[1] == c[0]:
				c[1] = c[1] + c[0]
				score = score + c[1]
				c[0] = 0
				dontMove = 1
# RIGHT to add up similar numbers, fourth row
		if d[3] != 0:
			if d[3] == d[2]:
				d[3] = d[3] + d[2]
				score = score + d[3]
				d[2] = d[1]
				d[1] = d[0]
				d[0] = 0
				dontMove = 1
		if d[2] != 0:
			if d[2] == d[1]:
				d[2] = d[2] + d[1]
				score = score + d[2]
				d[1] = d[0]
				d[0] = 0
				dontMove = 1
		if d[1] != 0:
			if d[1] == d[0]:
				d[1] = d[1] + d[0]
				score = score + d[1]
				d[0] = 0
				dontMove = 1
		randNum()
		printing()
		checking()
# Exit button: 'x'
	elif key == "x":
		print()
		print("\033[92m" + "Thank you for playing!" + "\033[0m")
		print()
		quit()
# Wrong button handling
	else:
		print("Not valid key")
