# 💓 Predicting Heart Disease Using Machine Learning (Logistic Regression + Streamlit App)
### 🗓️ Project Date: July 2025
### ✍️ Author: Sanjesh Chourasia
### 🏷️ Tags: #MachineLearning, #LogisticRegression, #HealthcareAI, #Streamlit, #Python, #DataScience

## 🧠 Introduction
Heart disease is one of the leading causes of death worldwide. Early prediction can help save lives through preventive care and early intervention. In this project, I’ve built a machine learning model that can predict the presence of heart disease using logistic regression — a simple yet powerful classification algorithm.
To make it even more accessible, I deployed the model using Streamlit, so anyone can try it through a friendly web interface!

## 📊 Dataset
I used the popular Heart Disease UCI dataset from Kaggle.
 This dataset contains medical attributes of patients, such as:
- Age
- Sex
- Chest pain type
- Blood pressure
- Cholesterol
- Max heart rate
- ST depression
- Thalassemia
and more…

Our target variable is target, where:
1 = patient has heart disease, 0 = patient does not have heart disease



## 🧪 Model Selection: Logistic Regression
Since our target is binary (Yes/No), I used Logistic Regression for this classification task.
Why Logistic Regression?
- Simple and interpretable
- Works well with linear decision boundaries
- Outputs probability of heart disease (great for threshold tuning)



## 🔧 Steps Followed
### - ✅ Data Preprocessing
- Handled missing values (if any)
- Standardized the features using StandardScaler
- Split the data into training (80%) and test (20%) sets


### - ✅ Model Training
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)

### - ✅ Evaluation Metrics
- Accuracy


- Precision

- Recall


- F1 Score


- ROC Curve & AUC Score

I achieved an accuracy of ~85%, with strong recall and precision — meaning the model can detect heart disease cases reliably.

### 🖥️ Deployment Using Streamlit
I used Streamlit to build a user interface that lets anyone enter patient details and get an instant prediction.
- 🌐 Live App:
- 👉 https://heart-disease-app-7jvekyhu9fb5ckfmqyyepa.streamlit.app/
- 📂 GitHub Repo: https://github.com/Sanjesh12/heart-disease-app
- Colab Notebook: [Colab notebook - Copy of Logistic Regression Notes](https://colab.research.google.com/drive/1gjM3BiKjFyeTvUohLPgigzn7I55NY6tk#scrollTo=iJZhaASsDEFf)

### 📌 Key Learnings
- ✅ Logistic regression is excellent for binary classification problems
-  ✅ Scaling input features helps improve model performance
-  ✅ Evaluation metrics like recall are crucial in healthcare — false negatives can be deadly
-  ✅ Streamlit makes deploying ML models simple and fast!


🙏 Thank You!

Links - 

Colab notebook - https://colab.research.google.com/drive/1gjM3BiKjFyeTvUohLPgigzn7I55NY6tk#scrollTo=iJZhaASsDEFf

GuitHub - https://github.com/Sanjesh12/heart-disease-app

Streamlit - https://heart-disease-app-7jvekyhu9fb5ckfmqyyepa.streamlit.app/
