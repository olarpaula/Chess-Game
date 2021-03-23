import os
import pygame

pygame.font.init()

# fonts
FONT = 'cambriacambriamath'
SMALL = pygame.font.SysFont(FONT, 17)
VSMALL = pygame.font.SysFont(FONT, 18)
MEDIUM = pygame.font.SysFont(FONT, 23)
VMEDIUM = pygame.font.SysFont(FONT, 20)
LARGE = pygame.font.SysFont(FONT, 80)

MEDIUM2 = pygame.font.SysFont(FONT, 35)
VMEDIUM2 = pygame.font.SysFont(FONT, 30)

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GREY = (169, 169, 169)
BROWN = (203, 136, 68)
BWHITE = (255,228,181)
LIGHT_BROWN = (92, 80, 30)
LIGHT_BORDER = (225, 187, 137)
STRONG_BORDER = (145, 79, 28)
BACKGROUND = (242, 240, 232)
PROMPT = (246, 237, 220)
PROMPTB = (92, 80, 30)
BLUE = (0, 51, 102)
GREY = (180, 180, 180)
GREEN = (0, 255, 0)
RED = (200, 20, 20)
GREY2 = (105, 105, 105)
DARK_GREY2 = (169, 169, 169)

# table size
ROWS = 8
COLS = 8
SQUARE_SIZE = 50

# pieces
PSPRITE = pygame.image.load(os.path.join("resources", "images", "piecesprite.png"))

"""
functie care verifica daca s-a selectat prin mouse un modul setat la o locatie prestabilita
"""
def checkPos(elem, x, y):
    if elem[0] < x < (elem[0] + elem[2]):
        if elem[1] < y < (elem[1] + elem[3]):
            return True
    return False

NUM = [VSMALL.render(str(i), True, BROWN) for i in range(10)]
LNUM = [VMEDIUM.render(str(i), True, BROWN) for i in range(10)]


"""
functii folosita la afisarea unui numar pe ecran
"""
def putNum(win, num, pos):
    for cnt, i in enumerate(list(str(num))):
        win.blit(NUM[int(i)], (pos[0] + (cnt * 8), pos[1]))

def putLargeNum(win, num, pos):
    for cnt, i in enumerate(list(str(num))):
        win.blit(LNUM[int(i)], (pos[0] + (cnt * 14), pos[1]))

head = pygame.font.SysFont(FONT, 80)
large = pygame.font.SysFont(FONT, 50)