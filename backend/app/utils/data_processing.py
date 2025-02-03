import pandas as pd
import numpy as np
import sqlite3
import re
import logging

logging.basicConfig(level=logging.INFO)

def process_file(file):
    df = pd.read_csv(file)
    return df.to_dict()

def process_mock_data(data):
    if isinstance(data, str):
        word_count = len(data.split())
        char_count = len(data)
        return {
            "type": "text_analysis",
            "word_count": word_count,
            "character_count": char_count,
            "sample_insight": f"The text contains {word_count} words."
        }
    elif isinstance(data, list):
        arr = np.array(data)
        return {
            "type": "numerical_analysis",
            "mean": float(np.mean(arr)),
            "median": float(np.median(arr)),
            "std_dev": float(np.std(arr)),
            "sample_insight": f"The average value is {float(np.mean(arr)):.2f}."
        }
    else:
        return {"error": "Unsupported data type"}

def process_database_file(file_content):
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    sql_dump = file_content.decode('utf-8')
    
    # Execute SQL statements
    for statement in sql_dump.split(';'):
        try:
            cursor.execute(statement)
        except sqlite3.Error as e:
            print(f"Error executing statement: {e}")
    
    # Analyze database structure
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    analysis_result = {}
    
    for table in tables:
        table_name = table[0]
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        
        analysis_result[table_name] = {
            "row_count": len(df),
            "column_count": len(df.columns),
            "columns": df.columns.tolist(),
            "sample_data": df.head().to_dict(orient='records'),
            "summary_stats": df.describe().to_dict()
        }
    
    conn.close()
    return analysis_result
