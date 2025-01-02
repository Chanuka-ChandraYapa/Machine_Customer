from flask import Blueprint, request, jsonify
from services.requirements import update_requirements

requirements_bp = Blueprint('requirements', __name__)

@requirements_bp.route('/requirements', methods=['POST'])
def requirements():
    data = request.json
    requirements = data.get('requirements')
    update_requirements(requirements)
    print(requirements)

    return jsonify({"status": "success", "processed_data": ""})
