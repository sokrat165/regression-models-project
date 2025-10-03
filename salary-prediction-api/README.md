# Salary Prediction API

This project is a Flask-based API for predicting salaries based on player statistics from the Hitters dataset. It utilizes a machine learning model to provide salary predictions and returns the results in a user-friendly HTML format.

## Project Structure

```
salary-prediction-api
├── src
│   ├── main.py               # Entry point of the application
│   ├── model
│   │   ├── predictor.py      # Contains the Predictor class for salary predictions
│   │   └── __init__.py       # Initializes the model package
│   ├── api
│   │   ├── routes.py         # Defines API routes for salary predictions
│   │   └── __init__.py       # Initializes the API package
│   ├── utils
│   │   ├── data_processing.py # Functions for processing input data
│   │   └── __init__.py       # Initializes the utils package
│   └── templates
│       └── results.html      # HTML template for displaying prediction results
├── requirements.txt           # Lists project dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Specifies files to ignore in version control
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd salary-prediction-api
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python src/main.py
   ```

2. Access the API at `http://127.0.0.1:5000/predict` to make salary predictions.

3. Input the required player statistics in the request body, and the API will return the predicted salary.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.