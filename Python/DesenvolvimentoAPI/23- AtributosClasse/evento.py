class Evento:
    id = 1 # Essa variável será compartilhada por todos os objetos da classe
    exemplo = 2

    def __init__(self, nome, local = ""):
        self.nome = nome
        self.local = local
        self.id = Evento.id # Se refere a um atributo de objeto, não de classe
        Evento.id += 1 # O nome da classe é utilizado para acessar o atributo de classe

    def toString(self):
        return self.nome + " em " + self.local + " id: " + str(self.id)
    
    @classmethod
    def criaEventoOnline(classe, nome):
        evento = classe(nome, f"internet{Evento.id}")
        return evento
    
    @staticmethod
    def calculaPessoas(area):
        return area*2

evento = Evento("Jogo do Vasco", "Rio de Janeiro")
print(evento.toString())

eventoOnline = evento.criaEventoOnline("Transmissão jogo do Vasco")
print(eventoOnline.toString())

print(evento.calculaPessoas(20))

print(eventoOnline.exemplo) # Se o objeto não tiver o atributo de objeto, o atributo de classe é buscado