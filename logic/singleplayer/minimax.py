from logic.singleplayer.heuristics import evaluatePiece
from logic.multiplayer.logics import legalMoves, endGame, makeMove

INF = 10000
DEPTH = 2

"""
aceatsa functie defineste algoritmul minimax utilizat in jocul singleplayer, avand o performanta buna, utilizandu-se strategia alpha beta prunning
"""
def minimax(boardS, flags):
    if not boardS[0]:
        return alphaBetaMax(boardS[0], boardS[1], flags, depth=DEPTH, alpha=-INF, beta=INF)
    else:
        return alphaBetaMin(boardS[0], boardS[1], flags, depth=DEPTH, alpha=-INF, beta=INF)

def alphaBetaMax(side, board, flags, depth=DEPTH, alpha=-INF, beta=INF):
    if depth == 0 or endGame([side, board], flags):
        return evaluatePiece([side, board])
    max_eval = -INF
    for fro, to in legalMoves([side, board], flags):
        move = makeMove([side,  board], fro, to, flags, moveAI=True)
        curr_eval = alphaBetaMin(1, *move, depth - 1, alpha, beta)
        if curr_eval > max_eval:
            max_eval = curr_eval
            best_move = (fro, to)
        alpha = max(alpha, max_eval)
        if alpha >= beta:
             break

    if depth == DEPTH:
        return best_move
    else:
        return max_eval


def alphaBetaMin(side, board, flags, depth=DEPTH, alpha=-INF, beta=INF):
    if depth == 0 or endGame([side, board], flags):
        return evaluatePiece([side, board])
    min_eval = INF
    for fro, to in legalMoves([side, board], flags):
        move = makeMove([side, board], fro, to, flags, moveAI=True)
        curr_eval = alphaBetaMax(0, *move, depth - 1, alpha, beta)
        if curr_eval < min_eval:
            min_eval = curr_eval
            best_move = (fro, to)
        beta = min(beta, min_eval)
        if alpha >= beta:
            break

    if depth == DEPTH:
        return best_move
    else:
        return min_eval




