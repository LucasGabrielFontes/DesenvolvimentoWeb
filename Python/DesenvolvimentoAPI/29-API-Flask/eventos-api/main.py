from flask import Flask

app = Flask(__name__) # __name__ e uma variavel especial que contem o nome do modulo que esta sendo executado no momento

@app.route("/") # Rota mapeada. A funcao sera executada quando essa rota por selecionada pelo servidor
def index(): 
    return "<h1>Vasco da Gama e nada mais. VASCO!</h1>" # Já escreve na tela

# Flask facilita muito, rapaz. Ta maluco

# $env:FLASK_APP="main.py"; $env:FLASK_ENV="development"; flask run