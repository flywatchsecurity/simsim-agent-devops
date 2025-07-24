# simsim_engine.py

def simsim_precision_climb(buy_price=3600, eth_amount=0.6, spread=0.062, target_profit=100):
    """
    Calculates the required market price to hit a target profit
    after accounting for spread losses.
    """
    capital = buy_price * eth_amount
    required_app_quote = (capital + target_profit) / eth_amount
    required_market_price = required_app_quote / (1 - spread)

    return {
        "Capital In (USDT)": round(capital, 2),
        "Required App Quote": round(required_app_quote, 2),
        "Required Market Price": round(required_market_price, 2),
        "Target Profit": target_profit
    }

# Example usage
if __name__ == "__main__":
    result = simsim_precision_climb()
    for k, v in result.items():
        print(f"{k}: {v}")
