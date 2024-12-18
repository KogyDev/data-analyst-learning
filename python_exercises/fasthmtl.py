from fasthtml.common import FastHTML, serve

app = FastHTML()

@app.get("/")
def homepage():
    return '<h1> Bem vindo ao site do Kogy veyr</h1>'

serve()