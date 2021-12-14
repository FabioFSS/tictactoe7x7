class TTT7x7():
    '''
    7x7 Tic Tac Toe. Objective is to put 4 symbols in a row before
    the oponent.
    '''

    def __init__(self) -> None:
        self.board = [[f' ' for i in range(7)] for j in range(7)]
        self.players = {0: 'X', 1: 'O'}
        self.current_player = 0

    def check_move(self, coords, board=None) -> bool:
        '''
        Verifies the validity of a player movement.
        Returns True if valid, False if not valid.
        '''

        if board == None:
            board = self.board

        if coords[0] < 0 or coords[0] > 6:
            return False
        elif coords[1] < 0 or coords[1] > 6:
            return False
        elif board[coords[0]][coords[1]] == ' ':
            return True
        else:
            return False

    def player_move(self, player, coords) -> bool:
        '''
        Places the current player's symbol in a space on the board
        if possible. Returns True if successful, False if not successful.
        '''

        if self.check_move(coords):
            self.board[coords[0]][coords[1]] = self.players[player]
            self.current_player = 1 if self.current_player == 0 else 0
            return True

        else:
            return False

    def check_board(self, board=None) -> str:
        '''
        Checks if the game has ended. Returns the symbol that won if it has ended.
        Returns space if it was a draw.
        '''

        if board == None:
            board = self.board

        # verifica espaços
        count_e = 0
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ' ':
                    count_e += 1

        # retorna espaço se não houver mais espaços
        # no tabuleiro
        if count_e == 0:
            return ' '

        # verifica linhas e colunas
        # i linhas
        for i in range(len(board)):

            # contadores de sequência
            count_h = 1
            count_v = 1

            # espaços visitados na iteração anterior
            prev_h = None
            prev_v = None

            # j colunas
            for j in range(len(board)):

                curr_h = board[i][j]  # valor atual na horizontal

                # verifica se o anterior é igual ao atual
                if prev_h == curr_h and curr_h != ' ':
                    count_h += 1
                else:
                    count_h = 1
                prev_h = curr_h  # atualiza o anterior

                curr_v = board[j][i]  # valor atual na vertical

                # verifica se o anterior é igual ao atual
                if prev_v == curr_v and curr_v != ' ':
                    count_v += 1
                else:
                    count_v = 1
                prev_v = curr_v  # atualiza o anterior

                # retorna o resultado da verificação
                if count_h == 4:
                    return curr_h
                if count_v == 4:
                    return curr_v

        # verificando diagonais direita-esquerda
        for i in range(len(board)):
            count = 1  # contador de sequencia

            prev = None  # espaço visitado na iteração anterior

            for j in range(i+1):
                curr = board[j][i-j]  # espaço curr

                # verifica se o anterior é igual ao curr
                if prev == curr and curr != ' ':
                    count += 1
                else:
                    count = 1
                prev = curr  # curriza o anterior

                if count == 4:
                    return curr

        for i in range(len(board)):
            count = 1  # countador de sequencia

            prev = None  # espaço visitado na iteração anterior

            for j in range(i+1, len(board)):
                curr = board[j][i-j]  # espaço curr

                # verifica se o anterior é igual ao curr
                if prev == curr and curr != ' ':
                    count += 1

                else:
                    count = 1
                prev = curr  # curriza o anterior

                if count == 4:
                    return curr

        # verificando diagonais esquerda-direita
        for i in range(len(board)):
            count = 1  # countador de sequencia

            prev = None  # espaço visitado na iteração anterior

            for j in range(len(board)-i):
                curr = board[i+j][j]  # espaço curr

                # verifica se o anterior é igual ao curr
                if prev == curr and curr != ' ':
                    count += 1
                else:
                    count = 1
                prev = curr  # curriza o anterior

                if count == 4:
                    return curr

        for i in range(1, len(board)):
            count = 1  # countador de sequencia

            prev = None  # espaço visitado na iteração anterior

            for j in range(len(board)-i):
                curr = board[j][i+j]  # espaço curr

                # verifica se o anterior é igual ao curr
                if prev == curr and curr != ' ':
                    count += 1

                else:
                    count = 1
                prev = curr  # curriza o anterior

                if count == 4:
                    return curr

        if count_e == 0:
            return ' '

    def get_board(self) -> list:
        '''
        Returns a list with the board of the game.
        '''

        board_copy = [[value for value in line] for line in self.board]

        return board_copy

    def get_current_player(self) -> int:
        '''
        Returns the current player number.
        '''

        return self.current_player

    def get_players(self) -> dict:
        '''
        Returns the dictionary of players.
        '''

        return self.players

    def __str__(self) -> str:
        '''
        Prints the current board.
        '''
        string = '     '

        for i in range(7):
            string += f'{i}     '

        string += '\n  ' + '------'*7 + '-' + '\n'

        line_count = 0
        for line in self.board:
            string += f'{line_count} |'
            for value in line:
                string += f'  {value}  |'

            string += '\n  ' + '------'*7 + '-' + '\n'
            line_count += 1

        return string

