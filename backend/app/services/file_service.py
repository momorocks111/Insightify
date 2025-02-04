import pandas as pd
import sqlparse
from typing import Union, List, Dict
from werkzeug.datastructures import FileStorage
import io

def process_csv(file: FileStorage) -> pd.DataFrame:
    # Reset the file pointer to the beginning of the file
    file.seek(0)
    return pd.read_csv(io.StringIO(file.read().decode('utf-8')))

def process_excel(file: FileStorage) -> pd.DataFrame:
    # Reset the file pointer to the beginning of the file
    file.seek(0)
    return pd.read_excel(io.BytesIO(file.read()))

def process_sql(file: FileStorage) -> List[Dict]:
    # Reset the file pointer to the beginning of the file
    file.seek(0)
    sql_content = file.read().decode('utf-8')
    statements = sqlparse.split(sql_content)
    parsed_statements = []
    for stmt in statements:
        parsed = sqlparse.parse(stmt)[0]
        if parsed.get_type() == 'CREATE':
            table_name = next((token.value for token in parsed.tokens if isinstance(token, sqlparse.sql.Identifier)), None)
            columns = [str(token) for token in parsed.tokens if isinstance(token, sqlparse.sql.Parenthesis)]
            parsed_statements.append({
                'type': 'CREATE',
                'table': table_name,
                'columns': columns[0] if columns else ''
            })
        elif parsed.get_type() == 'INSERT':
            table_name = next((token.value for token in parsed.tokens if isinstance(token, sqlparse.sql.Identifier)), None)
            values = next((str(token) for token in parsed.tokens if isinstance(token, sqlparse.sql.Values)), None)
            parsed_statements.append({
                'type': 'INSERT',
                'table': table_name,
                'values': values
            })
    return parsed_statements

def process_sqlite(file_path: str) -> Dict[str, pd.DataFrame]:
    import sqlite3
    conn = sqlite3.connect(file_path)
    tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
    data = {}
    for table in tables['name']:
        data[table] = pd.read_sql_query(f"SELECT * FROM {table}", conn)
    conn.close()
    return data

def process_file(file: FileStorage, file_path: str) -> Union[pd.DataFrame, List[Dict], Dict[str, pd.DataFrame]]:
    # Check if the file is empty
    file.seek(0, io.SEEK_END)
    if file.tell() == 0:
        raise ValueError("The uploaded file is empty")
    file.seek(0)  # Reset file pointer to the beginning
    
    file_extension = file.filename.split('.')[-1].lower()
    processors = {
        'csv': process_csv,
        'xlsx': process_excel,
        'sql': process_sql,
        'db': process_sqlite,
        'sqlite': process_sqlite
    }
    processor = processors.get(file_extension)
    if not processor:
        raise ValueError(f"Unsupported file type: {file_extension}")
    
    if file_extension in ['db', 'sqlite']:
        return processor(file_path)
    return processor(file)
