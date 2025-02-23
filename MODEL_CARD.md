# MODEL CARD: Random Forest Model

## Overview
This Random Forest model predicts credit card defaults based on client demographics, financial information, and payment history. It is interpretable using LIME and robust to small input noise.

## Performance Metrics
- Accuracy: 81.3% (Original Data)
- F1-Score: 0.67
- ROC-AUC: 0.83
- Robustness: 80.1% accuracy under noisy data.

## Training Details
- Model: Random Forest Classifier
- Hyperparameters:
  - `n_estimators`: 100
  - `max_depth`: None
  - `class_weight`: Balanced
- Data Split: 80% training, 20% testing.

## Explainability
- Tool Used: LIME
- Key Features:
  - `BILL_AMT5`
  - `LIMIT_BAL`
  - `PAY_0`

## Ethical Analysis
- Slight bias observed in default rates based on `SEX`:
  - Male default rate: ~23.36%
  - Female default rate: ~21.29%

## Limitations
1. Slight bias in predictions based on `SEX`.
2. Performance may degrade significantly with larger noise levels.

## Future Improvements
1. Address potential bias using fairness-aware techniques.
2. Explore other ensemble methods for improved performance.
