from fasthtml.common import Div, H1, P, Form, Input, Button

def gerar_titulo(titulo, subtitulo):
    return Div(
        H1(titulo),
        P(subtitulo),
        P(' Esse site foi gerado com fastHTML oiii')
    )
    
    
def gerar_formulario():
    formulario = Form(
        Input(type = 'texto', name='tarefa', placeholder = 'Insira aqui o seu comentário'),
        Button('Submeter'),
        method='post',
        action='/adicionar_tarefa'
    )
    return formulario

def listas_tarefas():
    pass