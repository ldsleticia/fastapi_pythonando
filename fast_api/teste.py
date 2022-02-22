from fastapi import FastAPI

app = FastAPI()


@app.get("/")  # Raiz, se não digitar nada, vai para a parte inicial
def root():
    x = 10
    for i in range(10):
        x += 1
    return {"mensagem": "você está na página principal", "valor": x}


@app.get("/cadastro")
def cadastro():
    return {"mensagem": "você está cadastrado"}


@app.get("/login")
def login():
    return {"mensagem": "você está logado"}
