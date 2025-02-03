from flask import Flask, request, jsonify
from flask_cors import CORS
from models.model import load_model, train_model
from utils.data_processing import process_mock_data, process_database_file
import numpy as np
import os
import base64

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

# Check if model exists, if not, create a dummy model
if not os.path.exists('models/model.joblib'):
    print("No model found. Creating a dummy model.")
    X_dummy = np.random.rand(100, 4)
    y_dummy = np.random.randint(2, size=100)
    train_model(X_dummy, y_dummy)

scaler, model = load_model()
print("Model loaded successfully.")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['data']
    scaled_data = scaler.transform(np.array(data).reshape(1, -1))
    prediction = model.predict(scaled_data)
    return jsonify({'prediction': prediction.tolist()})

@app.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'Backend is working!'})

@app.route("/")
def home():
    return "Backend is running"

@app.route('/analyze', methods=['POST'])
def analyze():
    print("Analyze route called")
    data = request.json.get('data')
    file_content = request.json.get('file_content')
    
    if file_content:
        print("Processing file content")
        try:
            file_bytes = base64.b64decode(file_content)
            result = process_database_file(file_bytes)
            if not result:
                return jsonify({"error": "No tables found in the SQL dump"}), 400
            return jsonify(result)
        except Exception as e:
            print(f"Error processing file: {str(e)}")
            return jsonify({"error": str(e)}), 500
    else:
        print("Processing mock data")
        result = process_mock_data(data)
        return jsonify(result)


if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True, port=5000)
