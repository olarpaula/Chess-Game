import os.path
import pygame
pygame.init()

from utils.constants import WHITE, GREEN, RED, BLACK

# fonts
FONT = 'cambriacambriamath'
SMALL = pygame.font.SysFont(FONT, 17)
VSMALL = pygame.font.SysFont(FONT, 18)
MEDIUM = pygame.font.SysFont(FONT, 23)
VMEDIUM = pygame.font.SysFont(FONT, 20)

large = pygame.font.SysFont(FONT, 40)

class Online:
    # colors
    BACKGROUND = (242, 240, 232)
    BROWN = (203, 136, 68)

    # connection and error messages
    TRYCONN = VSMALL.render("Trying to connect to server", True, BROWN)
    ERR = [
        VSMALL.render("Error Server not found", True, BROWN),
        VSMALL.render("Connection not estalished", True, BROWN),
        VSMALL.render("Full server (max 10)", True, BROWN),
        VSMALL.render("Server locked", True, BROWN),
    ]

    # messages handling the list of players in the lobby
    PLAYERS_LIST = large.render("List of Players", True, BROWN)
    PLAYER = VMEDIUM.render("Player", True, BROWN)
    NO_PLAYERS = VMEDIUM.render("No players. Try to refresh the list!", True, BROWN)
    REFRESH = pygame.image.load(os.path.join("resources", "images", "refresh.jpg"))
    DOT = SMALL.render(".", True, BROWN)

    # player stats
    ONLINE_P = VMEDIUM.render("Online", True, GREEN)
    IN_GAME_P = VMEDIUM.render("In game", True, RED)
    PLAYER_LEFT = VMEDIUM.render("Player left", True, BROWN)
    PLAYER_RESIGN = VMEDIUM.render("Player resigned", True, BROWN)

    # invitation to begin/end game between players
    INVITATION = VMEDIUM.render("Invite", True, BROWN)
    INVITATION_SENT = VMEDIUM.render("Wait...", True, BROWN)
    ACCEPT_INVITATION = (
        VMEDIUM.render("Player ", True, BROWN),
        VMEDIUM.render("asked for a game.", True, BROWN),
        VMEDIUM.render("Accept?", True, BROWN),
    )
    DRAW_SENT = VMEDIUM.render("Wait...", True, BROWN)
    ACCEPT_DRAW = VMEDIUM.render("Accept draw?", True, BROWN)
    ACCEPTED_DRAW = VMEDIUM.render("Draw has been agreed", True, BROWN)

    NO = VMEDIUM.render("NO", True, BROWN)
    YES = VMEDIUM.render("YES", True, BROWN)
    OK = VMEDIUM.render("Ok", True, BROWN)

    # btns positions
    PLAYER_POS = (180, 440)
    PLAYERS_LIST_POS = (80, 30)
    REFRESH_POS = (340, 45, 40, 40)
    PLAYER_POS_KEY = (260, 440)
    NO_PLAYERS_POS = (25, 130)

    INVITATION_SENT_POS = (210, 250)
    ACCEPT_INVITATION_POS = (
        (130, 205),
        (230, 205),
        (220, 225)
    )
    DRAW_SENT_POS = (225, 237)
    ACCEPTED_DRAW_POS = (150, 210)

    ACCEPT_YES_POS = (165, 260, 90, 40)
    ACCEPT_NO_POS = (295, 260, 90, 40)
    OK_POS = (230, 260, 40, 40)

    PLAYER_LEFT_POS = (200, 210)
    PLAYER_RESIGN_POS = (195, 210)
















