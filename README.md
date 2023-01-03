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

|  Algorithm    |  sensitivity(TPR) |  specificity(TNR)  |
|---------------|-------------------|--------------------|
| Decision Tree |        79,98%     |       99,9%        |
| Random Forest |        82,17%     |       99,9%        |
|     MLP       |        84,08%     |       99,6%        |
|     SVM       |          0%       |       99,99%       |
