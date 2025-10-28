
# streamlit_app/streamlit_app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.linear_model import LinearRegression

st.title('Car Price Predictor — AIIS-WH2')
st.markdown('Upload the CarDekho CSV or provide path `data/vehicle_data.csv`.')

uploaded = st.file_uploader('Upload CSV', type=['csv'])
if uploaded is not None:
    df = pd.read_csv(uploaded)
else:
    st.info('No file uploaded — app expects data/vehicle_data.csv in repo when deployed on Replit.')
    try:
        df = pd.read_csv('data/vehicle_data.csv')
    except Exception as e:
        st.stop()

st.write(df.head())

# Simple UI to choose features and predict median price for an example
if st.button('Run simple pipeline'):
    df = df.dropna().drop_duplicates()
    if 'selling_price' not in df.columns:
        st.error('CSV must contain "selling_price" column.')
    else:
        y = df['selling_price']
        X = pd.get_dummies(df.drop(columns=['selling_price']), drop_first=True)
        model = LinearRegression().fit(X, y)
        st.success('Trained LinearRegression on full data.')
        st.write('R2 (train):', model.score(X, y))
        st.write('Example prediction (first row):', float(model.predict(X.iloc[[0]])))
