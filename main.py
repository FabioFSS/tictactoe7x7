import os
import time as tm
from ttt_7x7 import TTT7x7
from ttt_actor import TTTActor

def play_jxc(player_number, cpu, game, paused=True):
    move = None
    result = None
    while result == None:
        if paused: tm.sleep(0.5)
        current_player = game.get_current_player()
        current_player_str = 'X' if current_player == 0 else 'O'
        os.system('cls')
        print(game)
        print(f'Ultimo movimento: {move}')
        print(f'Vez do jogador {current_player_str}:\n')

        move = None
        if player_number == current_player:
            while move == None or len(move) != 2:
                move = input('Faca um movimento (linha coluna): ')
                move = move.split()

            move = [int(coord) for coord in move]
            game.player_move(player_number, move)

        else:
            move = cpu.make_move()
            game.player_move(cpu.get_number(), move)

        result = game.check_board()
    
    os.system('cls')
    print(game)
    print(f'Ultimo movimento: {move}')
    print(f'Vez do jogador {current_player_str}:\n')

    return result

def play_jxj(game):
    move = None
    result = None
    while result == None:
        current_player = game.get_current_player()
        current_player_str = 'X' if current_player == 0 else 'O'
        os.system('cls')
        print(game)
        print(f'Ultimo movimento: {move}')
        print(f'Vez do jogador {current_player_str}:\n')

        move = None
        while move == None or len(move) != 2:
            move = input('Faca um movimento (linha coluna): ')
            move = move.split()

        move = [int(coord) for coord in move]
        game.player_move(current_player, move)

        result = game.check_board()

    os.system('cls')
    print(game)
    print(f'Ultimo movimento: {move}')
    print(f'Vez do jogador {current_player_str}:\n')
    
    return result

def play_cxc(game, paused=True):
    cpus = [
        TTTActor(0, game, USE_MINIMAX),
        TTTActor(1, game, USE_MINIMAX)
        ]

    move = None
    result = None
    while result == None:
        if paused: tm.sleep(0.5)
        current_player = game.get_current_player()
        current_player_str = 'X' if current_player == 0 else 'O'
        os.system('cls')
        print(game)
        print(f'Ultimo movimento: {move}')
        print(f'Vez do jogador {current_player_str}:\n')


        move = cpus[current_player].make_move()
        game.player_move(current_player, move)

        result = game.check_board()

    os.system('cls')
    print(game)
    print(f'Ultimo movimento: {move}')
    print(f'Vez do jogador {current_player_str}:\n')
    
    return result

USE_MINIMAX = False

if __name__ == '__main__':
    while True:
        result = None
        choice = None
        while choice not in ['0', '1', '2', '3']:
            os.system('cls')
            print('-----------------------------')
            print('1- Jogador x Computador')
            print('2- Jogador x Jogador')
            print('3- Computador x Computador')
            print('0- Finalizar')
            print('-----------------------------')
            choice = input('\nEscolha uma opção: ')

        if choice == '1':
            game = TTT7x7()

            choice = None
            paused = None
            while choice not in ['0', '1', '2']:
                os.system('cls')
                print('-----------------------------')
                print('1- Primeiro a jogar (X)')
                print('2- Segundo a jogar (O)')
                print('0- Cancelar')
                print('-----------------------------')
                choice = input('\nEscolha sua vez: ')

            if choice == '1':
                cpu_number = 1
                player_number = not(cpu_number)
                cpu = TTTActor(cpu_number, game, USE_MINIMAX)
                result = play_jxc(player_number, cpu, game, False)

            elif choice == '2':
                cpu_number = 0
                player_number = not(cpu_number)
                cpu = TTTActor(0, game, USE_MINIMAX)
                result = play_jxc(player_number, cpu, game, False)

            elif choice == '0':
                choice = None
                continue


        elif choice == '2':
            game = TTT7x7()
            result = play_jxj(game)

        elif choice == '3':
            game = TTT7x7()
            result = play_cxc(game, True)

        elif choice == '0':
            choice = None
            break


        if result == ' ': result = 'Empate!'
        elif result == 'X': result = 'X venceu!'
        elif result == 'O': result = 'O venceu!'

        print(f'{result}')
        input('\nPressione enter para continuar...')
        