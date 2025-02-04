from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from api.gemini_api import get_gemini_response
from data.data_processor import preprocess_data
from data.data_analyzer import analyze_data
from data.data_visualizer import generate_visualizations
import os

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

# Ensure the uploads directory exists
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Dictionary to store files per chat session
chat_files = {}

@app.route('/api/echo', methods=['POST', 'OPTIONS'])
def echo():
    if request.method == 'OPTIONS':
        return '', 204
    data = request.json
    message = data.get('message', '')
    
    if not message:
        return jsonify({"error": "Message is required."}), 400
    
    # Send the message to Gemini and get the response
    gemini_response = get_gemini_response(message, [])
    
    if isinstance(gemini_response, dict) and "error" in gemini_response:
        return jsonify(gemini_response), 500
    
    return jsonify({"message": gemini_response})

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part', 'message': 'No file part'}), 400

    file = request.files['file']
    chat_id = request.form.get('chat_id')  # Get chat ID from the request

    if not chat_id:
        return jsonify({'error': 'Chat ID is required', 'message': 'Chat ID is required'}), 400

    if file.filename == '':
        return jsonify({'error': 'No selected file', 'message': 'No selected file'}), 400

    if file:
        # Save the file to the uploads folder
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Read the file into a DataFrame
        try:
            if file.filename.endswith('.csv'):
                df = pd.read_csv(file_path)
            elif file.filename.endswith('.xlsx'):
                df = pd.read_excel(file_path)
            else:
                return jsonify({'error': 'Unsupported file type', 'message': 'Unsupported file type'}), 400

            # Store the file path in the chat_files dictionary
            if chat_id not in chat_files:
                chat_files[chat_id] = []
            chat_files[chat_id].append(file_path)

            # Return a success message and basic file info
            return jsonify({
                'message': 'File uploaded successfully',
                'filename': file.filename,
                'rows': df.shape[0],
                'columns': df.shape[1],
                'preview': df.head().to_dict(orient='records')  # First 5 rows as JSON
            })
        except Exception as e:
            return jsonify({'error': f'Error processing file: {str(e)}', 'message': f'Error processing file: {str(e)}'}), 500

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.json
    message = data.get('message', '')
    chat_id = data.get('chat_id', '')
    
    if not message:
        return jsonify({"error": "Message is required."}), 400
    
    # Get the file paths for this chat session
    file_paths = chat_files.get(chat_id, [])
    
    # Send the message and file paths to Gemini and get the response
    gemini_response = get_gemini_response(message, file_paths)
    
    if "error" in gemini_response:
        return jsonify(gemini_response), 500
    
    return jsonify({"message": gemini_response})

@app.route('/api/analyze_data', methods=['POST'])
def analyze_data_route():
    data = request.json
    chat_id = data.get('chat_id')
    
    if not chat_id:
        return jsonify({"error": "Chat ID is required."}), 400
    
    file_paths = chat_files.get(chat_id, [])
    
    if not file_paths:
        return jsonify({"error": "No files uploaded for this chat."}), 400
    
    try:
        results = []
        for file_path in file_paths:
            processed_df, preprocessor = preprocess_data(file_path)
            analysis_results = analyze_data(processed_df)
            visualizations = generate_visualizations(processed_df)
            
            file_result = {
                'file_name': os.path.basename(file_path),
                'analysis': analysis_results,
                'visualizations': visualizations
            }
            results.append(file_result)
        
        # Get insights from Gemini
        insights = get_gemini_response("Analyze this data and provide insights", results)
        
        return jsonify({
            "results": results,
            "insights": insights
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/analyze_with_file', methods=['POST'])
def analyze_with_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part', 'message': 'No file part'}), 400

    file = request.files['file']
    chat_id = request.form.get('chat_id')
    message = request.form.get('message')

    if not chat_id:
        return jsonify({'error': 'Chat ID is required', 'message': 'Chat ID is required'}), 400

    if file.filename == '':
        return jsonify({'error': 'No selected file', 'message': 'No selected file'}), 400

    if file:
        # Save the file to the uploads folder
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        try:
            processed_df, preprocessor = preprocess_data(file_path)
            analysis_results = analyze_data(processed_df)
            visualizations = generate_visualizations(processed_df)
            
            file_result = {
                'file_name': file.filename,
                'analysis': analysis_results,
                'visualizations': visualizations
            }
            
            # Get insights from Gemini
            insights = get_gemini_response(f"Analyze this data and provide insights. User message: {message}", [file_result])
            
            return jsonify({
                "message": insights,
                "file_info": {
                    'filename': file.filename,
                    'rows': processed_df.shape[0],
                    'columns': processed_df.shape[1],
                    'preview': processed_df.head().to_dict(orient='records')
                }
            })
        except Exception as e:
            return jsonify({'error': f'Error processing file: {str(e)}', 'message': f'Error processing file: {str(e)}'}), 500

    return jsonify({'error': 'Unknown error', 'message': 'Unknown error'}), 500


if __name__ == '__main__':
    app.run(debug=True)
