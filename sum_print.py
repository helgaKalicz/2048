# Colors:
C0 = '\033[0m'		# Reset colour
C1 = '\033[08m'		# Invisible
C2 = '\033[92m'		# Green
C3 = '\033[91m'		# Red
C4 = '\033[96m'		# LightBlue
C5 = '\033[34m'		# Blue
C6 = '\033[35m'		# Purple


def printer(first_row_list, second_row_list, third_row_list, fourth_row_list, first_row_display, second_row_display, third_row_display, fourth_row_display, label):
    arrange_center = ' '*37
    frame_top = '┌──────┬──────┬──────┬──────┐'
    frame_boarder = '│      │      │      │      │'
    arrange_center1 = '│  '
    frame_boarder1 = '├──────┼──────┼──────┼──────┤'
    frame_bottom = '└──────┴──────┴──────┴──────┘'
    print(C2 + "Score:" + C4 + " " + str(label) + C0)
    print()
    print(C3 + arrange_center + frame_top + C0)
    print(C3 + arrange_center + frame_boarder + C0)
    print(C3 + arrange_center + arrange_center1 + C0 + first_row_list[0] + C3 + first_row_display[0] + C0 + first_row_list[1] + C3 + first_row_display[1] + C0 + first_row_list[2] + C3 + first_row_display[2] + C0 +  first_row_list[3] + C3 + first_row_display[3] + C0)
    print(C3 + arrange_center + frame_boarder + C0)
    print(C3 + arrange_center + frame_boarder1 + C0)
    print(C3 + arrange_center + frame_boarder + C0)
    print(C3 + arrange_center + arrange_center1 + C0 + second_row_list[0] + C3 + second_row_display[0] + C0 + second_row_list[1] + C3 + second_row_display[1] + C0 + second_row_list[2] + C3 + second_row_display[2] + C0 + second_row_list[3] + C3 + second_row_display[3] + C0)
    print(C3 + arrange_center + frame_boarder + C0)
    print(C3 + arrange_center + frame_boarder1 + C0)
    print(C3 + arrange_center + frame_boarder + C0)
    print(C3 + arrange_center + arrange_center1 + C0 + third_row_list[0] + C3 + third_row_display[0] + C0 + third_row_list[1] + C3 + third_row_display[1] + C0 + third_row_list[2] + C3 + third_row_display[2] + C0 + third_row_list[3] + C3 + third_row_display[3] + C0)
    print(C3 + arrange_center + frame_boarder + C0)
    print(C3 + arrange_center + frame_boarder1 + C0)
    print(C3 + arrange_center + frame_boarder + C0)
    print(C3 + arrange_center + arrange_center1 + C0 + fourth_row_list[0] + C3 + fourth_row_display[0] + C0 + fourth_row_list[1] + C3 + fourth_row_display[1] + C0 + fourth_row_list[2] + C3 + fourth_row_display[2] + C0 + fourth_row_list[3] + C3 + fourth_row_display[3] + C0)
    print(C3 + arrange_center + frame_boarder + C0)
    print(C3 + arrange_center + frame_bottom + C0)
    print()