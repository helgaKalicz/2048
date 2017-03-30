import coloring
import display
import os
import welcome
import sum_print

# First board printing
a = ['1024', '1024', '0', '0']
b = ['0', '0', '0', '0']
c = ['0', '0', '0', '0']
d = ['0', '0', '0', '0']

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

	partBetween1 = display.display_table(a)
	partBetween2 = display.display_table(b)
	partBetween3 = display.display_table(c)
	partBetween4 = display.display_table(d)
	
	colored_a = coloring.coloring_list(a,C2)
	colored_b = coloring.coloring_list(b,C2)
	colored_c = coloring.coloring_list(c,C2)
	colored_d = coloring.coloring_list(d,C2)

# print part
	sum_print.printer(colored_a, colored_b, colored_c, colored_d, partBetween1, partBetween2, partBetween3, partBetween4, score)

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

welcome.floating_msg()
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