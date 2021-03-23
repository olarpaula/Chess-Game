import games
import logic
from utils.start_app import *
from utils.constants import checkPos
import pygame

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Chess')

# background
BACKGROUND = pygame.image.load('resources/images/bkgr1.jpg')
#show moves, flip
LOAD = [True, False]


def main():
    window.blit(BACKGROUND,(0, 0))
    window.blit(Main.TITLE_TEXT, Main.TITLE_POS)
    for x, y in zip(Main.btns_txt, Main.btns_pos):
         window.blit(x, y[:2])


running = True
while running:
    pygame.display.flip()
    clock.tick(10)

    main()
    x, y = pygame.mouse.get_pos()
    for index, z in enumerate(Main.btns_pos):
        if checkPos(z, x, y):
            window.blit(Main.btns_txtb[index], z[:2])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            # SINGLEPLAYER
            if checkPos(Main.SINGLEPLAYER_POS, x, y):
                games.singleplayer(window, -1, LOAD[0])

            # MULTIPLAYER
            elif checkPos(Main.MULTIPLAYER_POS, x, y):
                games.multiplayer(window, LOAD)

            # ONLINE
            elif checkPos(Main.ONLINE_POS, x, y):

                # add ipv4 address
                games.online(window, '', LOAD[0])

            # LOAD
            elif checkPos(Main.LOAD_POS, x, y):
                type, moves = games.load_game(window)
                if moves:
                    if type == 0:
                        games.singleplayer(window, type, LOAD[0], moves)
                    elif type == 1:
                        games.multiplayer(window, LOAD, moves)

            # SETTINGS
            elif checkPos(Main.SETTINGS_POS, x, y):
                LOAD = logic.settings(window)

    pygame.display.flip()

pygame.quit()
























