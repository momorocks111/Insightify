import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO

def generate_visualizations(df):
    visualizations = []

    # Histogram for numerical columns
    for col in df.select_dtypes(include=['int64', 'float64']).columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(df[col], kde=True)
        plt.title(f'Distribution of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')
        
        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        img_str = base64.b64encode(buf.getvalue()).decode()
        visualizations.append({
            'type': 'histogram',
            'column': col,
            'image': img_str
        })
        plt.close()

    # Correlation heatmap
    plt.figure(figsize=(12, 10))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_str = base64.b64encode(buf.getvalue()).decode()
    visualizations.append({
        'type': 'heatmap',
        'image': img_str
    })
    plt.close()

    return visualizations
