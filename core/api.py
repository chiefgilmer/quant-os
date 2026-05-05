from fastapi import FastAPI
from core.orchestrator import run_quant_os

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Quant OS is running"}

@app.get("/run")
def run():
    return run_quant_os()
