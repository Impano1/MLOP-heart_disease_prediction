import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder

class HeartDiseaseModel:
    def __init__(self):
        self.model = RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            random_state=42
        )
        self.scaler = StandardScaler()
        self.label_encoders = {}

    def preprocess_data(self, df):
        """
        Preprocess the input data by handling categorical variables and scaling numerical features.
        """
        
        df_processed = df.copy()
        
        
        categorical_cols = ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina']
        
        
        numerical_cols = ['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak']
        
        
        for col in categorical_cols:
            if col not in self.label_encoders:
                self.label_encoders[col] = LabelEncoder()
                df_processed[col] = self.label_encoders[col].fit_transform(df_processed[col])
            else:
                df_processed[col] = self.label_encoders[col].transform(df_processed[col])
        
        
        df_processed[numerical_cols] = self.scaler.fit_transform(df_processed[numerical_cols])
        
        
        X = df_processed.drop('HeartDisease', axis=1)
        y = df_processed['HeartDisease']
        
        return X, y

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def save_model(self, model_path, scaler_path, encoders_path):
        joblib.dump(self.model, model_path)
        joblib.dump(self.scaler, scaler_path)
        joblib.dump(self.label_encoders, encoders_path)

    def load_model(self, model_path, scaler_path, encoders_path):
        self.model = joblib.load(model_path)
        self.scaler = joblib.load(scaler_path)
        self.label_encoders = joblib.load(encoders_path)

    def predict(self, input_data):
        
        input_data_processed = input_data.copy()
        categorical_cols = ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina']
        numerical_cols = ['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak']
        
        for col in categorical_cols:
            input_data_processed[col] = self.label_encoders[col].transform(input_data_processed[col])
        
        input_data_processed[numerical_cols] = self.scaler.transform(input_data_processed[numerical_cols])
        
        return self.model.predict(input_data_processed)