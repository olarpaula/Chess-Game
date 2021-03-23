import pygame
from logic.online.socket import *
from utils import Online
from utils.constants import putNum, putLargeNum
from utils.constants import checkPos
pygame.init()
BROWN = (203, 136, 68)

# fonts
FONT = 'cambriacambriamath'
SMALL = pygame.font.SysFont(FONT, 17)

def showLoading(win, errcode=-1):
    
    if errcode == -1:
        win.blit(Online.TRYCONN, (135, 240))
        pygame.display.update()
        return
    
    win.blit(Online.ERR[errcode], (110, 240))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


# Show a popup message when user left, resigned or draw accepted.
def popup(win, typ):
    pygame.draw.rect(win, (225, 187, 137), (125, 190, 250, 120))
    pygame.draw.rect(win, (255, 255, 255), (125, 190, 250, 120), 3)
    win.blit(Online.OK, Online.OK_POS)

    if typ == "quit":
        win.blit(Online.PLAYER_LEFT, Online.PLAYER_LEFT_POS)
    elif typ == "resign":
        win.blit(Online.PLAYER_RESIGN, Online.PLAYER_RESIGN_POS)
    elif typ == "draw":
        win.blit(Online.ACCEPTED_DRAW, Online.ACCEPTED_DRAW_POS)

    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if checkPos(Online.OK_POS, x, y):
                    return


def request(win, key, sock=None):
    if sock is None:
        pygame.draw.rect(win, (145, 79, 28), (100, 180, 300, 130), 4)

        win.blit(Online.ACCEPT_INVITATION[0], Online.ACCEPT_INVITATION_POS[0])
        win.blit(Online.ACCEPT_INVITATION[1], Online.ACCEPT_INVITATION_POS[1])
        win.blit(Online.ACCEPT_INVITATION[2], Online.ACCEPT_INVITATION_POS[2])
        putNum(win, key, (188, 205))

        win.blit(Online.YES, Online.ACCEPT_YES_POS)
        win.blit(Online.NO, Online.ACCEPT_NO_POS)

        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if (checkPos(Online.ACCEPT_YES_POS, x, y)):
                        return True
                    if (checkPos(Online.ACCEPT_NO_POS, x, y)):
                        return False
    else:
        pygame.draw.rect(win, (145, 79, 28), (190, 230, 90, 65), 3)
        win.blit(Online.INVITATION_SENT, Online.INVITATION_SENT_POS)


        pygame.display.flip()
        while True:
            if readable():
                msg = read()
                if msg == "close":
                    return None

                elif msg == "start":
                    write(sock, "ready")
                    return True

                elif msg == "nostart":
                    write(sock, "pass")
                    return False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    write(sock, "quit")
                    return None


def draw(win, sock=None):
    if sock is None:
        pygame.draw.rect(win, (225, 187, 137), (125, 200, 250, 100))
        pygame.draw.rect(win, (255, 255, 255), (125, 200, 250, 100), 3)

        win.blit(Online.ACCEPT_DRAW, (200, 230))
        win.blit(Online.YES, Online.ACCEPT_YES_POS)
        win.blit(Online.NO, Online.ACCEPT_NO_POS)

        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if checkPos(Online.ACCEPT_YES_POS, x, y):
                        return True
                    if checkPos(Online.ACCEPT_NO_POS, x, y):
                        return False
    else:
        pygame.draw.rect(win, (225, 187, 137), (175, 220, 150, 60))
        pygame.draw.rect(win, (255, 255, 255), (175, 220, 150, 60), 3)
        win.blit(Online.DRAW_SENT, Online.DRAW_SENT_POS)

        pygame.display.flip()
        while True:
            if readable():
                msg = read()
                if msg == "close":
                    return True

                elif msg == "draw":
                    popup(win, msg)
                    write(sock, "end")
                    return True

                elif msg == "nodraw":
                    return False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    write(sock, "quit")
                    return True


def showLobby(win, key, playerlist):
    win.fill(Online.BACKGROUND)
    win.blit(Online.PLAYERS_LIST, Online.PLAYERS_LIST_POS)
    win.blit(Online.REFRESH, Online.REFRESH_POS)

    if not playerlist:
        win.blit(Online.NO_PLAYERS, Online.NO_PLAYERS_POS)
    
    for cnt, player in enumerate(playerlist):
        pkey, stat = int(player[:4]), player[4]
        yCord = 120 + cnt * 30
        
        putLargeNum(win, cnt + 1, (20, yCord))
        win.blit(Online.PLAYER, (52, yCord))
        putLargeNum(win, pkey, (132, yCord))

        if stat == "a":
            win.blit(Online.ONLINE_P, (200, yCord))
        elif stat == "b":
            win.blit(Online.IN_GAME_P, (200, yCord))

        win.blit(Online.INVITATION, (350, yCord))


    win.blit(Online.PLAYER, Online.PLAYER_POS)
    putLargeNum(win, key, Online.PLAYER_POS_KEY)

    pygame.display.update()