from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

import json
import pdfplumber
import re

app = FastAPI()

# SERVE STATIC FILES
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# HOME PAGE
@app.get("/")
def home():
    return FileResponse("frontend/index.html")

# LOAD DATA
@app.get("/run")
def run():
    try:
        with open("portfolio.json", "r") as f:
            portfolio = json.load(f)
    except:
        portfolio = {}

    return {"portfolio": portfolio}

# UPLOAD PDF
@app.post("/upload")
async def upload(file: UploadFile = File(...)):

    print("UPLOAD HIT")

    try:
        contents = await file.read()

        with open("temp.pdf", "wb") as f:
            f.write(contents)

        text = ""

        with pdfplumber.open("temp.pdf") as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        print("TEXT SAMPLE:", text[:200])

        matches = re.findall(r"\b([A-Z]{1,5})\b.*?(\d+\.?\d*)", text)

        portfolio = {}

        for symbol, qty in matches:
            try:
                portfolio[symbol] = float(qty)
            except:
                pass

        with open("portfolio.json", "w") as f:
            json.dump(portfolio, f)

        return {
            "status": "success",
            "portfolio": portfolio
        }

    except Exception as e:
        print("UPLOAD ERROR:", str(e))

        return {
            "status": "error",
            "message": str(e)
        }
