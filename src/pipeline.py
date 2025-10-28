
"""src/pipeline.py
Reproducible pipeline script for AIIS-WH2.
Assumes dataset placed at --input or data/vehicle_data.csv
"""
import argparse
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm
import matplotlib.pyplot as plt

def load_data(path):
    df = pd.read_csv(path)
    print('Loaded', df.shape)
    return df

def preprocess(df):
    # basic cleaning: drop duplicates and NA
    df = df.copy()
    df = df.drop_duplicates()
    df = df.dropna()
    # example: convert categorical to dummies
    cat_cols = df.select_dtypes(include=['object']).columns.tolist()
    df = pd.get_dummies(df, columns=cat_cols, drop_first=True)
    return df

def feature_selection(X, y, n_features=5):
    lr = LinearRegression()
    selector = RFE(lr, n_features_to_select=n_features)
    selector = selector.fit(X, y)
    support = selector.support_
    return X.columns[support].tolist()

def train_lr(X_train, y_train):
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    return lr

def evaluate(model, X_test, y_test):
    pred = model.predict(X_test)
    mse = mean_squared_error(y_test, pred)
    r2 = r2_score(y_test, pred)
    print('MSE', mse, 'R2', r2)
    return pred, mse, r2

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='data/vehicle_data.csv')
    args = parser.parse_args()
    df = load_data(args.input)
    df = preprocess(df)
    if 'selling_price' in df.columns:
        y = df['selling_price']
        X = df.drop(columns=['selling_price'])
    else:
        raise SystemExit('Please ensure file has selling_price column.')
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    feat = feature_selection(X_train, y_train, n_features=min(8, X_train.shape[1]))
    print('Selected features:', feat)
    model = train_lr(X_train[feat], y_train)
    pred, mse, r2 = evaluate(model, X_test[feat], y_test)
    # save a simple plot
    plt.scatter(y_test, pred, alpha=0.4)
    plt.xlabel('Actual')
    plt.ylabel('Predicted')
    plt.title('Actual vs Predicted')
    plt.savefig('reports/actual_vs_predicted.png', dpi=150)
    print('Saved reports/actual_vs_predicted.png')
if __name__=='__main__':
    main()
