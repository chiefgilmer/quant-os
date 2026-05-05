from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from core.orchestrator import run_quant_os

app = FastAPI()

# Serve frontend folder
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
def dashboard():
    return FileResponse("frontend/index.html")

@app.get("/run")
def run():
    return run_quant_os()
