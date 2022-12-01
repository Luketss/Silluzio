import json
from fastapi import FastAPI
from database import DatabaseConnection

app = FastAPI()

@app.get("/stock")
async def root():
    obj = DatabaseConnection()
    data = obj.list_all_stocks()
    return(data) 