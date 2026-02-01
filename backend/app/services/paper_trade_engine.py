class PaperTradingEngine:
    def place_order(self, symbol, side, qty, price):
        return {
            "symbol": symbol,
            "side": side,
            "qty": qty,
            "price": price,
            "status": "FILLED",
            "mode": "PAPER"
        }
