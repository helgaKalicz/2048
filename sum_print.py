def printer(board, first_row_display, second_row_display, third_row_display, fourth_row_display, label):
    import curses
    stdscr = curses.initscr()
    arrange_center = '                                      '
    frame_top = '┌──────┬──────┬──────┬──────┐'
    frame_boarder = '│      │      │      │      │'
    arrange_center1 = '│  '
    frame_boarder1 = '├──────┼──────┼──────┼──────┤'
    frame_bottom = '└──────┴──────┴──────┴──────┘'
    stdscr.addstr(0, 0, "Score: " + str(label))
    stdscr.addstr(2, 0, arrange_center + frame_top)
    stdscr.addstr(3, 0, arrange_center + frame_boarder)
    stdscr.addstr(4, 0, arrange_center + arrange_center1 + board[0][0] + first_row_display[0] + board[0][1] + first_row_display[1] + board[0][2] + first_row_display[2] +  board[0][3] + first_row_display[3])
    stdscr.addstr(5, 0, arrange_center + frame_boarder)
    stdscr.addstr(6, 0, arrange_center + frame_boarder1)
    stdscr.addstr(7, 0, arrange_center + frame_boarder)
    stdscr.addstr(8, 0, arrange_center + arrange_center1 + board[1][0] + second_row_display[0] + board[1][1] + second_row_display[1] + board[1][2] + second_row_display[2] + board[1][3] + second_row_display[3])
    stdscr.addstr(9, 0, arrange_center + frame_boarder)
    stdscr.addstr(10, 0, arrange_center + frame_boarder1)
    stdscr.addstr(11, 0, arrange_center + frame_boarder)
    stdscr.addstr(12, 0, arrange_center + arrange_center1 + board[2][0] + third_row_display[0] + board[2][1] + third_row_display[1] + board[2][2] + third_row_display[2] + board[2][3] + third_row_display[3])
    stdscr.addstr(13, 0, arrange_center + frame_boarder)
    stdscr.addstr(14, 0, arrange_center + frame_boarder1)
    stdscr.addstr(15, 0, arrange_center + frame_boarder)
    stdscr.addstr(16, 0, arrange_center + arrange_center1 + board[3][0] + fourth_row_display[0] + board[3][1] + fourth_row_display[1] + board[3][2] + fourth_row_display[2] + board[3][3] + fourth_row_display[3])
    stdscr.addstr(17, 0, arrange_center + frame_boarder)
    stdscr.addstr(18, 0, arrange_center + frame_bottom)