import pygame

pygame.font.init()

from utils.constants import PROMPT, PROMPTB
from utils import LoadGame
from utils.constants import checkPos

# fonts
FONT = 'cambriacambriamath'
LARGE = pygame.font.SysFont(FONT, 80)
VMEDIUM = pygame.font.SysFont(FONT, 30)

def  main(win):
    win.fill(LoadGame.BACKGROUND)
    pygame.draw.rect(win, PROMPT, LoadGame.PROMPT_POS)
    pygame.draw.rect(win, PROMPTB, LoadGame.PROMPTB_POS, 3)

    win.blit(LoadGame.LOAD_GAME, LoadGame.LOAD_POS)
    win.blit(LoadGame.SINGLE_YES, LoadGame.SINGLE_YES_POS)
    win.blit(LoadGame.MULTI_YES, LoadGame.MULTI_YES_POS)

    br = 0
    screen = -1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    return 0, ""

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if checkPos(LoadGame.SINGLE_YES_POS, x, y):
                    showScreen(win)
                    br = 1
                    screen = 0
                elif checkPos(LoadGame.MULTI_YES_POS, x, y):
                    showScreen2(win)
                    br = 1
                    screen = 1
        if br == 1:
            break
        pygame.display.update()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                if screen == 0:
                    for idx in range(len(LoadGame.SINGLE_BTNS_POS)):
                        if checkPos(LoadGame.SINGLE_BTNS_POS[idx], x, y):
                            #print(LoadGame.SINGLE_MOVES2[idx])
                            return screen, LoadGame.SINGLE_MOVES2[idx]
                elif screen == 1:
                    for idx in range(len(LoadGame.MULTI_BTNS_POS)):
                        if checkPos(LoadGame.MULTI_BTNS_POS[idx], x, y):
                            #print(LoadGame.MULTI_MOVES2[idx])
                            return screen, LoadGame.MULTI_MOVES2[idx]

        pygame.display.update()


def showScreen(win):
    win.fill(LoadGame.BACKGROUND)
    win.blit(LoadGame.SINGLE, LoadGame.SINGLE_POS)
    #win.blit(LoadGame.MULTI, LoadGame.MULTI_POS)

    for idx in range(len(LoadGame.SINGLE_BTNS)):
        win.blit(LoadGame.SINGLE_BTNS[idx], LoadGame.SINGLE_BTNS_POS[idx])

    for idx in range(len(LoadGame.SINGLE_INFO)):
        win.blit(LoadGame.SINGLE_INFO[idx], LoadGame.SINGLE_INFO_POS[idx])

    for idx in range(len(LoadGame.SINGLE_MOVES)):
        win.blit(LoadGame.SINGLE_MOVES[idx], LoadGame.SINGLE_MOVES_POS[idx])

    #win.blit(LoadGame.game, LoadGame.game_pos)

    pygame.display.update()

def showScreen2(win):
    win.fill(LoadGame.BACKGROUND)
    win.blit(LoadGame.MULTI, LoadGame.MULTI_POS)

    for idx in range(len(LoadGame.MULTI_BTNS)):
        win.blit(LoadGame.MULTI_BTNS[idx], LoadGame.MULTI_BTNS_POS[idx])

    for idx in range(len(LoadGame.MULTI_INFO)):
        win.blit(LoadGame.MULTI_INFO[idx], LoadGame.MULTI_INFO_POS[idx])

    for idx in range(len(LoadGame.MULTI_MOVES)):
        win.blit(LoadGame.MULTI_MOVES[idx], LoadGame.MULTI_MOVES_POS[idx])

    #win.blit(LoadGame.game, LoadGame.game_pos)

    pygame.display.update()
