import socket
import queue
q = queue.Queue()

def bgThread(sock):
    try:
        while True:
            msg = sock.recv(1024).decode("utf-8")

            if not msg:
                if q.empty():
                    q.put("close")
                return

            if "X" not in msg:
                q.put(msg.strip())
    except:
        if q.empty():
            q.put("close")

def read():
    return q.get()

def readable():
    return not q.empty()

def flush():
    while readable():
        read()

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


def getPlayers(sock):
    write(sock, "pStat")

    msg = read()
    if msg.startswith("enum"):
        data = []
        for i in range(int(msg[-1])):
            newmsg = read()
            if newmsg == "close":
                return None
            else:
                data.append(newmsg)
        return tuple(data)