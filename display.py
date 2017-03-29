def display_table():	
    
    # Handling several digit numbers
	one_digit = '   │  '
	two_digits = '  │  '
	three_digits = ' │  '
	four_digits = '│  '
	partBetween = []

	for i in range(len(a)):
		if len(a[i]) == 1:
			partBetween.append(one_digit)
		elif len(a[i]) == 2:
			partBetween.append(two_digits)
		elif len(a[i]) == 3:
			partBetween.append(three_digits)
		elif len(a[i]) == 4:
			partBetween.append(four_digits)
	
	for i in range(len(b)):
		if len(b[i]) == 1:
			partBetween.append(one_digit)
		elif len(b[i]) == 2:
			partBetween.append(two_digits)
		elif len(b[i]) == 3:
			partBetween.append(three_digits)
		elif len(b[i]) == 4:
			partBetween.append(four_digits)

	for i in range(len(c)):
		if len(c[i]) == 1:
			partBetween.append(one_digit)
		elif len(c[i]) == 2:
			partBetween.append(two_digits)
		elif len(c[i]) == 3:
			partBetween.append(three_digits)
		elif len(c[i]) == 4:
			partBetween.append(four_digits)
	
	for i in range(len(d)):
		if len(d[i]) == 1:
			partBetween.append(one_digit)
		elif len(d[i]) == 2:
			partBetween.append(two_digits)
		elif len(d[i]) == 3:
			partBetween.append(three_digits)
		elif len(d[i]) == 4:
			partBetween.append(four_digits)

    return partBetween

print(display_table())