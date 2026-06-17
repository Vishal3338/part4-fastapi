# Error Analysis

## False Positives

False positives occur when the model predicts churn but the customer actually remains active.

Business Risk:

* Unnecessary retention offers
* Increased marketing cost
* Discount leakage

## False Negatives

False negatives occur when the model predicts non-churn but the customer actually churns.

Business Risk:

* Customer loss
* Revenue loss
* Reduced customer lifetime value

## Observations

The confusion matrix shows that the model correctly identified 125 churned customers and 185 retained customers.

The model missed 96 churn cases, indicating opportunities for improved recall through additional features and tuning.

## Improvement Opportunities

* Add web activity features
* Add support ticket history
* Add campaign engagement signals
* Perform hyperparameter tuning
