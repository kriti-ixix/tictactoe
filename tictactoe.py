#Importing libraries
import os 

#Setting up game

print("Welcome to tic tac toe")

#Creating dictionary to store the moves
theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' ',}


#Defining Functions

#Function to clear the terminal screen
def clear_screen():
    if os.name == 'posix':
	#For UNIX Systems
        _ = os.system('clear')
    else:
	#For Windows
        _ = os.system('cls')

#Function to print out the board
#Parameters -> dictionary board
#No return
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

#Function to start the game
#No parameters or return
def playGame():

    #Taking player names:
    xPlayer = input("Enter first player X's name: ") 
    oPlayer = input("Enter second player O's name: ")

    turn = 'X'
    currentPlayer = xPlayer
    #Counting number of turns
    count = 0

    for num in range(10):
        print("")
        printBoard(theBoard)
        #Comes out of loop if all the nine places are filled
        if count == 9:
            break;
        
        #Take user from input in the form of integer 
        move = input("\n{} {}'s turn. Move to which place? ".format(currentPlayer, turn))

        #If the place is empty
        if theBoard[move] == ' ':
            theBoard[move] = turn
            #Checking if the current player won
            winner = checkWin(turn, currentPlayer)

            #If a winner is returned 
            if winner != "":
                print("")
                printBoard(theBoard);
                print("\nWinner is {}!".format(winner))
                break;
            else:
                count += 1
                #Changing user turn
                if turn=="X":
                    turn = "O"
                    currentPlayer = oPlayer
                else:
                    turn = "X"
                    currentPlayer = xPlayer

        #If the place is already filled    
        else:
            print("That place is filled. Choose another one.")
            continue
        
    print("\nGame Over!")


def checkWin(turn, currentPlayer):
    winner = "";
    #Checking rows
    if (theBoard['7'] == theBoard['8'] == theBoard['9'] == turn) or (theBoard['4'] == theBoard['5'] == theBoard['6'] == turn) or (theBoard['1'] == theBoard['2'] == theBoard['3'] == turn):
        winner = currentPlayer;

    #Checking all columns
    elif (theBoard['7'] == theBoard['4'] == theBoard['1'] == turn) or (theBoard['8'] == theBoard['5'] == theBoard['2'] == turn) or (theBoard['9'] == theBoard['6'] == theBoard['3'] == turn):
        winner = currentPlayer;
    
    #Checking diagonal
    elif (theBoard['7'] == theBoard['5'] == theBoard['3'] == turn) or (theBoard['9'] == theBoard['5'] == theBoard['1'] == turn):
        winner = currentPlayer;
    
    #No win
    else:
        winner = ""
    
    return winner


def restartGame():
    restart = input("Play again? (y/n) ")
    if restart == "y":
        for values in theBoard:
            theBoard[values] = ' '
        clear_screen()
        print("\nRestarting the game:\n")
        main()
    else:
        print("Thank you for playing!")


#Main function of the game
def main():
    playGame()
    restartGame()

if __name__ == '__main__':
    main()
