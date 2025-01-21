from flask import Blueprint, request, jsonify
from services.negotiation import generate_negotiation_email


createNegotiationEmail_bp = Blueprint('createNegotiationEmail', __name__)


@createNegotiationEmail_bp.route('/create-negotiation', methods=['POST'])
def process_products():
    data = request.json
    products = data.get('products', {})
    email = generate_negotiation_email(products)

    return {"status": "success", "email": email}
