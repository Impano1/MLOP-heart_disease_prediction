import sys
import os
from flask import Flask, request, jsonify, render_template
import pandas as pd

# Add the src directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from model import HeartDiseaseModel

app = Flask(__name__)

# Load the model, scaler, and label encoders
model = HeartDiseaseModel()
model.load_model('models/heart_disease_model.pkl', 'models/scaler.pkl', 'models/label_encoders.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return jsonify({'prediction': int(prediction[0])})

@app.route('/retrain', methods=['POST'])
def retrain():
    new_data = pd.read_csv('data/new_data.csv')
    X, y = model.preprocess_data(new_data)
    model.train(X, y)
    model.save_model('models/heart_disease_model.pkl', 'models/scaler.pkl', 'models/label_encoders.pkl')
    return jsonify({'message': 'Model retrained successfully'})

if __name__ == '__main__':
    app.run(debug=True)