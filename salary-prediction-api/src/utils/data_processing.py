import pandas as pd
import numpy as np

def preprocess_data(input_data):
    # Convert input data to DataFrame
    df = pd.DataFrame(input_data)

    # Handle missing values
    df.fillna(df.mean(), inplace=True)

    # Convert categorical variables to dummy variables
    df = pd.get_dummies(df, columns=['League', 'Division', 'NewLeague'], drop_first=True)

    return df

def extract_features(df):
    # Extract features for prediction
    features = df.drop('Salary', axis=1, errors='ignore')
    return features

def prepare_input_data(input_data):
    # Preprocess the input data
    processed_data = preprocess_data(input_data)
    
    # Extract features
    features = extract_features(processed_data)
    
    return features