import tensorflow as tf
from keras import Sequential
from keras.layers import Dense
import numpy as np

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