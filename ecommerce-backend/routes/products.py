from flask import Blueprint, request, jsonify
from services.feature_extraction import preprocess_products
from services.clustering import cluster
from services.ranking import rank
from services.logger import logger

products_bp = Blueprint('products', __name__)


@products_bp.route('/process-products', methods=['POST'])
def process_products():
    try:
        data = request.json

        # Check if products key exists in request
        if not data or 'products' not in data:
            logger.error("Invalid request payload. 'products' key missing.")
            return jsonify({"status": "error", "message": "Invalid payload"}), 400

        products = data.get('products', [])

        processed_products = []
        for product in products:
            try:
                processed_product = preprocess_products(product)
                processed_products.append(processed_product)
            except Exception as e:
                logger.exception(
                    f"An error occurred while processing product: {product}")

        clustered_products = cluster(processed_products)

        ranked_products = rank(clustered_products)

        return jsonify({"status": "success", "processed_data": ranked_products})

    except Exception as e:
        logger.exception("An error occurred while processing products.")
        return jsonify({"status": "error", "message": "Internal Server Error"}), 500
