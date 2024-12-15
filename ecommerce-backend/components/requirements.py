
user_criteria = {
    "price": 99.0,             # Preference for lower price (normalized)
    "rating": 4.5,            # Preference for highest rating (normalized)
    "review_sentiment": 0.1,  # Preference for positive reviews
    "shipping_time": 1,     # Moderate preference for fast shipping
}

# User-defined weight preferences for each attribute
user_weights = {
    "price": 0.1,             # Lower price is preferred
    "rating": 0.4,            # Higher rating is more important
    "review_sentiment": 0.1,  # Positive reviews are desirable
    "shipping_time": 0.1      # Faster shipping is slightly preferred
}


def update_requirements(requirements):
    # update only the price of the user_criteria
    user_criteria["price"] = float(requirements["minPrice"])
