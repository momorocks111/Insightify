import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro')

def get_gemini_response(message: str, data: str) -> str:
    try:
        chat = model.start_chat(history=[])
        
        if data:
            prompt = f"""
            Analyze the following CSV data and provide a comprehensive analytical report:

            Data Sample:
            {data[:1000]}  # Limiting to first 1000 characters for brevity

            User Query: {message}

            Please provide a detailed analysis including:

            1. Data Overview:
               - Describe the structure and content of the dataset
               - Identify the number of rows, columns, and data types

            2. Statistical Analysis:
               - Provide summary statistics for numerical columns (mean, median, standard deviation, min, max)
               - Identify any outliers or anomalies in the data

            3. Key Trends and Patterns:
               - Identify and describe any significant trends or patterns in the data
               - Analyze the distribution of categorical variables (e.g., gender)
               - Examine relationships between different variables

            4. Data Quality Assessment:
               - Identify any missing values, duplicates, or inconsistencies in the data
               - Suggest data cleaning or preprocessing steps if necessary

            5. Advanced Analytics (if applicable):
               - Perform correlation analysis between relevant variables
               - Suggest potential predictive models or machine learning approaches for this dataset

            6. Visualizations:
               - Recommend specific charts or graphs that would best represent the data and insights
               - Explain what each visualization would reveal about the data

            7. Business Insights and Recommendations:
               - Provide actionable insights based on the data analysis
               - Suggest areas for further investigation or data collection

            8. Limitations and Considerations:
               - Discuss any limitations of the current dataset or analysis
               - Suggest additional data that could enhance the analysis

            Format your response in a structured manner, using markdown for headings and lists. Provide detailed explanations and justifications for your analysis and recommendations.
            """
        else:
            prompt = message

        response = chat.send_message(prompt)
        return response.text
    except Exception as e:
        return {"error": f"Failed to get response from the Gemini API: {str(e)}"}

