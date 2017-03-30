import display
import welcome
import win
import lose
import sum_print
import biglist
import curses
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(1)

# First board printing
board = biglist.board(2)


def printing():
    stdscr.clear()

    partBetween1 = display.display_table(board[0])
    partBetween2 = display.display_table(board[1])
    partBetween3 = display.display_table(board[2])
    partBetween4 = display.display_table(board[3])

# print part
    sum_print.printer(board, partBetween1, partBetween2, partBetween3, partBetween4, score)

# checking the end of the game, in case if you achive 2048 or you don't have more moves


def checking():
    if ('2048' in board[0]) or ('2048' in board[1]) or ('2048' in board[2]) or ('2048' in board[3]):
        stdscr.clear()
        win.winning()
        key = stdscr.getch()
        if key == ord('q'):
            curses.echo()
            curses.nocbreak()
            stdscr.keypad(0)
            curses.endwin()
            quit()
        else:
            pass
    elif (board[0][0] == ' ') or (board[0][1] == ' ') or (board[0][2] == ' ') or (board[0][3] == ' '):
        pass
    elif (board[1][0] == ' ') or (board[1][1] == ' ') or (board[1][2] == ' ') or (board[1][3] == ' '):
        pass
    elif (board[2][0] == ' ') or (board[2][1] == ' ') or (board[2][2] == ' ') or (board[2][3] == ' '):
        pass
    elif (board[3][0] == ' ') or (board[3][1] == ' ') or (board[3][2] == ' ') or (board[3][3] == ' '):
        pass
    elif (board[0][0] == board[0][1]) or (board[0][0] == board[1][0]):
        pass
    elif (board[0][2] == board[0][1]) or (board[0][2] == board[0][3]) or (board[0][2] == board[1][2]):
        pass
    elif (board[1][1] == board[1][0]) or (board[1][1] == board[0][1]) or (board[1][1] == board[1][2]) or (board[1][1] == board[2][1]):
        pass
    elif (board[1][3] == board[1][2]) or (board[1][3] == board[0][3]) or (board[1][3] == board[2][3]):
        pass
    elif (board[2][0] == board[1][0]) or (board[2][0] == board[3][0]) or (board[2][0] == board[2][1]):
        pass
    elif (board[2][2] == board[2][1]) or (board[2][2] == board[2][3]) or (board[2][2] == board[1][2]) or (board[2][2] == board[3][2]):
        pass
    elif (board[3][1] == board[3][0]) or (board[3][1] == board[3][2]) or (board[3][1] == board[2][1]):
        pass
    elif (board[3][3] == board[2][3]) or (board[3][3] == board[3][2]):
        pass
    else:
        stdscr.clear()
        lose.losing()
        key = stdscr.getch()
        if key == ord('q'):
            curses.echo()
            curses.nocbreak()
            stdscr.keypad(0)
            curses.endwin()
        else:
            pass

# Put 2 (90% of the cases) or 4 (10% of the cases) to an empty random place (if there is), if the board changed.


def randNum():
    if dontMove == 1:
        randomList = list()
        randomItem = list()
        for i in range(len(board[0])):
            if board[0][i] == ' ':
                randomItem.append(i)
                randomList.append("a")

        for i in range(len(board[1])):
            if board[1][i] == ' ':
                randomItem.append(i)
                randomList.append("b")

        for i in range(len(board[2])):
            if board[2][i] == ' ':
                randomItem.append(i)
                randomList.append("c")

        for i in range(len(board[3])):
            if board[3][i] == ' ':
                randomItem.append(i)
                randomList.append("d")
# 2 or 4
        if len(randomList) != 0:
            import random
            chosen = random.randint(0, len(randomList) - 1)
            row = randomList[chosen]
            column = randomItem[chosen]
            twoOrFourlot = random.randint(1, 10)
            if twoOrFourlot == 1:
                twoOrFour = str(4)
            else:
                twoOrFour = str(2)

            if row == "a":
                board[0][column] = twoOrFour
            if row == "b":
                board[1][column] = twoOrFour
            if row == "c":
                board[2][column] = twoOrFour
            if row == "d":
                board[3][column] = twoOrFour

welcome.floating_msg()
game = 1
while game == 1:
    key = stdscr.getch()
    if key == curses.KEY_ENTER or key == 10 or key == 13:
        score = int()
        dontMove = 1
        randNum()
        randNum()
        printing()
        game = 0
    elif key == ord('q'):
        curses.echo()
        curses.nocbreak()
        stdscr.keypad(0)
        curses.endwin()
        quit()
    else:
        pass

# The game starts here:
while game < 1:
    key = stdscr.getch()
# UP direction with 'w'
# Exclusion of false movements caused by zeros
    if key == curses.KEY_UP:
        dontMove = 0
        for j in range(4):
            if board[0][j] == ' ':
                if board[1][j] == ' ':
                    if board[2][j] == ' ':
                        if board[3][j] == ' ':
                            pass
                        else:
                            dontMove = 1
                    else:
                        dontMove = 1
                else:
                    dontMove = 1
            else:
                if board[1][j] == ' ':
                    if board[2][j] == ' ':
                        if board[3][j] == ' ':
                            pass
                        else:
                            dontMove = 1
                    else:
                        dontMove = 1
                else:
                    if board[2][j] == ' ':
                        if board[3][j] == ' ':
                            pass
                        else:
                            dontMove = 1
# UP sorting
        for j in range(4):
            for i in range(3):
                if board[0][j] == ' ':
                    board[0][j] = board[1][j]
                    board[1][j] = board[2][j]
                    board[2][j] = board[3][j]
                    board[3][j] = ' '
                else:
                    for i in range(2):
                        if board[1][j] == ' ':
                            board[1][j] = board[2][j]
                            board[2][j] = board[3][j]
                            board[3][j] = ' '
                        else:
                            if board[2][j] == ' ':
                                board[2][j] = board[3][j]
                                board[3][j] = ' '
# UP to add up similar numbers
        for j in range(4):
            if board[0][j] != ' ':
                if board[0][j] == board[1][j]:
                    board[0][j] = str(int(board[0][j]) + int(board[1][j]))
                    score = score + int(board[0][j])
                    board[1][j] = board[2][j]
                    board[2][j] = board[3][j]
                    board[3][j] = ' '
                    dontMove = 1
            if board[1][j] != ' ':
                if board[1][j] == board[2][j]:
                    board[1][j] = str(int(board[1][j]) + int(board[2][j]))
                    score = score + int(board[1][j])
                    board[2][j] = board[3][j]
                    board[3][j] = ' '
                    dontMove = 1
            if board[2][j] != ' ':
                if board[2][j] == board[3][j]:
                    board[2][j] = str(int(board[2][j]) + int(board[3][j]))
                    score = score + int(board[2][j])
                    board[3][j] = ' '
                    dontMove = 1

        randNum()
        printing()
        checking()

# DOWN direction with 's'
    elif key == curses.KEY_DOWN:
        dontMove = 0
        for j in range(4):
            if board[3][j] == ' ':
                if board[2][j] == ' ':
                    if board[1][j] == ' ':
                        if board[0][j] == ' ':
                            pass
                        else:
                            dontMove = 1
                    else:
                        dontMove = 1
                else:
                    dontMove = 1
            else:
                if board[2][j] == ' ':
                    if board[1][j] == ' ':
                        if board[0][j] == ' ':
                            pass
                        else:
                            dontMove = 1
                    else:
                        dontMove = 1
                else:
                    if board[1][j] == ' ':
                        if board[0][j] == ' ':
                            pass
                        else:
                            dontMove = 1
# DOWN sorting
        for j in range(4):
            for i in range(3):
                if board[3][j] == ' ':
                    board[3][j] = board[2][j]
                    board[2][j] = board[1][j]
                    board[1][j] = board[0][j]
                    board[0][j] = ' '
                else:
                    for i in range(2):
                        if board[2][j] == ' ':
                            board[2][j] = board[1][j]
                            board[1][j] = board[0][j]
                            board[0][j] = ' '
                        else:
                            if board[1][j] == ' ':
                                board[1][j] = board[0][j]
                                board[0][j] = ' '
# DOWN to add up similar numbers
        for j in range(4):
            if board[3][j] != ' ':
                if board[3][j] == board[2][j]:
                    board[3][j] = str(int(board[3][j]) + int(board[2][j]))
                    score = score + int(board[3][j])
                    board[2][j] = board[1][j]
                    board[1][j] = board[0][j]
                    board[0][j] = ' '
                    dontMove = 1
            if board[2][j] != ' ':
                if board[2][j] == board[1][j]:
                    board[2][j] = str(int(board[2][j]) + int(board[1][j]))
                    score = score + int(board[2][j])
                    board[1][j] = board[0][j]
                    board[0][j] = ' '
                    dontMove = 1
            if board[1][j] != ' ':
                if board[1][j] == board[0][j]:
                    board[1][j] = str(int(board[1][j]) + int(board[0][j]))
                    score = score + int(board[1][j])
                    board[0][j] = ' '
                    dontMove = 1

        randNum()
        printing()
        checking()

# LEFT direction with 'a'
    elif key == curses.KEY_LEFT:
        dontMove = 0
        for j in range(4):
            if board[j][0] == ' ':
                if board[j][1] == ' ':
                    if board[j][2] == ' ':
                        if board[j][3] == ' ':
                            pass
                        else:
                            dontMove = 1
                    else:
                        dontMove = 1
                else:
                    dontMove = 1
            else:
                if board[j][1] == ' ':
                    if board[j][2] == ' ':
                        if board[j][3] == ' ':
                            pass
                        else:
                            dontMove = 1
                    else:
                        dontMove = 1
                else:
                    if board[j][2] == ' ':
                        if board[j][3] == ' ':
                            pass
                        else:
                            dontMove = 1

# LEFT sorting
        for j in range(4):
            for i in range(3):
                if board[j][0] == ' ':
                    board[j][0] = board[j][1]
                    board[j][1] = board[j][2]
                    board[j][2] = board[j][3]
                    board[j][3] = ' '
                else:
                    for i in range(2):
                        if board[j][1] == ' ':
                            board[j][1] = board[j][2]
                            board[j][2] = board[j][3]
                            board[j][3] = ' '
                        else:
                            if board[j][2] == ' ':
                                board[j][2] = board[j][3]
                                board[j][3] = ' '

# LEFT to add up similar numbers
        for j in range(4):
            if board[j][0] != ' ':
                if board[j][0] == board[j][1]:
                    board[j][0] = str(int(board[j][0]) + int(board[j][1]))
                    score = score + int(board[j][0])
                    board[j][1] = board[j][2]
                    board[j][2] = board[j][3]
                    board[j][3] = ' '
                    dontMove = 1
            if board[j][1] != ' ':
                if board[j][1] == board[j][2]:
                    board[j][1] = str(int(board[j][1]) + int(board[j][2]))
                    score = score + int(board[j][1])
                    board[j][2] = board[j][3]
                    board[j][3] = ' '
                    dontMove = 1
            if board[j][2] != ' ':
                if board[j][2] == board[j][3]:
                    board[j][2] = str(int(board[j][2]) + int(board[j][3]))
                    score = score + int(board[j][2])
                    board[j][3] = ' '
                    dontMove = 1
        randNum()
        printing()
        checking()

# RIGHT direction with 'd'
    elif key == curses.KEY_RIGHT:
        dontMove = 0
# RIGHT
        for j in range(4):
            if board[j][3] == ' ':
                if board[j][2] == ' ':
                    if board[j][1] == ' ':
                        if board[j][0] == ' ':
                            pass
                        else:
                            dontMove = 1
                    else:
                        dontMove = 1
                else:
                    dontMove = 1
            else:
                if board[j][2] == ' ':
                    if board[j][1] == ' ':
                        if board[j][0] == ' ':
                            pass
                        else:
                            dontMove = 1
                    else:
                        dontMove = 1
                else:
                    if board[j][1] == ' ':
                        if board[j][0] == ' ':
                            pass
                        else:
                            dontMove = 1

# RIGHT sorting
        for j in range(4):
            for i in range(3):
                if board[j][3] == ' ':
                    board[j][3] = board[j][2]
                    board[j][2] = board[j][1]
                    board[j][1] = board[j][0]
                    board[j][0] = ' '
                else:
                    for i in range(2):
                        if board[j][2] == ' ':
                            board[j][2] = board[j][1]
                            board[j][1] = board[j][0]
                            board[j][0] = ' '
                        else:
                            if board[j][1] == ' ':
                                board[j][1] = board[j][0]
                                board[j][0] = ' '

# RIGHT to add up similar numbers
        for j in range(4):
            if board[j][3] != ' ':
                if board[j][3] == board[j][2]:
                    board[j][3] = str(int(board[j][3]) + int(board[j][2]))
                    score = score + int(board[j][3])
                    board[j][2] = board[j][1]
                    board[j][1] = board[j][0]
                    board[j][0] = ' '
                    dontMove = 1
            if board[j][2] != ' ':
                if board[j][2] == board[j][1]:
                    board[j][2] = str(int(board[j][2]) + int(board[j][1]))
                    score = score + int(board[j][2])
                    board[j][1] = board[j][0]
                    board[j][0] = ' '
                    dontMove = 1
            if board[j][1] != ' ':
                if board[j][1] == board[j][0]:
                    board[j][1] = str(int(board[j][1]) + int(board[j][0]))
                    score = score + int(board[j][1])
                    board[j][0] = ' '
                    dontMove = 1

        randNum()
        printing()
        checking()
# Exit button: 'q'

    elif key == ord('q'):
        curses.echo()
        curses.nocbreak()
        stdscr.keypad(0)
        curses.endwin()
        quit()
# Wrong button handling
    else:
        pass
