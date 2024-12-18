from fasthmtl.common import fast_app, serve

app, routes = fast_app()

@route('/')
def homepage():
    return '<h1> Bem vindo ao site do Kogy veyr</h1>'


serve()