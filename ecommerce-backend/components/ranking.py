import pandas as pd
import numpy as np

# User-defined weight preferences for each attribute
user_weights = {
    "price": 0.1,             # Lower price is preferred
    "rating": 0.4,            # Higher rating is more important
    "review_sentiment": 0.1,  # Positive reviews are desirable
    "shipping_time": 0.1      # Faster shipping is slightly preferred
}

# Step 1: Normalize the numerical attributes


def normalize(series, inverse=False):
    """Normalize a pandas series to a 0-1 range. Invert if lower values are preferred."""
    normalized = (series - series.min()) / (series.max() - series.min())
    return 1 - normalized if inverse else normalized


def rank(products):
    # convert list of dictionaries to pandas dataframe
    df = pd.DataFrame(products)

    # Step 1: Normalize the numerical attributes
    df['price_normalized'] = normalize(df['price'], inverse=True)
    df['rating_normalized'] = normalize(df['rating'])
    df['review_sentiment_normalized'] = normalize(df['review_sentiment'])
    df['shipping_time_normalized'] = normalize(
        df['shipping_time'], inverse=True)

    # Step 2: Calculate weighted scores for each product
    df['weighted_score'] = (
        df['price_normalized'] * user_weights['price'] +
        df['rating_normalized'] * user_weights['rating'] +
        df['review_sentiment_normalized'] * user_weights['review_sentiment'] +
        df['shipping_time_normalized'] * user_weights['shipping_time']
    )

    # Step 3: Rank products by score
    df['rank'] = df['weighted_score'].rank(ascending=False)

    # Sort by rank
    ranked_products = df.sort_values(by='rank')

    # Display the results
    print("Ranked Products Based on Weighted Scoring:")
    print(ranked_products[['id', 'weighted_score', 'rank']])

    return ranked_products.to_dict(orient='records')
