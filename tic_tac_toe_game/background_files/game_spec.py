import random

# GAME BOARD
board = ['_'] * 9


# PRINTING THE BOARD TO THE CONSOLE
def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"{board[6]} | {board[7]} | {board[8]}")


# WELCOMING THE PLAYER
def welcome_script():
    print('\nHello! welcome to the TIC-TAC-TOE game.')
    print('You are " X " and the computer is " O "')
    print('Here is your board!!!')
    print()


# SELECTING A PLAYER AT RANDOM (COMPUTER, USER)
players = ['X', 'O']
current_player = random.choice(players)


# SWITCHING PLAYER AFTER EVERY ITERATION
def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


# USER SELECTS AN EMPTY TILE
def tile_selection():
    while True:
        try:
            selected_tile = int(input('\nPlease select an empty tile from 1 - 9: '))
            if 1 <= selected_tile <= 9:
                break
            else:
                print('select among 1 - 9 values only!!!')
        except ValueError:
            print('Invalid input. Enter an Integer from 1 - 9.')
    sign_allocation(selected_tile)


# INSERTING SIGNS INTO THE BOARD
def sign_allocation(tile):
    if board[tile-1] != '_':
        print('Selected tile is already filled!!!')
        tile_selection()
    elif board[tile-1] == '_':
        board[tile-1] = current_player
        switch_player()


# CHECKING FOR WIN
def check_for_winner():
    # HORIZONTAL WIN CONDITIONS
    if board[0] == board[1] == board[2] and board[0] != '_':
        return True
    elif board[3] == board[4] == board[5] and board[3] != '_':
        return True
    elif board[6] == board[7] == board[8] and board[6] != '_':
        return True

#     VERTICAL WIN CONDITIONS
    if board[0] == board[3] == board[6] and board[0] != '_':
        return True
    elif board[1] == board[4] == board[7] and board[1] != '_':
        return True
    elif board[2] == board[5] == board[8] and board[2] != '_':
        return True

#   DIAGONAL WIN CONDITIONS
    if board[0] == board[4] == board[8] and board[0] != '_':
        return True
    elif board[2] == board[4] == board[6] and board[2] != '_':
        return True


# TELLING THE COMPUTER TO MAKE A CHOICE
def computer_turn():
    if current_player == 'O':
        computer_choice = random.randint(1, 9)
        while board[computer_choice - 1] != '_':
            computer_choice = random.randint(1, 9)
        sign_allocation(computer_choice)
        print_board()


# GAME RUNNING FUNCTION
def run_game():

    welcome_script()

    if current_player == 'X':
        print('You go first.\n')
        print_board()
    else:
        print('Computer goes first!!!\n')

    while True:
        # GAME TERMINATION CONDITIONS
        if '_' not in board:
            print("It's a tie. Better luck next time...")
            break
        if check_for_winner():
            switch_player()
            print_board()
            print(f"TIC-TAC-TOE...Player {current_player} won!!!\nGAME OVER....")
            break

        # GAME CONTINUATION CONDITIONS
        if current_player == 'O':
            computer_turn()
        else:
            tile_selection()
