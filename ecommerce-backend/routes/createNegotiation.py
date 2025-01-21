from flask import Blueprint, request, jsonify
from services.negotiation import generate_negotiation_email, extract_response_email

createNegotiationEmail_bp = Blueprint('createNegotiationEmail', __name__)
extractDiscuntDetails_bp = Blueprint('extractDiscuntDetails', __name__)


@createNegotiationEmail_bp.route('/create-negotiation', methods=['POST'])
def process_products():
    data = request.json
    products = data.get('products', {})
    email = generate_negotiation_email(products)

    # Save products and email to a text file
    with open('create_negotiation_log.txt', 'a') as file:
        file.write(f"Products: {products}\nGenerated Email: {email}\n\n")

    return {"status": "success", "email": email}


@extractDiscuntDetails_bp.route('/extract-discount-details', methods=['POST'])
def extract_discount_details():
    data = request.json
    email = data.get('email', '')
    extracted_details = extract_response_email(email)

    # Save email and extracted details to a text file
    with open('extract_discount_details_log.txt', 'a') as file:
        file.write(f"Email: {email}\nExtracted Details: {extracted_details}\n\n")

    return {"status": "success", "extracted_details": extracted_details}
