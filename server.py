import random
import socket
import threading
import time

VERSION = "V8"

players = []
busyPpl = set()
total = 0

PORT = 26104

# main socket
mainSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mainSock.bind(("0.0.0.0", PORT))
mainSock.listen(10)
print("Server started.")

def read(sock, timeout=None):
    sock.settimeout(timeout)
    try:
        msg = sock.recv(1024).decode("utf-8")
        if "X" in msg:
            return read(sock, timeout)

        if msg:
            return msg.strip()
    except:
        pass
    return "quit"

def send_error_buffer(sock, bufsize):
    sent = sock.send(("X" * bufsize).encode("utf-8"))
    if sent < bufsize:
        send_error_buffer(sock, bufsize - sent)

def write(sock, msg):
    if msg:
        buffedmsg = msg + (" " * (1024 - len(msg)))
        try:
            sent = sock.send(buffedmsg.encode("utf-8"))
            if sent < 1024:
                send_error_buffer(sock, 1024 - sent)
                write(sock, msg)
        except:
            pass

def genKey():
    key = random.randint(1000, 9999)
    for player in players:
        if player[1] == key:
            return genKey()
    return key

def getByKey(key):
    for player in players:
        if player[1] == int(key):
            return player[0]

def mkBusy(*keys):
    global busyPpl
    for key in keys:
        busyPpl.add(int(key))

def rmBusy(*keys):
    global busyPpl
    for key in keys:
        busyPpl.discard(int(key))

def onQuit(sock, key):
    global players
    write(sock, "close")
    players.remove((getByKey(key), key))
    rmBusy(key)
    sock.close()

    print("Player{key} has Quit")

def game(sock1, sock2):
    while True:
        msg = read(sock1)
        write(sock2, msg)
        if msg == "quit":
            return True

        elif msg in ["draw", "resign", "end"]:
            return False

def player(sock, key):
    try:
        while True:
            msg = read(sock)

            if msg == "quit":
                onQuit(sock, key)
                return

            elif msg == "pStat":
                print(f"Player{key}: Made request for players Stats.")
                data = list(zip(*players))[1], list(busyPpl)
                if len(data[0]) - 1 in range(10):
                    write(sock, "enum" + str(len(data[0]) - 1))

                for i in data[0]:
                    if i != key:
                        if i in data[1]:
                            write(sock, str(i) + "b")
                        else:
                            write(sock, str(i) + "a")

            elif msg.startswith("rg"):
                print(f"Player{key}: Made request to play with Player{msg[2:]}")
                oSock = getByKey(msg[2:])
                if oSock is not None:
                    if int(msg[2:]) not in busyPpl:
                        mkBusy(key, msg[2:])
                        write(sock, "msgOk")
                        write(oSock, "gr" + str(key))
                        newMsg = read(sock)
                        if newMsg == "ready":
                            print(f"SERVER: Player{key} is in a game")
                            if game(sock, oSock):
                                onQuit(sock, key)
                                return
                            else:
                                rmBusy(key)
                                print(f"SERVER: Player{key} finished the game")

                        elif newMsg == "quit":
                            onQuit(sock, key)
                            write(oSock, "quit")
                            return

                    else:
                        print(f"SERVER: Player{key} requested busy player")
                        write(sock, "errPBusy")
                else:
                    print(f"SERVER: Player{key} Sent invalid key")
                    write(sock, "errKey")

            elif msg.startswith("gmOk"):
                print(f"Player{key}: Accepted Player{msg[4:]} request")
                oSock = getByKey(msg[4:])
                write(oSock, "start")
                print(f"SERVER: Player{key} is in a game")
                if game(sock, oSock):
                    onQuit(sock, key)
                    return
                else:
                    rmBusy(key)
                    print(f"SERVER: Player{key} finished the game")

            elif msg.startswith("gmNo"):
                print(f"Player{key}: Rejected Player{msg[4:]} request")
                oSock = getByKey(msg[4:])
                write(oSock, "nostart")
                rmBusy(key, msg[4:])

    except Exception as e:
        print(e)
        onQuit(sock, key)


def adminThread():
    global mainSock, players

    while True:
        try:
            msg = input().strip()

            if msg == "report":
                print(len(players) +  "players online")
                print(len(players) - len(busyPpl) + " players active.")
                print("Server is running " + threading.active_count() + " threads")
                if players:
                    print(" Players List:")
                    for cnt, (_, player) in enumerate(players):
                        if player not in busyPpl:
                            print(f" {cnt + 1}. Player{player}, Status: Active")
                        else:
                            print(f" {cnt + 1}. Player{player}, Status: Busy")

            elif msg == "kickall":
                latestplayers = list(players)
                for sock, key in latestplayers:
                    write(sock, "close")
                    sock.close()

                while threading.active_count() > 2 or players or busyPpl:
                    time.sleep(0.1)

                print("SERVER: All Players Kicked")

            else:
                print(f"SERVER: Invalid command entered ('{msg}')")

        except Exception as e:
            print(e)


threading.Thread(target=adminThread).start()

while True:
    try:
        newSock, _ = mainSock.accept()
    except:
        break

    total += 1

    if read(newSock, 3) == VERSION:
        if len(players) < 10:
            key = genKey()
            players.append((newSock, key))
            print("SERVER: Connection Successful, assigned key - {key}")
            write(newSock, "GTag" + str(key))
            threading.Thread(target=player, args=(newSock, key)).start()


        else:
            print("SERVER: Rejected connection")
            write(newSock, "errBusy")
            newSock.close()
    else:
        print("SERVER: Rejected connection")
        write(newSock, "errVer")
        newSock.close()

mainSock.close()
