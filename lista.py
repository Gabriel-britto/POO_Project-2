from node import Node


class ListaEncadeada:
    def __init__(self):
        self._cabeca = None

    @property
    def cabeca(self):
        return self._cabeca

    def vazia(self):
        self._cabeca == None

    def _buscarnode(self, index):
        apontador = self._cabeca
        for i in range(index):
            if apontador:
                apontador = apontador.prox
            else:
                raise IndexError("List index out of range")
        return apontador

    def inserir(self, index, dado):
        no = Node(dado)
        if index == 0:
            no.prox = self._cabeca
            self._cabeca = no
        else:
            apontador = self._buscarnode(index - 1)
            no.prox = apontador.prox
            apontador.prox = no

    def remover(self, index):
        assert self._cabeca, "Você não pode remover de lista vazia"
        if index == 0:
            if self.vazia():
                self._cabeca = self._cabeca.prox
        else:
            anterior = self._buscarnode(index - 1)
            apontador = anterior.prox
            anterior.prox = apontador.prox

    def tamanho(self):
        count = 0
        atual = self._cabeca
        while atual != None:
            count += 1
            atual = atual.prox
        return count

    def index(self, elemento):
        apontador = self._cabeca
        indice = 0
        while apontador:
            if apontador.dado.cod == elemento:
                return indice
            apontador = apontador.prox
            indice += 1

    def ordenar(self):
        # Adaptação de bubble sort
        ordenado = False
        while ordenado != True:
            ordenado = True
            apontador = self._cabeca
            proximo = self._cabeca.prox

            while proximo != None:
                if apontador.dado.cod > proximo.dado.cod:
                    ordenado = False
                    apontador.dado, proximo.dado = proximo.dado, apontador.dado
                apontador = proximo
                proximo = proximo.prox
        print("Ordenado")

    def __str__(self):
        saida = ""
        a = self._cabeca
        while a != None:
            saida += "{} ".format(a.dado)
            a = a.prox

        return saida

    def __getitem__(self, index):
        apontador = self._buscarnode(index)
        if apontador:
            return apontador.dado
        else:
            raise IndexError("List index out of range")

    def __setitem__(self, index, novo_dado):
        apontador = self._buscarnode(index)
        if apontador:
            apontador.dado = novo_dado
        else:
            raise IndexError("List index out of range")
