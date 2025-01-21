import numpy as np
import joblib
from flask import jsonify
import os

# Load the trained model
model_path = os.path.join(os.path.dirname(
    __file__), "food_consumption_model.pkl")
model = joblib.load(model_path)


def predict_threshold(input_data):
    """
    Predict the threshold (consumption of the next three days) based on input features.

    Args:
        input_data (dict): A dictionary containing the following keys:
            - average_consumption
            - daily_consumption_variance
            - refill_frequency
            - current_quantity
            - threshold
            - product_type
            - scaled_threshold

    Returns:
        float: Predicted threshold value.
    """
    # Extract features from input_data
    features = np.array([
        input_data['average_consumption'],
        input_data['daily_consumption_variance'],
        input_data['refill_frequency'],
        input_data['current_quantity'],
        input_data['product_type'],
        input_data['scaled_threshold']
    ]).reshape(1, -1)

    # Make prediction
    prediction = model.predict(features)
    return prediction[0]


# # Example input for prediction
# example_input = {
#     "average_consumption": 250,
#     "daily_consumption_variance": 20,
#     "refill_frequency": 10,
#     "current_quantity": 300,
#     "product_type": 1,          # Ensure this is a numeric value
#     "scaled_threshold": 0.75,
# }

# # Predict the threshold
# predicted_threshold = predict_threshold(example_input)
# print(f"Predicted threshold: {predicted_threshold}")
