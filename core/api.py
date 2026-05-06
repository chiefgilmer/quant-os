from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import json
import csv

app = FastAPI()

app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
def dashboard():
    return FileResponse("frontend/index.html")

@app.get("/run")
def run():
    with open("portfolio.json", "r") as f:
        portfolio = json.load(f)
    return {"portfolio": portfolio}

@app.post("/upload")
async def upload(file: UploadFile = File(...)):

    contents = await file.read()
    text = contents.decode("utf-8").splitlines()

    reader = csv.DictReader(text)

    portfolio = {}

    for row in reader:
        symbol = row.get("Symbol") or row.get("symbol")
        qty = row.get("Quantity") or row.get("quantity")

        if symbol and qty:
            portfolio[symbol] = int(float(qty))

    with open("portfolio.json", "w") as f:
        json.dump(portfolio, f)

    return {"status": "Portfolio updated", "data": portfolio}
