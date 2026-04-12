#!/usr/bin/env python
# coding: utf-8

# In[12]:


import streamlit as st
import numpy as np
import joblib


# In[19]:


model = joblib.load("wine_model.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config(page_title="Wine Classifier", layout="centered")

st.title(" Wine Classification App 🍷")
st.write("Predict the type of wine based on its chemical properties")


# In[20]:


feature_names = [
    "Alcohol", "Malic Acid", "Ash", "Alcalinity of Ash",
    "Magnesium", "Total Phenols", "Flavanoids",
    "Nonflavanoid Phenols", "Proanthocyanins",
    "Color Intensity", "Hue", "OD280/OD315", "Proline"
]


# ## Sample Data

# In[21]:


if "features" not in st.session_state:
    st.session_state.features = [0.0] * 13

if st.button("✨ Use Sample Data"):
    st.session_state.features = [
        13.2, 2.7, 2.5, 15.0, 100, 2.5, 2.0,
        0.3, 1.5, 5.0, 1.0, 3.0, 1000
    ]


# In[22]:


features = []
st.subheader("Enter Feature Values")

for i, name in enumerate(feature_names):
    val = st.slider(
        name,
        min_value=0.0,
        max_value=20.0 if i != 4 and i != 12 else 2000.0,
        value=float(st.session_state.features[i])
    )
    features.append(val)


# In[23]:


if st.button("🔍 Predict"):
    data = np.array(features).reshape(1, -1)
    data = scaler.transform(data)

    prediction = model.predict(data)

    class_names = {
        0: "🍇 Class 0 (Type A Wine)",
        1: "🍷 Class 1 (Type B Wine)",
        2: "🥂 Class 2 (Type C Wine)"
    }

    st.success(f"Prediction: {class_names[prediction[0]]}")


# In[ ]:


st.markdown("---")
st.caption("Built with Streamlit | ML Wine Classifier")


# In[ ]:




