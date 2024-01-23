"""
test.py: Script for testing the DecisionTreeClassifier on the Iris dataset.
"""

import pandas as pd
import pickle

X_test = pd.read_csv('data/inference_features.csv')
y_test = pd.read_csv('data/inference_labels.csv')

with open('models/model.pickle', 'rb') as f:
    model = pickle.load(f)

predictions = model.predict(X_test)


pd.DataFrame(predictions, columns=['Predictions']).to_csv('results/predictions.csv', index=False)