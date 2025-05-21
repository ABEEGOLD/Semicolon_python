for side_A  in range(0,19):
	for side_B in range(side_A, 19):
		for side_C in range(side_B, 19):
			if ((side_A * side_A) + (side_B * side_B) == (side_C * side_C)):
				print(side_A,side_B,side_C)
