import os
import json
import google.generativeai as genai
from typing import Union, Dict, List
from app.utils.logger import logger

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro')

def get_gemini_response(message: str, data: Union[str, Dict, List]) -> str:
    try:
        chat = model.start_chat(history=[])
        
        if isinstance(data, (dict, list)):
            data_str = json.dumps(data, indent=2, default=str)[:4000]
        else:
            data_str = str(data)[:4000]

        prompt = f"""
        Analyze the following data and provide a comprehensive analytical report:

        Data Type: {type(data).__name__}
        Data Sample:
        {data_str}

        User Query: {message}

        Please provide a detailed analysis including:

        1. Data Structure:
           - Describe the structure and content of the dataset
           - Identify the type of data (CSV, SQL, JSON, etc.)
           - List all columns/fields with their data types (if applicable)

        2. Data Content Analysis:
           - Provide a summary of the data (e.g., number of records, key statistics)
           - Analyze the distribution of values in key columns/fields
           - Identify any patterns or trends in the data

        3. Data Quality Assessment:
           - Evaluate data completeness (any missing values?)
           - Check for data consistency and validity
           - Identify any anomalies or outliers

        4. Specific Insights:
           - Highlight any interesting or unusual data points
           - Provide relevant statistics based on the data type
           - Analyze any geographical or temporal aspects if present

        5. Recommendations:
           - Suggest improvements to the data structure or content
           - Recommend additional data that could enhance the dataset
           - Propose potential use cases or analyses for this data

        Format your response in a structured manner, using markdown for headings and lists. 
        Provide specific examples and numbers from the data where relevant.
        """
        
        response = chat.send_message(prompt)
        return response.text
    except Exception as e:
        logger.error(f"Error in Gemini API: {str(e)}")
        return {"error": f"Failed to get response from the Gemini API: {str(e)}"}
