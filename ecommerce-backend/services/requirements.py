# User criteria for product selection
user_criteria = {
    "price": 99.0,             # Preference for lower price (normalized)
    "rating": 4.5,             # Preference for highest rating (normalized)
    "review_sentiment": 0.1,   # Preference for positive reviews
    "shipping_time": 1,        # Moderate preference for fast shipping
    "brand": "",               # Preferred brand
    "productName": "",         # Preferred product name
}

# User-defined weight preferences for each attribute
user_weights = {
    "price": 0.1,              # Lower price is preferred
    "rating": 0.4,             # Higher rating is more important
    "review_sentiment": 0.1,   # Positive reviews are desirable
    "shipping_time": 0.1,      # Faster shipping is slightly preferred
    "brand": "",
    "productName": "",
}

def update_requirements(requirements):
    """Update the user_criteria based on input requirements."""
    user_criteria["price"] = float(requirements.get("minPrice", user_criteria["price"]))
    user_criteria["rating"] = float(requirements.get("minRating", user_criteria["rating"]))
    user_criteria["review_sentiment"] = float(requirements.get("reviewSentiment", user_criteria["review_sentiment"]))
    user_criteria["shipping_time"] = float(requirements.get("shippingTime", user_criteria["shipping_time"]))
    user_criteria["brand"] = requirements.get("brand", user_criteria["brand"])
    user_criteria["productName"] = requirements.get("productName", user_criteria["productName"])
