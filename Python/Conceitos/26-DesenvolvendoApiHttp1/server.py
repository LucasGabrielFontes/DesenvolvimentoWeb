from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    visitas = 0 

    def do_GET(self): # Essa nomenclatura e padrao
        SimpleHandler.visitas += 1

        print(f"Visitas: {SimpleHandler.visitas}")

        self.send_response(200) # Envia a resposta da requisicao. Nesse caso, o codigo 200

        self.send_header("Content-Type", "text/html; charset=utf-8") # Especifica a tabela de codificacao de caracteres para o servidor. UTF-8 aceita acentos

        self.send_header("Cabeçalho de teste", "Vasco") # Recebe a chave (nome do cabecalho) e o valor

        self.end_headers() # Informa ao navegador que a resposta terminou, os cabecalhos terminaram de ser enviados (o servidor http python enviar um cabecalho padrao)

        # As tres aspas permitem escrever uma string em varias linhas
        data = f""" 
        <html>
            <head> 
                <title>Olá, mundo!</title> 
            </head>
            <body>
                <p>Testando o servidor HTTP!</p>
                <p>Diretório: {self.path}</p>
            </body>
        </html>
        """.encode()

        self.wfile.write(data) # Escreve no navegador. Envia dados binários, por isso e utilizado o metodo encode()

server = HTTPServer(('localhost', 8000), SimpleHandler) # Recebe como parametros uma tupla com o endereco do servidor e a porta que ele funcionara e a classe do handler a ser utilizado. O handler e responsavel por gerenciar as requisicoes e respostas 

# o BaseHTTPRequestHandler nao lida com requisicoes a nao ser que voce as implemente. E preciso criar um handler que herde de BaseHTTPRequestHandler

server.serve_forever() # Ate o programa ser interrompido, o servidor continuara 'escutando' requisicoes e fornecendo respostas