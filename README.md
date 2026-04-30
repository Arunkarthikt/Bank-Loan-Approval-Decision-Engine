# Loan Approval Prediction System

## Project Overview
This project builds a Machine Learning model to predict whether a loan application will be Approved or Rejected based on applicant details such as income, loan amount, CIBIL score, and assets.

The objective is to assist financial institutions in making faster and more accurate loan decisions.

---

## Dataset Information
The dataset contains 42269 records with the following features:

- no_of_dependents
- education
- self_employed
- income_annum
- loan_amount
- loan_term
- cibil_score
- residential_assets_value
- loan_status (Target Variable)

---

## Data Preprocessing

- Removed unnecessary column (loan_id)
- Cleaned column names
- No missing values found
- No duplicate values found
- Outlier handling using IQR method
- Label Encoding applied
- Dropped features:
  - education
  - no_of_dependents

---

## Exploratory Data Analysis

- Distribution plots
- Boxplots for outliers
- Countplot for class balance
- Scatter plot (income vs loan amount)
- Correlation heatmap

---

## Feature Selection

Used SelectKBest (ANOVA F-test)

Selected Features:
- income_annum
- loan_amount
- loan_term
- cibil_score
- residential

---

## Handling Imbalanced Data

Used SMOTE to balance dataset

---

## Models Used

- Decision Tree
- Random Forest
- Logistic Regression

---

## Model Performance

### Decision Tree

Confusion Matrix:
[[500 36]
 [  1 317]]

Classification Report:
precision    recall  f1-score   support

0       1.00      0.93      0.96       536
1       0.90      1.00      0.94       318

accuracy                           0.96
macro avg       0.95      0.96      0.95
weighted avg    0.96      0.96      0.96

---

### Random Forest

Confusion Matrix:
[[505 31]
 [  6 312]]

Classification Report:
precision    recall  f1-score   support

0       0.99      0.94      0.96       536
1       0.91      0.98      0.94       318

accuracy                           0.96
macro avg       0.95      0.96      0.95
weighted avg    0.96      0.96      0.96

---

### Logistic Regression

Confusion Matrix:
[[451 85]
 [103 215]]

Classification Report:
precision    recall  f1-score   support

0       0.81      0.84      0.83       536
1       0.72      0.68      0.70       318

accuracy                           0.78
macro avg       0.77      0.76      0.76
weighted avg    0.78      0.78      0.78

---

## Best Model

Decision Tree and Random Forest achieved highest accuracy (96%)

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Imbalanced-learn

---

## Streamlit App

Run the app using:

pip install streamlit  
streamlit run app.py

---

## Project Structure

loan-approval-prediction/
│
├── data/
├── notebooks/
├── app.py
├── model.pkl
├── README.md
└── requirements.txt

---

## Author

Arun Sundar
