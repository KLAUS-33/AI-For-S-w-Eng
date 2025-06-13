

print("👋 Hello! I'm CryptoBuddy – your AI-powered crypto sidekick.")
print("Ask me anything about trending cryptos, sustainable coins, or long-term growth! 🌍🚀")

crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

def crypto_advice(user_query):
    user_query = user_query.lower()

    if "sustainable" in user_query or "eco" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"🌱 Invest in {recommend}! It's eco-friendly and has long-term potential!"
    
    elif "trending" in user_query or "rising" in user_query:
        rising_coins = [name for name, data in crypto_db.items() if data["price_trend"] == "rising"]
        return f"📈 These coins are on the rise: {', '.join(rising_coins)}."
    
    elif "long-term" in user_query or "growth" in user_query:
        for name, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] > 0.7:
                return f"🚀 {name} is trending up and has a strong sustainability profile – great for long-term!"
        return "🔍 I couldn't find the perfect match, but always diversify your portfolio!"
    
    elif "market cap" in user_query:
        sorted_coins = sorted(crypto_db.items(), key=lambda x: x[1]["market_cap"], reverse=True)
        top_coin = sorted_coins[0][0]
        return f"💰 {top_coin} has the highest market cap among the options!"
    
    else:
        return "🤖 I’m not sure about that. Try asking about trends, sustainability, or growth!"

while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ["exit", "quit"]:
        print("CryptoBuddy: 🫡 Stay savvy, friend! Always DYOR – Do Your Own Research!")
        break
    response = crypto_advice(user_input)
    print("CryptoBuddy:", response)
