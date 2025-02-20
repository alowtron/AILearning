import random
board = [
[0, 0, 0],
[0, 0, 0],
[0, 0, 0]
]



def printBoard():
    for i in board:
        print(i)
    print("---")

def availableMoves():
    possibleMoves = []
    for i, row in enumerate(board):
        for j, spot in enumerate(row):
            if spot == 0:
                possibleMoves.append([i, j])
    return possibleMoves

def playMove(team, row, spot):
    if team == 'X':
        board[row][spot] = "X"
    else:
        board[row][spot] = "O"

def checkForWin(team):
    if board[0][0] == team and board[0][1] == team and board[0][2] == team:
        return True
    elif board[1][0] == team and board[1][1] == team and board[1][2] == team:
        return True
    elif board[2][0] == team and board[2][1] == team and board[2][2] == team:
        return True
    elif board[0][0] == team and board[1][0] == team and board[2][0] == team:
        return True
    elif board[0][1] == team and board[1][1] == team and board[2][1] == team:
        return True
    elif board[0][2] == team and board[1][2] == team and board[2][2] == team:
        return True
    elif board[0][0] == team and board[1][1] == team and board[2][2] == team:
        return True
    elif board[0][2] == team and board[1][1] == team and board[2][0] == team:
        return True
    else:
        return False

gameOver = False
i = 1
while not gameOver:
    availableMovesList = availableMoves()
    if availableMovesList == []:
        gameOver = True
        print("It is a tie!")
    
    if availableMovesList != []:
        team = "O"
        moveToPlay = availableMovesList[random.randint(0, len(availableMovesList) - 1)]
        playMove(team, moveToPlay[0], moveToPlay[1])
        gameOver = checkForWin(team)
        if gameOver:
            print(f"{team} wins!")
        printBoard()
    availableMovesList = availableMoves()
    if availableMovesList != []:
        team = "X"
        moveToPlay = availableMovesList[random.randint(0, len(availableMovesList) - 1)]
        playMove(team, moveToPlay[0], moveToPlay[1])
        gameOver = checkForWin(team)
        if gameOver:
            print(f"{team} wins!")
        printBoard()
    
    i += 1
    if i >= 100:
        gameOver = True
