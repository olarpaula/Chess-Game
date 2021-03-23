import pygame
pygame.font.init()
from utils.constants import BROWN, LIGHT_BROWN
from utils.file_processing import *

# fonts
FONT = 'cambriacambriamath'

MEDIUM = pygame.font.SysFont(FONT, 22)
VMEDIUM = pygame.font.SysFont(FONT, 20)
SMALL = pygame.font.SysFont(FONT, 17)
SMALL2 = pygame.font.SysFont(FONT, 18)


def rpl_string(s):
    x = s.replace('\n', '').replace('Singleplayer game ', 'Game ').replace('saved at:', '').replace('2020', '2020   ').replace('2021', '2021   ')
    p = x[:7]
    q = x[8:]
    return p, q

def rpl2_string(s):
    x = s.replace('\n', '').replace('Multiplayer game ', 'Game ').replace('saved at:', '').replace('2020', '2020   ').replace('2021', '2021   ')
    p = x[:6]
    q = x[7:]
    return p, q

def rpl_string2(s):
    x = s.replace('\n', '')
    return x

def rpl_string3(s):
    x = s.replace('Moves: ', '')
    return x

class LoadGame:
    # colors
    BACKGROUND = (242, 240, 232)

    # texts
    SINGLE = MEDIUM.render('SinglePlayer Games', True, BROWN)
    MULTI = MEDIUM.render('MultiPlayer Games', True, BROWN)
    SINGLE_YES = VMEDIUM.render("• SinglePlayer", True, BROWN)
    MULTI_YES = VMEDIUM.render("• Multiplayer", True, BROWN)
    LOAD_GAME = VMEDIUM.render("Load game:", True, BROWN)

    # positions
    SINGLE_POS = (30, 20, 50, 50)
    MULTI_POS = (30, 20, 50, 50)
    LOAD_POS = (200, 205, 90, 40)
    SINGLE_YES_POS = (190, 235, 90, 40)
    MULTI_YES_POS = (190, 265, 90, 40)
    PROMPT_POS = (150, 190, 200, 120)
    PROMPTB_POS = (155, 195, 190, 110)

    # files, games, moves
    games = getGames(); single_games = games[0]; multi_games = games[1]
    moves = getMoves(); single_moves = moves[0]; multi_moves = moves[1]

    SINGLE_BTNS = []
    SINGLE_INFO = []
    SINGLE_MOVES = []
    SINGLE_MOVES2 = []

    for idx in range(len(single_games)):
        game = ''
        for idx2 in range(3):
            game = game + single_games[idx][idx2]
        btns, info = rpl_string(game)

        mv = single_games[idx][3]
        mv = rpl_string2(mv)

        SINGLE_BTNS.append(btns)
        SINGLE_INFO.append(info)
        SINGLE_MOVES.append(mv)
        SINGLE_MOVES2.append(mv)


    for idx in range(len(SINGLE_MOVES2)):
        SINGLE_MOVES2[idx] = rpl_string3(SINGLE_MOVES2[idx])

    for idx in range(len(SINGLE_BTNS)):
        SINGLE_BTNS[idx] = SMALL2.render(SINGLE_BTNS[idx], BROWN, True)

    SINGLE_BTNS_POS = []
    for idx in range(len(SINGLE_BTNS)):
        SINGLE_BTNS_POS.append((30, 60 * (idx+1), 50, 50))


    for idx in range(len(SINGLE_INFO)):
        SINGLE_INFO[idx] = SMALL.render(SINGLE_INFO[idx], BROWN, True)

    SINGLE_INFO_POS = []
    for idx in range(len(SINGLE_INFO)):
        SINGLE_INFO_POS.append((30, 60 * (idx+1) + 20, 50, 50))


    for idx in range(len(SINGLE_MOVES)):
        SINGLE_MOVES[idx] = SMALL.render(SINGLE_MOVES[idx], BROWN, True)

    SINGLE_MOVES_POS = []
    for idx in range(len(SINGLE_MOVES)):
        SINGLE_MOVES_POS.append((30, 60 * (idx+1) + 40, 50, 50))


    #############################################################################33

    MULTI_BTNS = []
    MULTI_INFO = []
    MULTI_MOVES = []
    MULTI_MOVES2 = []

    for idx in range(len(multi_games)):
        game = ''
        for idx2 in range(3):
            game = game + multi_games[idx][idx2]
        btns, info = rpl2_string(game)

        mv = multi_games[idx][3]
        mv = rpl_string2(mv)

        MULTI_BTNS.append(btns)
        MULTI_INFO.append(info)
        MULTI_MOVES.append(mv)
        MULTI_MOVES2.append(mv)

    for idx in range(len(MULTI_MOVES2)):
        MULTI_MOVES2[idx] = rpl_string3(MULTI_MOVES2[idx])

    for idx in range(len(MULTI_BTNS)):
        MULTI_BTNS[idx] = SMALL2.render(MULTI_BTNS[idx], BROWN, True)

    MULTI_BTNS_POS = []
    for idx in range(len(MULTI_BTNS)):
        MULTI_BTNS_POS.append((30, 60 * (idx + 1), 50, 50))

    for idx in range(len(MULTI_INFO)):
        MULTI_INFO[idx] = SMALL.render(MULTI_INFO[idx], BROWN, True)

    MULTI_INFO_POS = []
    for idx in range(len(MULTI_INFO)):
        MULTI_INFO_POS.append((30, 60 * (idx + 1) + 20, 50, 50))

    for idx in range(len(MULTI_MOVES)):
        MULTI_MOVES[idx] = SMALL.render(MULTI_MOVES[idx], BROWN, True)

    MULTI_MOVES_POS = []
    for idx in range(len(MULTI_MOVES)):
        MULTI_MOVES_POS.append((30, 60 * (idx + 1) + 40, 50, 50))



