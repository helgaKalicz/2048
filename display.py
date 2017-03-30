def display_table(list_a):
    one_digit = '   │  '
    two_digits = '  │  '
    three_digits = ' │  '
    four_digits = '│  '
    partBetween = []
    for i in range(len(list_a)):
        if len(list_a[i]) == 1:
            partBetween.append(one_digit)
        elif len(list_a[i]) == 2:
            partBetween.append(two_digits)
        elif len(list_a[i]) == 3:
            partBetween.append(three_digits)
        elif len(list_a[i]) == 4:
            partBetween.append(four_digits)
    return partBetween
