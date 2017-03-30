# Colors:
C0 = '\033[0m'		# Reset colour
C1 = '\033[08m'		# Invisible
C2 = '\033[92m'		# Green
C3 = '\033[91m'		# Red
C4 = '\033[96m'		# LightBlue
C5 = '\033[34m'		# Blue
C6 = '\033[35m'		# Purple

def coloring_list(your_list, color):
    '''
    Hide the value if it is 0.
    Change the color of other values.
    '''
    colored_list = []
    for item in your_list:
        if item == "0":
            item = C1 + str(item) + C0
            colored_list.append(item)
        else:
            item = color + str(item) + C0
            colored_list.append(item)

    return colored_list
