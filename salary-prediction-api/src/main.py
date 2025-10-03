from flask import Flask, request, render_template
from model.predictor import Predictor
from utils.data_processing import process_input_data

app = Flask(__name__)
predictor = Predictor()

@app.route('/')
def home():
    return render_template('results.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.json
    processed_data = process_input_data(input_data)
    salary_prediction = predictor.predict(processed_data)
    return {'predicted_salary': salary_prediction}

if __name__ == '__main__':
    app.run(debug=True)