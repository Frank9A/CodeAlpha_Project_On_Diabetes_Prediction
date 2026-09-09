# Diabetes Prediction Pipeline

## Overview
This project is an end-to-end machine learning pipeline designed to predict the likelihood of diabetes in patients using the Pima Indians Diabetes Database. The project demonstrates core data science principles, including data imputation, feature importance analysis, model training, hyperparameter tuning, and model serialization for deployment.

## Project Structure
* `main.py`: The core script that loads the dataset, cleans the data, trains the Random Forest model, and exports the finalized model artifact.
* `predict.py`: An inference script that loads the saved model to classify new, unseen patient data instantly.
* `diabetes_model.pkl`: The serialized machine learning model (generated after running `main.py`).

## Installation & Environment Setup
To run this project, it is recommended to use a virtual environment. You will need Python installed along with a few specific data science libraries.

1. **Activate your virtual environment** (if you are using one).
2. **Install the required dependencies** by running the following command in your terminal:

```bash
pip install pandas scikit-learn joblib