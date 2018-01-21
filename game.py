import sys

class Player:
    total_games = 0
    draws = 0
    def __init__(self):
        self.wins = 0
        self.loses = 0
    
    def player_won(self):
        self.wins += 1

    def player_lost(self):
        self.loses += 1

x = Player()
o = Player()

def display_board(current_game):
    print '    *     *    '
    print ' {}  *  {}  *  {} '.format(current_game[0][0], current_game[0][1], current_game[0][2])
    print '*' * 15
    print '    *     *    '
    print ' {}  *  {}  *  {} '.format(current_game[1][0], current_game[1][1], current_game[1][2])
    print '*' * 15
    print '    *     *    '
    print ' {}  *  {}  *  {} '.format(current_game[2][0], current_game[2][1], current_game[2][2])

def move_handler(player, legal_moves, current_game):
    print 'Input the cell number you would like to put an \'{}\' in...'.format(player)
    move = raw_input('> ')
    move = move.strip().upper()
    check_move = legal_moves.get(move)

    if move == 'EXIT':
        sys.exit()
    elif move == 'RESTART':
        return None, None, None, True
    elif check_move != None:

        if legal_moves[move] == True:

            legal_moves[move] = False
            current_game = move_switch(player, current_game, move)
            player = 'X' if player == 'O' else 'O'

            return player, legal_moves, current_game, False

        elif legal_moves[move] == False:
            raw_input('Move has already been made... Enter any key and try again.')
            return player, legal_moves, current_game, False
    else:
        raw_input('Input is invalid... Enter any key and try again.' )

    return player, legal_moves, current_game, False

def move_switch(player, current_game, move):

    if move == '1':
        current_game[0][0] = player 
    elif move == '2':
        current_game[0][1] = player
    elif move == '3':
        current_game[0][2] = player
    elif move == '4':
        current_game[1][0] = player
    elif move == '5':
        current_game[1][1] = player
    elif move == '6':
        current_game[1][2] = player
    elif move == '7':
        current_game[2][0] = player
    elif move == '8':
        current_game[2][1] = player
    elif move == '9':
        current_game[2][2] = player

    return current_game

def check_win_or_draw(current_game, legal_moves):
    row1 = current_game[0][0] == current_game[0][1] == current_game[0][2]
    row2 = current_game[1][0] == current_game[1][1] == current_game[1][2]
    row3 = current_game[2][0] == current_game[2][1] == current_game[2][2]

    column1 = current_game[0][0] == current_game[1][0] == current_game[2][0]
    column2 = current_game[0][1] == current_game[1][1] == current_game[2][1]
    column3 = current_game[0][2] == current_game[1][2] == current_game[2][2]

    diagnol1 = current_game[0][0] == current_game[1][1] == current_game[2][2]
    diagnol2 = current_game[0][2] == current_game[1][1] == current_game[2][0]

    winner = row1 or row2 or row3 or column1 or column2 or column3 or diagnol1 or diagnol2
    
    if winner:
        return 'WINNER'
    elif True not in legal_moves.values():
        return 'DRAW'


def main():
    current_game = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
    ]
    legal_moves = {
        '1' : True,
        '2' : True,
        '3' : True, 
        '4' : True,
        '5' : True,
        '6' : True,
        '7' : True,
        '8' : True,
        '9' : True,
    }
    player = ''
    restart = False

    while True:
        print '[Menu: Exit]'
        print 'Team X Record: {}-{}-{} | Team O Record: {}-{}-{} | Total Games Played: {}'.format(
            x.wins, x.loses, Player.draws, o.wins, o.loses, Player.draws, Player.total_games
            )
        print 'Welcome to Tic Tac Toe! Who will move first, \'X\' or \'O\'?'
        game_setup = raw_input('> ')
        game_setup = game_setup.strip().upper()
        if game_setup == 'EXIT':
            sys.exit()
        elif game_setup == 'X':
            player = 'X'
            break
        elif game_setup == 'O':
            player = 'O'
            break
        else:
            raw_input('Input not recognized... Enter any key and try again.')

    while True:
        print '[Menu: Restart - Exit]'
        display_board(current_game) 
        player, legal_moves, current_game, restart = move_handler(player, legal_moves, current_game)
        if restart == True: return
        outcome = check_win_or_draw(current_game, legal_moves)
        if outcome == 'WINNER':
            Player.total_games += 1
            if player == 'X':
                o.player_won()
                x.player_lost()
            elif player == 'O':
                x.player_won()
                o.player_lost()
            break
        elif outcome == 'DRAW':
            Player.total_games += 1
            Player.draws += 1
            display_board(current_game)
            print 'Match ended in a draw :-('
            print 'To play again enter any key... To exit enter \'Exit\'.'
            end_game_decision = raw_input('> ')
            end_game_decision = end_game_decision.strip().upper()
            if end_game_decision == 'EXIT':
                sys.exit()
            else:
                return
        else:
            continue
    
    player = 'X' if player == 'O' else 'O'
    display_board(current_game)
    print '\n!*!*!*!*!*!{} wins!*!*!*!*!*!'.format(player)
    print '!*!*!*!*!*!{} wins!*!*!*!*!*!'.format(player)
    print '!*!*!*!*!*!{} wins!*!*!*!*!*!\n'.format(player)
    print 'To play again enter any key... To exit enter \'Exit\'.'
    end_game_decision = raw_input('> ')
    end_game_decision = end_game_decision.strip().upper()
    if end_game_decision == 'EXIT':
        sys.exit()

while True:
    main()