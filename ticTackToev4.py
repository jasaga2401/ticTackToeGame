# [your name]
# T Level Year one
# 15/10/2025
# Tic Tack Toe

import random

# checks to see if either the player or computer has won
def gameStatus(grid):
    # horizonal
    if ((grid[0][0]=='O' and grid[0][1]=='O' and grid[0][2]=='O') or \
        (grid[1][0]=='O' and grid[1][1]=='O' and grid[1][2]=='O') or \
        (grid[2][0]=='O' and grid[2][1]=='O' and grid[2][2]=='O') or \
        # vertical
        (grid[0][0]=='O' and grid[1][0]=='O' and grid[2][0]=='O') or \
        (grid[0][1]=='O' and grid[1][1]=='O' and grid[2][1]=='O') or \
        (grid[0][2]=='O' and grid[1][2]=='O' and grid[2][2]=='O') or \
        # diagonal
        (grid[0][0]=='O' and grid[1][1]=='O' and grid[2][2]=='O') or \
        (grid[0][2]=='O' and grid[1][1]=='O' and grid[2][0]=='O')):
        return 'playerWon'
    elif ((grid[0][0]=='X' and grid[0][1]=='X' and grid[0][2]=='X') or \
        (grid[1][0]=='X' and grid[1][1]=='X' and grid[1][2]=='X') or \
        (grid[2][0]=='X' and grid[2][1]=='X' and grid[2][2]=='X') or \
        # vertical
        (grid[0][0]=='X' and grid[1][0]=='X' and grid[2][0]=='X') or \
        (grid[0][1]=='X' and grid[1][1]=='X' and grid[2][1]=='X') or \
        (grid[0][2]=='X' and grid[1][2]=='X' and grid[2][2]=='X') or \
        # diagonal
        (grid[0][0]=='X' and grid[1][1]=='X' and grid[2][2]=='X') or \
        (grid[0][2]=='X' and grid[1][1]=='X' and grid[2][0]=='X')):
        return 'computerWon'
    elif not any("-" in row for row in grid):
        return 'draw'
    else:
        return 'noWin'

# Outputs either a win, draw or the game continues        
def outputGameStatus(winLossDrawCont):
    if (winLossDrawCont == 'playerWon'):
        print("\nPlayer has won the game!")
        return True
    elif (winLossDrawCont == 'computerWon'):
        print("\nComputer has won the game!")
        return True
    elif (winLossDrawCont == 'draw'):
        print("\nThe game is a draw")
        return True
    elif (winLossDrawCont == 'noWin'):
        return False

# checks the move to make sure it is valid
def checkMove(row, col, grid, gameTurn):
    print('')
    if (gameTurn == 'player'):
        if (grid[row][col] == '-'):
            grid[row][col] = 'O'            
            outputGrid(grid)
            return True
        else:
            print('Illegal move. go again ..')
            return False
        
    elif (gameTurn == 'comp'):
        if (grid[row][col] == '-'):
            grid[row][col] = 'X'            
            outputGrid(grid)
            return True
        else:
            print('Illegal move. go again ..')
            return False

# input from the computer     
def inputComp():
    print("\nThe computer's turn")
    row = random.randrange(0, 3)
    col = random.randrange(0, 3)
    return row, col

# input from the player 
def inputPlayer():
    print("\nThe player's turn")
    row = int(input('Input the row for your go: '))
    col = int(input('Input the column for your go: '))
    return row, col

# who has first go
def firstGo():
    outcome = random.randrange(1, 3)
    if (outcome == 1):
        return 'player'
    else:
        return 'comp'
    
# outputs the grid
def outputGrid(grid):    
    for i in range(3):
        print('')
        for j in range(3):
            print(grid[i][j], end=' ')

# generates the 3x3 grid
def createGrid():
    print('Here is the grid')
    grid = [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]
            ]
    return grid

# the main program loop
def main():    
    gameOver = False
    
    grid = createGrid()
    outputGrid(grid)
    gameTurn = firstGo()

    # gaming loop
    while (gameOver == False):

        move = False
         
        while (move == False):
            if (gameTurn == 'player'):                
                row, col = inputPlayer()
                state = checkMove(row, col, grid, gameTurn)
                if (state):
                    move = True
                    gameTurn = 'comp'
                else:   
                    move = False
                    gameTurn = 'player'
                    
            elif (gameTurn == 'comp'):                
                row, col = inputComp()
                state = checkMove(row, col, grid, gameTurn)
                if (state):
                    move = True
                    gameTurn = 'player'
                else:   
                    move = False
                    gameTurn = 'comp'

        winLossDrawCont = gameStatus(grid)
        gameOver = outputGameStatus(winLossDrawCont)        
        
# program starts here
if (__name__ == "__main__"):

    main()
    
