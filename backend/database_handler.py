import pandas as pd
import sqlite3
import sqlparse

def process_csv(file):
    return pd.read_csv(file)

def process_excel(file):
    return pd.read_excel(file)

def process_sql(file):
    sql_content = file.read().decode('utf-8')
    statements = sqlparse.split(sql_content)
    # For simplicity, we'll just return the statements as a list
    return statements

def process_sqlite(file_path):
    conn = sqlite3.connect(file_path)
    tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
    data = {}
    for table in tables['name']:
        data[table] = pd.read_sql_query(f"SELECT * FROM {table}", conn)
    conn.close()
    return data

def process_database_file(file, file_path=None):
    if file.filename.endswith('.csv'):
        return process_csv(file)
    elif file.filename.endswith('.xlsx'):
        return process_excel(file)
    elif file.filename.endswith('.sql'):
        return process_sql(file)
    elif file.filename.endswith('.db') or file.filename.endswith('.sqlite'):
        return process_sqlite(file_path)
    else:
        raise ValueError("Unsupported file type")
