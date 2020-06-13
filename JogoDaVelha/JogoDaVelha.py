class JogoDaVelha:
    __author__ = "João Queiroz"

    def __init__(self):
        self.__board = [["_"] * 3 for i in range(3)]

    def __mostrarTabuleiro(self):
        print()
        print(f"  \t0 \t1 \t2")
        for i in range(3):
            print(f"{i} \t{self.__board[i][0]} \t{self.__board[i][1]} \t{self.__board[i][2]}")
        print()

    def __setarLugar(self, row : int, column : int, item : str):
        if (self.__board[row][column] == '_'):
            self.__board[row][column] = item
            return True
        return False

    def __verificarSeGanhou(self):
        for row in self.__board:
            if (row[0] == row[1] == row[2] != '_'):
                return True
        for i in range(3):
            if (self.__board[0][i] == self.__board[1][i] == self.__board[2][i] != '_'):
                return True
        if (self.__board[0][0] == self.__board[1][1] == self.__board[2][2] != '_'):
            return True

        if (self.__board[2][0] == self.__board[1][1] == self.__board[0][2] != '_'):
            return True
        return False

    def __deuVelha(self):
        for row in self.__board:
            for column in row:
                if column == "_":
                    return False
        return True

    def startGame(self):
        vez_do_jogador = 0
        jogadores = ["\033[31mX\033[m", "\033[34mO\033[m"]
        while True:
            print(f"\nVez do {vez_do_jogador + 1}º jogador ({jogadores[vez_do_jogador]})" \
                  "\nSelecione a posição que deseja jogar:")
            self.__mostrarTabuleiro()

            row = int(input("Selecione a linha: "))
            while row > 2 or row < 0:
                print("Valor de linha inválido!")
                row = int(input("Selecione a linha: "))

            column = int(input("Seleciona a coluna: "))
            while column > 2 or column < 0:
                print("Valor de coluna inválido!")
                column = int(input("Seleciona a coluna: "))

            while not self.__setarLugar(row, column, jogadores[vez_do_jogador]):
                print("O lugar selecionado já foi oculpado")
                self.__mostrarTabuleiro()
                row = int(input("Selecione a linha: "))
                column = int(input("Seleciona a coluna: "))

            if self.__verificarSeGanhou():
                print(f"\n\n\033[34mO {vez_do_jogador + 1}º jogador ganhou!! Parabéns")
                self.__deuVelha()
                break

            elif self.__deuVelha():
                print('\n\033[34mVishhh deu velha!!')
                self.__deuVelha()
                break

            vez_do_jogador = 0 if(vez_do_jogador == 1) else 1

jogo = JogoDaVelha()

jogo.startGame()