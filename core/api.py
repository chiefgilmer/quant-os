from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import json
import csv

app = FastAPI()

# ---------------------------
# DASHBOARD PAGE
# ---------------------------
@app.get("/")
def home():
    return FileResponse("frontend/index.html")

# ---------------------------
# LOAD PORTFOLIO + SIGNALS
# ---------------------------
@app.get("/run")
def run():

    try:
        with open("portfolio.json", "r") as f:
            portfolio = json.load(f)
    except:
        portfolio = {}

    # simple fake signals (stable version)
    signals = []
    for ticker in portfolio.keys():
        signals.append({
            "ticker": ticker,
            "signal": "HOLD",
            "score": 0.0
        })

    return {
        "portfolio": portfolio,
        "signals": signals
    }

# ---------------------------
# UPLOAD CSV PORTFOLIO
# ---------------------------
@app.post("/upload")
async def upload(file: UploadFile = File(...)):

    contents = await file.read()
    lines = contents.decode("utf-8").splitlines()

    reader = csv.DictReader(lines)

    portfolio = {}

    for row in reader:
        symbol = row.get("Symbol") or row.get("symbol")
        qty = row.get("Quantity") or row.get("quantity")

        if symbol and qty:
            portfolio[symbol] = float(qty)

    with open("portfolio.json", "w") as f:
        json.dump(portfolio, f)

    return {"status": "ok", "portfolio": portfolio}
