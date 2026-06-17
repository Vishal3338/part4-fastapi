from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

app = FastAPI()

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

class Customer(BaseModel):
    total_orders: int
    total_spend: float
    avg_rating: float

class CustomerBatch(BaseModel):
    customers: list

@app.get("/")
def home():
    return {"message": "Customer Churn API Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/predict")
def predict(customer: Customer):

    data = pd.DataFrame([{
        "total_orders": customer.total_orders,
        "total_spend": customer.total_spend,
        "avg_rating": customer.avg_rating
    }])

    prediction = int(model.predict(data)[0])

    probability = float(model.predict_proba(data)[0][1])

    return {
        "prediction": prediction,
        "churn_probability": round(probability, 4)
    }

@app.post("/batch_predict")
def batch_predict(batch: CustomerBatch):

    results = []

    for customer in batch.customers:

        data = pd.DataFrame([customer])

        prediction = int(model.predict(data)[0])

        probability = float(model.predict_proba(data)[0][1])

        results.append({
            "prediction": prediction,
            "churn_probability": round(probability, 4)
        })

    return {"results": results}