#Name: Nana Kwasi Owusu
#Date: 24th February, 2023
#Program Description: A single player board placement game that the user wins by placing numbers on the board with different distances between them.

#Importing this module exits the program when the user does not select unique positions
import sys

#Importing this module allows me to use the square root function
import math

#This function takes in a question, and the allowed limits for the size of the board. It repeatedly asks the question until the user enters a numeric value within the range
def getInteger(question, a, b):
    while(True):
        answer = input(question)
        if answer.isdigit():
            number = int(answer)
            if a <= number <= b:
                return number
            else:
                print('Number outside of range')
                return getInteger(question,a,b)
        else:
            print('You did not enter a number.')
            return getInteger(question,a,b)
 
 #This function takes an integer value and prints the board with values 0 to the inputted integer value squared minus 1           
def printOptions(n):
    for i in range(n):
        for j in range(n):
            val = i * n + j
            print(f"{val:2}", end=" ")
        print()

#This function takes three integers and computes the distance between them
def distance(i, j, n):
    x1 = i % n
    y1 = i // n
    x2 = j % n
    y2 = j // n
    distanceBetweenValues = math.sqrt(((x2 - x1)**2)+((y2 - y1)**2))
    return distanceBetweenValues

#This function takes a board stored as a list of 0s and 1s as well as the size of the board. It then checks the distance between the position of the 1s on the board, returning true if all the distances are different. If this condition is not met. It returns a false value.
def checkBoard(board, n):
    distances = []
    
    for i in range(n**2):
        if board[i] == 1:
            for j in range(i+1,n**2):
                if board[j] == 1:
                    dist = distance(i, j, n)
                    print(f"The distance from {i} to {j} is {dist:.3f}")
                    for d in distances:
                        if abs(d-dist) < 0.0001:
                            return False
                    distances.append(dist)
    return True

#This function prints the board containing 0s and 1s.
def printBoard(board, boardSize):
    for i in range(boardSize**2):
        val = board[i]
        print(f"{val:2}", end=" ")
        if ((i+1) % boardSize == 0 ):
            print()

#This is the main part of the program 
if __name__ == "__main__":
    lowerBoardSize = 3
    upperBoardSize = 7
    print('Welcome to Placement Game')
    
    boardSize = getInteger('Enter Size of Board (between 3 and 7):',lowerBoardSize,upperBoardSize)
    
    print(f'Rules:')
    print(f"You must pick {boardSize} spaces on the board to place ones.")
    print(f'The distances between all the ones you placed must be different.')
    print(f"The possible spaces are shown below.")
    
    printOptions(boardSize)
    print(f"Pick {boardSize} spaces")
    
    board = [0] * (boardSize**2)
   
    positions = []
    alreadySelected = 0
    for i in range (boardSize):
        selectedPosition = getInteger(f"Pick Space (0 - {(boardSize**2)-1}): ",0,(boardSize**2)-1)
        if selectedPosition in positions:
            alreadySelected = 1
        board[selectedPosition] = 1
        positions.append(selectedPosition)
        
    if alreadySelected == 1:
        print('You did not pick unique sequence.')
        sys.exit()

    print('Your board is shown below')
    printBoard(board, boardSize)
    
    print('We will check the distance between all selections')
    checkBoardValue = checkBoard(board, boardSize)
    if (checkBoardValue == True):
        print("You Win: Your Board Passes the Test")
    else:
        print("You Lose: Your board contained multiple placements with the same distance")
        