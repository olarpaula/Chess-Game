import pygame
from utils import LoadGame
from utils.game import Chess
from logic.multiplayer import *
from utils.constants import checkPos
from logic.singleplayer.minimax import minimax
from utils.constants import PROMPT, PROMPTB

def main(win, player, show_moves, moves=""):
    if moves == "":
        win.fill(LoadGame.BACKGROUND)

        pygame.draw.rect(win, PROMPT, Chess.QS_PROMPT_POS)
        pygame.draw.rect(win, PROMPTB, Chess.QS_PROMPTB_POS, 3)

        win.blit(Chess.SG_GAME, Chess.SG_POS)
        win.blit(Chess.WHITE_C, Chess.WHITE_POS)
        win.blit(Chess.BLACK_C, Chess.BLACK_POS)

        player = -1
        br = 0
        clock = pygame.time.Clock()
        while True:
            clock.tick(30)
            pygame.display.update()

            '''
            x, y = pygame.mouse.get_pos()
            if checkPos(Chess.BLACK_POS, x, y):
                win.blit(Chess.BLACKB_C, Chess.BLACK_POS)
            elif checkPos(Chess.WHITE_POS, x, y):
                win.blit(Chess.WHITEB_C, Chess.WHITE_POS)
            '''

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if checkPos(Chess.BLACK_POS, x, y):
                        player = 1
                        br = 1
                    if checkPos(Chess.WHITE_POS, x, y):
                        player = 0
                        br = 1
            if br == 1:
                break


    side, board, flags = convertMoves(moves)
    clock = pygame.time.Clock()
    fromPos =  toPos = [0, 0]

    while True:
        boardS = [side, board]
        clock.tick(30)
        endG = endGame(boardS, flags)

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
                    if False and boardS[0]:
                        x, y = 9 - x, 9 - y

                    fromPos = toPos
                    toPos = [x, y]
                elif boardS[0] == player or endG:
                    toPos = [0, 0]
                    if checkPos(Chess.SAVE_POS, x, y):
                        if (savePrompt(win) == False):
                            pygame.time.delay(150)
                        else:
                            pygame.time.delay(150)
                            saveGame(moves, "Singleplayer game", 0)

        showScreen(win, boardS, flags, toPos, show_moves)
        if side != player:
            if not endG:
                fromPos, toPos = minimax(boardS, flags)
                animate(win, boardS, fromPos, toPos, False and player)
                if pieceType(boardS, fromPos) == 'p' and toPos[1] == 8 or toPos[1] == 1:
                    moves += " " + encode(fromPos, toPos, 'q')
                else:
                    moves += " " + encode(fromPos, toPos)
                side, board, flags = makeMove(boardS, fromPos, toPos, flags)
                toPos = [0, 0]

        elif isValidMove(boardS, flags, fromPos, toPos):
            promote = promotePawn(win, boardS, fromPos, toPos, True)
            animate(win, boardS, fromPos, toPos, bool(False and player))
            side, board, flags = makeMove(boardS, fromPos, toPos, flags, promote)
            moves += " " + encode(fromPos, toPos, promote)

