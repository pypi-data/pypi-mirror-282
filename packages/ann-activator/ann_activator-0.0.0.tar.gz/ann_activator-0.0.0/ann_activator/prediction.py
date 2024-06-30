from keras import Sequential
from keras.layers import Dense
import numpy as np

def predict_temperature(model, X_test):
    # Predict using the model
    y_pred = model.predict(X_test)
    
    return y_pred


