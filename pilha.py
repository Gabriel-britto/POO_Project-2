from node import Node


class PilhaEncadeada:
    def __init__(self):
        self._topo = None
        self._tamanho = 0

    @property
    def topo(self):
        if self.vazia():
            return "A pilha está vazia."
        else:
            return self._topo

    def vazia(self):
        return self._tamanho == 0

    def tamanho(self):
        return self._tamanho

    # Funções
    def inserir(self, dado):
        no = Node(dado)
        no.prox = self._topo
        self._topo = no
        self._tamanho += 1

    def remover(self):
        if self.vazia():
            return print("A pilha está vazia")
        else:
            self._topo = self._topo.prox
            self._tamanho -= 1

    def __str__(self):
        saida = ''
        p = self._topo

        while p != None:
            saida += f'{p.dado} '
            p = p.prox

        return saida

    def modificar(self, novo_dado):
        if self.vazia():
            return "A pilha está vazia"
        else:
            self._topo.dado = novo_dado
