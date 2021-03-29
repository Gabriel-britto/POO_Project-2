import processo
import pilha
import fila
import lista


class Advogado:
    def __init__(self, cod_oab):
        self._cod_oab = cod_oab
        self.processosL = lista.ListaEncadeada()
        self.processosP = pilha.PilhaEncadeada()
        self.processosF = fila.FilaEncadeada()

    # Methods
    def maior_custo(self):
        apontador = self.processosL
        for i in range(apontador.tamanho() - 1):
            if apontador[i].custo < apontador[i + 1].custo:
                maior = apontador[i+1]
            elif i == 0:
                maior = apontador[0]
        print("Processo Código: {} | Custo: {}".format(maior.cod, maior.custo))

    def menor_custo(self):
        apontador = self.processosL
        for i in range(apontador.tamanho() - 1):
            if apontador[i].custo > apontador[i+1].custo:
                menor = apontador[i+1]
            elif i == 0:
                menor = apontador[0]
        print("Processo Código: {} | Custo: {}".format(menor.cod, menor.custo))

    def incrementa_custo_processo(self, cod, valor):
        incrementa = self.busca_processo(cod)
        print("Custo do Processo código: {} aumentado! ".format(incrementa.cod, incrementa.custo))
        incrementa.incrementa_custo(valor)
        return incrementa

    def adicionar_processo_P(self, novo_processo):
        self.processosP.inserir(novo_processo)

    def adicionar_processo_L(self, posicao, novo_processo):
        self.processosL.inserir(posicao, novo_processo)

    def adicionar_processo_F(self, novo_processo):
        self.processosF.inserir(novo_processo)

    def remover_processo_P(self):
        self.processosP.remover()

    def remover_processo_L(self, posicao):
        self.processosL.remover(posicao)

    def remover_processo_F(self):
        self.processosF.remover()

    def busca_processo(self, cod):
        indice = self.processosL.index(cod)
        obj = self.processosL[indice]
        return obj

    def ordena_processos(self):
        self.processosL.ordenar()
        print("Objetos ordenados")

    def imprimir_processos(self):
        for i in range(self.processosL.tamanho()):
            print("Processo Posição {} | Código: {} | Status: {}".format(i, self.processosL[i].cod, self.processosL[i].status))

    def mostrar_tam_processosL(self):
        taml = self.processosL.tamanho()
        return taml

    def mostrar_tam_processosP(self):
        tamp = self.processosP.tamanho()
        return tamp

    def mostrar_tam_processosF(self):
        tamf = self.processosF.tamanho()
        return tamf

    # Property
    @property
    def cod_oab(self):
        return self._cod_oab

    # Setter
    @cod_oab.setter
    def cod_oab(self, new_cod_oab):
        self.cod_oab = new_cod_oab

    def __str__(self):
        saida_adv = "Código do Advogado:{}\nProcessos Pilha: {}\nProcessos Fila: {}\nProcessos Lista: {}".format(self.cod_oab, self.processosP, self.processosF, self.processosL)
        return saida_adv
