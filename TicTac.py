import random
import sys

def hasGameEnded(board) :
     #Checks the horizontal lines for X
     if board['top-L'] == 'X' and board['top-M'] == 'X' and board['top-R']  == 'X' :
          print("X was Won!!!!")
          return True
     if board['mid-L'] == 'X' and board['mid-M'] == 'X' and board['mid-R']  == 'X' :
          print("X was Won!!!!") 
          return True
     if board['low-L'] == 'X' and board['low-M'] == 'X' and board['low-R']  == 'X' : 
          print("X was Won!!!!")
          return True
     #Checks the horizontal lines for O
     if board['top-L'] == 'O' and board['top-M'] == 'O' and board['top-R']  == 'O' : 
          print("O was Won!!!!")
          return True
     if board['mid-L'] == 'O' and board['mid-M'] == 'O' and board['mid-R']  == 'O' : 
          print("O was Won!!!!")
          return True
     if board['low-L'] == 'O' and board['low-M'] == 'O' and board['low-R']  == 'O' : 
          print("O was Won!!!!")
          return True
     #Checks the vertical lines for X
     if board['top-L'] == 'X' and board['mid-L'] == 'X' and board['low-L']  == 'X' : 
          print("X was Won!!!!")
          return True
     if board['top-M'] == 'X' and board['mid-M'] == 'X' and board['low-M']  == 'X' : 
          print("X was Won!!!!")
          return True
     if board['top-R'] == 'X' and board['mid-R'] == 'X' and board['low-R']  == 'X' : 
          print("X was Won!!!!")
          return True
     #Checks the vertical lines for O
     if board['top-L'] == 'O' and board['mid-L'] == 'O' and board['low-L']  == 'O' : 
          print("O was Won!!!!")
          return True
     if board['top-M'] == 'O' and board['mid-M'] == 'O' and board['low-M']  == 'O' : 
          print("O was Won!!!!")
          return True
     if board['top-R'] == 'O' and board['mid-R'] == 'O' and board['low-R']  == 'O' : 
          print("O was Won!!!!")
          return True
     #Checks diagonals for X
     if board['top-L'] == 'X' and board['mid-M'] == 'X' and board['low-R']  == 'X' : 
          print("X was Won!!!!")
          return True
     if board['top-R'] == 'X' and board['mid-M'] == 'X' and board['low-L']  == 'X' : 
          print("X was Won!!!!")
          return True
     #Checks diagonals for O
     if board['top-L'] == 'O' and board['mid-M'] == 'O' and board['low-R']  == 'O' : 
          print("O was Won!!!!")
          return True
     if board['top-R'] == 'O' and board['mid-M'] == 'O' and board['low-L']  == 'O' : 
          print("O was Won!!!!")
          return True
     return False

def isPair(x):
     if x % 2 == 0 :
          return True
     else : 
          return False

def printBoard(board):
     print('*------------------------------*')
     print('               ' + board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
     print('               ' + '-+-+-')
     print('               ' + board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
     print('               ' + '-+-+-')
     print('               ' + board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
     print('*------------------------------*')

def printExBoard(board):
     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
     print('-----+-----+------')
     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
     print('-----+-----+------')
     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

ExBoard = theBoard = {'top-L': 'top-L', 'top-M': 'top-M', 'top-R': 'top-R',
 'mid-L': 'mid-L', 'mid-M': 'mid-M', 'mid-R': 'mid-R',
 'low-L': 'low-L', 'low-M': 'low-M', 'low-R': 'low-R'}

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

StartingPlayer = random.randint(1,100)
if StartingPlayer / 2 == 0:
     firstPlayer = 'O'
     secPlayer = 'X'
else : 
     firstPlayer = 'X'
     secPlayer = 'O'

print('this is how you will select your case')
print()
printExBoard(ExBoard)
print()
print('start of the game')
i = 0
while i < 9 : 
     printBoard(theBoard)
     print()
     if isPair(i) : 
          print('Turn ' + str(i) + ': it is ' + firstPlayer + ' his turn')
          print(firstPlayer + ' where do you want to place your token?')
          r = input()
          if r in theBoard and theBoard[r] == ' ': 
               theBoard[r] = firstPlayer
               i = i +1
               if hasGameEnded(theBoard) : 
                    printBoard(theBoard)
                    break
          else : 
               print('this is an invalid key please try again the keys are : ')
               printExBoard(ExBoard)
               print()
               print()

               
               
     else : 
          print('Turn ' + str(i) + ': it is ' + secPlayer + ' his turn')
          print(secPlayer + ' where do you want to place your token?')
          r = input()
          if r in theBoard and theBoard[r] == ' ': 
               theBoard[r] = secPlayer
               i = i +1
               if hasGameEnded(theBoard) : 
                    printBoard(theBoard)


          else : 
               print('this is an invalid key please try again the keys are : ')
               printExBoard(ExBoard)
               print()
               print()

if i == 9 :
	print('no one has won :(')