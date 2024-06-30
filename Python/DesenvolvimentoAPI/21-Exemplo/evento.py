class Evento:
    def __init__(self, nome, local = ""):
        self.nome = nome
        self.local = local

    def toString(self):
        return self.nome + " em " + self.local
    
    @classmethod
    def criaEventoOnline(classe, nome):
        evento = classe(nome, "internet")
        return evento
    
    @staticmethod
    def calculaPessoas(area):
        return area*2

evento = Evento("Jogo do Vasco", "Rio de Janeiro")
print(evento.toString())

eventoOnline = evento.criaEventoOnline("Transmissão jogo do Vasco")
print(eventoOnline.toString())

print(evento.calculaPessoas(20))