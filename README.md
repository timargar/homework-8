# Iris flower classification

A brief description of what this project does and who it's for.

## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have installed the latest version of Python.
* You have a Windows/Linux/Mac machine.
* You have read `requirements.txt`.

## Installing <project_name>

To install <project_name>, follow these steps:

`python3 -m pip install -r requirements.txt`


V
## Using <project_name> with Docker

### Building the Docker Image

1. Build the Docker image from the Dockerfile:
`docker build -t <image_name> .`

Replace `<image_name>` with the name you want to give to your Docker image.

### Running the Training

2. Run the training inside a Docker container:

`docker run -v $(pwd)/app/data:/app/data -v $(pwd)/app/models:/app/models <image_name> python train_model.py`

This command mounts your local `data` and `models` directories to the container and runs the training script.

### Running the Inference

3. To perform inference with the Docker container, use the following command:

`docker run -v $(pwd)/app/models:/app/models <image_name> python predict.py <input_data>`


Replace `<input_data>` with the appropriate data input for your model.

## Using <project_name> without Docker

### Training the Model

1. Ensure you have the training data in `/app/data` with the files `train_features.csv` and `train_labels.csv`.
2. Run the training script:

`python train_model.py`

This will create a trained model and save it in `/app/models`.

### Inference

1. Ensure the model is saved in `/app/models`.
2. To perform inference, use the following command:

`python predict.py <input_data>`


## Project structure:


```
homework-8/
│
├── data/
│ ├── inference_features.csv
│ ├── inference_labels.csv
│ ├── train_features.csv
│ └── train_labels.csv
│
├── test/
│ ├── Dockerfile
│ └── test.py
│
├── training/
│ ├── Dockerfile
│ ├── train.py
│
├── .gitignore
├── README.md
└── requirements.txt
```