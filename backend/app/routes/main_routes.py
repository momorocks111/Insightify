from flask import Blueprint, request, jsonify
from app.services.gemini_service import get_gemini_response
from app.utils.logger import logger

main_routes = Blueprint('main', __name__)

@main_routes.route('/api/echo', methods=['POST', 'OPTIONS'])
def echo():
    if request.method == 'OPTIONS':
        return '', 204
    data = request.json
    message = data.get('message', '')
    
    if not message:
        return jsonify({"error": "Message is required."}), 400
    
    gemini_response = get_gemini_response(message, None)
    
    if isinstance(gemini_response, dict) and "error" in gemini_response:
        return jsonify(gemini_response), 500
    
    return jsonify({"message": gemini_response, "file_info": None})
