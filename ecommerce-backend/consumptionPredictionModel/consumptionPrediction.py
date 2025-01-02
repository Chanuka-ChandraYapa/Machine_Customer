import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

# Load dataset
df = pd.read_csv("threshold_data_with_types.csv")

# One-hot encode product types
df = pd.get_dummies(df, columns=["product_type"], drop_first=True)

# Features and target
X = df.drop(columns=["threshold", "scaled_threshold"])
y = df["scaled_threshold"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Train a Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
predictions = model.predict(X_test)
rmse = mean_squared_error(y_test, predictions, squared=False)
print(f"Root Mean Squared Error: {rmse}")

# Save the trained model
joblib.dump(model, "threshold_model.pkl")
print("Model saved as threshold_model.pkl")
