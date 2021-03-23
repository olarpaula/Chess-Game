import pygame

pygame.font.init()

from utils.game import Chess
from utils.constants import checkPos, BLACK
from utils.constants import PROMPT, PROMPTB
from utils import LoadGame
from utils import Settings

# fonts
FONT = 'cambriacambriamath'
LARGE = pygame.font.SysFont(FONT, 80)
VMEDIUM = pygame.font.SysFont(FONT, 30)

# flag 0 = show moves
# flag 1 = flip board

def prompt(win, flag):
    pygame.draw.rect(win, PROMPT, Settings.PROMPT_POS)
    pygame.draw.rect(win, PROMPTB, Settings.PROMPTB_POS, 3)

    if (flag == 0):
        win.blit(Settings.SHOW_MOVES1, Settings.SHOW_MOVES1_POS)
    else:
        win.blit(Settings.FLIP_BOARD1, Settings.FLIP_BOARD1_POS)

  #  win.blit(Settings.YES1, Settings.YES1_POS)
  #  win.blit(Settings.NO1, Settings.NO1_POS)

    clock = pygame.time.Clock()
    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if checkPos(Settings.NO1_POS, x, y):
                    return False
                if checkPos(Settings.YES1_POS, x, y):
                    return True

        pygame.display.update()


def  main(win):
    win.fill(LoadGame.BACKGROUND)
    pygame.draw.rect(win, PROMPT, Settings.PROMPT_POS1)
    pygame.draw.rect(win, PROMPTB, Settings.PROMPTB_POS1, 3)

    win.blit(Settings.SHOW_MOVES, Settings.SHOW_MOVES_POS)
    #win.blit(Settings.YES, Settings.SHOW_YES_POS)
    #win.blit(Settings.NO, Settings.SHOW_NO_POS)

    pygame.draw.rect(win, PROMPT, Settings.PROMPT_POS2)
    pygame.draw.rect(win, PROMPTB, Settings.PROMPTB_POS2, 3)

    win.blit(Settings.FLIP_BOARD, Settings.FLIP_BOARD_POS)
    #win.blit(Settings.YES, Settings.FLIP_YES_POS)
    #win.blit(Settings.NO, Settings.FLIP_NO_POS)

    sett = [True, True]

    while True:

        x, y = pygame.mouse.get_pos()
        if (checkPos(Settings.SHOW_YES_POS, x, y)):
            win.blit(Settings.YESB, Settings.SHOW_YES_POS)
        else:
            win.blit(Settings.YES, Settings.SHOW_YES_POS)

        if (checkPos(Settings.SHOW_NO_POS, x, y)):
            win.blit(Settings.NOB, Settings.SHOW_NO_POS)
        else:
            win.blit(Settings.NO, Settings.SHOW_NO_POS)

        if (checkPos(Settings.FLIP_YES_POS, x, y)):
            win.blit(Settings.YESB, Settings.FLIP_YES_POS)
        else:
            win.blit(Settings.YES, Settings.FLIP_YES_POS)

        if (checkPos(Settings.FLIP_NO_POS, x, y)):
            win.blit(Settings.NOB, Settings.FLIP_NO_POS)
        else:
            win.blit(Settings.NO, Settings.FLIP_NO_POS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    return sett

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                if (checkPos(Settings.SHOW_YES_POS, x, y)):
                    sett[0] = True

                if (checkPos(Settings.SHOW_NO_POS, x, y)):
                    sett[0] = False

                if (checkPos(Settings.FLIP_YES_POS, x, y)):
                    sett[1] = True

                if (checkPos(Settings.FLIP_NO_POS, x, y)):
                    sett[1] = False

        pygame.display.update()



