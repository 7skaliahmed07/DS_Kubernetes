from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from Kubernetes! This is a Data Science demo"}

@app.get("/stats")
def get_stats():
    df = pd.read_csv("data/iris.csv")
    stats = {
        "rows": len(df),
        "columns": list(df.columns),
        "species_count": df["species"].value_counts().to_dict(),
        "mean_sepal_length": round(df["sepal_length"].mean(), 2)
    }
    return stats