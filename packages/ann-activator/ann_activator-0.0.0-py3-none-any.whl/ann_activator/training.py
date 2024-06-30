from keras import Sequential
from keras.layers import Dense
import numpy as np

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