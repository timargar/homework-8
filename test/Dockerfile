FROM python:3.10

WORKDIR /app

COPY models/model.pickle /app/models/model.pickle
COPY data/inference_features.csv /app/data/inference_features.csv
COPY data/inference_labels.csv /app/data/inference_labels.csv
COPY test/test.py /app/test.py

RUN pip install pandas

CMD ["python", "test.py"]

