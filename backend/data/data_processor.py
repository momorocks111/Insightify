import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def preprocess_data(file_path):
    # Read the file
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        df = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file type")

    # Identify numeric and categorical columns
    numeric_features = df.select_dtypes(include=['int64', 'float64']).columns
    categorical_features = df.select_dtypes(include=['object']).columns

    # Create preprocessing steps
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])

    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    # Combine preprocessing steps
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])

    # Fit and transform the data
    processed_data = preprocessor.fit_transform(df)

    # Get feature names
    numeric_feature_names = numeric_features.tolist()
    categorical_feature_names = preprocessor.named_transformers_['cat'].named_steps['onehot'].get_feature_names_out(categorical_features).tolist()
    all_feature_names = numeric_feature_names + categorical_feature_names

    # Ensure processed_data is 2D
    if processed_data.ndim == 1:
        processed_data = processed_data.reshape(-1, 1)

    # Create DataFrame, handling potential shape mismatches
    if processed_data.shape[1] == len(all_feature_names):
        processed_df = pd.DataFrame(processed_data, columns=all_feature_names, index=df.index)
    else:
        print(f"Warning: Shape mismatch. Data shape: {processed_data.shape}, Features: {len(all_feature_names)}")
        processed_df = pd.DataFrame(processed_data, index=df.index)

    return processed_df, preprocessor