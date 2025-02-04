import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro')

def get_gemini_response(message: str, data: str) -> str:
    print("Entering get_gemini_response function")
    try:
        chat = model.start_chat(history=[])
        
        if data:
            print("Preparing prompt with data")
            prompt = f"""
            Analyze the following JSON data and provide insights:

            Data:
            {data[:1000]}  # Limiting to first 1000 characters for brevity

            User Message: {message}

            Please provide the following:
            1. Identify key trends in the data
            2. Suggest relevant visualizations
            3. Provide insights based on the data characteristics
            4. Any additional observations or recommendations

            Format your response in a structured manner, using markdown for headings and lists.
            """
        else:
            print("No data provided, using message as prompt")
            prompt = message

        print("Sending message to Gemini API")
        response = chat.send_message(prompt)
        print("Received response from Gemini API")
        return response.text
    except Exception as e:
        print(f"Error while calling Gemini API: {e}")
        return {"error": f"Failed to get response from the Gemini API: {str(e)}"}

