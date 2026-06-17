# Model Card

## Model Name

Customer Churn Prediction Model

## Model Type

Random Forest Classifier

## Intended Use

Predict customers likely to churn within the next 60 days.

## Features Used

* Total Orders
* Total Spend
* Average Rating

## Training Data

Customer profile data combined with historical order behavior and churn labels.

## Performance

* Accuracy: 64.58%
* Precision: 62.81%
* Recall: 56.56%
* F1 Score: 59.52%
* ROC AUC: 0.7023

## Limitations

* Limited feature set
* No campaign engagement signals
* No web activity features
* No support interaction features

## Ethical Considerations

Predictions should support customer retention efforts and should not be used for discriminatory decision making.

## Monitoring

Monitor:

* Prediction distribution
* Data drift
* Churn rate changes
* Model performance degradation
