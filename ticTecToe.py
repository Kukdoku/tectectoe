#### NOTE : In this program pycharm special emoji or sybol is used please use this program in emoji competable compiler

# Game Tic Tec Toe

# Game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# if game is still going
game_still_going = True

# define winner
winner = None

# whos turn is it

player1 = input("write the name of first player 🙋🙋‍::")

t = ['⛄','❌','🎂','🚗','✈']
print(t)
symbol1 = input("select your symbol 1 to 5::")

while(symbol1 not in ['1','2','3','4','5']):
    symbol1 = input("select your symbol 1 to 5::")
symbol1 = t[int(symbol1)-1]

player2 = input("write the name of second player🙋🙋::")

t = ['🔘','💥','❤','🐶','🐕']

print(t)
symbol2 = input("select your symbol 1 to 5::")

while(symbol2 not in ['1','2','3','4','5']):
    symbol2 = input("select your symbol 1 to 5::")
symbol2 = t[int(symbol2)-1]


current_player = symbol1



# Game board display function

def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


# game play function
# loop_time = 0

def play_game():
    # display the board
    display_board()



    while game_still_going:


        handle_turn(current_player)


        check_if_game_over()


        flip_player()



    if winner == symbol1:
        print("winner:: " + str(player1) + str(symbol1))
    elif winner == symbol2:
        print("winner:: "+ str(player2) + str(symbol2))
    elif winner == None:
        print("Tie :: Play agin ")


# handle player

def handle_turn(player):

    # position = int(position) -1
    global position

    if(current_player == symbol1):
        print("🙋‍♀ "+ player1 + symbol1 + "'s turn")
    else:
        print("🙋‍♀ "+ player2 + symbol2 + "'s turn")

    position = input("choose a position from 1-9 which is not choisen before::🚀🚀")

    choice = ['1','2','3','4','5','6','7','8','9']


    while(position not in choice or board[int(position) - 1] != "-" ):
        position = input("Go agin choose 1 to 9 and empty choise  🛤🙋::‍")
            # position = input("Try again with valid input form 1 to 9  🛤🙋::‍")
        # if(perfect_choice == False):



    # position = int(position)





    position = int(position) -1


    board[position] = player
    display_board()

def check_if_game_over():

    global  loop_time

    # check if win()
    check_for_winner()

    # loop_time += 1

    #check if tie
    check_if_tie()



# function to check win

def check_for_winner():

    global winner

    row_winner = check_row()

    column_winner = check_column()

    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner

    elif column_winner:

        winner = column_winner

    elif diagonal_winner:

        winner = diagonal_winner
    else:
        winner = None
    return

    # check row

    # check column

    # check diagonals

def check_row():
    # setup global variables

    global game_still_going

    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    if row1 or row2 or row3:
        game_still_going = False

    # return Winner

    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return


def check_column():

    global game_still_going

    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"

    if col1 or col2 or col3:
        game_still_going = False

    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]
    return

def check_diagonals():

    global game_still_going

    dia1 = board[0] == board[4] == board[8] != "-"
    dia2 = board[2] == board[4] == board[6] != "-"


    if dia1 or dia2:
        game_still_going = False

    if dia1:
        return board[4]
    elif dia2:
        return board[4]
    return

# function to check tie

def check_if_tie():
    global  game_still_going

    if "-" not in board:
        game_still_going = False
        # winner = None
    return


# function to flip player

def flip_player():
    global current_player

    if current_player == symbol1:
        current_player = symbol2
    elif current_player == symbol2:
        current_player = symbol1
    return

play_game()
