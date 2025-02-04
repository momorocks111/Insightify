import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read the Google API key from environment variable
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure the Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-pro')

def get_gemini_response(message: str, file_paths: list) -> str:
    try:
        # Start a new chat
        chat = model.start_chat(history=[])
        
        # If there are file paths, include them in the message
        if file_paths:
            file_info = "\n".join([f"File: {path}" for path in file_paths])
            message = f"Files uploaded:\n{file_info}\n\nUser query: {message}"
        
        # Send the message and get the response
        response = chat.send_message(message)
        
        return response.text
    except Exception as e:
        print(f"Error while calling Gemini API: {e}")
        return {"error": "Failed to get response from the Gemini API."}
