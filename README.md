# Credit Card Default Prediction

## Purpose
This project predicts credit card defaults using machine learning to assist financial institutions in managing risk and minimizing losses. A Random Forest model was developed and trained on a dataset of 30,000 credit card clients. LIME was used to explain individual predictions and analyze feature importance. Robustness testing ensured the model's reliability under noisy conditions, and an ethical bias analysis evaluated fairness in predictions with respect to the SEX feature.

## Usage Instructions
1. Clone the Project
Clone this repository to your local system:

git clone https://github.com/Darshan-Deepak/Credi-Card-Default-Prediction.git

2. Install Dependencies

cd credit-default-prediction
pip install -r requirements.txt

3. Run the Project
Open and run the Jupyter notebook to view the full analysis:

jupyter notebook finalproject.ipynb

## Known Issues

The model shows slight bias in predictions based on the SEX feature:

Male Default Rate: ~23.36%

Female Default Rate: ~21.29%

Model performance may degrade under high levels of noise in the input data.

## Feature Roadmap
Future improvements planned for this project include:

1. Fairness Mitigation: Use fairness-aware algorithms to address potential bias in predictions.

2. Advanced Explainability: Integrate tools like SHAP for global feature explanations.

3. Model Export: Save the model in ONNX format for broader compatibility.

4. Improved Robustness: Implement adversarial training to enhance performance under noisy or adversarial conditions.

## Requirements
Prerequisites:
- Python 3.8 or above
- Libraries: pandas, numpy, scikit-learn, matplotlib, lime

## License

This dataset is licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) license.

## Contact
For questions or collaborations, 

Please contact:
Darshan Deepak

Email: dda58@scarletmail.rutgers.edu

