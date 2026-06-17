# Part 4 - FastAPI Churn Scoring Service

## Endpoints

### GET /

Returns API status message.

### GET /health

Returns health status.

### POST /predict

Predicts customer churn probability.

## Running the API

pip install -r requirements.txt

python -m uvicorn app:app --reload

## Documentation

Open:

http://127.0.0.1:8000/docs

## Monitoring

See monitoring_plan.md

## Responsible Use

See responsible_use.md