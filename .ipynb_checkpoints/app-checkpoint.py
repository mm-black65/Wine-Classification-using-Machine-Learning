#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import numpy as np
import joblib


# In[2]:


model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

st.title(" Wine Classification App 🍷")

st.write("Enter wine chemical properties to predict class")


# In[3]:


features = []

feature_names = [
    "Alcohol", "Malic Acid", "Ash", "Alcalinity of Ash",
    "Magnesium", "Total Phenols", "Flavanoids",
    "Nonflavanoid Phenols", "Proanthocyanins",
    "Color Intensity", "Hue", "OD280/OD315", "Proline"
]

for name in feature_names:
    val = st.number_input(f"{name}", value=0.0)
    features.append(val)


# In[4]:


if st.button("Predict"):
    data = np.array(features).reshape(1, -1)
    data = scaler.transform(data)

    prediction = model.predict(data)

    st.success(f"Predicted Wine Class: {prediction[0]}")


# In[ ]:




