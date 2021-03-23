"""
Acest fisier contine functii necesare in manipularea datelor unui joc in fisiere
"""
import glob

"""
functie care returneaza lista fisierelor de jocuri salvate
"""
def getFiles():
    dir = ['resources\games\singleplayer', 'resources\games\multiplayer']
    txtfiles = [[], []]

    for type in range(2):
        for file in glob.glob(dir[type] + "\*.txt"):
            txtfiles[type].append(file)

    return txtfiles

"""
functie care returneaza o lista de jocuri din cadrul unei liste de fisiere salvate
"""
def getGames():
    txtFiles = getFiles()
    games = [[], []]

    for type in range(2):
        for file in txtFiles[type]:
            f = open(file, 'r')
            games[type].append(f.readlines())

    return games

"""
functie care returneaza o lista de mutari din cadrul unei liste de jocuri salvate
"""
def getMoves():
    games = getGames()
    moves = [[], []]

    for type in range(2):
        for game in games[type]:
            move = (game[3].split(': '))[1]
            moves[type].append(move[:len(move)-1])

    return moves




