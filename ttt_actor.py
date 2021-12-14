import random as rd
import copy as cp
import math as mt

class TTTActor():
    '''
    Creates an actor for the 7x7 Tic Tac Toe.
    '''

    def __init__(self, number, game, use_minimax=False) -> None:
        self.number = number
        self.game = game
        self.use_minimax = use_minimax

    def make_move(self) -> list:
        '''
        Choses the move the actor will make next. Returns a list
        of coordinates [x, y]
        '''

        # valores iniciais
        board = self.game.get_board()
        valid_moves = self.valid_moves(board)
        non_fatal_moves = set()

        # verifica quais movimentos são vencedores ou fatais
        for move in valid_moves:
            if self.check_winning_move(move, board, self.number):
                return move
            if not self.check_losing_move(move, board, self.number):
                non_fatal_moves.add(move)

        # escolher o melhor movimento
        if len(non_fatal_moves) == 0:
            move = self.choose_best_move(valid_moves, board, self.number)

        else:
            move = self.choose_best_move(non_fatal_moves, board, self.number)

        return move

    def valid_moves(self, board=None) -> set:
        '''
        Returns a list of valid moves in a board.
        '''

        if board == None:
            board = self.game.get_board()

        # verifica em todo o campos do tabuleiro quais estão vazios
        # e os adiciona a lista de movimentos validos
        valid_moves = set()
        for i in range(7):
            for j in range(7):
                move = (i, j)
                check_result = self.game.check_move(move, board)

                if check_result:
                    valid_moves.add(move)

        return valid_moves

    def check_winning_move(self, move, board=None, number=None) -> bool:
        '''
        Returns whether a move leads to a victory.
        '''

        if board == None:
            board = self.game.get_board()

        if number == None:
            number = self.number

        # cria uma copia do tabuleiro
        board_copy = cp.deepcopy(board)

        # verifica se um movimento resulta na vitória
        if self.game.check_move(move, board):
            board_copy[move[0]][move[1]] = self.game.players[number]

            if self.game.check_board(board_copy) == self.game.players[number]:
                return True

        return False

    def check_losing_move(self, move, board=None, number=None) -> bool:
        '''
        Returns whether a move leads to a loss.
        '''

        if board == None:
            board = self.game.get_board()

        if number == None:
            number = self.number

        players = self.game.get_players()
        board_copy = cp.deepcopy(board)
        board_copy[move[0]][move[1]] = players[number]

        oponent_number = int(not number)
        valid_moves = self.valid_moves(board_copy)

        # verifica se um movimento resulta em derrota

        for valid_move in valid_moves:
            if self.check_winning_move(valid_move, board_copy, oponent_number):
                return True

        return False

    def choose_best_move(self, moves, board=None, number=None) -> tuple:
        '''
        Returns the best move following a set of rules.
        '''

        if board == None:
            board = self.game.get_board()

        if number == None:
            number = self.number

        oponent_number = int(not number)
        players = self.game.get_players()

        op_rewards = [8, 16]
        self_rewards = [2, 3]
        empty_rewards = [1]

        # melhores valores iniciais
        best = (rd.choice(tuple(moves)), 0)
        box = [best]

        # aplica as regras de pontuação para todos os movimentos
        # possíveis
        for move in moves:
            x, y = move[0], move[1]
            score_op = 0
            score_self = 0

            # verificações do oponente

            # horizontal
            if x >= 0:
                if y <= 5:
                    if board[x][y+1] == players[oponent_number]:
                        score_op += op_rewards[0]

                        if y < 5:
                            if board[x][y+2] in [players[oponent_number], ' ']:
                                score_op += empty_rewards[0] if board[x][y+2] == ' ' else op_rewards[1]

            if x <= 6:
                if y >= 1:
                    if board[x][y-1] == players[oponent_number]:
                        score_op += op_rewards[0]

                        if y > 1:
                            if board[x][y-2] in [players[oponent_number], ' ']:
                                score_op += empty_rewards[0] if board[x][y-2] == ' ' else op_rewards[1]

            # vertical
            if y >= 0:
                if x <= 5:
                    if board[x+1][y] == players[oponent_number]:
                        score_op += op_rewards[0]

                        if x < 5:
                            if board[x+2][y] in [players[oponent_number], ' ']:
                                score_op += empty_rewards[0] if board[x+2][y] == ' ' else op_rewards[1]

            if y <= 6:
                if x >= 1:
                    if board[x-1][y] == players[oponent_number]:
                        score_op += op_rewards[0]

                        if x > 1:
                            if board[x-2][y] in [players[oponent_number], ' ']:
                                score_op += empty_rewards[0] if board[x-2][y] == ' ' else op_rewards[1]

            # diagonal principal
            if x >= 0 and y >= 0:
                if x <= 5 and y <= 5:
                    if board[x+1][y+1] == players[oponent_number]:
                        score_op += op_rewards[0]

                        if x < 5 and y < 5:
                            if board[x+2][y+2] in [players[oponent_number], ' ']:
                                score_op += empty_rewards[0] if board[x+2][y+2] == ' ' else op_rewards[1]

            if x <= 6 and y <= 6:
                if x >= 1 and y >= 1:
                    if board[x-1][y-1] == players[oponent_number]:
                        score_op += op_rewards[0]

                        if x > 1 and y > 1:
                            if board[x-2][y-2] in [players[oponent_number], ' ']:
                                score_op += empty_rewards[0] if board[x-2][y-2] == ' ' else op_rewards[1]

            # diagonal secundária
            if x <= 6 and y >= 0:
                if x >= 1 and y <= 5:
                    if board[x-1][y+1] == players[oponent_number]:
                        score_op += op_rewards[0]

                        if x > 1 and y < 5:
                            if board[x-2][y+2] in [players[oponent_number], ' ']:
                                score_op += empty_rewards[0] if board[x-2][y+2] == ' ' else op_rewards[1]

            if x >= 0 and y <= 6:
                if x <= 5 and y >= 1:
                    if board[x+1][y-1] == players[oponent_number]:
                        score_op += op_rewards[0]

                        if x < 5 and y > 1:
                            if board[x+2][y-2] in [players[oponent_number], ' ']:
                                score_op += empty_rewards[0] if board[x+2][y-2] == ' ' else op_rewards[1]


            # verificações do ator

            # horizontal
            if x >= 0:
                if y <= 5:
                    if board[x][y+1] == players[number]:
                        score_self += self_rewards[0]

                        if y < 5:
                            if board[x][y+2] in [players[number], ' ']:
                                score_self += 1 if board[x][y +
                                                       2] == ' ' else self_rewards[1]

            if x <= 6:
                if y >= 1:
                    if board[x][y-1] == players[number]:
                        score_self += self_rewards[0]

                        if y > 1:
                            if board[x][y-2] in [players[number], ' ']:
                                score_self += 1 if board[x][y -
                                                       2] == ' ' else self_rewards[1]

            # vertical
            if y >= 0:
                if x <= 5:
                    if board[x+1][y] == players[number]:
                        score_self += self_rewards[0]

                        if x < 5:
                            if board[x+2][y] in [players[number], ' ']:
                                score_self += 1 if board[x +
                                                    2][y] == ' ' else self_rewards[1]

            if y <= 6:
                if x >= 1:
                    if board[x-1][y] == players[number]:
                        score_self += self_rewards[0]

                        if x > 1:
                            if board[x-2][y] in [players[number], ' ']:
                                score_self += 1 if board[x -
                                                    2][y] == ' ' else self_rewards[1]

            # diagonal principal
            if x >= 0 and y >= 0:
                if x <= 5 and y <= 5:
                    if board[x+1][y+1] == players[number]:
                        score_self += self_rewards[0]

                        if x < 5 and y < 5:
                            if board[x+2][y+2] in [players[number], ' ']:
                                score_self += empty_rewards[0] if board[x+2][y+2] == ' ' else self_rewards[1]

            if x <= 6 and y <= 6:
                if x >= 1 and y >= 1:
                    if board[x-1][y-1] == players[number]:
                        score_self += self_rewards[0]

                        if x > 1 and y > 1:
                            if board[x-2][y-2] in [players[number], ' ']:
                                score_self += empty_rewards[0] if board[x-2][y-2] == ' ' else self_rewards[1]

            # diagonal secundaria
            if x <= 6 and y >= 0:
                if x >= 1 and y <= 5:
                    if board[x-1][y+1] == players[number]:
                        score_self += self_rewards[0]

                        if x > 1 and y < 5:
                            if board[x-2][y+2] in [players[number], ' ']:
                                score_self += empty_rewards[0] if board[x-2][y+2] == ' ' else self_rewards[1]

            if x >= 0 and y <= 6:
                if x <= 5 and y >= 1:
                    if board[x+1][y-1] == players[number]:
                        score_self += self_rewards[0]

                        if x < 5 and y > 1:
                            if board[x+2][y-2] in [players[number], ' ']:
                                score_self += empty_rewards[0] if board[x+2][y-2] == ' ' else self_rewards[1]


            score = max(score_op, score_self)

            if score > best[1]:
                best = (move, score)
                box = [best]

            elif score == best[1]:
                box.append((move, score))

        new_box = []
        for item in box:
            new_box.append(item[0])

        if len(new_box) < 5 and self.use_minimax:
            result = self.minimax_best_move(new_box)
        else:
            result = rd.choice(new_box)
            
        return result

    def minimax_best_move(self, moves, board=None) -> list:
        if board == None:
            board = self.game.get_board()

        best_score = -mt.inf
        best_move = None
        players = self.game.get_players()

        for move in moves:
            board_copy = cp.deepcopy(board)
            board_copy[move[0]][move[1]] = players[self.number]
            score = self.minimax(False, self.number,
                                 board_copy, 4, -mt.inf, mt.inf)

            if score !=  0:
                print(score)
                input()


            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def minimax(self, max_turn, maximizer, board, max_depth, alpha, beta) -> int:
        state = self.game.check_board(board)
        players = self.game.get_players()

        if state == ' ':
            return 0

        elif state == players[maximizer]:
            return 1

        elif state == players[int(not maximizer)]:
            return -1

        if max_depth == 0:
            return 0

        scores = []
        valid_moves = self.valid_moves(board)

        for move in valid_moves:
            board_copy = cp.deepcopy(board)
            board_copy[move[0]][move[1]] = players[maximizer] if not max_turn else players[int(
                not maximizer)]
            scores.append(self.minimax(not max_turn, maximizer,
                          board, max_depth-1, alpha, beta))

            if max_turn:
                alpha = max(alpha, max(scores))
            else:
                beta = min(beta, min(scores))

            if beta <= alpha:
                break

        return max(scores) if max_turn else min(scores)

    def get_number(self) -> int:
        '''
        Returns the actor number.
        '''

        return self.number

    def __str__(self) -> str:
        '''
        Returns the actor's data.
        '''

        string = f'Actor number: {self.number}'

        return string
