# Data Card
The DATA_CARD file describes the dataset used in the project.

#### **Structure for DATA_CARD.md**
```markdown
# DATA CARD: Credit Card Dataset

## Overview
The dataset contains records of 30,000 credit card clients, including demographic, financial, and payment history information. It was used to train a machine learning model to predict defaults.

## Dataset Details
- Source: Publicly available dataset for credit default prediction.
- Size: 30,000 rows, 25 columns.
- Target Variable: `default payment next month` (0 = No, 1 = Yes).

## Features
1. Demographics: 
   - `SEX`, `AGE`, `EDUCATION`, `MARRIAGE`.
2. Financial Information:
   - `LIMIT_BAL`, `BILL_AMT1-6`, `PAY_AMT1-6`.
3. Payment History:
   - `PAY_0`, `PAY_2-6`.

## Preprocessing
1. Encoding: Categorical features (`SEX`, `EDUCATION`, `MARRIAGE`) were label-encoded.
2. Scaling: Numerical features were scaled using MinMaxScaler.
3. Class Balance: SMOTE was used to balance the `default payment next month` classes.

## License
This dataset is licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) license.
