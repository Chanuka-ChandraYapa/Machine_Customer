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
    "images": ["https://img.freepik.com/premium-vector/cartoon-vector-illustration-isolated-object-fresh-whole-drink-milk-bottle_311865-9523.jpg"],
    "thumbnail": "https://img.freepik.com/premium-vector/cartoon-vector-illustration-isolated-object-fresh-whole-drink-milk-bottle_311865-9523.jpg"
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
    "images": ["https://media.istockphoto.com/id/1419219172/vector/tall-strawberry-milk-carton-clipart-element-cute-simple-flat-vector-illustration-design.jpg?s=612x612&w=0&k=20&c=VP5iRzIK_wrsWiviRoh62BdvbvEQkE-0jtAJJ51N2EU="],
    "thumbnail": "https://media.istockphoto.com/id/1419219172/vector/tall-strawberry-milk-carton-clipart-element-cute-simple-flat-vector-illustration-design.jpg?s=612x612&w=0&k=20&c=VP5iRzIK_wrsWiviRoh62BdvbvEQkE-0jtAJJ51N2EU="
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
    "images": ["https://img.freepik.com/premium-vector/bottle-almond-milk-with-almonds-illustration-cartoon-drawing-artwork-vector_893055-18237.jpg"],
    "thumbnail": "https://img.freepik.com/premium-vector/bottle-almond-milk-with-almonds-illustration-cartoon-drawing-artwork-vector_893055-18237.jpg"
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
    "images": ["https://ih1.redbubble.net/image.518787332.2793/st,small,507x507-pad,600x600,f8f8f8.jpg"],
    "thumbnail": "https://ih1.redbubble.net/image.518787332.2793/st,small,507x507-pad,600x600,f8f8f8.jpg"
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
    "images": ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4dhP5-02kpPnFMETGPMdGoeukrUt2Sdr24Q&s"],
    "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4dhP5-02kpPnFMETGPMdGoeukrUt2Sdr24Q&s"
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
    "images": ["https://i0.wp.com/taylorproduce.co.uk/wp-content/uploads/2022/01/IMG_9812-scaled.jpg?fit=2370%2C2560&ssl=1"],
    "thumbnail": "https://i0.wp.com/taylorproduce.co.uk/wp-content/uploads/2022/01/IMG_9812-scaled.jpg?fit=2370%2C2560&ssl=1"
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
    "images": ["data:image/jpeg;base64,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"],
    "thumbnail": "data:image/jpeg;base64,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"
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
    "images": ["https://nonveglovers.in/wp-content/uploads/2020/12/NVL-BE30-500x300-1.jpg"],
    "thumbnail": "https://nonveglovers.in/wp-content/uploads/2020/12/NVL-BE30-500x300-1.jpg"
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
    "images": ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJo1Ax9YA3Ga7FzOdtm8KYMuZE_vc8vGeYeg&s"],
    "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJo1Ax9YA3Ga7FzOdtm8KYMuZE_vc8vGeYeg&s"
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