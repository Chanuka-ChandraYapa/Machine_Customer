from flask import Blueprint, request, jsonify
from services.negotiation import generate_negotiation_email
from services.negotiation import extract_response_email


createNegotiationEmail_bp = Blueprint('createNegotiationEmail', __name__)
extractDiscuntDetails_bp = Blueprint('extractDiscuntDetails', __name__)


@createNegotiationEmail_bp.route('/create-negotiation', methods=['POST'])
def process_products():
    data = request.json
    products = data.get('products', {})
    email = generate_negotiation_email(products)

    return {"status": "success", "email": email}

@extractDiscuntDetails_bp.route('/extract-discount-details', methods=['POST'])
def extract_discount_details():
    data = request.json
    email = data.get('email', '')
    extracted_details = extract_response_email(email)

    return {"status": "success", "extracted_details": extracted_details}
