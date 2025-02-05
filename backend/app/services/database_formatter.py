import json

def format_sql_analysis(analysis_results):
    formatted_results = {
        'tables': []
    }
    
    for stmt in analysis_results['create_statements']:
        table_info = {
            'name': stmt['table'],
            'columns': parse_columns(stmt['columns'])
        }
        formatted_results['tables'].append(table_info)
    
    return formatted_results

def parse_columns(columns_str):
    columns = []
    # Remove parentheses and split by comma
    column_defs = columns_str.strip('()').split(',')
    for column_def in column_defs:
        parts = column_def.strip().split()
        if len(parts) >= 2:
            columns.append({
                'name': parts[0],
                'type': ' '.join(parts[1:])
            })
    return columns

def format_dataframe_analysis(analysis_results):
    return {
        'tables': [{
            'name': 'Data',
            'columns': [{'name': col, 'type': str(dtype)} for col, dtype in analysis_results['dtypes'].items()]
        }]
    }

def format_sqlite_analysis(analysis_results):
    formatted_results = {
        'tables': []
    }
    
    for table_name, table_info in analysis_results['tables'].items():
        formatted_table = {
            'name': table_name,
            'columns': [{'name': col, 'type': str(dtype)} for col, dtype in table_info['dtypes'].items()]
        }
        formatted_results['tables'].append(formatted_table)
    
    return formatted_results
