from evento import Evento
from eventoOnline import EventoOnline

eventoOnline1 = EventoOnline("Monitoria Matemática Discreta", "Discord")

print(eventoOnline1.nome)
print(eventoOnline1.plataforma)

print(eventoOnline1.toJson()) # Json é muito parecido com o dicionário