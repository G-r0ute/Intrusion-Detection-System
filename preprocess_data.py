import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

def preprocess_data():
    df = pd.read_csv('features.csv')

    # Encode categorical features
    le = LabelEncoder()
    df['proto'] = le.fit_transform(df['proto'])

    # Separating features and target (assuming the last column is the target)
    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Standardize the features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = preprocess_data()
    print("Data preprocessing complete.")
