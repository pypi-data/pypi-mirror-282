import tensorflow as tf
from keras import Sequential
from keras.layers import Dense
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

def calculate_rmse(model, X_test, y_test):
    # Predict using the model
    y_pred = model.predict(X_test)
    
    from sklearn.metrics import mean_squared_error
    
    # Calculate Root Mean Squared Error (RMSE)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    
    return rmse

def calculate_r2(model, X_test, y_test):
    # Predict using the model
    y_pred = model.predict(X_test)
    
    from sklearn.metrics import r2_score
    # Calculate R-squared score
    r2 = r2_score(y_test, y_pred)
    
    
    return r2


def predict_temperature(model, X_test):
    # Predict using the model
    y_pred = model.predict(X_test)
    
    return y_pred


def preprocess_data(filepath, test_size):
    # Load data with latin1 encoding
    try:
        df = pd.read_csv(filepath, encoding='latin1')
    except UnicodeDecodeError as e:
        raise ValueError(f"Failed with latin1 encoding: {e}")
    
    # Clean data by dropping NA values
    df_cleaned = df.dropna()
    
    # Select relevant columns and drop NA values again if necessary
    df1 = df_cleaned[['temp', 'pressure', 'humidity', 'dew_point', 'clouds', 'wind_speed', 'wind_deg', 'weather_description']].dropna()
    
    # Encode the 'weather_description' column using LabelEncoder
    label_encoder = LabelEncoder()
    df1['weather_encoded'] = label_encoder.fit_transform(df1['weather_description'])
    
    # Convert temperature from Kelvin to Celsius
    df1['temp'] = df1['temp'] - 273.15
    
    # Separate features (X) and target (y)
    X = df1.drop(columns=['temp', 'weather_description'])
    y = df1['temp']
    
    # Scale the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=test_size)
    
    return X_train, X_test, y_train, y_test


def train_model(X_train, y_train):
    # Define the ANN model
    model = Sequential()
    model.add(Dense(16, input_dim=X_train.shape[1], activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1))
    
    # Compile the model
    model.compile(optimizer='adam', loss='mean_squared_error')
    
    # Train the model
    history = model.fit(X_train, y_train, epochs=100, batch_size=10, validation_split=0.2)
    
    return model, history

def select_features(model, X_train, X_test, threshold=0.1):
    # Extract the weights of the trained model
    weights = model.get_weights()
    
    # Get the weights of the input layer and first hidden layer
    weights_input_hidden1 = weights[0]
    weights_hidden1_hidden2 = weights[2]
    
    # Calculate the absolute sum of weights for each input feature
    feature_importance_input_hidden1 = np.abs(weights_input_hidden1).sum(axis=1)
    
    # Select only the important features
    selected_features = np.where(feature_importance_input_hidden1 > threshold)[0]
    
    # Select only the important features
    X_train_selected = X_train[:, selected_features]
    X_test_selected = X_test[:, selected_features]
    
    return X_train_selected, X_test_selected, selected_features