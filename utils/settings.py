import pygame
pygame.font.init()
from utils.constants import BROWN, LIGHT_BROWN, BLACK

# fonts
FONT = 'cambriacambriamath'

MEDIUM = pygame.font.SysFont(FONT, 22)
VMEDIUM = pygame.font.SysFont(FONT, 20)
SMALL = pygame.font.SysFont(FONT, 17)
SMALL2 = pygame.font.SysFont(FONT, 18)

class Settings:
    # colors
    BACKGROUND = (242, 240, 232)

    # texts
    FLIP_BOARD = VMEDIUM.render("Flip board:", True, BROWN)
    FLIP_BOARD1 = VMEDIUM.render("Flip board?", True, BROWN)
    SHOW_MOVES = VMEDIUM.render("Show moves:", True, BROWN)
    SHOW_MOVES1 = VMEDIUM.render("Show moves?", True, BROWN)

    YES = VMEDIUM.render("• Yes", True, BROWN)
    NO = VMEDIUM.render("• No", True, BROWN)

    YESB = VMEDIUM.render("• Yes", True, BLACK)
    NOB = VMEDIUM.render("• No", True, BLACK)

    # btns positions
    PROMPT_POS1 = (100, 90, 200, 120)
    PROMPTB_POS1 = (105, 95, 190, 110)
    SHOW_MOVES_POS = (140, 105, 90, 40)
    SHOW_YES_POS = (170, 135, 90, 40)
    SHOW_NO_POS = (170, 165, 90, 40)


    PROMPT_POS2 = (200, 290, 200, 120)
    PROMPTB_POS2 = (205, 295, 190, 110)
    FLIP_BOARD_POS = (250, 305, 90, 40)
    FLIP_YES_POS = (280, 335, 90, 40)
    FLIP_NO_POS = (280, 365, 90, 40)

    PROMPT_POS = (160, 190, 180, 120)
    PROMPTB_POS = (165, 195, 170, 110)

    SHOW_MOVES1_POS = (200, 210, 90, 40)
    FLIP_BOARD1_POS = (200, 210, 90, 40)

    YES1_POS = (195, 250, 90, 40)
    NO1_POS = (275, 250, 90, 40)

    YES1 = (VMEDIUM.render("Yes", True, BLACK))
    NO1 = (VMEDIUM.render("No", True, BLACK))



