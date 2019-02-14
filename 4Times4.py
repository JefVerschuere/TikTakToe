import random
import sys
from CheckIfSomeoneWon import *

def createBoard() : 
	board = []
	for a in range (7) : 
		tabCollumn = []
		for b in range(7) : 
			tabCollumn.append(" ")
		board.append(tabCollumn)

	return board


def insertInCollumn(numCollumn, board, car): 
	numCollumn = numCollumn - 1 
	for a in range(7) : 
		if board[numCollumn][a] == " ":
			board[numCollumn][a] = car
			return board

	print("This collumn is full")


def printBoard(board):
	print("  1   2   3   4   5   6   7")
	print("_____________________________")
	print ("|",board[0][6], "|",board[1][6], "|",board[2][6], "|",board[3][6], "|",board[4][6], "|",board[5][6], "|",board[6][6], "|")
	print ("|",board[0][5], "|",board[1][5], "|",board[2][5], "|",board[3][5], "|",board[4][5], "|",board[5][5], "|",board[6][5], "|")
	print ("|",board[0][4], "|",board[1][4], "|",board[2][4], "|",board[3][4], "|",board[4][4], "|",board[5][4], "|",board[6][4], "|")
	print ("|",board[0][3], "|",board[1][3], "|",board[2][3], "|",board[3][3], "|",board[4][3], "|",board[5][3], "|",board[6][3], "|")
	print ("|",board[0][2], "|",board[1][2], "|",board[2][2], "|",board[3][2], "|",board[4][2], "|",board[5][2], "|",board[6][2], "|")
	print ("|",board[0][1], "|",board[1][1], "|",board[2][1], "|",board[3][1], "|",board[4][1], "|",board[5][1], "|",board[6][1], "|")
	print ("|",board[0][0], "|",board[1][0], "|",board[2][0], "|",board[3][0], "|",board[4][0], "|",board[5][0], "|",board[6][0], "|")
	print("-----------------------------")

def isPair(x):
     if x % 2 == 0 :
          return True
     else : 
          return False

StartingPlayer = random.randint(1,100)
if StartingPlayer / 2 == 0:
     firstPlayer = 'O'
     secPlayer = 'X'
else : 
     firstPlayer = 'X'
     secPlayer = 'O'

board = createBoard()
for i in range(49):
	printBoard(board)
	if isPair(i) : 
		print("turn : ", i, " it's ", firstPlayer , "his turn type de collumn")
		r = input()
		board = insertInCollumn(int(r), board, firstPlayer)
		if hasSomeoneWon(board) : 
			printBoard(board)
			break
	else : 
		print("turn : ", i, " it's ", secPlayer , "his turn type de collumn")
		r = input()
		board = insertInCollumn(int(r), board, secPlayer)
		if hasSomeoneWon(board) : 
			printBoard(board)
			break


