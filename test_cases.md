# API Test Cases

## Test Case 1 - Health Check

Endpoint:
GET /health

Expected Response:

{
"status": "healthy"
}

## Test Case 2 - Single Prediction

Endpoint:
POST /predict

Input:

{
"total_orders": 5,
"total_spend": 2500,
"avg_rating": 4.2
}

Expected Response:

{
"churn_probability": 0.xx,
"prediction": 0 or 1
}

## Test Case 3 - High Risk Customer

Input:

{
"total_orders": 1,
"total_spend": 100,
"avg_rating": 2.5
}

Expected Response:

Higher churn probability
