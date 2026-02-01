
from fastapi import FastAPI
from app.api.v1 import users, paper_trading

app = FastAPI(title="StockSteward AI")

app.include_router(users.router, prefix="/api/v1")
app.include_router(paper_trading.router, prefix="/api/v1")

@app.get("/health")
def health():
    return {"status": "ok"}
