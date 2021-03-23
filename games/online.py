import socket
import threading

from logic.online import *

VERSION = "V8"

def main(win, addr, LOAD):
    if addr is None:
        return

    showLoading(win)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((addr, 26104))

    except:
        showLoading(win, 0)
        return


    thread = threading.Thread(target=bgThread, args=(sock,))
    thread.start()

    write(sock, VERSION)

    msg = read()
    if msg == "errVer":
        showLoading(win, 1)

    elif msg == "errBusy":
        showLoading(win, 2)

    elif msg == "errLock":
        showLoading(win, 3)

    elif msg.startswith("GTag"):
        lobby(win, sock, int(msg[4:]), LOAD)

    sock.close()
    thread.join()
    flush()