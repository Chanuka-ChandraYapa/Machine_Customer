from flask import Blueprint, request, jsonify
from services.logger import logger
from services.processProduct import ProcessProduct
from services.negotiation import generate_negotiation_email, extract_response_email

file_path = "logs/dummy_supplier.txt"

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

    with open(file_path, 'r') as file:
        content = file.read()  # Reads the entire file content into one variable

        # Extract the response email to get the discount details
        extracted_details = extract_response_email(content)
        logger.info(f"Extracted details: {extracted_details}")

        best_product["discountPercentage"] = extracted_details.get("discount_for_double_quantity", 0)
        best_product["minimumOrderQuantity"] = extracted_details.get("quantity", 0)*2
        best_product["price"] = extracted_details.get("quoted_price_per_unit", 0)*best_product["minimumOrderQuantity"]

    
    if best_product:
        return jsonify({"status": "success", "best_product": best_product})
    else:
        return jsonify({"status": "no_update", "message": "No update needed"})
