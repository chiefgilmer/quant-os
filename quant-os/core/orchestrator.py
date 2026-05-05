def run_quant_os():

    signals = [
        {"ticker": "AAPL", "signal": "BUY", "score": 1.2},
        {"ticker": "TSLA", "signal": "HOLD", "score": 0.1},
        {"ticker": "NVDA", "signal": "BUY", "score": 2.1}
    ]

    risk = {
        "risk_level": "NORMAL",
        "exposure": 0.45
    }

    portfolio = {
        "AAPL": 0.3,
        "TSLA": 0.1,
        "NVDA": 0.4
    }

    return {
        "signals": signals,
        "risk": risk,
        "portfolio": portfolio
    }
