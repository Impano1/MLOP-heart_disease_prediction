# MLOP-heart_disease_prediction

## Project Description

This project demonstrates the deployment of a machine learning model for heart disease prediction. The model is trained on a dataset from the UCI repository and deployed using a Flask web application. The application allows users to make predictions, upload new data, and trigger model retraining.

## Features

- **Model Prediction**: Allow a user to make a prediction on one data point.
- **Visualizations**: Create visualizations that make sense of different features in your dataset.
- **Upload Data**: Allow users to upload new data for retraining.
- **Trigger Retraining**: Allow users to trigger model retraining based on the uploaded data.


## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (optional but recommended)

### Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/Impano1/MLOP-heart_disease_prediction
   cd heart-disease-prediction

   Create and Activate a Virtual Environment:

   python -m venv venv
source venv/bin/activate  # On macOS/Linux
.\venv\Scripts\activate  # On Windows


Install Dependencies:

pip install -r requirements.txt

Train the Model:
python train_model.py

Run the Flask Application:

python app/app.py


Visualizations
The project includes visualizations to analyze and interpret the dataset features. These visualizations are created and saved in the visualizations directory.

Example Visualizations
Age Distribution by Heart Disease Status
Chest Pain Type vs Heart Disease
Maximum Heart Rate vs Age
Correlation Matrix of Numerical Features