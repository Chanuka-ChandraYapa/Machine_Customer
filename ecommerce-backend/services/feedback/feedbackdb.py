from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create database
db = client["machine_customer"]

# Create collection
feedback_collection = db["product_feedback"]

# Insert example data
example_data = {
    "product_id": "12345",
    "vendor_id": "67890",
    "order_time": "2025-01-20T15:30:00Z",
    "arrival_time": "2025-01-20T18:00:00Z",
    "expected_arrival_time": "2025-01-20T17:00:00Z",
    "usage_data": [
        {"date": "2025-01-21", "quantity_used": 2},
        {"date": "2025-01-22", "quantity_used": 1}
    ],
    "expiry_date": "2025-01-25",
    "remaining_quantity": 1,
    "feedback_score": 8.5,
    "wastage_flag": True
}

# Insert example data
feedback_collection.insert_one(example_data)

print("Example data inserted into MongoDB!")
