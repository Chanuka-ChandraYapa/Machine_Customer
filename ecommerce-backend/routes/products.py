from flask import Blueprint, request, jsonify
from services.feature_extraction import preprocess_products
from services.clustering import cluster
from services.ranking import rank

products_bp = Blueprint('products', __name__)

@products_bp.route('/process-products', methods=['POST'])
def process_products():
    data = request.json
    products = data.get('products', [])
    processed_products = []
    for product in products:
        processed_products.append(preprocess_products(product))

    print(processed_products)
    clustered_products = cluster(processed_products)
    ranked_products = rank(clustered_products)

    return jsonify({"status": "success", "processed_data": ranked_products})
