from typing import Union, Dict, List
import pandas as pd
import json

def analyze_data(data: Union[pd.DataFrame, List[Dict], Dict[str, pd.DataFrame], str]) -> Dict:
    if isinstance(data, pd.DataFrame):
        return analyze_dataframe(data)
    elif isinstance(data, list) and all(isinstance(item, dict) for item in data):
        return analyze_sql_statements(data)
    elif isinstance(data, dict) and all(isinstance(value, pd.DataFrame) for value in data.values()):
        return analyze_sqlite_database(data)
    elif isinstance(data, str):
        return analyze_text(data)
    else:
        raise ValueError("Unsupported data format for analysis")

def analyze_dataframe(df: pd.DataFrame) -> Dict:
    analysis = {
        'shape': df.shape,
        'columns': df.columns.tolist(),
        'dtypes': df.dtypes.astype(str).to_dict(),
        'summary': df.describe().to_dict(),
        'null_counts': df.isnull().sum().to_dict(),
        'sample': df.head().to_dict(orient='records')
    }
    return json.loads(json.dumps(analysis, default=str))

def analyze_sql_statements(statements: List[Dict]) -> Dict:
    create_statements = [stmt for stmt in statements if stmt['type'] == 'CREATE']
    insert_statements = [stmt for stmt in statements if stmt['type'] == 'INSERT']
    
    analysis = {
        'table_count': len(create_statements),
        'create_statements': create_statements,
        'insert_count': len(insert_statements),
        'sample_inserts': insert_statements[:5]
    }
    return analysis

def analyze_sqlite_database(data: Dict[str, pd.DataFrame]) -> Dict:
    analysis = {
        'table_count': len(data),
        'tables': {
            table_name: analyze_dataframe(df)
            for table_name, df in data.items()
        }
    }
    return analysis

def analyze_text(text: str) -> Dict:
    analysis = {
        'character_count': len(text),
        'word_count': len(text.split()),
        'line_count': len(text.splitlines()),
        'sample': text[:1000] if len(text) > 1000 else text
    }
    return analysis
