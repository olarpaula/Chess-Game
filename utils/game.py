import pygame

from utils.constants import BROWN, BLACK, PSPRITE, SQUARE_SIZE
from utils.constants import VMEDIUM, MEDIUM

class Chess:
    # messages involved in game choices
    CHECK = VMEDIUM.render("Check!", True, BROWN)
    PROMOTION = VMEDIUM.render("Pawn promotion!", True, BROWN)
    GAME_ENDED = [VMEDIUM.render("Checkmate!", True, BROWN), VMEDIUM.render("Stalemate!", True, BROWN)]
    MOVE = [VMEDIUM.render("Others turn", True, BROWN), VMEDIUM.render("Your turn", True, BROWN)]
    END_GAME0 = [VMEDIUM.render("Checkmate, you won!", True, BROWN), VMEDIUM.render("Checkmate, you lost!", True, BROWN)]

    # quit messages
    MSG_Q = (VMEDIUM.render("Quit game?", True, BLACK))

    # save messages
    SAVE_TEXT = VMEDIUM.render("Save game", True, BROWN)
    SAVE_TEXTB = VMEDIUM.render("Save game", True, BLACK)
    MSG_S = (VMEDIUM.render("Save game?", True, BLACK))

    # quit and save messages
    QS_YES = (VMEDIUM.render("Yes", True, BLACK))
    QS_NO = (VMEDIUM.render("No", True, BLACK))

    # draw and resign messages
    DRAW_TEXT = VMEDIUM.render("Draw", True, BROWN)
    DRAW_TEXTB = VMEDIUM.render("Draw", True, BLACK)
    RESIGN_TEXT = VMEDIUM.render("Resign", True, BROWN)
    RESIGN_TEXTB = VMEDIUM.render("Resign", True, BLACK)

    # promotion messages
    W_PROM = ['rsz_whiteQueen.png', 'rsz_whitebishop.png', 'rsz_whiterook.png', 'rsz_whiteknight.png']
    B_PROM = ['rsz_blackQueen.png', 'rsz_blackbishop.png', 'rsz_blackrook.png', 'rsz_blackknight.png']

    # singleplayer color choice
    SG_GAME = VMEDIUM.render("Play as:", True, BROWN)
    WHITE_C = VMEDIUM.render("White", True, BROWN)
    WHITEB_C = VMEDIUM.render("White", True, BLACK)
    BLACK_C = VMEDIUM.render("Black", True, BROWN)
    BLACKB_C = VMEDIUM.render("Black", True, BLACK)

    # singleplayer color choice btns
    SG_POS = (220, 210, 90, 40)
    WHITE_POS = (185, 250, 90, 40)
    BLACK_POS = (265, 250, 90, 40)

    # quit and save btns
    QS_PROMPT_POS = (160, 190, 180, 120)
    QS_PROMPTB_POS = (165, 195, 170, 110)
    QS_MSG_POS = (200, 210, 90, 40)

    YES_SQ_POS = (195, 250, 90, 40)
    NO_SQ_POS = (275, 250, 90, 40)
    SAVE_POS = (360, 462, 90, 40)

    # draw, move and resign btns
    DRAW_POS = (10, 12, 90, 40)
    RESIGN_POS = (400, 462, 90, 40)

    # check, checkmate btns
    CHECK_POS = (215, 15, 90, 40)
    CM_PROMPT_POS = (150, 200, 200, 100)
    CM_PROMPTB_POS = (155, 205, 190, 90)
    GAME_ENDED_POS = (200, 20, 90, 40)
    END_GAME_POS = (155, 15, 90, 50)

    # promotion btns
    QUEEN_POS = (235, 7, 35, 35)
    BISHOP_POS = (285, 7, 35, 35)
    ROOK_POS = (335, 7, 35, 35)
    KNIGHT_POS = (385, 7, 35, 35)
    WB_POS = [(235, 7), (285, 7), (335, 7), (385, 7)]

    PIECES = ({}, {})
    for i, ptype in enumerate(["k", "q", "b", "n", "r", "p"]):
        for side in range(2):
            PIECES[side][ptype] = PSPRITE.subsurface((i * SQUARE_SIZE, side * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

pygame.font.quit()