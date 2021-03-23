import pygame
from utils.game import Chess
from logic.multiplayer import *
from utils.constants import checkPos

#load[0] = show moves
#load[1] = flip

def main(win, LOAD=[False, False], moves=""):
    side, board, flags = convertMoves(moves)
    clock = pygame.time.Clock()
    fromPos =  toPos = [0, 0]
    #boardS = [side, board]

    while True:
        boardS = [side, board]
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if (quitPrompt(win) == True):
                    pygame.time.delay(150)
                    return
                else:
                    pygame.time.delay(150)
                    pass

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 50 < x < 450 and 50 < y < 450:
                    x, y = x // 50, y // 50
                    if LOAD[1] and side:
                        x, y = 9 - x, 9 - y

                    fromPos = toPos
                    toPos = [x, y]
                else:
                    toPos = [0, 0]
                    if checkPos(Chess.SAVE_POS, x, y):
                        if (savePrompt(win) == False):
                            pygame.time.delay(150)
                        else:
                            pygame.time.delay(150)
                            saveGame(moves, "Multiplayer game", 1)

        showScreen(win, boardS, flags, toPos, LOAD[0], LOAD[1])

        if isValidMove(boardS, flags, fromPos, toPos):
            promote = promotePawn(win, boardS, fromPos, toPos)
            animate(win, boardS, fromPos, toPos, bool(LOAD[1] and side))
            side, board, flags = makeMove(boardS, fromPos, toPos, flags, promote)
            moves += " " + encode(fromPos, toPos, promote)



