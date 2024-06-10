from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import re

# Carrega as credenciais do arquivo token.json
creds = Credentials.from_authorized_user_file('token.json')

# Constrói o serviço
service = build('docs', 'v1', credentials=creds)

# ID do documento
DOCUMENT_ID = 'IdDocumento'

def read_paragraph_element(element):
    """Returns the text in the given ParagraphElement."""
    text_run = element.get('textRun')
    if text_run:
        return text_run.get('content')
    else:
        return ''

def read_strucutural_elements(elements):
    """Recurses through a list of Structural Elements to read a document's text where text may be
    in nested elements."""
    text = ''
    for value in elements:
        if 'paragraph' in value:
            elements = value.get('paragraph').get('elements')
            for elem in elements:
                text += read_paragraph_element(elem)
        elif 'table' in value:
            # The text in table cells are in nested Structural Elements and tables may be
            # nested.
            table = value.get('table')
            for row in table.get('tableRows'):
                cells = row.get('tableCells')
                for cell in cells:
                    text += read_strucutural_elements(cell.get('content'))
        elif 'tableOfContents' in value:
            # The text in the TOC is also in a Structural Element.
            toc = value.get('tableOfContents')
            text += read_strucutural_elements(toc.get('content'))
    return text

# Obtém o conteúdo do documento
document = service.documents().get(documentId=DOCUMENT_ID).execute()

# Obtém o texto do documento
text = read_strucutural_elements(document.get('body').get('content'))

# Encontra todos os pontos finais seguidos de um espaço
indices = [i for i in range(len(text)) if text.startswith('.\n', i)]

# Insere uma quebra de linha após cada ponto final seguido de um espaço
for index in reversed(indices):
    requests = [
        {
            'insertText': {
                'location': {
                    'index': index + 2,  # +2 para ir após o ponto final e o espaço
                },
                'text': '\n'
            }
        }
    ]
    result = service.documents().batchUpdate(
        documentId=DOCUMENT_ID, body={'requests': requests}).execute()
    
links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)

# Substitui cada link por uma imagem
for link in links:
    # Obtém o conteúdo do documento
    document = service.documents().get(documentId=DOCUMENT_ID).execute()

    # Obtém o texto do documento
    text = read_strucutural_elements(document.get('body').get('content'))

    # Encontra o índice do link no texto
    index = text.find(link)

    # Cria uma solicitação para excluir o link
    delete_request = {
        'deleteContentRange': {
            'range': {
                'startIndex': index,
                'endIndex': index + len(link) + 1
            }
        }
    }

    # Cria uma solicitação para inserir a imagem
    insert_request = {
        'insertInlineImage': {
            'location': {
                'index': index
            },
            'uri': link,
            'objectSize': {
                'height': {
                    'magnitude': 250,
                    'unit': 'PT'
                },
                'width': {
                    'magnitude': 250,
                    'unit': 'PT'
                }
            }
        }
    }

    # Cria uma solicitação para atualizar o estilo da imagem
    update_style_request = {
        'updateParagraphStyle': {
            'range': {
                'startIndex': index,
                'endIndex': index + 1
            },
            'paragraphStyle': {
                'alignment': 'CENTER'
            },
            'fields': 'alignment'
        }
    }

    # Adiciona a solicitação de atualização de estilo à lista de solicitações
    requests = [delete_request, insert_request, update_style_request]

    # Executa as solicitações
    result = service.documents().batchUpdate(
        documentId=DOCUMENT_ID, body={'requests': requests}).execute()