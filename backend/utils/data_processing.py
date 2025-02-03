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
    
    # Remove MariaDB-specific syntax
    sql_dump = re.sub(r'AUTO_INCREMENT', '', sql_dump)
    sql_dump = re.sub(r'UNSIGNED', '', sql_dump)
    sql_dump = re.sub(r'ENGINE=\w+', '', sql_dump)
    
    # Split the SQL dump into individual statements
    statements = sql_dump.split(';')
    
    executed_statements = 0
    for statement in statements:
        statement = statement.strip()
        if statement:
            try:
                cursor.execute(statement)
                executed_statements += 1
            except sqlite3.OperationalError as e:
                logging.error(f"Error executing statement: {e}")
                logging.error(f"Problematic statement: {statement}")
                continue
    
    logging.info(f"Executed {executed_statements} out of {len(statements)} statements")
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    logging.info(f"Found {len(tables)} tables")
    
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
