import random


def display_board(board):
    print('\n'*100)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


def player_input():

    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('player 1 choose x or o: ').upper()

    if marker == 'X':
        return ('X', 'O')

    return ('O', 'X')


def place_marker(board, marker, pos):
    board[pos] = marker


def win_check(board, mark):
    # logic to chec who is winning on every move
    # all rows, columns and 2 diag
    return ((board[1] == board[2] == board[3] == mark) or (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or (board[7] == board[4] == board[1] == mark) or
            (board[8] == board[5] == board[2] == mark) or (board[9] == board[6] == board[3] == mark) or
            (board[1] == board[5] == board[9] == mark) or (board[7] == board[5] == board[3] == mark))


def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'p1'
    return 'p2'


def space_check(board, pos):
    return board[pos] == ' '


def full_board_check(board):
    if " " in board[1:]:
        return False
    return True


def player_choice(board):
    pos = 0
    while pos not in range(1, 10) or not space_check(board, pos):
        pos = int(input('Chose a position: (1-9) '))

    return pos


def replay():
    choice = input('Play Again? Enter only y/n')
    return choice == 'y'


print("Welcome to tic-tac-toe!")
player1 = input('Please enter your name player 1: ')
player2 = input('Please enter your name player 2: ')
while True:
    # game setup (board, who is first and player markers)
    the_board = [' '] * 10
    p1_marker, p2_marker = player_input()
    print('Your choices')
    print(player1 + ': ' + p1_marker + '\n' + player2 + ': ' + p2_marker)
    turn = choose_first()
    if (turn == 'p1'):
        print(player1 + ' will go first')
    else:
        print(player2 + ' will go first')

    play_game = input('Ready to play? y or n ?').lower()

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    # game play
    while game_on:
        # player 1
        if turn == 'p1':
            # show the board
            display_board(the_board)
            # chose a pos
            pos = player_choice(the_board)
            # place marker
            place_marker(the_board, p1_marker, pos)
            # check if they won or tie
            if win_check(the_board, p1_marker):
                display_board(the_board)
                print(player1 + ' has won!!!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board
                    print('Its a tie!!')
                    game_on = False
                else:
                    turn = 'p2'
            # no tie, no win, pass the turn to p2
        # payer 2
        else:
            # show the board
            display_board(the_board)
            # chose a pos
            pos = player_choice(the_board)
            # place marker
            place_marker(the_board, p2_marker, pos)
            # check if they won or tie
            if win_check(the_board, p2_marker):
                display_board(the_board)
                print(player2+' has won!!!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board
                    print('Its a tie!!')
                    game_on = False
                else:
                    turn = 'p1'
            # no tie, no win, pass the turn to p1
    if not replay():
        break


# test_board = [' '] * 10
# display_board(test_board)
# p1_marker, p2_marker = player_input()
# place_marker(test_board, 'X', 8)
# display_board(test_board)
# sample output:
# X | |O
#   |O|X
# O | |X
# Tyler has won!!!!
# Play Again? Enter only y/n
