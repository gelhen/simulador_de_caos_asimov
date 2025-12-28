from ast import main
import random
import os


class TicTacToe:
    def __init__(self) -> None:
        self.reset()

    def print_board(self):
        print("")
        separado_boad = "-----------"
        for linha in range(0,3):
            line_board = ""
            for coluna in range(0,3):
                line_board += " " + self.board[linha][coluna]
                if coluna < 2:
                    line_board += ' | '
            if linha > 0:
                print(separado_boad)
            print (line_board)
        print("")

    def reset(self):
        self.board = [[" "," "," "], [" "," "," "], [" "," "," "]]
        self.done = ""


    def check_win_or_draw(self):
        dict_win = {}

        for i in ['X', 'O']:
            #Horizonais
            for linha in range(0,3):
                if i in dict_win: 
                    dict_win[i] = (self.board[linha][0] == self.board[linha][1]  == self.board[linha][2] == i) or dict_win[i]
                else:
                    dict_win[i] = (self.board[linha][0] == self.board[linha][1]  == self.board[linha][2] == i)
                    
            #Verticais
            for colunas in range(0,3):
                dict_win[i] = (self.board[0][colunas] == self.board[1][colunas]  == self.board[2][colunas] == i) or dict_win[i]
            #Diagonais
            dict_win[i] = (self.board[0][0] == self.board[1][1]  == self.board[2][2] == i) or dict_win[i]
            dict_win[i] = (self.board[2][0] == self.board[1][1]  == self.board[0][2] == i) or dict_win[i]
            #
        if dict_win['X']:
            self.done = 'X'
            print("X Venceu!!!!")
            return
        if dict_win['O']:
            self.done = 'O'
            print("O Venceu!!!!")
            return
        
        #Verificar se está tudo preenchido
        c = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    c += 1
                    break
        
        if c == 0:
            self.done = 'd'
            print("Empate")
            return
    
    def get_player_move(self):
        invalid_move = True

        while invalid_move:
            try:
                # Solicita ao jogador a entrada de X e Y
                print("Digite a linha de seu próximo lance:")
                x = int(input())

                print("Digite a coluna de seu próximo lance:")
                y = int(input(""))

                if x not in (0,1,2) or y not in (0,1,2):
                    print("Coordenadas inválidas")
                    continue

                if self.board[x][y] != " ":
                    print("Posição já preenchida")
                    continue

            except Exception as e:
                print (e)
                continue

            invalid_move = False
            self.board[x][y] = "X"
        

    def make_move(self):
        list_moves = []

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    list_moves.append((i,j))
            
        if len(list_moves) > 0:
            x,y = random.choice(list_moves)
            self.board[x][y] = "O"


if __name__ == "__main__":
    tic_tac_toe = TicTacToe()
    next = 0

    while next == 0:
        os.system('clear')
        tic_tac_toe.print_board()
        while tic_tac_toe.done == "":
            tic_tac_toe.get_player_move()
            tic_tac_toe.make_move()
            os.system('clear')
            tic_tac_toe.print_board()
            tic_tac_toe.check_win_or_draw()
    
        next = input("Digite 1 para sair do jogo ou qualquer tecla para jogar novamente.")

        # Verifica se a variável next é nula e, se for, define como 0
        if not isinstance(next, int):
            next = 0
        else:
            next = int(next)

        if next == 1:
            break
        else:
            tic_tac_toe.reset()
            next = 0

        