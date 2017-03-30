def board(board_size):
    big_list = []
    small_list = []
    for i in range(int(board_size) ** 2):
        small_list.append(' ')
    for i in range(int(board_size) ** 2):
        big_list.append(list(small_list))
    return big_list