from logic.online.utils import *
from utils.constants import *
from logic.multiplayer import *
from utils.online import Online

def lobby(win, sock, key, LOAD):
    clock = pygame.time.Clock()

    playerList = getPlayers(sock)
    if playerList is None:
        return

    showLobby(win, key, playerList)

    while True:
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                write(sock, "quit")
                return

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if checkPos(Online.REFRESH_POS, x, y):
                    playerList = getPlayers(sock)
                    if playerList is None:
                        return

                    showLobby(win, key, playerList)

                if 300 < x < 475:
                    for i in range(len(playerList)):
                        if 122 + 30 * i < y < 148 + 30 * i:
                            write(sock, "rg" + playerList[i][:4])
                            newMsg = read()
                            if newMsg == "msgOk":
                                stat = request(win, None, sock)
                                if stat is None:
                                    return
                                elif stat and chess(win, sock, 0, LOAD):
                                    return

                            playerList = getPlayers(sock)
                            if playerList is None:
                                return
                            showLobby(win, key, playerList)

        if readable():
            msg = read()

            if msg == "close":
                return

            elif msg.startswith("gr"):
                if request(win, msg[2:]):
                    write(sock, "gmOk" + msg[2:])
                    if chess(win, sock, 1, LOAD):
                        return
                    else:
                        playerList = getPlayers(sock)
                        if playerList is None:
                            return
                        showLobby(win, key, playerList)
                else:
                    write(sock, "gmNo" + msg[2:])
                    showLobby(win, key, playerList)


# This is called when user enters chess match, handles chess.
def chess(win, sock, player, show_moves):
    side, board, flags = convertMoves("")

    clock = pygame.time.Clock()
    sel = [0, 0]
    prevsel = [0, 0]

    FLIP = False and player
    while True:
        clock.tick(25)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                write(sock, "quit")
                return True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 50 < x < 450 and 50 < y < 450:
                    x, y = x // 50, y // 50
                    if FLIP:
                        x, y = 9 - x, 9 - y

                    prevsel = sel
                    sel = [x, y]

                elif not (endGame([side, board], flags) or endGame([flip(side), board], flags)):
                    if 0 < x < 70 and 0 < y < 50:
                        write(sock, "draw?")
                        if draw(win, sock):
                            return False

                    if 400 < x < 500 and 450 < y < 500:
                        write(sock, "resign")
                        return False

        showScreen(win, [side, board], flags, sel, show_moves, False, player)
        if readable():
            msg = read()
            if msg == "close":
                return True

            elif msg == "quit" or msg == "resign":
                popup(win, msg)
                write(sock, "end")
                return False

            elif msg == "draw?":
                if draw(win):
                    write(sock, "draw")
                    while readable():
                        if read() == "close":
                            return True
                    return False

                else:
                    write(sock, "nodraw")

            elif side != player:
                fro, to, promote = decode(msg)
                if isValidMove([side, board], flags, fro, to):
                    animate(win, [side, board], fro, to, FLIP)

                    side, board, flags = makeMove([side, board], fro, to, flags, promote)
                    sel = [0, 0]
                else:
                    write(sock, "quit")
                    return True

        if side == player and isValidMove([side, board], flags, prevsel, sel):
            promote = promotePawn(win, [player, board], prevsel, sel)
            write(sock, encode(prevsel, sel, promote))
            animate(win, [player, board], prevsel, sel, FLIP)
            side, board, flags = makeMove([side, board], prevsel, sel, flags, promote)