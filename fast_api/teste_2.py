from fastapi import FastAPI

app = FastAPI()


@app.get("/teste/{id}")
def main(id):
    return {"valor": id}
