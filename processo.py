class Processo:
    def __init__(self, status, custo, descricao, cod):
        self._status = status
        self._custo = custo
        self._descricao = descricao
        self._cod = cod
        self._prox = None
        # Acabei criando um Node desnecessáriamente e utilizando dele para ligar os processos.

    # Methods
    def incrementa_custo(self, valor):
        self._custo += valor

    # Property
    @property
    def status(self):
        return self._status

    @property
    def custo(self):
        return self._custo

    @property
    def descricao(self):
        return self._descricao

    @property
    def cod(self):
        return self._cod

    # Setters
    @status.setter
    def status(self, new_status):
        self._status = new_status

    @custo.setter
    def custo(self, new_custo):
        self._custo = new_custo

    @descricao.setter
    def descricao(self, new_descricao):
        self._descricao = new_descricao

    @cod.setter
    def cod(self, new_cod):
        self._cod = new_cod

    def __str__(self):
        return "\nStatus: {} | Custo: R$ {} | Descrição: {} | Código: {}".format(self._status, self._custo, self._descricao, self._cod)
