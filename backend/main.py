from flask import Flask, request, jsonify
from flask_cors import CORS
from models.model import load_model, train_model
from models.gpt_model import load_gpt2_model, generate_response
from backend.app.utils.data_processing import process_mock_data, process_database_file
import numpy as np
import os
import base64
import sqlite3
from utils.prompts import DATABASE_ANALYSIS_PROMPT

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

gpt2_model, gpt2_tokenizer = load_gpt2_model()

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
    data = request.json.get('data')
    file_content = request.json.get('file_content')
    
    if file_content:
        file_bytes = base64.b64decode(file_content)
        result = process_database_file(file_bytes)
        
        # Generate GPT-2 response based on the analysis
        prompt = DATABASE_ANALYSIS_PROMPT.format(database_structure=str(result))
        gpt2_response = generate_response(gpt2_model, gpt2_tokenizer, prompt)
        
        result['gpt2_analysis'] = gpt2_response
        
        return jsonify(result)
    else:
        return jsonify({"error": "No file content provided"}), 400

@app.route('/test_gpt2', methods=['GET'])
def test_gpt2():
    # Load the test database
    conn = sqlite3.connect('test_db.sqlite')
    cursor = conn.cursor()
    
    # Get the database structure
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    db_structure = {}
    for table in tables:
        table_name = table[0]
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()
        db_structure[table_name] = [col[1] for col in columns]
    
    conn.close()
    
    # Create a prompt
    prompt = f"Analyze this database structure: {db_structure}"
    
    # Generate response
    response = generate_response(gpt2_model, gpt2_tokenizer, prompt, max_length=200)
    
    return jsonify({"gpt2_analysis": response})


if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True, port=5000)
