from flask import Blueprint, request, jsonify
from services.logger import logger
from services.processProduct import ProcessProduct
from services.negotiation import generate_negotiation_email, extract_response_email

updateProductQuantity_bp = Blueprint('updateProductQuantity', __name__)

@updateProductQuantity_bp.route('/updateProductQuantity', methods=['POST'])
def updateProductQuantity():
    data = request.json
    product = data.get('productName')
    remainingQuantity = data.get('remainingQuantity')
    
    # Get the best product to buy based on the current product and quantity
    best_product = ProcessProduct(product, remainingQuantity)

    logger.info(f"Best product to buy: {best_product}")

    # Generate a negotiation email for the best product
    generated_email = generate_negotiation_email(best_product)
    logger.info(f"Generated email: {generated_email}")

    # Extract the response email to get the discount details
    # extracted_details = extract_response_email(generated_email)
    # logger.info(f"Extracted details: {extracted_details}")

    
    if best_product:
        return jsonify({"status": "success", "best_product": best_product})
    else:
        return jsonify({"status": "no_update", "message": "No update needed"})
