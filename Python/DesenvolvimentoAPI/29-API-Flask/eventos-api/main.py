from flask import Flask, jsonify
from evento import Evento
from eventoOnline import EventoOnline
import json

app = Flask(__name__) # __name__ e uma variavel especial que contem o nome do modulo que esta sendo executado no momento
eventoOnline1 = EventoOnline("Aula de como ficar rico", "https://pablomarcal")
eventoOnline2 = EventoOnline("Curso super introdutório de Java", "https://gustavoguanabara")
eventoPresencial1 = Evento("Imagine Land", "João Pessoa")
eventoPresencial2 = Evento("Aula de Linguagens Formais", "Centro de Informática - UFPB")

eventos = [eventoOnline1, eventoOnline2, eventoPresencial1, eventoPresencial2]

@app.route("/") # Rota mapeada. A funcao sera executada quando essa rota por selecionada pelo servidor
def index(): 
    return "<h1>Flask configurado!</h1>"  # Já escreve na tela

@app.route("/api/eventos/") # E uma boa pratica terminar a rota com a barra
def listar_eventos():
    lista_eventos = []

    for evento in eventos:
        lista_eventos.append(evento.__dict__) # O __dict__ e um atributo padrao do python que retorna uma representacao em dicionario do objeto
        print(evento.toJSON())

    return jsonify(lista_eventos) #jsonifica algo

# $env:FLASK_APP="main.py"; $env:FLASK_ENV="development"; flask run