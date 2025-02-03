from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib

def train_model(X, y):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    model = RandomForestClassifier()
    model.fit(X_scaled, y)
    joblib.dump((scaler, model), 'models/model.joblib')

def load_model():
    return joblib.load('models/model.joblib')
