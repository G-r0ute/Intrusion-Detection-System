from flask import Flask, request, jsonify
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

app = Flask(__name__)

# Load the trained model
model = joblib.load('ids_model.pkl')

# Initialize the standard scaler and label encoder (use the same ones as during training)
scaler = StandardScaler()
le = LabelEncoder()

@app.route('/')
def home():
    return "Welcome to the IDS/IPS Machine Learning API. Use /predict endpoint to get predictions."

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)

    # Convert the input data to a DataFrame
    df = pd.DataFrame([data])

    # Preprocess the data
    df['proto'] = le.fit_transform(df['proto'])
    features = df[['time_diff', 'packet_size', 'proto']]
    features = scaler.transform(features)

    # Make a prediction
    prediction = model.predict(features)

    # Return the result as a JSON response
    result = {'prediction': int(prediction[0])}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
