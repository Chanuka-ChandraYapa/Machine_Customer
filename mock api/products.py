from flask import Flask, request, jsonify

app = Flask(__name__)

# Mocked product list for testing
mocked_products = [
  {
    "id": 1,
    "title": "Whole Milk",
    "description": "Fresh whole milk with rich, creamy texture.",
    "category": "groceries",
    "price": 3.49,
    "discountPercentage": 10.5,
    "rating": 4.6,
    "stock": 80,
    "tags": ["dairy"],
    "sku": "WMILK01",
    "weight": 1,
    "dimensions": {"width": 22.5, "height": 20.5, "depth": 12},
    "warrantyInformation": "6 months warranty",
    "shippingInformation": "Ships in 1-2 weeks",
    "availabilityStatus": "In Stock",
    "reviews": [
      {"rating": 5, "comment": "Delicious and creamy!", "date": "2024-01-01", "reviewerName": "John Doe", "reviewerEmail": "john.doe@example.com"},
      {"rating": 4, "comment": "Good quality, would recommend.", "date": "2024-01-02", "reviewerName": "Jane Smith", "reviewerEmail": "jane.smith@example.com"}
    ],
    "returnPolicy": "7 days return policy",
    "minimumOrderQuantity": 10,
    "meta": {
      "createdAt": "2024-01-01",
      "updatedAt": "2024-01-01",
      "barcode": "1234567890123",
      "qrCode": "https://example.com/qr-code.png"
    },
    "images": ["https://example.com/images/whole_milk.png"],
    "thumbnail": "https://example.com/images/whole_milk_thumbnail.png"
  },
  {
    "id": 2,
    "title": "Skim Milk",
    "description": "Low-fat milk with a smooth taste, perfect for health-conscious individuals.",
    "category": "groceries",
    "price": 3.29,
    "discountPercentage": 12.3,
    "rating": 4.3,
    "stock": 60,
    "tags": ["dairy"],
    "sku": "SKMILK02",
    "weight": 1,
    "dimensions": {"width": 22, "height": 20.8, "depth": 12.2},
    "warrantyInformation": "6 months warranty",
    "shippingInformation": "Ships in 1-2 weeks",
    "availabilityStatus": "In Stock",
    "reviews": [
      {"rating": 5, "comment": "Great taste without the fat!", "date": "2024-01-01", "reviewerName": "Alice Johnson", "reviewerEmail": "alice.johnson@example.com"},
      {"rating": 4, "comment": "Good product, but the price could be better.", "date": "2024-01-03", "reviewerName": "Bob Lee", "reviewerEmail": "bob.lee@example.com"}
    ],
    "returnPolicy": "7 days return policy",
    "minimumOrderQuantity": 15,
    "meta": {
      "createdAt": "2024-01-01",
      "updatedAt": "2024-01-01",
      "barcode": "2345678901234",
      "qrCode": "https://example.com/qr-code.png"
    },
    "images": ["https://example.com/images/skim_milk.png"],
    "thumbnail": "https://example.com/images/skim_milk_thumbnail.png"
  },
  {
    "id": 3,
    "title": "Almond Milk",
    "description": "A plant-based alternative to traditional milk, perfect for vegan diets.",
    "category": "groceries",
    "price": 4.19,
    "discountPercentage": 5.5,
    "rating": 4.8,
    "stock": 50,
    "tags": ["dairy-free"],
    "sku": "ALMILK03",
    "weight": 1,
    "dimensions": {"width": 21.8, "height": 20.6, "depth": 12.3},
    "warrantyInformation": "6 months warranty",
    "shippingInformation": "Ships in 1-2 weeks",
    "availabilityStatus": "In Stock",
    "reviews": [
      {"rating": 5, "comment": "Delicious and creamy!", "date": "2024-01-01", "reviewerName": "Chris Adams", "reviewerEmail": "chris.adams@example.com"},
      {"rating": 4, "comment": "Good for dairy alternatives, but expensive.", "date": "2024-01-02", "reviewerName": "Dana Lee", "reviewerEmail": "dana.lee@example.com"}
    ],
    "returnPolicy": "7 days return policy",
    "minimumOrderQuantity": 20,
    "meta": {
      "createdAt": "2024-01-01",
      "updatedAt": "2024-01-01",
      "barcode": "3456789012345",
      "qrCode": "https://example.com/qr-code.png"
    },
    "images": ["https://example.com/images/almond_milk.png"],
    "thumbnail": "https://example.com/images/almond_milk_thumbnail.png"
  },
  {
    "id": 4,
    "title": "Salted Butter",
    "description": "Creamy salted butter made from fresh milk, perfect for baking and cooking.",
    "category": "groceries",
    "price": 2.99,
    "discountPercentage": 8.7,
    "rating": 4.7,
    "stock": 120,
    "tags": ["dairy"],
    "sku": "BUTTER01",
    "weight": 0.5,
    "dimensions": {"width": 10, "height": 8, "depth": 3},
    "warrantyInformation": "6 months warranty",
    "shippingInformation": "Ships in 1-2 weeks",
    "availabilityStatus": "In Stock",
    "reviews": [
      {"rating": 5, "comment": "Perfect for my cooking!", "date": "2024-01-01", "reviewerName": "Emma Green", "reviewerEmail": "emma.green@example.com"},
      {"rating": 4, "comment": "Good quality, could be cheaper.", "date": "2024-01-02", "reviewerName": "Frank Wright", "reviewerEmail": "frank.wright@example.com"}
    ],
    "returnPolicy": "7 days return policy",
    "minimumOrderQuantity": 5,
    "meta": {
      "createdAt": "2024-01-01",
      "updatedAt": "2024-01-01",
      "barcode": "4567890123456",
      "qrCode": "https://example.com/qr-code.png"
    },
    "images": ["https://example.com/images/salted_butter.png"],
    "thumbnail": "https://example.com/images/salted_butter_thumbnail.png"
  },
  {
    "id": 5,
    "title": "Unsalted Butter",
    "description": "Rich and creamy unsalted butter for those who prefer natural flavors.",
    "category": "groceries",
    "price": 3.49,
    "discountPercentage": 12.5,
    "rating": 4.4,
    "stock": 100,
    "tags": ["dairy"],
    "sku": "BUTTER02",
    "weight": 0.5,
    "dimensions": {"width": 10, "height": 8, "depth": 3},
    "warrantyInformation": "6 months warranty",
    "shippingInformation": "Ships in 1-2 weeks",
    "availabilityStatus": "In Stock",
    "reviews": [
      {"rating": 5, "comment": "Great butter for cooking and baking!", "date": "2024-01-01", "reviewerName": "Helen Parker", "reviewerEmail": "helen.parker@example.com"},
      {"rating": 4, "comment": "A little too soft, but good flavor.", "date": "2024-01-02", "reviewerName": "George Davis", "reviewerEmail": "george.davis@example.com"}
    ],
    "returnPolicy": "7 days return policy",
    "minimumOrderQuantity": 5,
    "meta": {
      "createdAt": "2024-01-01",
      "updatedAt": "2024-01-01",
      "barcode": "5678901234567",
      "qrCode": "https://example.com/qr-code.png"
    },
    "images": ["https://example.com/images/unsalted_butter.png"],
    "thumbnail": "https://example.com/images/unsalted_butter_thumbnail.png"
  },
  {
    "id": 6,
    "title": "Free-Range Eggs",
    "description": "Fresh eggs from free-range chickens, ensuring quality and flavor.",
    "category": "groceries",
    "price": 2.49,
    "discountPercentage": 15.0,
    "rating": 4.9,
    "stock": 200,
    "tags": ["eggs", "organic"],
    "sku": "EGG01",
    "weight": 1.2,
    "dimensions": {"width": 10, "height": 6, "depth": 5},
    "warrantyInformation": "No warranty",
    "shippingInformation": "Ships in 3-5 days",
    "availabilityStatus": "In Stock",
    "reviews": [
      {"rating": 5, "comment": "Tastes amazing, very fresh!", "date": "2024-01-01", "reviewerName": "Sophia Wilson", "reviewerEmail": "sophia.wilson@example.com"},
      {"rating": 4, "comment": "Good quality, but a bit expensive.", "date": "2024-01-03", "reviewerName": "Luke Harris", "reviewerEmail": "luke.harris@example.com"}
    ],
    "returnPolicy": "No return policy",
    "minimumOrderQuantity": 6,
    "meta": {
      "createdAt": "2024-01-01",
      "updatedAt": "2024-01-01",
      "barcode": "6789012345678",
      "qrCode": "https://example.com/qr-code.png"
    },
    "images": ["https://example.com/images/free_range_eggs.png"],
    "thumbnail": "https://example.com/images/free_range_eggs_thumbnail.png"
  },
  {
    "id": 7,
    "title": "Organic Eggs",
    "description": "Organic eggs with no added hormones or antibiotics.",
    "category": "groceries",
    "price": 3.19,
    "discountPercentage": 7.0,
    "rating": 4.8,
    "stock": 150,
    "tags": ["eggs", "organic"],
    "sku": "EGG02",
    "weight": 1.1,
    "dimensions": {"width": 9.8, "height": 6, "depth": 5},
    "warrantyInformation": "No warranty",
    "shippingInformation": "Ships in 3-5 days",
    "availabilityStatus": "In Stock",
    "reviews": [
      {"rating": 5, "comment": "Best eggs I've ever had!", "date": "2024-01-02", "reviewerName": "Olivia Brown", "reviewerEmail": "olivia.brown@example.com"},
      {"rating": 4, "comment": "Good quality but expensive.", "date": "2024-01-04", "reviewerName": "James Green", "reviewerEmail": "james.green@example.com"}
    ],
    "returnPolicy": "No return policy",
    "minimumOrderQuantity": 6,
    "meta": {
      "createdAt": "2024-01-02",
      "updatedAt": "2024-01-02",
      "barcode": "7890123456789",
      "qrCode": "https://example.com/qr-code.png"
    },
    "images": ["https://example.com/images/organic_eggs.png"],
    "thumbnail": "https://example.com/images/organic_eggs_thumbnail.png"
  },
  {
    "id": 8,
    "title": "Brown Eggs",
    "description": "Brown eggs with rich flavor and a natural appearance.",
    "category": "groceries",
    "price": 2.89,
    "discountPercentage": 10.0,
    "rating": 4.5,
    "stock": 180,
    "tags": ["eggs"],
    "sku": "EGG03",
    "weight": 1.3,
    "dimensions": {"width": 9.9, "height": 6.1, "depth": 5.1},
    "warrantyInformation": "No warranty",
    "shippingInformation": "Ships in 3-5 days",
    "availabilityStatus": "In Stock",
    "reviews": [
      {"rating": 5, "comment": "Great taste, very fresh.", "date": "2024-01-03", "reviewerName": "Liam Scott", "reviewerEmail": "liam.scott@example.com"},
      {"rating": 4, "comment": "Good quality, will buy again.", "date": "2024-01-05", "reviewerName": "Ella Mitchell", "reviewerEmail": "ella.mitchell@example.com"}
    ],
    "returnPolicy": "No return policy",
    "minimumOrderQuantity": 6,
    "meta": {
      "createdAt": "2024-01-03",
      "updatedAt": "2024-01-03",
      "barcode": "8901234567890",
      "qrCode": "https://example.com/qr-code.png"
    },
    "images": ["https://example.com/images/brown_eggs.png"],
    "thumbnail": "https://example.com/images/brown_eggs_thumbnail.png"
  },
  {
    "id": 9,
    "title": "White Eggs",
    "description": "Fresh white eggs from happy, free-range chickens.",
    "category": "groceries",
    "price": 2.69,
    "discountPercentage": 12.0,
    "rating": 4.6,
    "stock": 160,
    "tags": ["eggs"],
    "sku": "EGG04",
    "weight": 1.1,
    "dimensions": {"width": 9.7, "height": 5.9, "depth": 4.9},
    "warrantyInformation": "No warranty",
    "shippingInformation": "Ships in 3-5 days",
    "availabilityStatus": "In Stock",
    "reviews": [
      {"rating": 5, "comment": "Nice quality eggs, good taste.", "date": "2024-01-04", "reviewerName": "Jack Taylor", "reviewerEmail": "jack.taylor@example.com"},
      {"rating": 4, "comment": "Fresh, but packaging could be better.", "date": "2024-01-06", "reviewerName": "Mia Roberts", "reviewerEmail": "mia.roberts@example.com"}
    ],
    "returnPolicy": "No return policy",
    "minimumOrderQuantity": 6,
    "meta": {
      "createdAt": "2024-01-04",
      "updatedAt": "2024-01-04",
      "barcode": "9012345678901",
      "qrCode": "https://example.com/qr-code.png"
    },
    "images": ["https://example.com/images/white_eggs.png"],
    "thumbnail": "https://example.com/images/white_eggs_thumbnail.png"
  },
  {
  "id": 10,
  "title": "Butter",
  "description": "Fresh butter made from cow milk",
  "category": "groceries",
  "price": 2.99,
  "discountPercentage": 10.0,
  "rating": 4.5,
  "stock": 100,
  "tags": ["dairy"],
  "sku": "BUTTER03",
  "weight": 0.5,
  "dimensions": {
    "width": 10,
    "height": 8,
    "depth": 3
  },
  "warrantyInformation": "6 months warranty",
  "shippingInformation": "Ships in 1-2 weeks",
  "availabilityStatus": "In Stock",
  "reviews": [
    {
      "rating": 5,
      "comment": "Great taste and quality",
      "date": "2024-01-01",
      "reviewerName": "Alice Johnson",
      "reviewerEmail": "alice.johnson@example.com"
    },
    {
      "rating": 4,
      "comment": "Good flavor, but a little expensive",
      "date": "2024-01-02",
      "reviewerName": "Bob Smith",
      "reviewerEmail": "bob.smith@example.com"
    }
  ],
  "returnPolicy": "7 days return policy",
  "minimumOrderQuantity": 5,
  "meta": {
    "createdAt": "2024-01-01",
    "updatedAt": "2024-01-01",
    "barcode": "1234567890123",
    "qrCode": "https://example.com/qr-code.png"
  },
  "images": [
    "https://example.com/images/fresh_butter.png"
  ],
  "thumbnail": "https://example.com/images/fresh_butter_thumbnail.png"
}


]


@app.route('/products/search', methods=['GET'])
def search_products():
    query = request.args.get('q', '').lower()
    if not query:
        return jsonify({"error": "Missing query parameter 'q'"}), 400

    # Filter mocked products based on the query
    filtered_products = [
        product for product in mocked_products if query in product['title'].lower()
    ]
    print("Filtered Products************",filtered_products)
    results = {"products": filtered_products, "total": len(filtered_products)}
    print("results++++++++++",results)
    return jsonify(results)

if __name__ == '__main__':
    # Run the server on localhost and port 5000
    app.run(host='localhost', port=5001, debug=True)
