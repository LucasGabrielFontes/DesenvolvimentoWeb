class Evento:
    def __init__(self, nome, local):
        self._nome = nome
        self._local = local

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def local(self):
        return self._local

    @local.setter
    def local(self, local):
        self._local = local