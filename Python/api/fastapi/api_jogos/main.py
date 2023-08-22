from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def main_route():
    return {"message": "Hey, It is me Goku"}


@app.get("/livros")
async def get_all_livros():
    pass
