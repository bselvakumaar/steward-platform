
from fastapi import APIRouter
from app.services.paper_trade_engine import PaperTradingEngine

router = APIRouter()
engine = PaperTradingEngine()

@router.post("/paper/order")
def place_order(symbol: str, side: str, qty: int, price: float):
    return engine.place_order(symbol, side, qty, price)
