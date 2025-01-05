from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Mocked product list for testing
mocked_products = [
  {
    "id": 1,
    "title": "Whole Milk",
    "description": "Fresh whole milk with rich, creamy texture.",
    "category": "groceries",
    "price": 3.49,
    "discountPercentage": 4,
    "rating": 4.6,
    "stock": 80,
    "tags": ["dairy"],
    "sku": "WMILK01",
    "volume": 1750,
    "dimensions": {"width": 22.5, "height": 20.5, "depth": 12},
    "warrantyInformation": "No warranty",
    "shippingInformation": "Ships in 1-2 days",
    "availabilityStatus": "In Stock",
    "reviews": [
      {"rating": 5, "comment": "Delicious and creamy!", "date": "2024-11-01", "reviewerName": "John Doe", "reviewerEmail": "john.doe@example.com"},
      {"rating": 4, "comment": "Good quality, would recommend.", "date": "2024-12-09", "reviewerName": "Jane Smith", "reviewerEmail": "jane.smith@example.com"}
    ],
    "returnPolicy": "1 days return policy",
    "minimumOrderQuantity": 1,
    "meta": {
      "createdAt": "2024-01-01",
      "updatedAt": "2024-01-01",
      "barcode": "1234567890123",
      "qrCode": "https://example.com/qr-code.png"
    },
    "images": ["https://img.freepik.com/premium-vector/cartoon-vector-illustration-isolated-object-fresh-whole-drink-milk-bottle_311865-9523.jpg"],
    "thumbnail": "https://img.freepik.com/premium-vector/cartoon-vector-illustration-isolated-object-fresh-whole-drink-milk-bottle_311865-9523.jpg"
  },
  {
    "id": 2,
    "title": "Skim Milk",
    "description": "Low-fat milk with a smooth taste, perfect for health-conscious individuals.",
    "category": "groceries",
    "price": 3.29,
    "discountPercentage": 5,
    "rating": 4.3,
    "stock": 60,
    "tags": ["dairy"],
    "sku": "SKMILK02",
    "volume": 1000,
    "dimensions": {"width": 22, "height": 20.8, "depth": 12.2},
    "warrantyInformation": "No warranty",
    "shippingInformation": "Ships in 1-2 days",
    "availabilityStatus": "In Stock",
    "reviews": [
      {"rating": 5, "comment": "Great taste without the fat!", "date": "2024-10-05", "reviewerName": "Alice Johnson", "reviewerEmail": "alice.johnson@example.com"},
      {"rating": 4, "comment": "Good product, but the price could be better.", "date": "2024-10-28", "reviewerName": "Bob Lee", "reviewerEmail": "bob.lee@example.com"}
    ],
    "returnPolicy": "1 days return policy",
    "minimumOrderQuantity": 1,
    "meta": {
      "createdAt": "2024-01-01",
      "updatedAt": "2024-01-01",
      "barcode": "2345678901234",
      "qrCode": "https://example.com/qr-code.png"
    },
    "images": ["https://media.istockphoto.com/id/1419219172/vector/tall-strawberry-milk-carton-clipart-element-cute-simple-flat-vector-illustration-design.jpg?s=612x612&w=0&k=20&c=VP5iRzIK_wrsWiviRoh62BdvbvEQkE-0jtAJJ51N2EU="],
    "thumbnail": "https://media.istockphoto.com/id/1419219172/vector/tall-strawberry-milk-carton-clipart-element-cute-simple-flat-vector-illustration-design.jpg?s=612x612&w=0&k=20&c=VP5iRzIK_wrsWiviRoh62BdvbvEQkE-0jtAJJ51N2EU="
  },
  {
    "id": 3,
    "title": "Almond Milk",
    "description": "A plant-based alternative to traditional milk, perfect for vegan diets.",
    "category": "groceries",
    "price": 3.99,
    "discountPercentage": 5.5,
    "rating": 4.8,
    "stock": 50,
    "tags": ["dairy-free"],
    "sku": "ALMILK03",
    "volume": 1000,
    "dimensions": {"width": 21.8, "height": 20.6, "depth": 12.3},
    "warrantyInformation": "No warranty",
    "shippingInformation": "Ships in 1-2 days",
    "availabilityStatus": "In Stock",
    "reviews": [
      {"rating": 5, "comment": "Delicious and creamy!", "date": "2024-11-20", "reviewerName": "Chris Adams", "reviewerEmail": "chris.adams@example.com"},
      {"rating": 4, "comment": "Good for dairy alternatives, but expensive.", "date": "2024-12-02", "reviewerName": "Dana Lee", "reviewerEmail": "dana.lee@example.com"}
    ],
    "returnPolicy": "7 days return policy",
    "minimumOrderQuantity": 1,
    "meta": {
      "createdAt": "2024-01-01",
      "updatedAt": "2024-01-01",
      "barcode": "3456789012345",
      "qrCode": "https://example.com/qr-code.png"
    },
    "images": ["https://img.freepik.com/premium-vector/bottle-almond-milk-with-almonds-illustration-cartoon-drawing-artwork-vector_893055-18237.jpg"],
    "thumbnail": "https://img.freepik.com/premium-vector/bottle-almond-milk-with-almonds-illustration-cartoon-drawing-artwork-vector_893055-18237.jpg"
  },
  {
    "id": 4,
    "title": "Salted Butter",
    "description": "Creamy salted butter made from fresh milk, perfect for baking and cooking.",
    "category": "groceries",
    "price": 2.99,
    "discountPercentage": 3,
    "rating": 4.7,
    "stock": 120,
    "tags": ["dairy"],
    "sku": "BUTTER01",
    "weight": 113,
    "dimensions": {"width": 10, "height": 8, "depth": 3},
    "warrantyInformation": "No warranty",
    "shippingInformation": "Ships in 1-3 days",
    "availabilityStatus": "In Stock",
    "reviews": [
      {"rating": 5, "comment": "Perfect for my cooking!", "date": "2024-10-05", "reviewerName": "Emma Green", "reviewerEmail": "emma.green@example.com"},
      {"rating": 4, "comment": "Good quality, could be cheaper.", "date": "2024-11-22", "reviewerName": "Frank Wright", "reviewerEmail": "frank.wright@example.com"}
    ],
    "returnPolicy": "2 days return policy",
    "minimumOrderQuantity": 1,
    "meta": {
      "createdAt": "2024-01-01",
      "updatedAt": "2024-01-01",
      "barcode": "4567890123456",
      "qrCode": "https://example.com/qr-code.png"
    },
    "images": ["https://ih1.redbubble.net/image.518787332.2793/st,small,507x507-pad,600x600,f8f8f8.jpg"],
    "thumbnail": "https://ih1.redbubble.net/image.518787332.2793/st,small,507x507-pad,600x600,f8f8f8.jpg"
  },
  {
    "id": 5,
    "title": "Unsalted Butter",
    "description": "Rich and creamy unsalted butter for those who prefer natural flavors.",
    "category": "groceries",
    "price": 3.49,
    "discountPercentage": 4,
    "rating": 4.4,
    "stock": 100,
    "tags": ["dairy"],
    "sku": "BUTTER02",
    "weight": 113,
    "dimensions": {"width": 10, "height": 8, "depth": 3},
    "warrantyInformation": "No warranty",
    "shippingInformation": "Ships in 1-2 days",
    "availabilityStatus": "In Stock",
    "reviews": [
      {"rating": 5, "comment": "Great butter for cooking and baking!", "date": "2024-10-30", "reviewerName": "Helen Parker", "reviewerEmail": "helen.parker@example.com"},
      {"rating": 4, "comment": "A little too soft, but good flavor.", "date": "2024-12-12", "reviewerName": "George Davis", "reviewerEmail": "george.davis@example.com"}
    ],
    "returnPolicy": "4 days return policy",
    "minimumOrderQuantity": 1,
    "meta": {
      "createdAt": "2024-01-01",
      "updatedAt": "2024-01-01",
      "barcode": "5678901234567",
      "qrCode": "https://example.com/qr-code.png"
    },
    "images": ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4dhP5-02kpPnFMETGPMdGoeukrUt2Sdr24Q&s"],
    "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4dhP5-02kpPnFMETGPMdGoeukrUt2Sdr24Q&s"
  },
  {
    "id": 6,
    "title": "Free-Range Eggs",
    "description": "Fresh eggs from free-range chickens, ensuring quality and flavor.",
    "category": "groceries",
    "price": 1.5,
    "discountPercentage": 1,
    "rating": 4.9,
    "stock": 200,
    "tags": ["eggs", "organic"],
    "sku": "EGG01",
    "weight": 45,
    "warrantyInformation": "No warranty",
    "shippingInformation": "Ships in 1-2 days",
    "availabilityStatus": "In Stock",
    "reviews": [
      {"rating": 5, "comment": "Tastes amazing, very fresh!", "date": "2024-12-01", "reviewerName": "Sophia Wilson", "reviewerEmail": "sophia.wilson@example.com"},
      {"rating": 4, "comment": "Good quality, but a bit expensive.", "date": "2024-12-31", "reviewerName": "Luke Harris", "reviewerEmail": "luke.harris@example.com"}
    ],
    "returnPolicy": "No return policy",
    "minimumOrderQuantity": 5,
    "meta": {
      "createdAt": "2024-01-01",
      "updatedAt": "2024-01-01",
      "barcode": "6789012345678",
      "qrCode": "https://example.com/qr-code.png"
    },
    "images": ["https://i0.wp.com/taylorproduce.co.uk/wp-content/uploads/2022/01/IMG_9812-scaled.jpg?fit=2370%2C2560&ssl=1"],
    "thumbnail": "https://i0.wp.com/taylorproduce.co.uk/wp-content/uploads/2022/01/IMG_9812-scaled.jpg?fit=2370%2C2560&ssl=1"
  },
  {
    "id": 7,
    "title": "Organic Eggs",
    "description": "Organic eggs with no added hormones or antibiotics.",
    "category": "groceries",
    "price": 1.8,
    "discountPercentage": 1.2,
    "rating": 4.8,
    "stock": 150,
    "tags": ["eggs", "organic"],
    "sku": "EGG02",
    "weight": 46,
    "warrantyInformation": "No warranty",
    "shippingInformation": "Ships in 1-2 days",
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
    "images": ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQllqhzk09rZnb48v9lWlwP3Hww9jjnFm-i2A&s"],
    "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQllqhzk09rZnb48v9lWlwP3Hww9jjnFm-i2A&s"
  },
  {
    "id": 8,
    "title": "Brown Eggs",
    "description": "Brown eggs with rich flavor and a natural appearance.",
    "category": "groceries",
    "price": 1.2,
    "discountPercentage": 0,
    "rating": 4.5,
    "stock": 180,
    "tags": ["eggs"],
    "sku": "EGG03",
    "weight": 43,
    "warrantyInformation": "No warranty",
    "shippingInformation": "Ships in 1-2 days",
    "availabilityStatus": "In Stock",
    "reviews": [
      {"rating": 5, "comment": "Great taste, very fresh.", "date": "2024-11-03", "reviewerName": "Liam Scott", "reviewerEmail": "liam.scott@example.com"},
      {"rating": 4, "comment": "Good quality, will buy again.", "date": "2024-11-05", "reviewerName": "Ella Mitchell", "reviewerEmail": "ella.mitchell@example.com"}
    ],
    "returnPolicy": "No return policy",
    "minimumOrderQuantity": 6,
    "meta": {
      "createdAt": "2024-01-03",
      "updatedAt": "2024-01-03",
      "barcode": "8901234567890",
      "qrCode": "https://example.com/qr-code.png"
    },
    "images": ["https://nonveglovers.in/wp-content/uploads/2020/12/NVL-BE30-500x300-1.jpg"],
    "thumbnail": "https://nonveglovers.in/wp-content/uploads/2020/12/NVL-BE30-500x300-1.jpg"
  },
  {
    "id": 9,
    "title": "White Eggs",
    "description": "Fresh white eggs from happy, free-range chickens.",
    "category": "groceries",
    "price": 1.5,
    "discountPercentage": 0,
    "rating": 4.6,
    "stock": 160,
    "tags": ["eggs"],
    "sku": "EGG04",
    "weight": 44,
    "warrantyInformation": "No warranty",
    "shippingInformation": "Ships in 1-2 days",
    "availabilityStatus": "In Stock",
    "reviews": [
      {"rating": 5, "comment": "Nice quality eggs, good taste.", "date": "2024-12-04", "reviewerName": "Jack Taylor", "reviewerEmail": "jack.taylor@example.com"},
      {"rating": 4, "comment": "Fresh, but packaging could be better.", "date": "2025-01-02", "reviewerName": "Mia Roberts", "reviewerEmail": "mia.roberts@example.com"}
    ],
    "returnPolicy": "No return policy",
    "minimumOrderQuantity": 6,
    "meta": {
      "createdAt": "2024-01-04",
      "updatedAt": "2024-01-04",
      "barcode": "9012345678901",
      "qrCode": "https://example.com/qr-code.png"
    },
    "images": ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJo1Ax9YA3Ga7FzOdtm8KYMuZE_vc8vGeYeg&s"],
    "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJo1Ax9YA3Ga7FzOdtm8KYMuZE_vc8vGeYeg&s"
  },
  {
  "id": 10,
  "title": "Butter",
  "description": "Fresh butter made from cow milk",
  "category": "groceries",
  "price": 2.99,
  "discountPercentage": 2,
  "rating": 4.5,
  "stock": 100,
  "tags": ["dairy"],
  "sku": "BUTTER03",
  "weight": 113,
  "dimensions": {
    "width": 10,
    "height": 8,
    "depth": 3
  },
  "warrantyInformation": "No Warranty",
  "shippingInformation": "Ships in 1-2 days",
  "availabilityStatus": "In Stock",
  "reviews": [
    {
      "rating": 5,
      "comment": "Great taste and quality",
      "date": "2024-10-01",
      "reviewerName": "Alice Johnson",
      "reviewerEmail": "alice.johnson@example.com"
    },
    {
      "rating": 4,
      "comment": "Good flavor, but a little expensive",
      "date": "2024-11-02",
      "reviewerName": "Bob Smith",
      "reviewerEmail": "bob.smith@example.com"
    }
  ],
  "returnPolicy": "7 days return policy",
  "minimumOrderQuantity":1,
  "meta": {
    "createdAt": "2024-01-01",
    "updatedAt": "2024-01-01",
    "barcode": "1234567890123",
    "qrCode": "https://example.com/qr-code.png"
  },
  "images": [
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTxm6Cjt7C2Du2k5PljTdJp6a3YxwiKWe0cPw&s"
  ],
  "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTxm6Cjt7C2Du2k5PljTdJp6a3YxwiKWe0cPw&s"
}


]


@app.route('/products', methods=['GET'])
def get_products():
    """Get all products."""
    return jsonify({"products": mocked_products, "total": len(mocked_products)})

@app.route('/products/search', methods=['GET'])
def search_products():
    """Search products by query."""
    query = request.args.get('q', '').lower()
    if not query:
        return jsonify({"error": "Missing query parameter 'q'"}), 400

    # Filter mocked products based on the query
    filtered_products = [
        product for product in mocked_products if query in product['title'].lower()
    ]
    results = {"products": filtered_products, "total": len(filtered_products)}
    return jsonify(results)

@app.route('/products/category-list', methods=['GET'])
def get_categories():
    """Fetch all unique categories."""
    categories = list(set(product["category"] for product in mocked_products))
    return jsonify(categories)

@app.route('/products/category/<string:category>', methods=['GET'])
def get_products_by_category(category):
    """Fetch products by category."""
    filtered_products = [
        product for product in mocked_products if product['category'].lower() == category.lower()
    ]
    return jsonify({"products": filtered_products, "total": len(filtered_products)})

@app.route('/products/brands', methods=['GET'])
def get_brands():
    """Fetch all unique brands (if brand data exists)."""
    brands = list(set(product.get("brand", "Unknown") for product in mocked_products))
    return jsonify(brands)

if __name__ == '__main__':
    # Run the server on localhost and port 5000
    app.run(host='localhost', port=5001, debug=True)