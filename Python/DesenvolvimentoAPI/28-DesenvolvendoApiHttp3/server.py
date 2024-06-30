from http.server import HTTPServer, BaseHTTPRequestHandler
from eventoOnline import EventoOnline
from evento import Evento
import json

eventoOnline1 = EventoOnline("Aula de Python", "https://tamarcado.com/eventos/id=")
eventoOnline2 = EventoOnline("Aula de Java", "https://tamarcado.com/eventos/id=")
eventoPresencial1 = Evento("Aula de Linguagens Formais", "Centro de Informática - UFPB")

eventos = [eventoOnline1, eventoOnline2, eventoPresencial1]

class SimpleHandler (BaseHTTPRequestHandler):

    visitas = 0

    def do_GET(self):
        SimpleHandler.visitas += 1

        if (self.path == '/'):
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()

            data = f"""
            <html>
                <head>
                    <title>Resposta</title>
                </head>
                <body>
                    <p>Testando o servidor HTTP!</p>
                    <p>Diretório: {self.path}</p>
                    <p>Número de visitas: {self.visitas}</p>
                </body>
            </html> 
            """.encode() # Dessa maneira, o usuario e forcado a consumir os dados da maneira preestabelecida. Retornando os dados como json, isso fica a cargo do servidor decidir

            self.wfile.write(data)
        elif (self.path == '/eventos'):
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()

            stylesheet = """
            <style>
                table {
                    border-collapse: collapse;
                }

                td, th{
                    border: 1px solid #dddddd;
                    text-align: left;
                    padding: 8px;
                }
            </style>
            """

            eventos_html = ""

            for evento in eventos:
                eventos_html += f"""
                <tr>
                    <td>{evento.nome}</td>
                    <td>{evento.local}</td>
                </tr>
                """

            data = f"""
            <html>
                <head>
                    {stylesheet}
                </head>
                <table>
                    <tr>
                        <th>Nome</th>
                        <th>Local</th>
                    </tr>
                    {eventos_html}
                </table>
            </html>
            """.encode()

            self.wfile.write(data)
        elif (self.path == '/api/eventos'): # api indica que a resposta sera gerada em json (majoritariamente)
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            lista_dic_eventos = []
            for evento in eventos:
                lista_dic_eventos.append({
                    "nome": evento.nome,
                    "local": evento.local
                })

            data = (json.dumps(lista_dic_eventos)).encode() # Retorna uma representacao em Json de objetos do tipo dicionario

            self.wfile.write(data)

server = HTTPServer(("localhost", 8000), SimpleHandler)

server.serve_forever()
