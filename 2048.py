# Colors:
C0 = '\033[0m'		# Reset colour
C1 = '\033[08m'		# Invisible
C2 = '\033[92m'		# Green
C3 = '\033[91m'		# Red
C4 = '\033[96m'		# LightBlue
C5 = '\033[34m'		# Blue
C6 = '\033[35m'		# Purple



def printing():
	os.system('clear')

# colour part, 0 is invisible

	if a[0] == '0':
		a0 = C1+(a[0])+C0
	else:
		a0 = C2+(a[0])+C0
	if a[1] == '0':
		a1 = C1+(a[1])+C0
	else:
		a1 = C2+(a[1])+C0
	if a[2] == '0':
		a2 = C1+(a[2])+C0
	else:
		a2 = C2+(a[2])+C0
	if a[3] == '0':
		a3 = C1+(a[3])+C0
	else:
		a3 = C2+(a[3])+C0
	if b[0] == '0':
		b0 = C1+(b[0])+C0
	else:
		b0 = C2+(b[0])+C0
	if b[1] == '0':
		b1 = C1+(b[1])+C0
	else:
		b1 = C2+(b[1])+C0
	if b[2] == '0':
		b2 = C1+(b[2])+C0
	else:
		b2 = C2+(b[2])+C0
	if b[3] == '0':
		b3 = C1+(b[3])+C0
	else:
		b3 = C2+(b[3])+C0
	if c[0] == '0':
		c0 = C1+(c[0])+C0
	else:
		c0 = C2+(c[0])+C0
	if c[1] == '0':
		c1 = C1+(c[1])+C0
	else:
		c1 = C2+(c[1])+C0
	if c[2] == '0':
		c2 = C1+(c[2])+C0
	else:
		c2 = C2+(c[2])+C0
	if c[3] == '0':
		c3 = C1+(c[3])+C0
	else:
		c3 = C2+(c[3])+C0
	if d[0] == '0':
		d0 = C1+(d[0])+C0
	else:
		d0 = C2+(d[0])+C0
	if d[1] == '0':
		d1 = C1+(d[1])+C0
	else:
		d1 = C2+(d[1])+C0
	if d[2] == '0':
		d2 = C1+(d[2])+C0
	else:
		d2 = C2+(d[2])+C0
	if d[3] == '0':
		d3 = C1+(d[3])+C0
	else:
		d3 = C2+(d[3])+C0

# handling several digit numbers, first row
	one_digit = '   │  '
	two_digits = '  │  '
	three_digits = ' │  '
	four_digits = '│  '
	if len(str(a[0])) == 1:
		partBetween1 = one_digit
	elif len(str(a[0])) == 2:
		partBetween1 = two_digits
	elif len(str(a[0])) == 3:
		partBetween1 = three_digits
	elif len(str(a[0])) == 4:
		partBetween1 = four_digits

	if len(str(a[1])) == 1:
		partBetween2 = one_digit
	elif len(str(a[1])) == 2:
		partBetween2 = two_digits
	elif len(str(a[1])) == 3:
		partBetween2 = three_digits
	elif len(str(a[1])) == 4:
		partBetween2 = four_digits

	if len(str(a[2])) == 1:
		partBetween3 = one_digit
	elif len(str(a[2])) == 2:
		partBetween3 = two_digits
	elif len(str(a[2])) == 3:
		partBetween3 = three_digits
	elif len(str(a[2])) == 4:
		partBetween3 = four_digits
	
	if len(str(a[3])) == 1:
		partRight1 = one_digit
	elif len(str(a[3])) == 2:
		partRight1 = two_digits
	elif len(str(a[3])) == 3:
		partRight1 = three_digits
	elif len(str(a[3])) == 4:
		partRight1 = four_digits

# digits: second row
	if len(str(b[0])) == 1:
		partBetween4 = one_digit
	elif len(str(b[0])) == 2:
		partBetween4 = two_digits
	elif len(str(b[0])) == 3:
		partBetween4 = three_digits
	elif len(str(b[0])) == 4:
		partBetween4 = four_digits

	if len(str(b[1])) == 1:
		partBetween5 = one_digit
	elif len(str(b[1])) == 2:
		partBetween5 = two_digits
	elif len(str(b[1])) == 3:
		partBetween5 = three_digits
	elif len(str(b[1])) == 4:
		partBetween5 = four_digits

	if len(str(b[2])) == 1:
		partBetween6 = one_digit
	elif len(str(b[2])) == 2:
		partBetween6 = two_digits
	elif len(str(b[2])) == 3:
		partBetween6 = three_digits
	elif len(str(b[2])) == 4:
		partBetween6 = four_digits
	
	if len(str(b[3])) == 1:
		partRight2 = one_digit
	elif len(str(b[3])) == 2:
		partRight2 = two_digits
	elif len(str(b[3])) == 3:
		partRight2 = three_digits
	elif len(str(b[3])) == 4:
		partRight2 = four_digits

# digits: third row
	if len(str(c[0])) == 1:
		partBetween7 = one_digit
	elif len(str(c[0])) == 2:
		partBetween7 = two_digits
	elif len(str(c[0])) == 3:
		partBetween7 = three_digits
	elif len(str(c[0])) == 4:
		partBetween7 = four_digits

	if len(str(c[1])) == 1:
		partBetween8 = one_digit
	elif len(str(c[1])) == 2:
		partBetween8 = two_digits
	elif len(str(c[1])) == 3:
		partBetween8 = three_digits
	elif len(str(c[1])) == 4:
		partBetween8 = four_digits

	if len(str(c[2])) == 1:
		partBetween9 = one_digit
	elif len(str(c[2])) == 2:
		partBetween9 = two_digits
	elif len(str(c[2])) == 3:
		partBetween9 = three_digits
	elif len(str(c[2])) == 4:
		partBetween9 = four_digits
	
	if len(str(c[3])) == 1:
		partRight3 = one_digit
	elif len(str(c[3])) == 2:
		partRight3 = two_digits
	elif len(str(c[3])) == 3:
		partRight3 = three_digits
	elif len(str(c[3])) == 4:
		partRight3 = four_digits

# digits: fourth row
	if len(str(d[0])) == 1:
		partBetween10 = one_digit
	elif len(str(d[0])) == 2:
		partBetween10 = two_digits
	elif len(str(d[0])) == 3:
		partBetween10 = three_digits
	elif len(str(d[0])) == 4:
		partBetween10 = four_digits

	if len(str(d[1])) == 1:
		partBetween11 = one_digit
	elif len(str(d[1])) == 2:
		partBetween11 = two_digits
	elif len(str(d[1])) == 3:
		partBetween11 = three_digits
	elif len(str(d[1])) == 4:
		partBetween11 = four_digits

	if len(str(d[2])) == 1:
		partBetween12 = one_digit
	elif len(str(d[2])) == 2:
		partBetween12 = two_digits
	elif len(str(d[2])) == 3:
		partBetween12 = three_digits
	elif len(str(d[2])) == 4:
		partBetween12 = four_digits
	
	if len(str(d[3])) == 1:
		partRight4 = one_digit
	elif len(str(d[3])) == 2:
		partRight4 = two_digits
	elif len(str(d[3])) == 3:
		partRight4 = three_digits
	elif len(str(d[3])) == 4:
		partRight4 = four_digits

# print part
	print(C2 + "Score:" + C4 + " " + str(score) + C0)
	print()
	print(C3+'                                     ┌──────┬──────┬──────┬──────┐' + C0)
	print(C3+'                                     │      │      │      │      │' + C0)
	print(C3+'                                     │  ' + C0 + a0 + C3 + partBetween1 + C0 + a1 + C3 + partBetween2 + C0 + a2 + C3 + partBetween3 + C0 + a3 + C3 + partRight1 + C0)
	print(C3+'                                     │      │      │      │      │' + C0)
	print(C3+'                                     ├──────┼──────┼──────┼──────┤' + C0)
	print(C3+'                                     │      │      │      │      │' + C0)
	print(C3+'                                     │  ' + C0 + b0 + C3 + partBetween4 + C0 + b1 + C3 + partBetween5 + C0 + b2 + C3 + partBetween6 + C0 + b3 + C3 + partRight2 + C0)
	print(C3+'                                     │      │      │      │      │' + C0)
	print(C3+'                                     ├──────┼──────┼──────┼──────┤' + C0)
	print(C3+'                                     │      │      │      │      │' + C0)
	print(C3+'                                     │  ' + C0 + c0 + C3 + partBetween7 + C0 + c1 + C3 + partBetween8 + C0 + c2 + C3 + partBetween9 + C0 + c3 + C3 + partRight3 + C0)
	print(C3+'                                     │      │      │      │      │' + C0)
	print(C3+'                                     ├──────┼──────┼──────┼──────┤' + C0)
	print(C3+'                                     │      │      │      │      │' + C0)
	print(C3+'                                     │  ' + C0 + d0 + C3 + partBetween10 + C0 + d1 + C3 + partBetween11 + C0 + d2 + C3 + partBetween12 + C0 + d3 + C3 + partRight4 + C0)
	print(C3+'                                     │      │      │      │      │' + C0)
	print(C3+'                                     └──────┴──────┴──────┴──────┘' + C0)
	print()

# checking the end of the game, in case if you achive 2048 or you don't have more moves
def checking():
	if ('2048' in a) or ('2048' in b) or ('2048' in c) or ('2048' in d):
		print()
		print(C2 + "You win!!!" + C0)
		continue_game = input("Press \'y\' if you want to continue the game")
		if continue_game == 'y':
			pass
		else:
			quit()
	elif (a[0] == '0') or (a[1] == '0') or (a[2] == '0') or (a[3] == '0'):
		pass
	elif (b[0] == '0') or (b[1] == '0') or (b[2] == '0') or (b[3] == '0'):
		pass
	elif (c[0] == '0') or (c[1] == '0') or (c[2] == '0') or (c[3] == '0'):
		pass
	elif (d[0] == '0') or (d[1] == '0') or (d[2] == '0') or (d[3] == '0'):
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
		print(C2 + "No more moves! Game over!" + C0)
		print()
		quit()

# Put 2 (90% of the cases) or 4 (10% of the cases) to an empty random place (if there is), if the board changed. 
def randNum():
	if dontMove == 1:
		randomList = list()
		randomItem = list()
		for i in range(len(a)):
			if a[i] == '0':
				randomItem.append(i)
				randomList.append("a")

		for i in range(len(b)):
			if b[i] == '0':
				randomItem.append(i)
				randomList.append("b")

		for i in range(len(c)):
			if c[i] == '0':
				randomItem.append(i)
				randomList.append("c")

		for i in range(len(d)):
			if d[i] == '0':
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
				twoOrFour = str(4)
			else:
				twoOrFour = str(2)

			if row == "a":
				a[column] = twoOrFour
			if row == "b":
				b[column] = twoOrFour
			if row == "c":
				c[column] = twoOrFour
			if row == "d":
				d[column] = twoOrFour

# First board printing
a = ['0', '0', '0', '0']
b = ['0', '0', '0', '0']
c = ['0', '0', '0', '0']
d = ['0', '0', '0', '0']
board_size = 4

from functions2048 import coolStart
import os
game = 1
print()
print()
while game == 1:
	start = input(C2 + "Press \'s\' to start the game! (or \'x\' to EXIT): " + C0)
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
	key = input(C2 + "Select a direction and press enter (use \'x\' to EXIT): " + C0)
# UP direction with 'w'
# Exclusion of false movements caused by zeros
	if key == "w":
		dontMove = 0
		for j in range(4):
			if a[j] == '0':
				if b[j] == '0':
					if c[j] == '0':
						if d[j] == '0':
							pass
						else:
							dontMove = 1
					else:
						dontMove = 1
				else:
					dontMove = 1
			else:
				if b[j] == '0':
					if c[j] == '0':
						if d[j] == '0':
							pass
						else:
							dontMove = 1
					else:
						dontMove = 1
				else:
					if c[j] == '0':
						if d[j] == '0':
							pass
						else:
							dontMove = 1
# UP sorting
		for j in range(4):
			for i in range(3):
				if a[j] == '0':
					a[j] = b[j]
					b[j] = c[j]
					c[j] = d[j]
					d[j] = '0'
				else:
					for i in range(2):
						if b[j] == '0':
							b[j] = c[j]
							c[j] = d[j]
							d[j] = '0'
						else:
							if c[j] == '0':
								c[j] = d[j]
								d[j] = '0'
# UP to add up similar numbers
		for j in range(4):
			if a[j] != '0':
				if a[j] == b[j]:
					a[j] = str(int(a[j]) + int(b[j]))
					score = score + int(a[j])
					b[j] = c[j]
					c[j] = d[j]
					d[j] = '0'
					dontMove = 1
			if b[j] != '0':
				if b[j] == c[j]:
					b[j] = str(int(b[j]) + int(c[j]))
					score = score + int(b[j])
					c[j] = d[j]
					d[j] = '0'
					dontMove = 1
			if c[j] != '0':
				if c[j] == d[j]:
					c[j] = str(int(c[j]) + int(d[j]))
					score = score + int(c[j])
					d[j] = '0'
					dontMove = 1
			j = j + 1
		randNum()
		printing()
		checking()

# DOWN direction with 's'
	elif key == "s":
		dontMove = 0
		for j in range(4):
			if d[j] == '0':
				if c[j] == '0':
					if b[j] == '0':
						if a[j] == '0':
							pass
						else:
							dontMove = 1
					else:
						dontMove = 1
				else:
					dontMove = 1
			else:
				if c[j] == '0':
					if b[j] == '0':
						if a[j] == '0':
							pass
						else:
							dontMove = 1
					else:
						dontMove = 1
				else:
					if b[j] == '0':
						if a[j] == '0':
							pass
						else:
							dontMove = 1
# DOWN sorting
		for j in range(4):
			for i in range(3):
				if d[j] == '0':
					d[j] = c[j]
					c[j] = b[j]
					b[j] = a[j]
					a[j] = '0'
				else:
					for i in range(2):
						if c[j] == '0':
							c[j] = b[j]
							b[j] = a[j]
							a[j] = '0'
						else:
							if b[j] == '0':
								b[j] = a[j]
								a[j] = '0'
# DOWN to add up similar numbers
		j = 0
		while j < 4:
			if d[j] != '0':
				if d[j] == c[j]:
					d[j] = str(int(d[j]) + int(c[j]))
					score = score + int(d[j])
					c[j] = b[j]
					b[j] = a[j]
					a[j] = '0'
					dontMove = 1
			if c[j] != '0':
				if c[j] == b[j]:
					c[j] = str(int(c[j]) + int(b[j]))
					score = score + int(c[j])
					b[j] = a[j]
					a[j] = '0'
					dontMove = 1
			if b[j] != '0':
				if b[j] == a[j]:
					b[j] = str(int(b[j]) + int(a[j]))
					score = score + b[j]
					a[j] = '0'           
					dontMove = 1
			j = j + 1
		randNum()
		printing()
		checking()

# LEFT direction with 'a'
	elif key == "a":
		dontMove = 0
# LEFT First row
		if a[0] == '0':
			if a[1] == '0':
				if a[2] == '0':
					if a[3] == '0':
						pass
					else:
						dontMove = 1
				else:
					dontMove = 1
			else:
				dontMove = 1
		else:
			if a[1] == '0':
				if a[2] == '0':
					if a[3] == '0':
						pass
					else:
						dontMove = 1
				else:
					dontMove = 1
			else:
				if a[2] == '0':
					if a[3] == '0':
						pass
					else:
						dontMove = 1
# LEFT Second row
		if b[0] == '0':
			if b[1] == '0':
				if b[2] == '0':
					if b[3] == '0':
						pass
					else:
						dontMove = 1
				else:
					dontMove = 1
			else:
				dontMove = 1
		else:
			if b[1] == '0':
				if b[2] == '0':
					if b[3] == '0':
						pass
					else:
						dontMove = 1
				else:
					dontMove = 1
			else:
				if b[2] == '0':
					if b[3] == '0':
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
			if c[1] == '0':
				if c[2] == '0':
					if c[3] == '0':
						pass
					else:
						dontMove = 1
				else:
					dontMove = 1
			else:
				if c[2] == '0':
					if c[3] == '0':
						pass
					else:
						dontMove = 1
# LEFT Fourth row
		if d[0] == '0':
			if d[1] == '0':
				if d[2] == '0':
					if d[3] == '0':
						pass
					else:
						dontMove = 1
				else:
					dontMove = 1
			else:
				dontMove = 1
		else:
			if d[1] == '0':
				if d[2] == '0':
					if d[3] == '0':
						pass
					else:
						dontMove = 1
				else:
					dontMove = 1
			else:
				if d[2] == '0':
					if d[3] == '0':
						pass
					else:
						dontMove = 1
# LEFT sorting, first row
		for i in range(3):
			if a[0] == '0':
				a[0] = a[1]
				a[1] = a[2]
				a[2] = a[3]
				a[3] = '0'
			else:
				for i in range(2):
					if a[1] == '0':
						a[1] = a[2]
						a[2] = a[3]
						a[3] = '0'
					else:
						if a[2] == '0':
							a[2] = a[3]
							a[3] = '0'
# LEFT sorting, second row
		for i in range(3):
			if b[0] == '0':
				b[0] = b[1]
				b[1] = b[2]
				b[2] = b[3]
				b[3] = '0'
			else:
				for i in range(2):
					if b[1] == '0':
						b[1] = b[2]
						b[2] = b[3]
						b[3] = '0'
					else:
						if b[2] == '0':
							b[2] = b[3]
							b[3] = '0'
# LEFT sorting, third row
		for i in range(3):
			if c[0] == '0':
				c[0] = c[1]
				c[1] = c[2]
				c[2] = c[3]
				c[3] = '0'
			else:
				for i in range(2):
					if c[1] == '0':
						c[1] = c[2]
						c[2] = c[3]
						c[3] = '0'
					else:
						if c[2] == '0':
							c[2] = c[3]
							c[3] = '0'
# LEFT sorting, fourth row
		for i in range(3):
			if d[0] == '0':
				d[0] = d[1]
				d[1] = d[2]
				d[2] = d[3]
				d[3] = '0'
			else:
				for i in range(2):
					if d[1] == '0':
						d[1] = d[2]
						d[2] = d[3]
						d[3] = '0'
					else:
						if d[2] == '0':
							d[2] = d[3]
							d[3] = '0'
# LEFT to add up similar numbers, first row
		if a[0] != '0':
			if a[0] == a[1]:
				a[0] = str(int(a[0]) + int(a[1]))
				score = score + int(a[0])
				a[1] = a[2]
				a[2] = a[3]
				a[3] = '0'
				dontMove = 1
		if a[1] != '0':
			if a[1] == a[2]:
				a[1] = str(int(a[1]) + int(a[2]))
				score = score + int(a[1])
				a[2] = a[3]
				a[3] = '0'
				dontMove = 1
		if a[2] != '0':
			if a[2] == a[3]:
				a[2] = str(int(a[2]) + int(a[3]))
				score = score + int(a[2])
				a[3] = '0'
				dontMove = 1
# LEFT to add up similar numbers, second row
		if b[0] != '0':
			if b[0] == b[1]:
				b[0] = str(int(b[0]) + int(b[1]))
				score = score + int(b[0])
				b[1] = b[2]
				b[2] = b[3]
				b[3] = '0'
				dontMove = 1
		if b[1] != '0':
			if b[1] == b[2]:
				b[1] = str(int(b[1]) + int(b[2]))
				score = score + int(b[1])
				b[2] = b[3]
				b[3] = '0'
				dontMove = 1
		if b[2] != '0':
			if b[2] == b[3]:
				b[2] = str(int(b[2]) + int(b[3]))
				score = score + int(b[2])
				b[3] = '0'
				dontMove = 1
# LEFT to add up similar numbers, third row
		if c[0] != '0':
			if c[0] == c[1]:
				c[0] = str(int(c[0]) + int(c[1]))
				score = score + int(c[0])
				c[1] = c[2]
				c[2] = c[3]
				c[3] = '0'
				dontMove = 1
		if c[1] != '0':
			if c[1] == c[2]:
				c[1] = str(int(c[1]) + int(c[2]))
				score = score + int(c[1])
				c[2] = c[3]
				c[3] = '0'
				dontMove = 1
		if c[2] != '0':
			if c[2] == c[3]:
				c[2] = str(int(c[2]) + int(c[3]))
				score = score + int(c[2])
				c[3] = '0'
				dontMove = 1
# LEFT to add up similar numbers, fourth row
		if d[0] != '0':
			if d[0] == d[1]:
				d[0] = str(int(d[0]) + int(d[1]))
				score = score + int(d[0])
				d[1] = d[2]
				d[2] = d[3]
				d[3] = '0'
				dontMove = 1
		if d[1] != '0':
			if d[1] == d[2]:
				d[1] = str(int(d[1]) + int(d[2]))
				score = score + int(d[1])
				d[2] = d[3]
				d[3] = '0'
				dontMove = 1
		if d[2] != '0':
			if d[2] == d[3]:
				d[2] = str(int(d[2]) + int(d[3]))
				score = score + int(d[2])
				d[3] = '0'
				dontMove = 1
		randNum()
		printing()
		checking()

# RIGHT direction with 'd'
	elif key == "d":
		dontMove = 0
# RIGHT First row
		if a[3] == '0':
			if a[2] == '0':
				if a[1] == '0':
					if a[0] == '0':
						pass
					else:
						dontMove = 1
				else:
					dontMove = 1
			else:
				dontMove = 1
		else:
			if a[2] == '0':
				if a[1] == '0':
					if a[0] == '0':
						pass
					else:
						dontMove = 1
				else:
					dontMove = 1
			else:
				if a[1] == '0':
					if a[0] == '0':
						pass
					else:
						dontMove = 1
# RIGHT Second row
		if b[3] == '0':
			if b[2] == '0':
				if b[1] == '0':
					if b[0] == '0':
						pass
					else:
						dontMove = 1
				else:
					dontMove = 1
			else:
				dontMove = 1
		else:
			if b[2] == '0':
				if b[1] == '0':
					if b[0] == '0':
						pass
					else:
						dontMove = 1
				else:
					dontMove = 1
			else:
				if b[1] == '0':
					if b[0] == '0':
						pass
					else:
						dontMove = 1
# RIGHT Third row
		if c[3] == '0':
			if c[2] == '0':
				if c[1] == '0':
					if c[0] == '0':
						pass
					else:
						dontMove = 1
				else:
					dontMove = 1
			else:
				dontMove = 1
		else:
			if c[2] == '0':
				if c[1] == '0':
					if c[0] == '0':
						pass
					else:
						dontMove = 1
				else:
					dontMove = 1
			else:
				if c[1] == '0':
					if c[0] == '0':
						pass
					else:
						dontMove = 1
# RIGHT Fourth row
		if d[3] == '0':
			if d[2] == '0':
				if d[1] == '0':
					if d[0] == '0':
						pass
					else:
						dontMove = 1
				else:
					dontMove = 1
			else:
				dontMove = 1
		else:
			if d[2] == '0':
				if d[1] == '0':
					if d[0] == '0':
						pass
					else:
						dontMove = 1
				else:
					dontMove = 1
			else:
				if d[1] == '0':
					if d[0] == '0':
						pass
					else:
						dontMove = 1
# RIGHT sorting, first row
		for i in range(3):
			if a[3] == '0':
				a[3] = a[2]
				a[2] = a[1]
				a[1] = a[0]
				a[0] = '0'
			else:
				for i in range(2):
					if a[2] == '0':
						a[2] = a[1]
						a[1] = a[0]
						a[0] = '0'
					else:
						if a[1] == '0':
							a[1] = a[0]
							a[0] = '0'
# RIGHT sorting, second row
		for i in range(3):
			if b[3] == '0':
				b[3] = b[2]
				b[2] = b[1]
				b[1] = b[0]
				b[0] = '0'
			else:
				for i in range(2):
					if b[2] == '0':
						b[2] = b[1]
						b[1] = b[0]
						b[0] = '0'
					else:
						if b[1] == '0':
							b[1] = b[0]
							b[0] = '0'
# RIGHT sorting, third row
		for i in range(3):
			if c[3] == '0':
				c[3] = c[2]
				c[2] = c[1]
				c[1] = c[0]
				c[0] = '0'
			else:
				for i in range(2):
					if c[2] == '0':
						c[2] = c[1]
						c[1] = c[0]
						c[0] = '0'
					else:
						if c[1] == '0':
							c[1] = c[0]
							c[0] = '0'
# RIGHT sorting, fourth row
		for i in range(3):
			if d[3] == '0':
				d[3] = d[2]
				d[2] = d[1]
				d[1] = d[0]
				d[0] = '0'
			else:
				for i in range(2):
					if d[2] == '0':
						d[2] = d[1]
						d[1] = d[0]
						d[0] = '0'
					else:
						if d[1] == '0':
							d[1] = d[0]
							d[0] = '0'
# RIGHT to add up similar numbers, first row
		if a[3] != '0':
			if a[3] == a[2]:
				a[3] = str(int(a[3]) + int(a[2]))
				score = score + int(a[3])
				a[2] = a[1]
				a[1] = a[0]
				a[0] = '0'
				dontMove = 1
		if a[2] != '0':
			if a[2] == a[1]:
				a[2] = str(int(a[2]) + int(a[1]))
				score = score + int(a[2])
				a[1] = a[0]
				a[0] = '0'
				dontMove = 1
		if a[1] != '0':
			if a[1] == a[0]:
				a[1] = str(int(a[1]) + int(a[0]))
				score = score + int(a[1])
				a[0] = '0'
				dontMove = 1
# RIGHT to add up similar numbers, second row
		if b[3] != '0':
			if b[3] == b[2]:
				b[3] = str(int(b[3]) + int(b[2]))
				score = score + int(b[3])
				b[2] = b[1]
				b[1] = b[0]
				b[0] = '0'
				dontMove = 1
		if b[2] != '0':
			if b[2] == b[1]:
				b[2] = str(int(b[2]) + int(b[1]))
				score = score + int(b[2])
				b[1] = b[0]
				b[0] = '0'
				dontMove = 1
		if b[1] != '0':
			if b[1] == b[0]:
				b[1] = str(int(b[1]) + int(b[0]))
				score = score + int(b[1])
				b[0] = '0'
				dontMove = 1
# RIGHT to add up similar numbers, third row
		if c[3] != '0':
			if c[3] == c[2]:
				c[3] = str(int(c[3]) + int(c[2]))
				score = score + int(c[3])
				c[2] = c[1]
				c[1] = c[0]
				c[0] = '0'
				dontMove = 1
		if c[2] != '0':
			if c[2] == c[1]:
				c[2] = str(int(c[2]) + int(c[1]))
				score = score + int(c[2])
				c[1] = c[0]
				c[0] = '0'
				dontMove = 1
		if c[1] != '0':
			if c[1] == c[0]:
				c[1] = str(int(c[1]) + int(c[0]))
				score = score + int(c[1])
				c[0] = '0'
				dontMove = 1
# RIGHT to add up similar numbers, fourth row
		if d[3] != '0':
			if d[3] == d[2]:
				d[3] = str(int(d[3]) + int(d[2]))
				score = score + int(d[3])
				d[2] = d[1]
				d[1] = d[0]
				d[0] = '0'
				dontMove = 1
		if d[2] != '0':
			if d[2] == d[1]:
				d[2] = str(int(d[2]) + int(d[1]))
				score = score + int(d[2])
				d[1] = d[0]
				d[0] = '0'
				dontMove = 1
		if d[1] != '0':
			if d[1] == d[0]:
				d[1] = str(int(d[1]) + int(d[0]))
				score = score + int(d[1])
				d[0] = '0'
				dontMove = 1
		randNum()
		printing()
		checking()
# Exit button: 'x'
	elif key == "x":
		print()
		print(C2 + "Thank you for playing!" + C0)
		print()
		quit()
# Wrong button handling
	else:
		print("Not valid key")
