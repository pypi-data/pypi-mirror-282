import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

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