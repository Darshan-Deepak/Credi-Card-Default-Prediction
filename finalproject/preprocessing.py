import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

def encode_categorical(data, categorical_columns):
    """
    Encode categorical columns using LabelEncoder.
    """
    label_encoder = LabelEncoder()
    for col in categorical_columns:
        data[col] = label_encoder.fit_transform(data[col])
    return data

def scale_numerical(data, numerical_columns):
    """
    Scale numerical columns using MinMaxScaler.
    """
    scaler = MinMaxScaler()
    data[numerical_columns] = scaler.fit_transform(data[numerical_columns])
    return data




def add_noise(X, noise_level=0.01):
    """
    Add random Gaussian noise to numerical features.

    Args:
        X: Input data (DataFrame).
        noise_level: Standard deviation of the noise.

    Returns:
        X_noisy: Data with added noise.
    """
    X_noisy = X.copy()
    for col in X.columns:
        X_noisy[col] += noise_level * np.random.normal(0, 1, X[col].shape)
    return X_noisy
