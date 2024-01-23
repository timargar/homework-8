import os
import pandas as pd
import pickle
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

model_dir = '/app/models'
os.makedirs(model_dir, exist_ok=True)  # Ensure the directory exists

X_train = pd.read_csv('/app/data/train_features.csv')
y_train = pd.read_csv('/app/data/train_labels.csv')

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train.values.ravel())

model_path = os.path.join(model_dir, 'model.pickle')
with open(model_path, 'wb') as f:
    pickle.dump(model, f)
