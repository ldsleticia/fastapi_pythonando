import requests

retorno = requests.get("http://127.0.0.1:8000")

print(retorno.json()["mensagem"])
print(type(retorno.json()["mensagem"]))

print(retorno.json()["valor"])
print(type(retorno.json()["valor"]))

retorno = requests.get("http://127.0.0.1:8000/login")

print(retorno.json()["mensagem"])
print(type(retorno.json()["mensagem"]))
