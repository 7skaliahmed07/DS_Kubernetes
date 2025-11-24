from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib
import os

app = FastAPI(title="Iris ML API on Kubernetes", version="1.0")

# Pydantic model for incoming data
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Train the model once when the container starts
MODEL_PATH = "iris_model.pkl"

if not os.path.exists(MODEL_PATH):
    print("Training model for the first time...")
    df = pd.read_csv("data/iris.csv")
    X = df.drop("species", axis=1)
    y = df["species"]
    model = LogisticRegression(max_iter=200)
    model.fit(X, y)
    joblib.dump(model, MODEL_PATH)
    print("Model trained and saved!")
else:
    print("Loading existing model...")

# Load the model
model = joblib.load(MODEL_PATH)

@app.get("/")
def home():
    return {"message": "Iris ML model running on Kubernetes!", "endpoints": ["/stats", "/predict"]}

@app.get("/stats")
def get_stats():
    df = pd.read_csv("data/iris.csv")
    return {
        "rows": len(df),
        "species_distribution": df["species"].value_counts().to_dict(),
        "model_accuracy_on_training_data": round(model.score(df.drop("species", axis=1), df["species"]), 3)
    }

@app.post("/predict")
def predict(features: IrisFeatures):
    data = [[
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.petal_width
    ]]
    prediction = model.predict(data)[0]
    probability = model.predict_proba(data).max()
    return {
        "predicted_species": prediction,
        "confidence": round(probability, 3)
    }