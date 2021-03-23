from utils.constants import *
from utils.game import Chess
from logic.multiplayer.logics import pieceType, endGame, inCheck
from logic.multiplayer.utils import showMoves
from utils.constants import checkPos


def drawBoard(win):
    win.fill(BACKGROUND)
    pygame.draw.rect(win, BLACK, (48, 48, 403, 403), 2)

    for x in range(0, ROWS):
        for y in range(0, COLS):
            if (x + y) % 2 == 0:
                pygame.draw.rect(win, BWHITE, (50 * (x+1), 50 * (y+1), SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(win, BROWN, (50 * (x+1), 50 * (y+1), SQUARE_SIZE, SQUARE_SIZE))

def drawPieces(win, board, flip):
    for side in range(2):
        for x, y, ptype in board[side]:
            if flip:
                x, y = ROWS + 1 - x, COLS + 1 - y
            win.blit(Chess.PIECES[side][ptype], (x * SQUARE_SIZE, y * SQUARE_SIZE))


def savePrompt(win):
    pygame.draw.rect(win, PROMPT, Chess.QS_PROMPT_POS)
    pygame.draw.rect(win, PROMPTB, Chess.QS_PROMPTB_POS, 3)

    win.blit(Chess.MSG_S, Chess.QS_MSG_POS)
    win.blit(Chess.QS_YES, Chess.YES_SQ_POS)
    win.blit(Chess.QS_NO, Chess.NO_SQ_POS)

    clock = pygame.time.Clock()
    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if checkPos(Chess.NO_SQ_POS, x, y):
                    return False
                if checkPos(Chess.YES_SQ_POS, x, y):
                    return True

        pygame.display.update()

def quitPrompt(win):
    pygame.draw.rect(win, PROMPT, Chess.QS_PROMPT_POS)
    pygame.draw.rect(win, PROMPTB, Chess.QS_PROMPTB_POS, 3)

    win.blit(Chess.MSG_Q, Chess.QS_MSG_POS)
    win.blit(Chess.QS_YES, Chess.YES_SQ_POS)
    win.blit(Chess.QS_NO, Chess.NO_SQ_POS)

    clock = pygame.time.Clock()
    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if checkPos(Chess.NO_SQ_POS, x, y):
                    return False
                if checkPos(Chess.YES_SQ_POS, x, y):
                    return True

        pygame.display.update()


def animate(win, boardS, fromPos, toPos, flip, player=None):
    piece = Chess.PIECES[boardS[0]][pieceType(boardS, fromPos)]
    x1, y1 = fromPos[0], fromPos[1]
    x2, y2 = toPos[0] , toPos[1]
    if flip:
        x1, y1 = 9 - x1, 9 - y1
        x2, y2 = 9 - x2, 9 - y2

    dx = (x2 - x1)
    dy = (y2 - y1)


    clk = pygame.time.Clock()
    for i in range(51):
        clk.tick(100)
        drawBoard(win)
        drawPieces(win, boardS[1], flip)

        if (fromPos[0] + fromPos[1]) % 2 == 0:
            pygame.draw.rect(win, BWHITE, (x1*50, y1*50, 50, 50))
        else:
            pygame.draw.rect(win, BROWN, (x1*50, y1*50, 50, 50))

        win.blit(piece, (x1*50 + (i * dx), y1*50 + (i * dy)))
        pygame.display.update()
    drawBoard(win)

def showScreen(win, boardS, flags, pos, show_moves, load=False, player=None):
    side = boardS[0]
    board = boardS[1]

    if player is None:
        flip = load and boardS[0]
    else:
        flip = load and player
    drawBoard(win)

    if player is not None:
        win.blit(Chess.DRAW_TEXT, Chess.DRAW_POS)
        win.blit(Chess.RESIGN_TEXT, Chess.RESIGN_POS)

        x, y = pygame.mouse.get_pos()

        if checkPos(Chess.DRAW_POS, x, y):
            win.blit(Chess.DRAW_TEXTB, Chess.DRAW_POS[:2])

        if checkPos(Chess.RESIGN_POS, x, y):
            win.blit(Chess.RESIGN_TEXTB, Chess.RESIGN_POS[:2])

        win.blit(Chess.MOVE[int(side == player)], (10, 460))

    else:
        win.blit(Chess.SAVE_TEXT, Chess.SAVE_POS[:2])
        x, y = pygame.mouse.get_pos()

        if checkPos(Chess.SAVE_POS, x, y):
            win.blit(Chess.SAVE_TEXTB, Chess.SAVE_POS[:2])

    if endGame(boardS, flags):
        #pygame.draw.rect(win, PROMPT, Chess.CM_PROMPT_POS)
        #pygame.draw.rect(win, PROMPTB, Chess.CM_PROMPTB_POS, 3)
        if inCheck(boardS):
            if player is None:
                win.blit(Chess.GAME_ENDED[0], Chess.GAME_ENDED_POS)

            if player is not None:
                win.blit(Chess.END_GAME0[int(side == player)], Chess.END_GAME_POS)

        else:
            if player is None:
                win.blit(Chess.GAME_ENDED[1], Chess.GAME_ENDED_POS)

    elif inCheck(boardS):
        win.blit(Chess.CHECK, Chess.CHECK_POS)

    drawPieces(win, board, flip)

    if show_moves:
        showMoves(win, boardS, pos, flags, flip)

    pygame.display.update()
