class CryptoChatbot:
    def __init__(self):
        self.name = "CryptoBuddy"
        self.personality = "Friendly, smart, and eco-conscious 💚"
        self.crypto_db = {
            "Bitcoin": {
                "price_trend": "rising",
                "market_cap": "high",
                "energy_use": "high",
                "sustainability_score": 3 / 10
            },
            "Ethereum": {
                "price_trend": "stable",
                "market_cap": "high",
                "energy_use": "medium",
                "sustainability_score": 6 / 10
            },
            "Cardano": {
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 8 / 10
            }
        }
        self.history = []
    # This function generates a response based on the user's query
    def response(self, user_query):
        user_query = user_query.lower()  # Normalize query for comparison

        # If user is asking about sustainability
        if "sustainable" in user_query:
            recommend = max(
                self.crypto_db,
                key=lambda x: self.crypto_db[x]["sustainability_score"]
            )
            reply = f"Invest in {recommend}! 🌱 It’s eco-friendly and has long-term potential!"

        # If user is asking about trending coins
        elif "trending" in user_query:
            trending_coins = list(filter(
                lambda coin: self.crypto_db[coin]["price_trend"] == "rising",
                self.crypto_db
            ))
            reply = f"The trending coins are: {', '.join(trending_coins)}"
