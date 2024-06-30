import json

class Evento:
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def toString(self):
        return f"Nome: {self.nome}"
    
    def toJson(self):
        return json.dumps({
            "nome": self.nome
        })