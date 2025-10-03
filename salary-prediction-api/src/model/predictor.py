class Predictor:
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = None

    def load_model(self):
        import joblib
        self.model = joblib.load(self.model_path)

    def predict_salary(self, input_data):
        if self.model is None:
            raise Exception("Model not loaded. Please call load_model() before prediction.")
        return self.model.predict(input_data)