import pandas as pd
import numpy as np
from scipy import stats

def analyze_data(df):
    # Basic statistical analysis
    basic_stats = df.describe()

    # Generate summary statistics for each column
    summary_stats = pd.DataFrame({
        'data_type': df.dtypes,
        'non_null_count': df.notnull().sum(),
        'null_count': df.isnull().sum(),
        'unique_count': df.nunique(),
        'mean': df.mean(numeric_only=True),
        'median': df.median(numeric_only=True),
        'std': df.std(numeric_only=True),
        'min': df.min(numeric_only=True),
        'max': df.max(numeric_only=True)
    })

    # Identify correlations between variables
    correlations = df.corr()

    # Identify top correlations
    top_correlations = (correlations.where(np.triu(np.ones(correlations.shape), k=1).astype(bool))
                        .stack()
                        .sort_values(ascending=False)
                        .head(10))

    return {
        'basic_stats': basic_stats.to_dict(),
        'summary_stats': summary_stats.to_dict(),
        'correlations': correlations.to_dict(),
        'top_correlations': top_correlations.to_dict()
    }
