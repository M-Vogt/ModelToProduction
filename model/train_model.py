import json
from pathlib import Path
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load the training dataset from the JSON file
with open("dataset.json", "r") as f:
    training_data = json.load(f)

# Extract the features and labels
X = []
y = []
for entry in training_data:
    features, label = entry
    features = np.array([
        features["Temperature"]["value"],
        features["Humidity"]["value"],
        features["Sound Volume"]["value"],
    ])
    # label = entry["label"]
    X.append(features)
    y.append(label)

# Convert the lists to numpy arrays
X = np.array(X)
y = np.array(y)

# Split the dataset into training and test data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Initialize and train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate the model on the test data
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy)

# Save the trained model
model_path = Path('.')
model_filename = Path("trained_model.pkl")
with open(model_path / model_filename, "wb") as f:
    pickle.dump(model, f)
