class Node:
    def __init__(self, dado = None):
        self._dado = dado
        self._prox = None

    # Property
    @property
    def dado(self):
        return self._dado

    @property
    def prox(self):
        return self._prox

    # Setters
    @dado.setter
    def dado(self, novo):
        self._dado = novo

    @prox.setter
    def prox(self, novo):
        self._prox = novo
