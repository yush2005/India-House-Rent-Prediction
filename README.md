
# 🏠 India House Rent Prediction & Recommendation System

## 📌 Project Overview

This project is an **end-to-end Machine Learning application** that predicts house rental prices and recommends suitable houses based on user budget and preferences.

The system combines:

* 📊 ML-based rent prediction (Regression)
* 🧠 Budget-aware recommendation logic
* 🌐 Interactive Streamlit web application
* 🐳 Docker containerization for deployment

---

## 🚀 Features

### 🔹 Rent Prediction

* Predicts monthly house rent based on:

  * City
  * Locality
  * Area (sqft)
  * Bedrooms & Bathrooms
  * Furnishing Type
  * Area Rate

### 🔹 Budget-Based Recommendation System

* Recommends houses under user budget
* Filters by:

  * City & locality
  * Bedrooms
  * Minimum area
  * Furnishing type
* Ranks houses based on predicted rent

---

## 🧠 Machine Learning Pipeline

The project uses a **production-style ML pipeline**:

```
Input Data
     ↓
ColumnTransformer
 (Scaling + Encoding)
     ↓
Random Forest Regressor
     ↓
Rent Prediction
```

### Preprocessing

* StandardScaler for numerical features
* OneHotEncoder for categorical features

### Model

* RandomForestRegressor

---

## 📊 Dataset

The dataset contains Indian house rental listings with features such as:

* House type
* City & locality
* Area
* Beds, bathrooms, balconies
* Furnishing
* Area rate
* Rent (target)

---

## ⚙️ Project Workflow

```
Data Collection
      ↓
Data Cleaning & Outlier Handling
      ↓
Exploratory Data Analysis (EDA)
      ↓
Feature Engineering (BHK extraction)
      ↓
Model Training & Evaluation
      ↓
Streamlit Deployment
      ↓
Recommendation System
```

---

## 📈 Model Evaluation Metrics

* MAE (Mean Absolute Error)
* RMSE (Root Mean Squared Error)
* R² Score

These metrics were used to evaluate prediction performance.

---

## 🏗️ Tech Stack

* Python
* Scikit-learn
* Pandas & NumPy
* Matplotlib / Seaborn
* Streamlit
* Docker
* Git & GitHub

---

## 🖥️ Run Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/India-House-Rent-Prediction.git
cd India-House-Rent-Prediction
```

---

### 2️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run Streamlit App

```bash
streamlit run app.py
```

Open:

```
http://localhost:8501
```

---

## 🐳 Run Using Docker

### Build Image

```bash
docker build -t house-rent-app .
```

### Run Container

```bash
docker run -p 8501:8501 house-rent-app
```

---

## 📂 Project Structure

```
India-House-Rent-Prediction/
│
├── data/
│   └── data.csv
├── notebooks/
├── app.py
├── house_rent_model.pkl
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🎯 Future Improvements

* Map-based location visualization
* Similarity-based recommendations
* Model optimization & tuning
* Cloud deployment (AWS / Render)

---
