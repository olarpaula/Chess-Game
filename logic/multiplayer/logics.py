from copy import deepcopy as copy
from utils.constants import ROWS, COLS

def flip(side):
    return int(not side)

def updateFlags(boardS, fro, to, castle):
    if [5, 8, "k"] not in boardS[1][0] or [1, 8, "r"] not in boardS[1][0]:
        castle[0] = False
    if [5, 8, "k"] not in boardS[1][0] or [8, 8, "r"] not in boardS[1][0]:
        castle[1] = False
    if [5, 1, "k"] not in boardS[1][1] or [1, 1, "r"] not in boardS[1][1]:
        castle[2] = False
    if [5, 1, "k"] not in boardS[1][1] or [8, 1, "r"] not in boardS[1][1]:
        castle[3] = False

    enP = None
    if pieceType(boardS, to) == "p":
        if fro[1] - to[1] == 2:
            enP = [to[0], 6]
        elif to[1] - fro[1] == 2:
            enP = [to[0], 3]

    return castle, enP

def samePos(pos1, pos2):
    if pos1[:2] == pos2[:2]:
        return True
    return False

def pieceType(boardS, pos):
    for piece in (boardS[1])[boardS[0]]:
        if samePos(piece, pos):
            return piece[2]

def takenPos(boardS, pos):
    for piece in (boardS[1])[boardS[0]]:
        if piece[:2] == pos:
            return True
    return False

def notTakenPos(board, *positions):
    for pos in positions:
        for side in range(2):
            if takenPos([side, board], pos):
                return False
    return True

def inCheck(boardS):
    for piece in (boardS[1])[boardS[0]]:
        if piece[2] == "k":
            for i in (boardS[1])[flip(boardS[0])]:
                if piece[:2] in availableMoves([flip(boardS[0]), boardS[1]], i):
                    return True
            return False

def legalMoves(boardS, flags):
    for piece in (boardS[1])[boardS[0]]:
        for pos in availableMoves(boardS, piece, flags):
            if not takenPos(boardS, pos):
                if moveTest(boardS, piece[:2], pos):
                    yield [piece[:2], pos]

def endGame(boardS, flags):
    for _ in legalMoves(boardS, flags):
        return False
    return True

def move(boardS, fromPos, toPos, promote="q"):
    UP = 8 if boardS[0]  else 1
    DOWN = 1 if boardS[0] else 8
    allowENP = fromPos[1] == 4 + boardS[0] and toPos[0] != fromPos[0] and notTakenPos((boardS[1]), toPos)
    for piece in (boardS[1])[flip(boardS[0])]:
        if piece[:2] == toPos:
            (boardS[1])[flip(boardS[0])].remove(piece)
            break

    for piece in (boardS[1])[boardS[0]]:
        if piece[:2] == fromPos:
            piece[:2] = toPos
            if piece[2] == "k":
                if fromPos[0] - toPos[0] == 2:
                    move(boardS, [1, DOWN], [4, DOWN])
                elif toPos[0] - fromPos[0] == 2:
                    move(boardS, [8, DOWN], [6, DOWN])

            if piece[2] == "p":
                if toPos[1] == UP:
                    (boardS[1])[boardS[0]].remove(piece)
                    (boardS[1])[boardS[0]].append([toPos[0], UP, promote])
                if allowENP:
                    (boardS[1])[flip(boardS[0])].remove([toPos[0], fromPos[1], "p"])
            break
    return (boardS[1])


def moveTest(boardS, fro, to):
    return not inCheck([boardS[0], move([boardS[0], copy(boardS[1])], fro, to)])

"""
DACA O MISCARE E VALIDA SAU NU
modif in 3.2
"""
def isValidMove(boardS, flags, fromPos, toPos):
    piece = fromPos + [pieceType(boardS, fromPos)]
    if not takenPos(boardS, toPos):
        if toPos in availableMoves(boardS, piece, flags):
            return moveTest(boardS, fromPos, toPos)
    return False

"""
SE FACE MUTAREA, SE UPDATEAZA FLAGUL[castling, enpassant] SI SE FACE FLIP LA TABLA SI SE RETURNEAZA TOATE ACESTE DATE
"""
def makeMove(boardS, fro, to, flags, promote="q", moveAI=False):
    nBoard = move([boardS[0], copy(boardS[1])], fro, to, promote)
    nFlags = updateFlags([boardS[0], nBoard], fro, to, list(flags[0]))
    if moveAI == False:
        return flip(boardS[0]), nBoard, nFlags
    else:
        return nBoard, nFlags


def insideTable(x, y):
    if 0 < x < COLS + 1 and 0 < y < ROWS + 1:
        return True
    return False

def moveBishop(boardS, pos):
    x = pos[0]; y = pos[1]
    for idx in range(1, 8):
        xUp = x + idx; yDown = y + idx
        if insideTable(xUp, yDown):
            yield [xUp, yDown]
            if not notTakenPos(boardS[1], [xUp, yDown]):
                break

    for idx in range(1, 8):
        xUp = x + idx; yUp = y - idx;
        if insideTable(xUp, yUp):
            yield [xUp, yUp]
            if not notTakenPos(boardS[1], [xUp, yUp]):
                break

    for idx in range(1, 8):
        xDown = x - idx; yDown = y + idx
        if insideTable(xDown, yDown):
            yield [xDown, yDown]
            if not notTakenPos(boardS[1], [xDown, yDown]):
                break

    for idx in range(1, 8):
        xDown = x - idx; yUp = y - idx;
        if insideTable(xDown, yUp):
            yield [xDown, yUp]
            if not notTakenPos(boardS[1], [xDown, yUp]):
                break

def moveRook(boardS, pos):
    x = pos[0]; y=pos[1]

    for i in range(1, 8):
        yDown = y + i
        if insideTable(x, yDown):
            yield [x, yDown]
            if not notTakenPos(boardS[1], [x, yDown]):
                break

    for i in range(1, 8):
        yUp = y - i
        if insideTable(x, yUp):
            yield [x, yUp]
            if not notTakenPos(boardS[1], [x, yUp]):
                break

    for i in range(1, 8):
        xDown = x - i
        if insideTable(xDown, y):
            yield [xDown, y]
            if not notTakenPos(boardS[1], [xDown, y]):
                break

    for i in range(1, 8):
        xUp = x + i
        if insideTable(xUp, y):
            yield [xUp, y]
            if not notTakenPos(boardS[1], [xUp, y]):
                break

def moveKnight(pos):
    x = pos[0]; y=pos[1]
    for x1, y1 in (
    (x - 1, y - 2), (x + 1, y - 2), (x + 2, y - 1), (x + 2, y + 1), (x - 1, y + 2), (x + 1, y + 2), (x - 2, y - 1),
    (x - 2, y + 1)):
        if insideTable(x1, y1):
            yield [x1, y1]

def movePawn(boardS, pos, flags):
    x = pos[0]; y = pos[1]

    if boardS[0] == 1:
        if notTakenPos(boardS[1], [x, y+1]):
            yield [x, y+1]
        if pos == [x, 2] and notTakenPos(boardS[1], [x, 3], [x, 4]):
            yield [x, 4]
        for pos in ([x+1, y+1], [x-1, y+1]):
            if takenPos([0, boardS[1]], pos) or flags[1] == pos:
                yield pos

    if boardS[0] == 0:
        if notTakenPos(boardS[1], [x, y-1]):
            yield [x, y-1]
        if pos == [x, 7] and notTakenPos(boardS[1], [x, 6], [x, 5]):
            yield [x, 5]
        for pos in ([x + 1, y - 1], [x - 1, y - 1]):
            if takenPos([1, boardS[1]], pos) or flags[1] == pos:
                yield pos


def moveKing(boardS, pos, flags):
    x = pos[0]; y = pos[1]
    if flags[0] is not None and not inCheck(boardS):
        if flags[0][0] and notTakenPos(boardS[1], [2, 8], [3, 8], [4, 8]):
            if moveTest([0, boardS[1]], [5, 8], [4, 8]):
                yield [3, 8]
        if flags[0][1] and notTakenPos(boardS[1], [6, 8], [7, 8]):
            if moveTest([0, boardS[1]], [5, 8], [6, 8]):
                yield [7, 8]
        if flags[0][2] and notTakenPos(boardS[1], [2, 1], [3, 1], [4, 1]):
            if moveTest([1, boardS[1]], [5, 1], [4, 1]):
                yield [3, 1]
        if flags[0][3] and notTakenPos(boardS[1], [6, 1], [7, 1]):
            if moveTest([1, boardS[1]], [5, 1], [6, 1]):
                yield [7, 1]

    for x1, y1 in ((x, y+1), (x, y-1), (x-1, y), (x+1, y), (x+1, y-1), (x-1, y-1), (x+1, y+1), (x-1, y+1)):
        if insideTable(x1, y1):
            yield [x1, y1]

def availableMoves(boardS, piece, flags=[None, None]):
    x, y, pieceType = piece

    if pieceType == "p":
        yield from movePawn(boardS, [x, y], flags)

    elif pieceType == "n":
        yield from moveKnight([x, y])

    elif pieceType == "b":
        yield from moveBishop(boardS, [x, y])

    elif pieceType == "r":
        yield from moveRook(boardS, [x, y])

    elif pieceType == "q":
        yield from moveBishop(boardS, [x, y])
        yield from moveRook(boardS, [x, y])

    elif pieceType == "k":
        yield from moveKing(boardS, [x, y], flags)


