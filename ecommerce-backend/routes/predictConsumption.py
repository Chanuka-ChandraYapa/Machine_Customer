from flask import Blueprint, request, jsonify
from consumptionPredictionModel.prediction import predict_threshold

predictConsumption_bp = Blueprint('predictConsumption', __name__)


@predictConsumption_bp.route('/predictConsumption', methods=['POST'])
def predictConsumption():
    try:
        # Extract data from the request
        data = request.json
        if not data or not isinstance(data, dict):
            return jsonify({"status": "error", "message": "Invalid input data"}), 400

        # Extract features from the request data
        features = data.get('data')
        if not features:
            return jsonify({"status": "error", "message": "Missing 'data' key in the input"}), 400

        # Predict threshold
        threshold = predict_threshold(features)
        return jsonify({"status": "success", "threshold": threshold}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
