from random import randint, choice
from time import sleep

print("\n\n         ____  __  ___     ____  __    ___     ____  __  ____ ")
print("        (_  _)(  )/ __)___(_  _)/ _\  / __)___(_  _)/  \(  __)")
print("          )(   )(( (__(___) )( /    \( (__(___) )( (  O )) _) ")
print("         (__) (__)\___)    (__)\_/\_/ \___)    (__) \__/(____)\n\n")

print("    board design:")
print("")
print("       |     |")
print("    A  |  B  |  C")
print("  _____|_____|_____")
print("       |     |")
print("    D  |  E  |  F")
print("  _____|_____|_____")
print("       |     |")
print("    G  |  H  |  I")
print("       |     |")

print("\n\nTo make a move, enter the letter corresponding to the square in which you want to move (Aa-Ii)\n")
sleep(2)

tictactoe = False
first_move = -1
p_moves = []
m_moves = []
game_on = True
move_indices = [0, 1, 2, 3, 4, 5, 6, 7, 8]
MOVE_INDICES = [20, 26, 32, 74, 80, 86, 128, 134, 140]
ROWS_AND_COLUMNS = [(0, 1, 2), (0, 3, 6), (0, 4, 8), (1, 4, 7), (2, 4, 6), (2, 5, 8),  (3, 4, 5), (6, 7, 8)]
board_list = []


def print_board(board_list):
    for c in board_list:
        print(c, end="")


def make_board_list():

    for i in range(9):
        for n in range(18):
            if n==17:
                board_list.append("\n")
            if (n==5) or (n==11):
                board_list.append('|')
            if (i == 2 and n != 5) and (i == 2 and n != 11) and (i==2 and n !=17):
                board_list.append('_')
            elif (i == 5 and n != 5) and (i==5 and n!=11) and (i==5 and n !=17):
                board_list.append('_')
            elif (n != 17) and (n != 11) and (n != 5) and (i != 2) and (i != 5):
                board_list.append(' ')


## deprecated -- used to have the letters in the squares until a move was made in the square ##
def set_board(moves):
    i = 65
    for m in moves:
        board_list[m] = chr(i)
        i += 1 


def validate_player_input(player_input):
    if ord(player_input.lower()) not in range(97, 106):
        return False
    else:
        return True


def is_occupied(my_move):
    if board_list[MOVE_INDICES[my_move]] == 'X' or board_list[MOVE_INDICES[my_move]] == '0':
        return True
    else:
        return False


def is_tictactoe(my_move, x0):           #x0 is either 'X' (capital) or '0' (zero) characters
    matched_moves = []
    unmatched_moves = []
    for line in ROWS_AND_COLUMNS:
        if my_move in line:
            for a_move in line:
                if board_list[MOVE_INDICES[a_move]] == x0:
                    matched_moves.append(a_move)
                else:
                    unmatched_moves.append(a_move)
            if len(matched_moves) == 3:
                game_on = False
                return True
        matched_moves.clear()
        unmatched_moves.clear()
    return False


def colinearity(move_list, x0):
    opp_char = '0' if x0 == 'X' else 'X'
    for move in move_list:
        for line in ROWS_AND_COLUMNS:
            if move in line:
                matched_moves = []
                unmatched_moves = []
                for loc_index in line:
                    if board_list[MOVE_INDICES[loc_index]] == x0:
                        matched_moves.append(loc_index)
                    else:
                        unmatched_moves.append(loc_index)
                if len(matched_moves) == 2 and board_list[MOVE_INDICES[unmatched_moves[0]]] != opp_char:
                    return unmatched_moves[0]
    return -1


def is_draw():
    filled = 0
    for line in ROWS_AND_COLUMNS:
        pmoves = 0
        mmoves = 0
        for loc in line:
            if loc in p_moves:
                pmoves += 1
            if loc in m_moves:
                mmoves += 1
        if pmoves >= 1 and mmoves >= 1:
            filled += 1
    if filled == 8:
        return True
    else:
        return False


def move():

    global game_on
    global first_move
    print_board(board_list)
    if first_move == -1:
        first_move = randint(0, 1)
    else:
        first_move = abs(first_move-1)


    if first_move:
        while 1 == 1:
            sleep(5)
            p_input = input("\nEnter the letter that corresponds to the move you would like to make (ie 'a' or 'd'): \n")
            move_loc_index = ord(p_input.lower()) - 97
            if validate_player_input(p_input) and not is_occupied(move_loc_index):
                p_moves.append(move_loc_index)
                board_list[MOVE_INDICES[move_loc_index]] = 'X'
                if is_tictactoe(move_loc_index, 'X'):
                    print_board(board_list)
                    print("\nTic-Tac-Toe! You win the game!")
                    game_on = False
                return
            else:
                continue
    else:
        print(f"\nThe machine moves ...\n")
        sleep(2)
        if len(p_moves + m_moves) == 0:
            board_list[MOVE_INDICES[4]] = '0'
            m_moves.append(ord('e')-97)
        else:
            ret_val = colinearity(m_moves, '0')
            if ret_val != -1:
                board_list[MOVE_INDICES[ret_val]] = '0'
                m_moves.append(ret_val)
                if is_tictactoe(ret_val, '0'):
                    print_board(board_list)
                    print("\nTic-Tac-Toe! Sorry, you lost :(")
                    game_on = False
                    return
            ret_val = colinearity(p_moves, 'X')
            if ret_val != -1:
                board_list[MOVE_INDICES[ret_val]] = '0'
                m_moves.append(ret_val)
                return
            remaining = list(set(move_indices).difference(p_moves + m_moves))
            choice_index = choice(remaining)
            m_moves.append(choice_index)
            next_move = MOVE_INDICES[choice_index]
            board_list[next_move] = '0'

make_board_list()

#set_board(MOVE_INDICES)

while game_on:
    move()
    if is_draw():
        game_on = False
        print_board(board_list)
        print("The game is drawn--neither player can win!")



