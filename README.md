# 🍷 Wine Classification using Machine Learning

A machine learning project focused on classifying wine types based on their chemical properties. This project compares multiple classification algorithms, with special emphasis on Support Vector Machine (SVM), to identify the most effective model for wine prediction.

An interactive **Streamlit web app** is also included for real-time predictions.

---

## 📌 Project Overview

The goal of this project is to build a robust wine classification system using physicochemical features from the built-in wine dataset in Scikit-learn.

Multiple machine learning algorithms are trained, evaluated, and compared using cross-validation. The best-performing model is then optimized and deployed through a Streamlit-based interface.

---

## 🎯 Objectives

- Compare multiple machine learning algorithms  
- Identify the best-performing classifier  
- Optimize SVM using hyperparameter tuning  
- Evaluate models using classification metrics  
- Build an interactive prediction system  

---

## 📊 Dataset

- **Source:** Built-in wine dataset from Scikit-learn  
- **Features:** 13 chemical properties of wine  
- **Target:** 3 wine classes  

---

## ⚙️ Methodology

1. Load and preprocess the dataset  
2. Scale features using `StandardScaler`  
3. Train multiple classification models  
4. Compare models using cross-validation  
5. Tune SVM using `GridSearchCV`  
6. Evaluate the final model using:
   - Confusion Matrix  
   - Classification Report  
7. Deploy the model using Streamlit  

---

## 🤖 Models Used

- Logistic Regression  
- K-Nearest Neighbors (KNN)  
- Decision Tree  
- Naive Bayes  
- Linear Discriminant Analysis (LDA)  
- Support Vector Machine (SVM)  

---

## 🚀 Key Features

- Multi-model comparison using cross-validation  
- SVM optimization with hyperparameter tuning  
- Feature scaling for improved performance  
- Interactive Streamlit app for live predictions  
- Clean and practical ML workflow  

---

## 📈 Results

- Several models were evaluated and compared  
- SVM performed strongly after tuning  
- The final model provides reliable predictions  
- Streamlit app allows real-time user interaction  

---

## ⚠️ Challenges Faced

- Selecting the most suitable model  
- Understanding the impact of feature scaling  
- Tuning SVM hyperparameters effectively  
- Avoiding overfitting  
- Interpreting cross-validation results  

---

## 🔮 Future Scope

- Implement advanced models (Random Forest, Gradient Boosting)  
- Improve Streamlit UI/UX  
- Deploy the app on cloud platforms (AWS, Heroku, etc.)  
- Add feature importance visualizations  
- Test on larger real-world datasets  

---

## 🛠️ Technologies Used

- Python  
- Jupyter Notebook  
- Streamlit  
- Scikit-learn  
- NumPy  
- Pandas  
- Matplotlib  
- Seaborn  
- Joblib  

---

## ▶️ How to Run

```bash
git clone <your-repo-link>
cd <your-folder>
pip install -r requirements.txt
jupyter notebook
streamlit run app.py
```

---

## 📚 What I Learned
 - Model comparison and evaluation techniques
- Importance of feature scaling
- SVM for classification tasks
- Hyperparameter tuning using GridSearchCV
- Deploying ML models using Streamlit

---

## ✅ Conclusion

This project demonstrates a complete machine learning workflow for classification tasks — from preprocessing and model comparison to optimization and deployment.

The focus on SVM tuning and Streamlit deployment makes it both technically strong and presentation-ready.
