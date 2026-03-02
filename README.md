# 🚀 Swiggy Delivery Time Prediction

## 📌 Overview
This project predicts the **delivery time of food orders** based on factors like rider details, traffic, distance, and order conditions.  
It helps improve delivery efficiency and customer satisfaction.

---

## 🎯 Objective
- Predict delivery time (in minutes)
- Identify key factors affecting delivery performance
- Build a machine learning model for real-time prediction

---

## 📂 Dataset Features
- Rider: `age`, `ratings`, `vehicle_condition`
- Order: `multiple_deliveries`, `order_time_hour`, `order_time_of_day`
- External: `traffic`, `weather`, `festival`
- Location: `distance`, `city_type`

---

## ⚙️ Tech Stack
- Python  
- Pandas, NumPy  
- Scikit-learn  
- XGBoost  
- Matplotlib, Seaborn  
- Streamlit  

---

## 🔄 Workflow (CRISP-ML(Q))
1. Business Understanding  
2. Data Preparation  
3. Feature Selection  
4. Model Building  
5. Model Evaluation  
6. Deployment  

---

## 🧹 Data Preprocessing
- Handled missing values:
  - Mean → age, ratings  
  - Mode → categorical features  
  - Median → multiple deliveries  
- Created time-based features  
- Removed inconsistent data  

---

## 🔠 Encoding
- One-Hot Encoding for categorical features  
- Ordinal Encoding for traffic  
- Converted all data into numeric format  

---

## 📏 Feature Scaling
- Applied **StandardScaler**
- Ensured all features are on same scale
- Prevented model bias

---

## 🎯 Feature Selection
Techniques used:
- Correlation Analysis  
- SelectKBest  
- Mutual Information  
---

## 📊 Model Evaluation
- Training R²: ~0.78  
- Testing R²: ~0.72  
- Indicates good generalization  

---

## 🔁 Cross Validation
- Used K-Fold (5 splits)  
- Mean R² Score: ~0.72  
- Ensures model stability  

---

## ⚡ Hyperparameter Tuning
Methods used:
- Grid Search  
- Random Search  
- Optuna  
---

## 🏆 Final Model
- XGBoost Regressor  
- Best R² Score: ~0.72  
- Selected for deployment  
---

## 🌐 Deployment
- Built using Streamlit  
- Takes user inputs  
- Predicts delivery time instantly  

---
