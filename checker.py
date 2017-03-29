# Colors:
C0 = '\033[0m'		# Reset colour
C1 = '\033[08m'		# Invisible
C2 = '\033[92m'		# Green
C3 = '\033[91m'		# Red
C4 = '\033[96m'		# LightBlue
C5 = '\033[34m'		# Blue
C6 = '\033[35m'		# Purple

a = ['2048', '1024', '0', '0']
b = ['0', '0', '0', '0']
c = ['0', '0', '0', '0']
d = ['0', '0', '0', '0']

def checking(a, b, c, d):
    if ('2048' in a) or ('2048' in b) or ('2048' in c) or ('2048' in d):
        msg = C2 + "You win!!!" + C0
    return msg

print(checking(a, b, c, d)
'''
    print()
		continue_game = input("Press \'y\' if you want to continue the game")
		if continue_game == 'y':
			pass
		else:
			quit()
'''

'''
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
'''
