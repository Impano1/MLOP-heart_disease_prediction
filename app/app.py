from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib
from src.preprocessing import load_data
from src.model import HeartDiseaseModel

app = Flask(__name__)


model = HeartDiseaseModel()
model.load_model('models/heart_disease_model.pkl', 'models/scaler.pkl')

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
    
    new_data = load_data('data/new_data.csv')
    X, y = model.preprocess_data(new_data)
    model.train(X, y)
    model.save_model('models/heart_disease_model.pkl', 'models/scaler.pkl')
    return jsonify({'message': 'Model retrained successfully'})

if __name__ == '__main__':
    app.run(debug=True)