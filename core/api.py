from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import json
import re
import pdfplumber

app = FastAPI()

# -------------------------
# DASHBOARD PAGE
# -------------------------
@app.get("/")
def home():
    return FileResponse("frontend/index.html")

# -------------------------
# LOAD PORTFOLIO
# -------------------------
@app.get("/run")
def run():
    try:
        with open("portfolio.json", "r") as f:
            portfolio = json.load(f)
    except:
        portfolio = {}

    return {"portfolio": portfolio}

# -------------------------
# PDF UPLOAD + PARSE
# -------------------------
@app.post("/upload")
async def upload(file: UploadFile = File(...)):

    content = await file.read()

    # Save temp file
    with open("temp.pdf", "wb") as f:
        f.write(content)

    text = ""

    # Extract text from PDF
    with pdfplumber.open("temp.pdf") as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    # -------------------------
    # SIMPLE TICKER DETECTION
    # -------------------------
    # Looks for patterns like: AAPL 10, TSLA 5, NVDA 3
    matches = re.findall(r"\b([A-Z]{1,5})\b.*?(\d+\.?\d*)", text)

    portfolio = {}

    for symbol, qty in matches:
        try:
            portfolio[symbol] = float(qty)
        except:
            pass

    # Save portfolio
    with open("portfolio.json", "w") as f:
        json.dump(portfolio, f)

    return {
        "status": "PDF processed",
        "portfolio": portfolio
    }
