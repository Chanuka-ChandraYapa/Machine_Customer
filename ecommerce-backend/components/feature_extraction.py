from textblob import TextBlob
import re


def preprocess_products(product_data):

    extracted_features = {
        "id": product_data.get("id"),
        "title": product_data.get("title"),
        "brand": product_data.get("brand"),
        "description": product_data.get("description"),
        # "keywords": product_data.get("description").apply(lambda x: re.findall(r'\w+', x.lower())),
        "price": product_data.get("price"),
        "rating": product_data.get("rating"),
        "availability": product_data.get("availabilityStatus", "Unknown"),
        "stock": product_data.get("stock"),
        "discount": product_data.get("discountPercentage", 0),
        "shipping_time": extract_shipping_time(product_data.get("shippingInformation", "")),
        "average_review_score": calculate_average_review_score(product_data.get("reviews", [])),
        "review_sentiment": analyze_sentiment(product_data.get("reviews", [])),
        "tags": ", ".join(product_data.get("tags", [])),

    }

    # # Normalize numerical features
    # extracted_features["price_normalized"] = normalize_value(
    #     extracted_features["price"], 0, 1000, inverse=True)
    # extracted_features["rating_normalized"] = normalize_value(
    #     extracted_features["rating"], 0, 5)
    # extracted_features["stock_normalized"] = normalize_value(
    #     extracted_features["stock"], 0, 100)

    return extracted_features


def extract_shipping_time(shipping_info):
    """
    Extract numerical shipping time from shipping information string.
    """
    import re
    match = re.search(r"(\d+)", shipping_info)
    return int(match.group(1)) if match else 0


def calculate_average_review_score(reviews):
    """
    Calculate the average score from reviews.
    """
    if not reviews:
        return 0
    total_score = sum(review.get("rating", 0) for review in reviews)
    return total_score / len(reviews)


def analyze_sentiment(reviews):

    if not reviews:
        return 0
    sentiments = [TextBlob(review.get("comment", 0)
                           ).sentiment.polarity for review in reviews]
    return sum(sentiments) / len(sentiments) if sentiments else 0


def normalize_value(value, min_value, max_value, inverse=False):
    """
    Normalize a value to a range between 0 and 1.
    """
    if max_value == min_value:
        return 0
    normalized = (value - min_value) / (max_value - min_value)
    return 1 - normalized if inverse else normalized
