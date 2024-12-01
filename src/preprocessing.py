import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data, scaler=None):
    # Handle categorical features
    data = pd.get_dummies(data, columns=['ChestPainType'], drop_first=True)
    
    # Split data into features and target
    X = data.drop('HeartDisease', axis=1)
    y = data['HeartDisease']
    
    # Standardize the features
    if scaler is None:
        scaler = StandardScaler()
        X = scaler.fit_transform(X)
    else:
        X = scaler.transform(X)
    
    return X, y, scaler