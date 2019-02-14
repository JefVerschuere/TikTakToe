def hasSomeoneWon(board):
	for a in board:
		if a[0] == "X" and a[1] == "X" and a[2] == "X" and a[3] == "X":
			print("X has won!!!")
			return True
		if a[1] == "X" and a[2] == "X" and a[3] == "X" and a[4] == "X":
			print("X has won!!!")
			return True
		if a[2] == "X" and a[3] == "X" and a[4] == "X" and a[5] == "X":
			print("X has won!!!")
			return True
		if a[3] == "X" and a[4] == "X" and a[5] == "X" and a[6] == "X":
			print("X has won!!!")
			return True
		if a[0] == "O" and a[1] == "O" and a[2] == "O" and a[3] == "O":
			print("O has won!!!")
			return True
		if a[1] == "O" and a[2] == "O" and a[3] == "O" and a[4] == "O":
			print("O has won!!!")
			return True
		if a[2] == "O" and a[3] == "O" and a[4] == "O" and a[5] == "O":
			print("O has won!!!")
			return True
		if a[3] == "O" and a[4] == "O" and a[5] == "O" and a[6] == "O":
			print("O has won!!!")
			return True
