from flask import Blueprint, request, jsonify
from src.model.predictor import Predictor
from src.utils.data_processing import process_input_data

api = Blueprint('api', __name__)
predictor = Predictor()

@api.route('/predict', methods=['POST'])
def predict_salary():
    data = request.get_json()
    processed_data = process_input_data(data)
    prediction = predictor.predict(processed_data)
    
    return jsonify({'predicted_salary': prediction})