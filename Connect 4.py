# Purpose: Connect 4.
# Description: it is a game that when you put 4 x in any shap or 4 o in any shap , you win.
# Author: Esraa Emary Abd Elsalam.
#version: 4.
#*******************************************************************************************************

Player1 = "Player 1" #definition for some variables
Player2 = "Player 2"
check = False
def game():# printing the shape of the game
        for i in row1:
            print(i, " ", end="")
        print()
        for i in row2:
            print(i, " ", end="")
        print()
        for i in row3:
            print(i, " ", end="")
        print()
        for i in row4:
            print(i, " ", end="")
        print()
        for i in row5:
            print(i, " ", end="")
        print()
        for i in row6:
            print(i, " ", end="")
        print()
        for i in row7:
            print(i, " ", end="")
        print()
        for i in row8:
            print(i, " ", end="")
        print()

def validity_column(move,Player, col):#get the column and check the validity of it
    while True:#add the move of the players to the game
        if row6[col] == '*':
            row6[col] = move
            break
        elif row5[col] == '*':
            row5[col] = move
            break
        elif row4[col] == '*':
            row4[col] = move
            break
        elif row3[col] == '*':
            row3[col] = move
            break
        elif row2[col] == '*':
            row2[col] = move
            break
        elif row1[col] == '*':
            row1[col] = move
            break
        else: #check if the column 1 is full and take an available column from the player
            print("It's full!, Please enter an available column!")
            while True:
                try:
                    col = int(input(f"{Player} , enter a column number (1-7): "))
                    break
                except:
                    print("Please enter a valid column!")

            while col < 1 or col > 7:
                print("Please enter a valid column!")
                while True:
                    try:
                        col = int(input(f"{Player} , enter a column number (1-7): "))
                        break
                    except:
                        print("Please enter a valid column!")

def winner(move, Player):#check if any player won
    for i in range(1, 5):#check if player 1 won horizontally
        if (row1[i] == row1[i+1] == row1[i+2] == row1[i+3] == move or
            row2[i] == row2[i + 1] == row2[i + 2] == row2[i + 3] == move or
            row3[i] == row3[i + 1] == row3[i + 2] == row3[i + 3] == move or
            row4[i] == row4[i + 1] == row4[i + 2] == row4[i + 3] == move or
            row5[i] == row5[i + 1] == row5[i + 2] == row5[i + 3] == move or
            row6[i] == row6[i + 1] == row6[i + 2] == row6[i + 3] == move):
            print(f"{Player} is the winner!")
            return True

    for i in range(1, 8):#check if player 1 won vertically
        if (row1[i] == row2[i] == row3[i] == row4[i] == move or
            row2[i] == row3[i] == row4[i] == row5[i] == move or
            row3[i] == row4[i] == row5[i] == row6[i] == move):
            print(f"{Player} is the winner!")
            return True

    for j in range(1, 5):#check if player 1 won diagonally
        if (row6[j] == row5[j + 1] == row4[j + 2] == row3[j + 3] == move or
            row5[j] == row4[j + 1] == row3[j + 2] == row2[j + 3] == move or
            row4[j] == row3[j + 1] == row2[j + 2] == row1[j + 3] == move):
            print(f"{Player} is the winner!")
            return True

    for j in range(1, 5):#check if player 1 won diagonally
        if (row1[j] == row2[j + 1] == row3[j + 2] == row4[j + 3] == move or
            row2[j] == row3[j + 1] == row4[j + 2] == row5[j + 3] == move or
            row3[j] == row4[j + 1] == row5[j + 2] == row6[j + 3] == move):
            print(f"{Player} is the winner!")
            return True
    return False

def draw():#check draw
    count = 0
    for i in range(1, 8):
        if row1[i] != '*' and row2[i] != '*' and row3[i] != '*' and row4[i] != '*' and row5[i] != '*' and row6[i] != '*':
            count += 1
    if count == 7:
        print("DRAW!!\n")
        return True
#===============================================MAIN PROGRAM=======================================================#
print("#==========Welcome to connect 4 Game!==========#")#printing a welcome message and the shape of the game
print("Player 1 (X) and Player 2 (O)")
row1 = ['6|', '*', '*', '*', '*', '*', '*', '*']
row2 = ['5|', '*', '*', '*', '*', '*', '*', '*']
row3 = ['4|', '*', '*', '*', '*', '*', '*', '*']
row4 = ['3|', '*', '*', '*', '*', '*', '*', '*']
row5 = ['2|', '*', '*', '*', '*', '*', '*', '*']
row6 = ['1|', '*', '*', '*', '*', '*', '*', '*']
row7 = ['_|', '_', '_', '_', '_', '_', '_', '_']
row8 = [' |', '1', '2', '3', '4', '5', '6', '7']
game()# printing the shape of the game
while True:
    print()
    while True:#check the input is integer
        try:
            col = int(input("Player1 , enter a column number (1-7): "))
            while col < 1 or col > 7:#check the range of the input column
                print("Please enter a valid column!")
                col = int(input("Player2 , enter a column number (1-7): "))
            break
        except:
            print("Please enter a valid column!")

    validity_column('X', Player1, col)#get the column and check the validity of it

    game()# printing the shape of the game

    if winner('X', Player1):#check if player 1 won
        break

    if draw():#check draw
        break

    print()

    while True:#check the input is integer
        try:
            col = int(input("Player2 , enter a column number (1-7): "))
            while col < 1 or col > 7:#check the range of the input column
                print("Please enter a valid column!")
                col = int(input("Player2 , enter a column number (1-7): "))
            break
        except:
            print("Please enter a valid column!")

    validity_column('O', Player2, col)#get the column and check the validity of it

    game()# printing the matrix of the game

    if winner('O', Player2):#check if player 2 won
        break

    if draw():#check draw
        break
