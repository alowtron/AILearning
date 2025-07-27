import random
import json
import copy



learnSpeed = 1

userPlay = 1
train = 0
continueTrain = False
chanceToRandomMove = 5

if train:
    numOfGames = 10
    trainingIterations = 100
else:
    numOfGames = 1
    trainingIterations = 1

createNewJson = train



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

def saveGameMoves(row, spot):
    boardHistory.append(copy.deepcopy(board))
    move = 0
    if row == 0:
        if spot == 0:
            move = 1
        elif spot == 1:
            move = 2
        else:
            move = 3
    elif row == 1:
        if spot == 0:
            move = 4
        elif spot == 1:
            move = 5
        else:
            move = 6
    else:
        if spot == 0:
            move = 7
        elif spot == 1:
            move = 8
        else:
            move = 9
    moveHistory.append(copy.deepcopy(move))

def changeWeights(team):
    #team== winning team
    
    
    for r, round in enumerate(boardHistory):
        #round = boardHistory[len(boardHistory)-1]
        if r % 2 != 0:
            if team == "X" or team == "draw":
                multiplier = 1
            else:
                multiplier = -1 / 4
            for i, row in enumerate(round):
                for j, spot in enumerate(row):
                    if spot == "X":
                        spotType = 2
                    elif spot == "O":
                        spotType = 1
                    else:
                        spotType = 0
                    moveSpot = moveHistory[r]
                    if i == 0 and j == 0:
                        jsonX[str(moveSpot)]["1"][str(spotType)] += learnSpeed * multiplier
                    elif i == 0 and j == 1:
                        jsonX[str(moveSpot)]["2"][str(spotType)] += learnSpeed * multiplier
                    elif i == 0 and j == 2:
                        jsonX[str(moveSpot)]["3"][str(spotType)] += learnSpeed * multiplier
                    elif i == 1 and j == 0:
                        jsonX[str(moveSpot)]["4"][str(spotType)] += learnSpeed * multiplier
                    elif i == 1 and j == 1:
                        jsonX[str(moveSpot)]["5"][str(spotType)] += learnSpeed * multiplier
                    elif i == 1 and j == 2:
                        jsonX[str(moveSpot)]["6"][str(spotType)] += learnSpeed * multiplier
                    elif i == 2 and j == 0:
                        jsonX[str(moveSpot)]["7"][str(spotType)] += learnSpeed * multiplier
                    elif i == 2 and j == 1:
                        jsonX[str(moveSpot)]["8"][str(spotType)] += learnSpeed * multiplier
                    elif i == 2 and j == 2:
                        jsonX[str(moveSpot)]["9"][str(spotType)] += learnSpeed * multiplier
        else:
            if team == "O" or team == "draw":
                multiplier = 1
            else:
                multiplier = -1 / 4
            for i, row in enumerate(round):
                for j, spot in enumerate(row):
                    if spot == "X":
                        spotType = 2
                    elif spot == "O":
                        spotType = 1
                    else:
                        spotType = 0
                    moveSpot = moveHistory[r]
                    if i == 0 and j == 0:
                        jsonO[str(moveSpot)]["1"][str(spotType)] += learnSpeed * multiplier
                    elif i == 0 and j == 1:
                        jsonO[str(moveSpot)]["2"][str(spotType)] += learnSpeed * multiplier
                    elif i == 0 and j == 2:
                        jsonO[str(moveSpot)]["3"][str(spotType)] += learnSpeed * multiplier
                    elif i == 1 and j == 0:
                        jsonO[str(moveSpot)]["4"][str(spotType)] += learnSpeed * multiplier
                    elif i == 1 and j == 1:
                        jsonO[str(moveSpot)]["5"][str(spotType)] += learnSpeed * multiplier
                    elif i == 1 and j == 2:
                        jsonO[str(moveSpot)]["6"][str(spotType)] += learnSpeed * multiplier
                    elif i == 2 and j == 0:
                        jsonO[str(moveSpot)]["7"][str(spotType)] += learnSpeed * multiplier
                    elif i == 2 and j == 1:
                        jsonO[str(moveSpot)]["8"][str(spotType)] += learnSpeed * multiplier
                    elif i == 2 and j == 2:
                        jsonO[str(moveSpot)]["9"][str(spotType)] += learnSpeed * multiplier
    with open("jsonO.json", "w") as json_file:
        json.dump(jsonO, json_file)
    with open("jsonX.json", "w") as json_file:
        json.dump(jsonX, json_file)


def findBestMove(team):
    moveValues = []

    for move in availableMovesList:
        moveSpot = 0
        moveValue = 0
        if move == [0, 0]:
            moveSpot = 1
        elif move == [0, 1]:
            moveSpot = 2
        elif move == [0, 2]:
            moveSpot = 3
        elif move == [1, 0]:
            moveSpot = 4
        elif move == [1, 1]:
            moveSpot = 5
        elif move == [1, 2]:
            moveSpot = 6
        elif move == [2, 0]:
            moveSpot = 7
        elif move == [2, 1]:
            moveSpot = 8
        else:
            moveSpot = 9
        if team == "X":
            # jsonX
            for i, row in enumerate(board):
                for j, spot in enumerate(row):
                    if spot == 0:
                        spotValue = 0
                    elif spot == "O":
                        spotValue = 1
                    else:
                        spotValue = 2
                    moveValue += jsonX[str(moveSpot)][str((i*3) + (j+1))][str(spotValue)]

        else:
            # jsonO
            for i, row in enumerate(board):
                for j, spot in enumerate(row):
                    if spot == 0:
                        spotValue = 0
                    elif spot == "O":
                        spotValue = 1
                    else:
                        spotValue = 2
                    moveValue += jsonO[str(moveSpot)][str((i*3) + (j+1))][str(spotValue)]
        moveValues.append(moveValue)
    highestNumber = max(moveValues)
    return moveValues.index(highestNumber)
            

    
    
for j in range(trainingIterations):
    if j > 1:
        continueTrain = True
    if createNewJson and not continueTrain:

        jsonStructure = {
        "1": {
            "1": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "2": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "3": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "4": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "5": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "6": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "7": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "8": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "9": {
            "0": 0,
            "1": 0,
            "2": 0
            }
        },
        "2": {
            "1": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "2": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "3": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "4": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "5": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "6": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "7": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "8": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "9": {
            "0": 0,
            "1": 0,
            "2": 0
            }
        },
        "3": {
            "1": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "2": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "3": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "4": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "5": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "6": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "7": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "8": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "9": {
            "0": 0,
            "1": 0,
            "2": 0
            }
        },
        "4": {
            "1": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "2": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "3": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "4": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "5": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "6": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "7": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "8": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "9": {
            "0": 0,
            "1": 0,
            "2": 0
            }
        },
        "5": {
            "1": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "2": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "3": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "4": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "5": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "6": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "7": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "8": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "9": {
            "0": 0,
            "1": 0,
            "2": 0
            }
        },
        "6": {
            "1": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "2": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "3": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "4": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "5": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "6": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "7": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "8": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "9": {
            "0": 0,
            "1": 0,
            "2": 0
            }
        },
        "7": {
            "1": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "2": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "3": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "4": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "5": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "6": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "7": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "8": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "9": {
            "0": 0,
            "1": 0,
            "2": 0
            }
        },
        "8": {
            "1": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "2": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "3": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "4": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "5": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "6": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "7": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "8": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "9": {
            "0": 0,
            "1": 0,
            "2": 0
            }
        },
        "9": {
            "1": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "2": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "3": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "4": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "5": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "6": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "7": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "8": {
            "0": 0,
            "1": 0,
            "2": 0
            },
            "9": {
            "0": 0,
            "1": 0,
            "2": 0
            }
        }
        }

        jsonO = jsonStructure
        jsonX = jsonStructure
    else:
        with open("jsonO.json", "r") as json_file:
            jsonO = json.load(json_file)

        with open("jsonX.json", "r") as json_file:
            jsonX = json.load(json_file)
        if j > 0:
            continueTrain = True
    for i in range(numOfGames):
        board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
        ]

        boardHistory = []
        moveHistory = []
        gameOver = False
 
        while not gameOver:
            availableMovesList = availableMoves()
            if availableMovesList == []:
                gameOver = True
                print("It is a tie!")
            if userPlay:
                row = int(input("input your answer for the row you want to play"))
                column = int(input("input your answer for the column you want to play"))
                playMove("O", row, column)
                printBoard()
            if availableMovesList != [] and not userPlay:
                team = "O"
                if continueTrain:
                    if random.randint(1, 100) < chanceToRandomMove:
                        moveToPlay = availableMovesList[random.randint(0, len(availableMovesList) - 1)]
                    else:
                        moveToPlay = availableMovesList[findBestMove(team)]
                elif train:
                    moveToPlay = availableMovesList[random.randint(0, len(availableMovesList) - 1)]
                else:
                    moveToPlay = availableMovesList[findBestMove(team)]
                playMove(team, moveToPlay[0], moveToPlay[1])
                gameOver = checkForWin(team)
                if gameOver:
                    print(f"{team} wins!")
                    if train:
                        changeWeights(team)
                if not train:
                    printBoard()
                saveGameMoves(moveToPlay[0], moveToPlay[1])
            availableMovesList = availableMoves()
            if availableMovesList != [] and not gameOver:
                team = "X"
                if continueTrain:
                    if random.randint(1, 100) < chanceToRandomMove:
                        moveToPlay = availableMovesList[random.randint(0, len(availableMovesList) - 1)]
                    else:
                        moveToPlay = availableMovesList[findBestMove(team)]
                elif train:
                    moveToPlay = availableMovesList[random.randint(0, len(availableMovesList) - 1)]
                else:
                    moveToPlay = availableMovesList[findBestMove(team)]
                playMove(team, moveToPlay[0], moveToPlay[1])
                gameOver = checkForWin(team)
                if gameOver:
                    print(f"{team} wins!")
                    if train:
                        changeWeights(team)
                if not train:
                    printBoard()
                saveGameMoves(moveToPlay[0], moveToPlay[1])
            # if availableMovesList == [] and not gameOver:
            #     learnSpeed = learnSpeed / 2
            #     changeWeights('draw')
            #     learnSpeed = learnSpeed * 2

            # if gameOver == True:
            #     print("board history")

            #     for i, move in enumerate(boardHistory):
            #         print(moveHistory[i])
            #         for row in move:
            #             print(row)
                        
            #         print("---")
                
            i += 1
            if i >= 100:
                gameOver = True
