# Brandon Willett
    
def Col(Col1,Col2,Col3,COl4):
    Col1={1 and 5 and 9 and 13}
    Col2={2 and 6 and 10 and 14}
    Col3={3 and 7 and 11 and 15}
    Col4={4 and 8 and 12 and 16}

def printBoard(board):
    print('|' + str(1) + '|' + str(2) + '|' + str(3) + '|' + str(4) + '|')
    print('---------')
    print('|' + board[1] + '|' + board[2] + '|' + board[3] + '|' + board[4] + '|')
    print('---------')
    print('|' + board[5] + '|' + board[6] + '|' + board[7] + '|' + board[8] + '|')
    print('---------')
    print('|' + board[9] + '|' + board[10] + '|' + board[11] + '|' + board[12] + '|')
    print('---------')
    print('|' + board[13] + '|' + board[14] + '|' + board[15] + '|' + board[16] + '|')
    print('---------')

def checkWinner(board, player):
    print('Checking if ' + player + ' is a winner...')
    
    # Code for checking if either the player R or Y has won.
    return ((board[1] == player and board[2] == player and board[3] == player and board[4] == player) or # Winner opt across row 1
    (board[5] == player and board[6] == player and board[7] == player and board[8] == player) or         # Winner opt across row 2
    (board[9] == player and board[10] == player and board[11] == player and board[12] == player) or         # Winner opt across row 3
    (board[13] == player and board[14] == player and board[15] == player and board[16] == player) or         # Winner opt across row 4
    (board[1] == player and board[5] == player and board[9] == player and board[13] == player) or         # Winner opt down column 1
    (board[2] == player and board[2] == player and board[6] == player and board[14] == player) or         # Winner opt down column 2
    (board[3] == player and board[7] == player and board[11] == player and board[15] == player) or         # Winner opt down column 3
    (board[4] == player and board[8] == player and board[12] == player and board[16] == player) or         # Winner opt down column 4
    (board[1] == player and board[6] == player and board[11] == player and board[16] == player) or         # Winner opt for diagonal
    (board[4] == player and board[7] == player and board[10] == player and board[13] == player))           # Winner opt for other diagonal

def startGame(board, Col)
    
    

def startGame(startingPlayer, board):
    turn = startingPlayer# This line is taking startingPlayer and storing ii in the value turn.
    for i in range(0,16):# This line is the beginning of the for loop from 0-15, therefore running 16 times.
        printBoard(board)# This line is printing the board after every turn.
        print('Turn for ' + turn + '. pick the column you want to put your piece in?')# This line is asking either player Y or R to take their turn.
        move = int(input())
        board[move] = turn
        if( checkWinner(board, 'R') ):# The lines from 28-30 are checking if the player R has won.
            print('R wins!')
            break
        elif ( checkWinner(board, 'Y') ):# The lines from 31-33 are checking if the player Y has won.
            print('Y wins!')
            break
    
        if turn == 'R':# The line from 35-38 swaps the players from R to Y or Y to R.
            turn = 'Y'
        else:
            turn = 'R'
        
    printBoard(board)# this line prints the TicTac board at the end.

