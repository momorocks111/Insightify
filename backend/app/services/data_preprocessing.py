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
        self.is_fitted = False
        self.feature_names = None
        self.categorical_features = None
        self.numeric_features = None

    def fit_transform(self, data: pd.DataFrame):
        logger.info("Starting data preprocessing")
        
        # Identify numeric and categorical columns
        self.numeric_features = data.select_dtypes(include=['int64', 'float64']).columns
        self.categorical_features = data.select_dtypes(include=['object', 'category']).columns

        # If no categorical features, just return the original data
        if len(self.categorical_features) == 0:
            logger.info("No categorical features found. Skipping preprocessing.")
            self.is_fitted = True
            return data

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
                ('num', numeric_transformer, self.numeric_features),
                ('cat', categorical_transformer, self.categorical_features)
            ])

        logger.info("Fitting and transforming data")
        transformed_data = self.preprocessor.fit_transform(data)
        
        # Store feature names
        self.feature_names = (self.numeric_features.tolist() + 
                              self.preprocessor.named_transformers_['cat']
                              .named_steps['onehot'].get_feature_names_out(self.categorical_features).tolist())
        
        transformed_df = pd.DataFrame(transformed_data, columns=self.feature_names, index=data.index)
        
        self.is_fitted = True
        logger.info("Data preprocessing completed")
        return transformed_df

    def transform(self, data: pd.DataFrame):
        if not self.is_fitted:
            raise ValueError("Preprocessor has not been fitted. Call fit_transform first.")
        
        logger.info("Transforming new data")
        
        # If no categorical features were present during fitting, just return the original data
        if len(self.categorical_features) == 0:
            logger.info("No categorical features found. Skipping preprocessing.")
            return data

        transformed_data = self.preprocessor.transform(data)
        
        transformed_df = pd.DataFrame(transformed_data, columns=self.feature_names, index=data.index)
        
        logger.info("Data transformation completed")
        return transformed_df
