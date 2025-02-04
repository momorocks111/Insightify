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
        
        # Convert data to a string representation
        if isinstance(data, (dict, list)):
            data_str = json.dumps(data, indent=2)
        else:
            data_str = str(data)

        prompt = f"""
        Analyze the following SQL data and provide a comprehensive analytical report:

        Data:
        {data_str}

        User Query: {message}

        Please provide a detailed analysis including:

        1. Data Structure:
           - Describe the table structure(s) in detail
           - List all columns with their data types
           - Identify primary keys and potential relationships

        2. Data Content Analysis:
           - Provide a summary of the data (e.g., number of records, date ranges if applicable)
           - Analyze the distribution of values in key columns (e.g., gender, email domains)
           - Identify any patterns or trends in the data

        3. Data Quality Assessment:
           - Evaluate data completeness (any missing values?)
           - Check for data consistency and validity
           - Identify any anomalies or outliers

        4. Specific Insights:
           - Highlight any interesting or unusual data points
           - Provide statistics on gender distribution, email providers, etc.
           - Analyze IP addresses for any geographical insights

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


