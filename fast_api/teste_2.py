from fastapi import FastAPI

app = FastAPI()

tupla_de_usuarios = [(1, "caio", "minhasenha1"), (2, "joao", "minhasenha2")]


@app.get("/usuario/{id}")
def main(id: int):
    encontrou = False
    for i in tupla_de_usuarios:
        if i[0] == id:
            return i
    return "Não existe esse usuário"


@app.post("/usuario")
def main(nome):
    encontrou = False
    for i in tupla_de_usuarios:
        if i[1] == nome:
            return i
    return "Não existe esse usuário"
