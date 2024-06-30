from evento import Evento

class EventoOnline(Evento): # Classe Evento online extends Evento
    def __init__(self, nome, plataforma): # O método construtor é sobreposto
        super().__init__(nome) # Chama o construtor da super classe
        self._plataforma = plataforma

    @property
    def plataforma(self):
        return self._plataforma
    
    @plataforma.setter
    def plataforma(self, plataforma):
        self._plataforma = plataforma

    def toString(self): # O método da super classe é sobreposto
        return f"Nome: {self.nome}\nPlataforma: {self.plataforma}"
        