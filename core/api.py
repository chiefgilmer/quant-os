from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import json
import pdfplumber
import re
import os

app = FastAPI()

# -------------------------
# FRONTEND
# -------------------------
@app.get("/")
def home():
    return FileResponse("frontend/index.html")

# -------------------------
# DASHBOARD DATA
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
# PDF UPLOAD
# -------------------------
@app.post("/upload")
async def upload(file: UploadFile = File(...)):

    try:
        contents = await file.read()

        # Save temp file
        temp_path = "temp.pdf"
        with open(temp_path, "wb") as f:
            f.write(contents)

        text = ""

        # Extract PDF text safely
        with pdfplumber.open(temp_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

        # DEBUG PRINT (IMPORTANT FOR RENDER LOGS)
        print("PDF TEXT EXTRACTED:", text[:500])

        # Extract ticker + numbers
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
            "status": "success",
            "portfolio": portfolio
        }

    except Exception as e:
        print("UPLOAD ERROR:", str(e))
        return {"status": "error", "message": str(e)}
        json.dump(portfolio, f)

    return {
        "status": "PDF processed",
        "portfolio": portfolio
    }
