#En lista där sin input skickas till och plasera ditt x i en av de 9 rutor.
board = [' ' for x in range(10)]

#Här nedan så finns alla funktioner.
#Nummertill är var på brädan de finns ett nummer ska vara.
def nummertill(letter,pos):
    board[pos] = letter
#openspace är var de finns en öppen yta på brädan.
def openspace(pos):
    return board[pos] == ' '
#Detta är layouten till hur brädan ser ut och var sina imputs ska vara.
def theboard(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')
#om brädan är full så startas det om.
def boardisdrunk(board):
    if board.count(' ') > 1:
        return False
    else:
        return True
#Denna funktion används för att lysta out om spelaren har vunnit.
def numberuno(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))
#Har väljer spelaren sitt val där de ska plasera ett x på en av de 9 rutor.
def movefirst():
    run = True
    while run:
        move = input("snälla välj en position där du vill sätta in X, Välj 1 to 9\n")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if openspace(move):
                    run = False
                    nummertill('X' , move)
                else:
                    print('Den hära ytan är upptagen')
            else:
                print('snälla vlj ett nummer mellan 1 and 9')

        except:
            print('snälla sätt in ett nummer')
#Denna funktionen låter datorn välja sina plaseringar på brädan där de försöker vinna över dig.
def robomove():
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0  ]
    move = 0

    for let in ['O' , 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if numberuno(boardcopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1 , 3 , 7 , 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = randomman(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = randomman(edgesOpen)
        return move
#Funktion där en random val väljs på brädan.
def randomman(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
#Detta är de första man ser när man öppnar spelet.
def mainman():
    print("Välkomen till spelet!")
    theboard(board)
#Om man förlorar så kommer detta fram.
    while not(boardisdrunk(board)):
        if not(numberuno(board , 'O')):
            movefirst()
            theboard(board)
        else:
            print("Du har förlorat!")
            break
#Om man har vunnit spelet så ska denna print komma upp.
        if not(numberuno(board , 'X')):
            move = robomove()
            if move == 0:
                print(" ")
            else:
                nummertill('O' , move)
                print('datorn placerade en O på denna ytan' , move , ':')
                theboard(board)
        else:
            print("Du har vunnit!")
            break


#Om de blir oavgjort där ingen vinner så ska detta printas.

    if boardisdrunk(board):
        print("det är oavgjort")

while True:
    x = input("Vill du spela? tryck y for ja eller n for nej (y/n)\n")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('--------------------')
        mainman()
    if x.lower() == 'n':
        print("Varför inte :(")
        break
