import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import logging

logger = logging.getLogger(__name__)

class DataPreprocessor:
    def __init__(self):
        self.preprocessor = None

    def fit_transform(self, data: pd.DataFrame):
        logger.info("Starting data preprocessing")
        
        # Identify numeric and categorical columns
        numeric_features = data.select_dtypes(include=['int64', 'float64']).columns
        categorical_features = data.select_dtypes(include=['object', 'category']).columns

        numeric_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ])

        categorical_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
            ('onehot', OneHotEncoder(handle_unknown='ignore'))
        ])

        self.preprocessor = ColumnTransformer(
            transformers=[
                ('num', numeric_transformer, numeric_features),
                ('cat', categorical_transformer, categorical_features)
            ])

        logger.info("Fitting and transforming data")
        transformed_data = self.preprocessor.fit_transform(data)
        
        # Convert to DataFrame and set column names
        feature_names = (numeric_features.tolist() + 
                         self.preprocessor.named_transformers_['cat']
                         .named_steps['onehot'].get_feature_names_out(categorical_features).tolist())
        
        transformed_df = pd.DataFrame(transformed_data, columns=feature_names, index=data.index)
        
        logger.info("Data preprocessing completed")
        return transformed_df

    def transform(self, data: pd.DataFrame):
        if self.preprocessor is None:
            raise ValueError("Preprocessor has not been fitted. Call fit_transform first.")
        
        logger.info("Transforming new data")
        transformed_data = self.preprocessor.transform(data)
        
        feature_names = (self.preprocessor.named_transformers_['num'].get_feature_names_out().tolist() + 
                         self.preprocessor.named_transformers_['cat']
                         .named_steps['onehot'].get_feature_names_out().tolist())
        
        transformed_df = pd.DataFrame(transformed_data, columns=feature_names, index=data.index)
        
        logger.info("Data transformation completed")
        return transformed_df
