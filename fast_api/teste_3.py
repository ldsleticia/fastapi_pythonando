from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Usuario(BaseModel):
    id: int
    nome: Optional[str]
    senha: str


lista = [
    Usuario(id=1, nome="caio", senha="minhasenha1"),
    Usuario(id=2, nome="marcos", senha="minhasenha2"),
    Usuario(id=3, nome="joao", senha="minhasenha3"),
]


@app.post("/usuario")
def main(usuario: Usuario):
    lista.append(usuario)
    return "usuario cadastrado"


@app.get("/listarUsuario")
def main():
    return lista
