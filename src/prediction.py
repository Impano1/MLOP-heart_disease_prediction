import joblib
import numpy as np

def load_model(model_path, scaler_path):
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    return model, scaler

def predict(model, scaler, input_data):
    input_data = np.array(input_data).reshape(1, -1)
    input_data = scaler.transform(input_data)
    prediction = model.predict(input_data)
    return prediction