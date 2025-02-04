import os
import json
from typing import Union
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

def get_gemini_response(message: str, data: Union[list, dict]) -> str:
    try:
        chat = model.start_chat(history=[])
        
        # Prepare a structured prompt with the data and analysis request
        if isinstance(data, list):
            data_summary = "\n".join([f"File: {file_path}" for file_path in data])
        else:
            data_summary = json.dumps(data, indent=2)

        prompt = f"""
        Analyze the following data and provide insights:

        Data Summary:
        {data_summary}

        User Message: {message}

        Please provide the following:
        1. Identify key trends in the data
        2. Suggest relevant visualizations
        3. Provide insights based on the data characteristics
        4. Any additional observations or recommendations

        Format your response in a structured manner, using markdown for headings and lists.
        """
        
        response = chat.send_message(prompt)
        return response.text
    except Exception as e:
        print(f"Error while calling Gemini API: {e}")
        return {"error": f"Failed to get response from the Gemini API: {str(e)}"}
