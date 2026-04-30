Loan Approval Prediction System
Project Overview

This project builds a Machine Learning model to predict whether a loan application will be Approved or Rejected based on applicant details such as income, loan amount, CIBIL score, and assets.

The objective is to assist financial institutions in making faster and more accurate loan decisions.

Dataset Information

The dataset contains 42269 records with the following features:

no_of_dependents
education
self_employed
income_annum
loan_amount
loan_term
cibil_score
residential_assets_value
loan_status (Target Variable)
Data Preprocessing
Removed unnecessary column (loan_id)
Cleaned column names
Verified no missing values and duplicates
Handled outliers using IQR method
Applied Label Encoding for categorical variables
Dropped less relevant features:
education
no_of_dependents
Exploratory Data Analysis
Distribution plots for numerical features
Boxplots for outlier detection
Countplot for class distribution
Scatter plot for income vs loan amount
Correlation heatmap
Feature Selection

Used SelectKBest (ANOVA F-test) to identify important features.

Selected features:

income_annum
loan_amount
loan_term
cibil_score
residential
Handling Imbalanced Data

Used SMOTE to balance the dataset before training.

Models Used
Decision Tree Classifier
Random Forest Classifier
Logistic Regression
Model Performance

Decision Tree:

Accuracy: 96 percent

Random Forest:

Accuracy: 96 percent

Logistic Regression:

Accuracy: 78 percent

Best performing models are Decision Tree and Random Forest.

Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Imbalanced-learn
