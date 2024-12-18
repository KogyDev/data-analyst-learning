from fasthtml.common import fast_app, serve, Titled
from componentes import gerar_titulo, gerar_formulario

app, routes = fast_app()

@routes ("/") 
def homepage():
    formulario = gerar_formulario()
    return Titeld('Lista do Kogy', formulario)


@routes('/blog')
def homepage():
    return gerar_titulo('Blog','Blog com artigos de Python')


serve()