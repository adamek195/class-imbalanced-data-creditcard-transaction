# class-imbalanced-data-creditcard-transaction

The research was made for the studies of Computer Engineering with a specialization in Computer Graphics and Multimedia Systems at the Wrocław University of Science and Technology. The goal of the research was to create a predictive model for classifying credit card transactions as fraud or a regular transaction. Class-imbalanced data was used to create the model.

## Creditcard dataset

Data is CSV file with anonymized credit card transactions labeled as fraudulent or genuine.
The datasets contains transactions made by credit cards in September 2013 by european cardholders. This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions. It contains only numerical input variables which are the result of a PCA transformation.
Due to confidentiality issues, the authors do not provide the original features and more background information about the data. Features V1, V2, ... V28 are the principal components obtained with PCA. The only features which have not been transformed with PCA are 'Time' and 'Amount'. Feature 'Time' contains the seconds elapsed between each transaction and the first transaction in the dataset. The feature 'Amount' is the transaction Amount. Feature 'Class' is the response variable and it takes value 1 in case of fraud and 0 otherwise. The dataset has been collected and analysed during a research collaboration of Worldline and the Machine Learning Group  of ULB (University Libre de Bruxelles).

Columns:

- Time Number of seconds elapsed between this transaction and the first transaction in the dataset
- V1 may be result of a PCA Dimensionality reduction to protect user identities and sensitive features (v1-v28)
- V2
- V3
- V4
- V5
- V6
- V7
- V8
- V9
- V10
- V11
- V12
- V13
- V14
- V15
- V16
- V17
- V18
- V19
- V20
- V21
- V22
- V23
- V24
- V25
- V26
- V27
- V28 abc
- Amount Transaction amount
- Class 1 for fraudulent transactions, 0 otherwise

## Research

### 1. Different  Algorithms

|     Algorithm     |  accuracy  |  sensitivity(TPR) |  specificity(TNR)  |
|-------------------|------------|-------------------|--------------------|
|   Decision Tree   |   99.92%   |       75.93%      |       99.96%       |
|   Random Forest   |   99.95%   |       77.16%      |       99.99%       |
|       MLP         |   99.75%   |       78.40%      |       99.79%       |
|       SVM         |   99.90%   |       51.85%      |       99.99%       |
|Logistic regression|   99.91%   |       60.49%      |       99.98%       |
|       KNN         |   99.83%   |       4.32%       |       99,99%       |
|   Naive Bayes     |   99.29%   |       62.96%      |       99.35%       |

### 2. Feature Selection

#### 2.1. RFECV

|     Algorithm     |  accuracy  |  sensitivity(TPR) |  specificity(TNR)  |
|-------------------|------------|-------------------|--------------------|
|   Decision Tree   |   99.92%   |       75.93%      |       99.96%       |
|   Random Forest   |   99.95%   |       77.16%      |       99.99%       |
|       MLP         |   99.75%   |       77.16%      |       99.79%       |

#### 2.2. Forward Logistic Regression

|     Algorithm     |  accuracy  |  sensitivity(TPR) |  specificity(TNR)  |
|-------------------|------------|-------------------|--------------------|
|   Decision Tree   |   99.91%   |       70.99%      |       99.96%       |
|   Random Forest   |   99.96%   |       78.40%      |       99.99%       |
|       MLP         |   99.93%   |       60.49%      |       99.99%       |

#### 2.3. PCA

|     Algorithm     |  accuracy  |  sensitivity(TPR) |  specificity(TNR)  |
|-------------------|------------|-------------------|--------------------|
|   Decision Tree   |   99.91%   |       69.14%      |       99.96%       |
|   Random Forest   |   99.95%   |       77.78%      |       99.99%       |
|       MLP         |   99.88%   |       45.06%      |       99.98%       |

### 3. Class-imbalanced problem

#### 3.1 Under Sampling

|     Algorithm     |  accuracy  |  sensitivity(TPR) |  specificity(TNR)  |
|-------------------|------------|-------------------|--------------------|
|   Decision Tree   |   90.79%   |       89.51%      |       90.79%       |
|   Random Forest   |   97.96%   |       89.51%      |       97.98%       |
|       MLP         |    1.04%   |       99.99%      |        0.86%       |

#### 3.2 Over Sampling

|     Algorithm     |  accuracy  |  sensitivity(TPR) |  specificity(TNR)  |
|-------------------|------------|-------------------|--------------------|
|   Decision Tree   |   99.92%   |       75.31%      |       99.97%       |
|   Random Forest   |   99.95%   |       78.40%      |       99.99%       |
|       MLP         |   97.25%   |       90.74%      |       97.26%       |

#### 3.3 Smote

|     Algorithm     |  accuracy  |  sensitivity(TPR) |  specificity(TNR)  |
|-------------------|------------|-------------------|--------------------|
|   Decision Tree   |   99.77%   |       76.54%      |       99.81%       |
|   Random Forest   |   99.95%   |       82.10%      |       99.98%       |
|       MLP         |   99.75%   |       85.19%      |       99.78%       |

#### 3.4 Cluster Centroids

|     Algorithm     |  accuracy  |  sensitivity(TPR) |  specificity(TNR)  |
|-------------------|------------|-------------------|--------------------|
|   Decision Tree   |   26.09%   |       98.15%      |       25.97%       |
|   Random Forest   |    6.25%   |       99.38%      |        6.09%       |
|       MLP         |   99.70%   |       20.99%      |       99.84%       |

#### 3.5 SMOTETomek

|     Algorithm     |  accuracy  |  sensitivity(TPR) |  specificity(TNR)  |
|-------------------|------------|-------------------|--------------------|
|   Decision Tree   |   99.79%   |       75.31%      |       99.84%       |
|   Random Forest   |   99.95%   |       82.72%      |       99.98%       |
|       MLP         |   99.33%   |       86.42%      |       99.35%       |
