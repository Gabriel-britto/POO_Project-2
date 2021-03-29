from node import Node


class FilaEncadeada:
    def __init__(self):
        self._inicio = None
        self._tamanho = 0

    # Property
    @property
    def inicio(self):
        if self.vazia():
            return "A fila está vazia"
        else:
            return self._inicio

    def vazia(self):
        self._tamanho == 0

    def tamanho(self):
        return self._tamanho

    def inserir(self, dado):
        a = Node(dado)

        b = self._inicio
        if b == None:
            self._inicio = a

        else:
            while b.prox != None:
                b = b.prox

            b.prox = a

        self._tamanho += 1

    def remover(self):
        if self.vazia():
            return "A fila está vazia"

        else:
            self._inicio = self._inicio.prox
            self._tamanho -= 1

    def modificar(self, novo_dado):
        if self.vazia():
            return "Fila vazia"
        else:
            self._inicio.dado = novo_dado

    def __str__(self):
        saida = ""
        a = self._inicio

        while a != None:
            saida += "{} ".format(a.dado)
            a = a.prox

        return saida
