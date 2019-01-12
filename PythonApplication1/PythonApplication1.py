import time
import random
from IPython.display import clear_output

take = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
avail = ['0', '1','2','3','4','5','6','7','8','9']
players = [0,'X','O']

def randomPlayer():
    return random.choice((-1,1))

def full_board_check(board):
    return ' ' not in board[1:]

def spacecheck(board, position):
    return board[position] == ' '

def replay():
    return input("Would you like to play again? Enter Yes or No").lower().startswith('y')


def welcome():
    print("Welcome to Tic-Tac-Toe you will play against an opponent.\nHAVE FUN")
    time.sleep(1)
    print("""
░░░░░▄▄▀▀▀▀▀▀▀▀▀▄▄░░░░░
░░░░█░░░░░░░░░░░░░█░░░░
░░░█░░░░░░░░░░▄▄▄░░█░░░
░░░█░░▄▄▄░░▄░░███░░█░░░
░░░▄█░▄░░░▀▀▀░░░▄░█▄░░░
░░░█░░▀█▀█▀█▀█▀█▀░░█░░░
░░░▄██▄▄▀▀▀▀▀▀▀▄▄██▄░░░
░▄█░█▀▀█▀▀▀█▀▀▀█▀▀█░█▄░""")
    time.sleep(0.25)
    print('\n')
    time.sleep(0.25)
    print('\n')
    time.sleep(0.25)
    print('\n')
    time.sleep(0.25)
    print('\n')
    time.sleep(0.25)
    print('\n')
    time.sleep(0.25)
    print('\n')
    time.sleep(0.25)
    print('\n')
    time.sleep(0.25)
    print('\n')
    time.sleep(0.25)
    print('\n')
    time.sleep(0.25)
    print('\n')
    time.sleep(0.25)
    print('\n')
    time.sleep(0.25)
    print('\n')
    time.sleep(0.25)
    print('\n')
    time.sleep(0.25)
    print('\n')
    time.sleep(0.25)
    print('\n')
    time.sleep(0.25)
    print('\n')

def board(a, board):
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + " " + "\t\t " + a[7] + " | " + a[8] + " | " + a[9] + " ")
    print('____________\t\t____________')
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + " " + "\t\t " + a[4] + " | " + a[5] + " | " + a[6] + " ")
    print('____________\t\t____________')
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + " " + "\t\t " + a[1] + " | " + a[2] + " | " + a[3] + " ")
    return board

def placemarker(take, avail, position, marker):
    take[position] = marker
    avail[position] = ' '

def playerchoice(board, player):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not spacecheck(board, position):
        try:
            position = int(input("It's Player %s's turn, Chose your position"%player))
        except:
            print('Im sorry please try again')
    return position

def win_check(board, mark):
    return((board[7] == board[8] == board[9]==mark)or
           (board[4] == board[5] == board[6]==mark)or
           (board[1] == board[2] == board[3]==mark)or
           (board[7] == board[4] == board[1]==mark)or
           (board[8] == board[5] == board[2]==mark)or
           (board[9] == board[6] == board[3]==mark)or
           (board[7] == board[5] == board[3]==mark)or
           (board[9] == board[5] == board[1]==mark))

def finish(player):
    print("""________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
¶¶¶¶______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_______¶¶¶¶ 
¶¶¶_______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________¶¶¶ 
¶¶________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________¶¶¶ 
¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶______¶¶¶ 
¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____¶¶¶¶ 
_¶¶¶___¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶____¶¶¶ 
_¶¶¶¶___¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶__¶¶¶¶ 
___¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶ 
____¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶ 
______¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶___¶¶¶¶¶¶ 
_______________¶¶¶¶¶¶¶¶¶¶¶¶ 
_________________¶¶¶¶¶¶¶¶ 
___________________¶¶¶¶ 
___________________¶¶¶¶ 
___________________¶¶¶¶ 
___________________¶¶¶¶ 
_______________¶¶¶¶¶¶¶¶¶¶¶¶ 
____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
____________¶¶¶____________¶¶¶ 
____________¶¶¶______""" + player +"""_____¶¶¶ 
____________¶¶¶____________¶¶¶ 
____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
__________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶"""
    )

    time.sleep(10)
    print('\n')
    time.sleep(0.5)
    print('\n')
    time.sleep(0.5)
    print('\n')
    time.sleep(0.5)
    print('\n')
    time.sleep(0.5)
    print('\n')
    time.sleep(0.5)
    print('\n')
    time.sleep(0.5)
    print('\n')
    time.sleep(0.5)
    print('\n')
    time.sleep(0.5)
    print('\n')
    time.sleep(0.5)
    print('\n')
    time.sleep(0.5)
    print('\n')
    time.sleep(0.5)
    print('\n')
    time.sleep(0.5)
    print('\n')
    time.sleep(0.5)
    print('\n')
    time.sleep(0.5)
    print('\n')
    time.sleep(0.5)
    print('\n')

def tie():
    print("""_____________________$$$
____________________$___$
_____________________$$$
_____________________$_$
_____________________$_$
___________________$$$_$$$
_________________$$__$$$__$$$
_______________$$__$$$$$$$___$
______________$_______________$
_____________$_________________$
_____________$_________________$
_____________$_____$$$$$$$$$$$$$$$
_____________$____$_______________$
_____________$____$___$$$$$$$$$$$$$
_____________$___$___$___________$$$
_____________$___$___$_$$$___$$$__$$
_____________$___$___$_$$$___$$$__$$
_____________$___$___$___________$$$
_____________$____$___$$$$$$$$$$$$$
_____________$_____$$$$$$$$$$$$$$
_____________$_________________$
_____________$____$$$$$$$$$$$$$$
_____________$___$__$__$__$__$
_____________$__$$$$$$$$$$$$$$
_____________$__$___$__$__$__$
_____________$___$$$$$$$$$$$$$$$
____________$$$_________________$$$
__________$$___$$$_________$$$$$___$$
________$$________$$$$$$$$$__________$$$
_______$__$$_____________________$$$$___$$
____$$$$$___$$$$$$$$______$$$$$$$_______$_$
__$______$$_________$$$$$$______________$_$$
_$____$____$____________________________$_$_$
_$_____$___$______________$$$$$$$$$$$___$_$_$$
_$$$____$___$__$$$$$$$$$$$$__________$___$_$_$$
$___$$$$____$__$_____________________$___$_$$_$
$$$____$___$$__$_____________________$$__$_$__$
$___$__$__$$___$______________________$__$$$__$
$_____$$_$$____$_______________$$$____$__$_$__$
""")
    time.sleep(1)
    print('\n')
    time.sleep(0.5)
    print('\n')
    time.sleep(0.5)
    print('\n')
    time.sleep(0.5)
    print('\n')
    time.sleep(0.5)
    print('\n')
    time.sleep(0.5)
    print('\n')
    time.sleep(0.5)
    print('\n')
    time.sleep(0.5)
    print('\n')
    time.sleep(0.5)
    print('\n')
    time.sleep(0.5)
    print('\n')
    time.sleep(0.5)
    print('\n')
    time.sleep(0.5)
    print('\n')


while True:
    clear_output()
    welcome()
    toggle = randomPlayer()
    player = players[toggle]
    print('For this round, Player %s will go first!' %(player))
    gameon= True
    input('Hit enter to continue')
    while gameon:
        board(take, avail)
        position = playerchoice(take, player)
        placemarker(take, avail, position, player)
        if win_check(take, player) == True:
            board(take, avail)
            print('Congratulations! Player'+ player+' WINS')
            finish(player)
            break
        else:
            if full_board_check(take):
                board(take, avail)
                print('This game is a tie')
                tie()
                break
            else:
                toggle *= -1
                player = players[toggle]
                clear_output()
    take = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    avail = [' ', 1,2,3,4,5,6,7,8,9]

    if not replay():
        break