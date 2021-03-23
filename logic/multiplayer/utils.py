import glob
from datetime import datetime
from datetime import date
import os
import pygame

from utils.game import Chess
from utils.constants import SQUARE_SIZE, BLUE
from logic.multiplayer.logics import pieceType, availableMoves, takenPos, moveTest, makeMove
from utils.constants import checkPos

today = date.today()
LETTER = ["", "a", "b", "c", "d", "e", "f", "g", "h"]

def convertMoves(moves):
    side = 0
    board = (
        [
            [1, 7, "p"], [2, 7, "p"], [3, 7, "p"], [4, 7, "p"], [5, 7, "p"], [6, 7, "p"], [7, 7, "p"], [8, 7, "p"],
            [1, 8, "r"], [2, 8, "n"], [3, 8, "b"], [4, 8, "q"], [5, 8, "k"], [6, 8, "b"], [7, 8, "n"], [8, 8, "r"],
        ],
        [
            [1, 2, "p"], [2, 2, "p"], [3, 2, "p"], [4, 2, "p"], [5, 2, "p"], [6, 2, "p"], [7, 2, "p"], [8, 2, "p"],
            [1, 1, "r"], [2, 1, "n"], [3, 1, "b"], [4, 1, "q"], [5, 1, "k"], [6, 1, "b"], [7, 1, "n"], [8, 1, "r"],
        ]
    )
    flags = [[True for _ in range(4)], None]

    movelist = map(decode, filter(lambda x: x != "", moves.strip().split(" ")))

    for fromPos, toPos, piece in movelist:
        side, board, flags = makeMove([side, board], fromPos, toPos, flags, piece)

    return side, board, flags

def encode(fromPos, toPos, promote=None):
    data = LETTER[fromPos[0]] + str(9 - fromPos[1]) + LETTER[toPos[0]] + str(9 - toPos[1])
    if promote is not None:
        return data + promote
    return data

def decode(data):
    if len(data) == 4:
        return (
            [LETTER.index(data[0]), 9 - int(data[1])],
            [LETTER.index(data[2]), 9 - int(data[3])],
            None,
        )
    elif len(data) == 5:
        return (
            [LETTER.index(data[0]), 9 - int(data[1])],
            [LETTER.index(data[2]), 9 - int(data[3])],
            data[4],
        )

def showMoves(win, boardS, pos, flags, flip):
    piece = pos + [pieceType(boardS, pos)]
    list = availableMoves(boardS, piece, flags)
    for newPos in list:
        if not takenPos(boardS, newPos) and moveTest(boardS, pos, newPos):
            if flip:
                newPos[0] = 475 - newPos[0] * SQUARE_SIZE
                newPos[1] = 475 - newPos[1] * SQUARE_SIZE
            else:
                newPos[0] = newPos[0] * SQUARE_SIZE + 25
                newPos[1] = newPos[1] * SQUARE_SIZE + 25

            pygame.draw.circle(win, BLUE, (newPos[0], newPos[1]), 3)

#type - multiplayer 1, singleplayer - 0
def saveGame(moves, gametype, type):
    dir = ['resources\games\singleplayer', 'resources\games\multiplayer']

    txtfiles = []
    for file in glob.glob(dir[type] + "\*.txt"):
        txtfiles.append(file)
    if not txtfiles:
        gameNo = 1
    else:
        gameNo = int(((txtfiles[-1])[-5:])[0]) + 1

    fileN = os.path.join(dir[type], "Game " + str(gameNo) + ".txt")
    date = today.strftime("%B %d, %Y")
    time = datetime.now().strftime("%H:%M:%S")

    text = (gametype + " " + str(gameNo) + ". saved at:\n" + "Date: " + str(date) + "\nTime: " + str(time) + "\nMoves: " + moves.strip())
    with open(fileN, "w") as file:
        file.write(text + "\n")

"""
cand un pion atinge ultimul/primul rand de pe tabla, poate readuce orice piesa in joc 
"""
def promotePawn(win, boardS, fromPos, toPos, single=False):
    if pieceType(boardS, fromPos) == "p":
        if (boardS[0] == 0 and toPos[1] == 1) or (boardS[0] == 1 and toPos[1] == 8):
            if single:
                return "q"
            else:
                return promoteChoice(win, boardS[0])


"""
CAND UN PION PROMOVEAZA, FUNCTIA RETURNEAZA CE PIESA A ALES JUCATORUL
"""
def promoteChoice(win, side):
    win.blit(Chess.PROMOTION, (65, 15))
    if side == 0:
        for idx in range(4):
            win.blit(pygame.image.load('resources/images/' + Chess.W_PROM[idx]), Chess.WB_POS[idx])

        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if checkPos(Chess.QUEEN_POS, x, y):
                        return 'q'
                    elif checkPos(Chess.BISHOP_POS, x, y):
                        return 'b'
                    elif checkPos(Chess.ROOK_POS, x, y):
                        return 'r'
                    elif checkPos(Chess.KNIGHT_POS, x, y):
                        return 'n'

    else:
        for idx in range(4):
            win.blit(pygame.image.load('resources/images/' + Chess.B_PROM[idx]), Chess.WB_POS[idx])

        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if checkPos(Chess.QUEEN_POS, x, y):
                        return 'q'
                    elif checkPos(Chess.BISHOP_POS, x, y):
                        return 'b'
                    elif checkPos(Chess.ROOK_POS, x, y):
                        return 'r'
                    elif checkPos(Chess.KNIGHT_POS, x, y):
                        return 'n'
