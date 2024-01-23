FROM python:3.10

WORKDIR /app

COPY data/train_features.csv /app/data/train_features.csv
COPY data/train_labels.csv /app/data/train_labels.csv
COPY training/train.py /app/train.py

RUN pip install pandas scikit-learn mlflow numpy

CMD ["python", "train.py"]
