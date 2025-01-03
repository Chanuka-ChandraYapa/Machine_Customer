import pandas as pd
import pickle

# Load the trained model
with open('threshold_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the columns used during training (replace with actual columns)
training_columns = [
    "average_consumption",
    "daily_consumption_variance",
    "refill_frequency",
    "current_quantity",
    "product_type_Milk",  # Example: One-hot encoded feature
    "product_type_Butter",
    "product_type_Egg"
]

# Prediction function


def predict_threshold(input_data):
    """Predict the scaled threshold for a given input."""
    # Convert input dictionary to DataFrame
    input_df = pd.DataFrame([input_data])

    # One-hot encode the 'product_type' column
    input_df = pd.get_dummies(
        input_df, columns=["product_type"], drop_first=True)

    # Align with the training data columns
    input_df = input_df.reindex(columns=training_columns, fill_value=0)

    # Make the prediction
    prediction = model.predict(input_df)[0]
    return prediction


# Example input for prediction
example_input = {
    "average_consumption": 250,
    "daily_consumption_variance": 20,
    "refill_frequency": 10,
    "current_quantity": 300,
    "product_type": "Milk",
}

# Predict the threshold
predicted_threshold = predict_threshold(example_input)
print(f"Predicted scaled threshold: {predicted_threshold}")
