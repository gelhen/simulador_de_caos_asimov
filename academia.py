import random
from pprint import pprint


class Academia:
    def __init__(self):
        self.halteres = [i for i in range(10, 36) if i % 2 == 0]
        self.porta_halteres = {}
        self.reiniciar_o_dia()

    def reiniciar_o_dia(self):
        self.porta_halteres = {i:i for i in self.halteres}

    def listar_halteres(self):
        return [i for i in self.porta_halteres.values() if i != 0]

    def pegar_halteres(self, peso):
        # Verifica se o halter está disponível pelo indice
        haltere_posicao = list(self.porta_halteres.values()).index(peso)
        key_haltere = list(self.porta_halteres.keys())[haltere_posicao]
        # Remove o haltere do porta halteres
        self.porta_halteres[key_haltere] = 0
        return peso

    def devolver_halteres(self, pos, peso):
        self.porta_halteres[pos] = peso

    # retorna quantidade de halteres fora do lugar em porcentagem
    def calcular_caos(self):
        caos = [i for i, j in self.porta_halteres.items() if i != j]
        return len(caos) / len(self.halteres)


self = Academia()


if __name__ == "__main__":
    print(self.halteres)
    pprint(self.porta_halteres)
    print(self.listar_halteres())
    print(self.calcular_caos())
