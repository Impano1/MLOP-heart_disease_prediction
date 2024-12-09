import pandas as pd
from src.model import HeartDiseaseModel

# Load the dataset
data = pd.read_csv('data/UCI_Heart_Disease_Dataset_Combined.csv')


model = HeartDiseaseModel()


X, y = model.preprocess_data(data)


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model.train(X_train, y_train)


model.save_model('models/heart_disease_model.pkl', 'models/scaler.pkl', 'models/label_encoders.pkl')