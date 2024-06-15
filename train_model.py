import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib

def preprocess_data():
    df = pd.read_csv('features.csv')

    # Encode categorical features
    le = LabelEncoder()
    df['proto'] = le.fit_transform(df['proto'])

    # Separate features and target (assuming the last column is the target)
    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Standardize the features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test

def train_model():
    X_train, X_test, y_train, y_test = preprocess_data()

    # Initialize the Random Forest classifier
    clf = RandomForestClassifier(n_estimators=100, random_state=42)

    # Train the model
    clf.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = clf.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')

    print(f'Accuracy: {accuracy}')
    print(f'Precision: {precision}')
    print(f'Recall: {recall}')
    print(f'F1 Score: {f1}')

    # Save the model to a file
    joblib.dump(clf, 'ids_model.pkl')
    print("Model saved as ids_model.pkl")

if __name__ == "__main__":
    train_model()
