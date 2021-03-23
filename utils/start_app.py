import pygame
pygame.font.init()

from utils.constants import BLACK, DARK_GREY2 as DARK_GREY

# fonts
FONT = 'cambriacambriamath'
LARGE = pygame.font.SysFont(FONT, 80)
VMEDIUM = pygame.font.SysFont(FONT, 30)


class Main:
    # buttons positions (x y length width)
    TITLE_POS = (140, 15, 90, 40)
    SINGLEPLAYER_POS = (10, 300, 90, 40)
    MULTIPLAYER_POS = (10, 350, 90, 40)
    ONLINE_POS = (10, 400, 90, 40)
    #ABOUT_POS = (380, 100, 110, 40)
    #DOCS_POS = (380, 150, 90, 40)
    SETTINGS_POS = (330, 100, 90, 40)
    LOAD_POS = (330, 140, 90, 40)

    # texts
    TITLE_TEXT = LARGE.render("Chess", True, DARK_GREY)
    SINGLEPLAYER_TEXT = VMEDIUM.render("• SinglePlayer", True, DARK_GREY)
    MULTIPLAYER_TEXT = VMEDIUM.render("• MultiPlayer", True, DARK_GREY)
    ONLINE_TEXT = VMEDIUM.render("• Online", True, DARK_GREY)
    LOGIN_TEXT = VMEDIUM.render("• Login", True, DARK_GREY)
    #ABOUT_TEXT = VMEDIUM.render("• About", True, DARK_GREY)
    #DOCS_TEXT = VMEDIUM.render("• Docs", True, DARK_GREY)
    LOAD_TEXT = VMEDIUM.render("• Load Game", True, DARK_GREY)
    SETTINGS_TEXT = VMEDIUM.render("• Settings", True, DARK_GREY)

    # blitting texts
    SINGLEPLAYER_TEXTB = VMEDIUM.render("• SinglePlayer", True, BLACK)
    MULTIPLAYER_TEXTB = VMEDIUM.render("• MultiPlayer", True, BLACK)
    ONLINE_TEXTB = VMEDIUM.render("• Online", True, BLACK)
    LOGIN_TEXTB = VMEDIUM.render("• Login", True, BLACK)
    #ABOUT_TEXTB = VMEDIUM.render("• About", True, BLACK)
    #DOCS_TEXTB = VMEDIUM.render("• Docs", True, BLACK)
    LOAD_TEXTB = VMEDIUM.render("• Load Game", True, BLACK)
    SETTINGS_TEXTB = VMEDIUM.render("• Settings", True, BLACK)

    # lists for window blitting
    btns_pos = [SINGLEPLAYER_POS, MULTIPLAYER_POS, ONLINE_POS, LOAD_POS, SETTINGS_POS]
    btns_txt = [SINGLEPLAYER_TEXT, MULTIPLAYER_TEXT, ONLINE_TEXT, LOAD_TEXT, SETTINGS_TEXT]
    btns_txtb = [SINGLEPLAYER_TEXTB, MULTIPLAYER_TEXTB, ONLINE_TEXTB, LOAD_TEXTB, SETTINGS_TEXTB]

    pygame.font.quit()
