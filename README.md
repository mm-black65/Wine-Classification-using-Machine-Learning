# 🍷 Wine Classification using Machine Learning (SVM Focus)

## 📌 Overview

This project presents a comparative analysis of multiple machine learning algorithms to classify wine types based on their chemical properties. The primary focus is on optimizing and evaluating the performance of Support Vector Machine (SVM) alongside other classification models.

An interactive web application is also developed using Streamlit to allow users to input wine characteristics and receive real-time predictions.

---

## 📄 Project Description

The goal of this project is to build a robust classification system that can accurately predict the type of wine using its physicochemical features. The dataset is obtained from the built-in wine dataset available in Scikit-learn.

Multiple machine learning algorithms including Logistic Regression, K-Nearest Neighbors, Decision Tree, Naive Bayes, Linear Discriminant Analysis, and Support Vector Machine are implemented and compared using cross-validation.

Special emphasis is given to SVM, where hyperparameter tuning is applied to improve performance. The best-performing model is then selected and deployed using a Streamlit-based web interface.

This project demonstrates a complete machine learning workflow including preprocessing, model comparison, optimization, evaluation, and deployment.

---

## 🎯 Objectives

* Compare multiple machine learning algorithms
* Identify the best-performing model
* Optimize SVM using hyperparameter tuning
* Evaluate models using classification metrics
* Build an interactive prediction system

---

## 📊 Dataset

* Source: Built-in dataset from Scikit-learn
* Features: 13 chemical properties of wine
* Target: 3 wine classes

---

## 🧠 Methodology

1. Data loading and preprocessing
2. Feature scaling using StandardScaler
3. Model training using multiple algorithms
4. Cross-validation for performance comparison
5. Selection of best model based on accuracy
6. Hyperparameter tuning of SVM using GridSearchCV
7. Model evaluation using confusion matrix and classification report
8. Deployment using Streamlit

---

## 🔍 Key Features

* Multi-model comparison using cross-validation
* Implementation of SVM with parameter tuning
* Use of StandardScaler for improved model performance
* Visualization of model performance
* Interactive Streamlit application for predictions

---

## 📈 Results

* Multiple models were evaluated and compared
* SVM achieved competitive performance after tuning
* The best model was selected based on cross-validation accuracy
* The final model provides reliable predictions for wine classification

---

## 🚧 Challenges Faced

* Model selection complexity
* Hyperparameter tuning
* Scaling requirement for SVM
* Overfitting during evaluation
* Understanding cross-validation

---

## 🔮 Future Scope

* Use advanced models like Random Forest and Gradient Boosting
* Improve UI/UX of the Streamlit app
* Deploy application on cloud platforms
* Use real-world datasets for better generalization
* Add feature importance visualization

---

## 🛠️ Technologies Used

* Python
* Jupyter Notebook
* Streamlit
* Scikit-learn
* NumPy & Pandas
* Matplotlib & Seaborn
* Joblib

---

## ▶️ How to Run

### 1. Clone Repository

```
git clone <your-repo-link>
cd <your-folder>
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Run Notebook

```
jupyter notebook
```

### 4. Run Streamlit App

```
streamlit run app.py
```

---

## 📸 App Preview

* The Streamlit app allows users to input wine features
* Provides real-time classification results
* Displays predicted wine class

---

## 📚 What I Learned

* Model comparison and evaluation techniques
* Importance of feature scaling
* Working of Support Vector Machines
* Hyperparameter tuning using GridSearchCV
* Deploying ML models using Streamlit

---

## 📌 Conclusion

This project successfully demonstrates the implementation and comparison of multiple machine learning models for classification tasks. The integration of SVM optimization and deployment through Streamlit highlights practical applications of machine learning in real-world scenarios.

---
