from flask import Blueprint, request, jsonify
from services.feature_extraction import preprocess_products
from services.clustering import cluster
from services.ranking import rank
from logger import logger  # Import the logger

products_bp = Blueprint('products', __name__)


@products_bp.route('/process-products', methods=['POST'])
def process_products():
    try:
        logger.info("Received request to process products.")
        data = request.json

        # Check if products key exists in request
        if not data or 'products' not in data:
            logger.error("Invalid request payload. 'products' key missing.")
            return jsonify({"status": "error", "message": "Invalid payload"}), 400

        products = data.get('products', [])
        logger.info(f"Number of products received: {len(products)}")

        processed_products = []
        for product in products:
            try:
                processed_product = preprocess_products(product)
                logger.info(f"Processed product: {product}")
                processed_products.append(processed_product)
            except Exception as e:
                logger.error(
                    f"Error processing product: {product}. Error: {e}")

        logger.info(
            f"Processed all products. Count: {len(processed_products)}")

        clustered_products = cluster(processed_products)
        logger.info(f"Clustered products: {clustered_products}")

        ranked_products = rank(clustered_products)
        logger.info(f"Ranked products: {ranked_products}")

        return jsonify({"status": "success", "processed_data": ranked_products})

    except Exception as e:
        logger.exception("An error occurred while processing products.")
        return jsonify({"status": "error", "message": "Internal Server Error"}), 500
