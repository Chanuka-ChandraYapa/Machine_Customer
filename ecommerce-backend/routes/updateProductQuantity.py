from flask import Blueprint, request, jsonify
from logger import logger
from services.processProduct import ProcessProduct

updateProductQuantity_bp = Blueprint('updateProductQuantity', __name__)

@updateProductQuantity_bp.route('/updateProductQuantity', methods=['POST'])
def updateProductQuantity():
    data = request.json
    product = data.get('productName')
    remainingQuantity = data.get('remainingQuantity')
    
    # Get the best product to buy based on the current product and quantity
    best_product = ProcessProduct(product, remainingQuantity)

    logger.info(f"Best product to buy: {best_product}")
    
    if best_product:
        return jsonify({"status": "success", "best_product": best_product})
    else:
        return jsonify({"status": "no_update", "message": "No update needed"})
