# Loan Approval Prediction – End-to-End Machine Learning Project

## 📌 Project Overview

This project implements a complete supervised Machine Learning pipeline to predict whether a loan application will be **Approved or Rejected** based on applicant demographic, financial, and credit-related information.

The objective is to build, evaluate, and compare multiple classification models and select the best-performing model for final use.

---

## 🎯 Problem Statement

Given structured applicant data, predict:

- **Loan Status (Approved / Rejected)**
- Probability-based confidence of approval

This is a binary classification problem.

---

## 📂 Dataset Description

The dataset contains structured tabular data with the following features:

### Personal Information
- Gender
- Married
- Dependents
- Education
- Self_Employed

### Financial Information
- ApplicantIncome
- CoapplicantIncome
- LoanAmount
- Loan_Amount_Term

### Credit & Property Information
- Credit_History
- Property_Area

### Target Variable
- Loan_Status (1 = Approved, 0 = Rejected)

---

## 🔧 Data Preprocessing

The following preprocessing steps were performed:

- Handling missing values  
  - Categorical features filled using mode  
  - Numerical features filled using median  
- Converting categorical variables into numeric form  
- Correcting inconsistent values (e.g., "3+" dependents mapped to 3)  
- Removing unnecessary columns (Loan_ID)  
- Train–Validation split (80% / 20%, random_state=42)

---

## 📊 Feature Engineering

Additional meaningful features were created:

- **Total_Income** = ApplicantIncome + CoapplicantIncome  
- **Loan_to_Income_Ratio** = LoanAmount / Total_Income  
- **EMI_to_Income_Ratio** = LoanAmount / Loan_Amount_Term  

These engineered features help improve predictive performance by capturing financial burden and repayment capacity.

---

## 🔍 Feature Importance Analysis

Mutual Information was used to evaluate feature relevance and understand which variables contribute most to loan approval prediction.

Credit_History showed strong predictive influence.

---

## 🤖 Machine Learning Models Implemented

The following classification models were trained and compared:

- Logistic Regression  
- Support Vector Machine (SVM)  
- Random Forest Classifier  

Random Forest was selected as the final model due to its balanced performance and robustness to outliers.

---

## 📈 Evaluation Metrics

Models were evaluated using:

- Accuracy  
- Precision  
- Recall  
- F1 Score  
- ROC-AUC  

These metrics ensure both predictive accuracy and proper class discrimination.

---
---

## 📊 Model Performance Summary

Models were evaluated on the validation set using Accuracy, Precision, Recall, F1-Score, and ROC-AUC (80/20 split, random_state=42).

| Model                  | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|------------------------|----------|-----------|--------|----------|---------|
| Logistic Regression    | 0.85     | 0.83      | 0.99   | 0.90     | 0.83    |
| Support Vector Machine | 0.85     | 0.83      | 0.99   | 0.90     | 0.84    |
| Random Forest          | 0.87     | 0.88      | 0.94   | 0.91     | 0.85    |

### Final Model Selection

Random Forest was selected as the final model as it achieved the highest overall accuracy (87%) and maintained a strong balance between precision and recall with the best ROC-AUC score.

## 📤 Output

The project generates:

- Model performance metrics  
- Prediction results saved as `submission.csv`

---

## 🛠 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
