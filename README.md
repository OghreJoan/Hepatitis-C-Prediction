Hepatitis C Prediction Model
Project Overview
This repository contains the source code and necessary files for a machine learning model designed to predict Hepatitis C progression categories. The project includes a Flask-based web API for serving predictions and a simple HTML frontend for user interaction.

The primary goal is to provide a data-driven tool to assist in the early identification and classification of Hepatitis C disease stages based on patient biochemical parameters.

Table of Contents
Project Structure

Features and Model

Performance Metrics

Setup and Local Run

Prerequisites

Installation

Running the Application

Accessing the Web Interface

Testing the API Endpoint (Optional)

Deployment (Optional)

Contributing

License

Project Structure
The core application files are located in the flaskapp_hepatitis/ directory.

Hepatitis-C-Prediction/
├── flaskapp_hepatitis/
│   ├── app.py                      # Flask backend application
│   ├── logistic_regression_HepatitisC_model.pkl # Trained ML model
│   ├── requirements.txt            # Python dependencies
│   └── templates/
│       └── index.html              # HTML frontend for user interface
├── Code.ipynb                      # Jupyter Notebook for model training & analysis
├── Hepatitis C Presentation.pptx   # Project presentation/pitch deck
├── HepatitisCdata.csv              # Dataset used for training
└── README.md                       # This README file

Features and Model
Selected Features
The model utilizes the following four key biochemical features, identified through Recursive Feature Elimination (RFE), for prediction:

AST (Aspartate Aminotransferase)

ALP (Alkaline Phosphatase)

BIL (Bilirubin)

CREA (Creatinine)

Model Used
Type: Logistic Regression

Reasoning: Chosen for its interpretability, efficiency, and effectiveness as a classification baseline model.

Prediction Categories
The model classifies patients into one of five categories, numerically encoded as follows:

0: Blood Donor

1: Hepatitis

2: Fibrosis

3: Cirrhosis

4: Suspect Blood Donor

Performance Metrics
The model's performance was evaluated using standard classification metrics.

Overall Accuracy: 0.91 (or 91%)

F1-Score (Macro Avg): 0.53 (Unweighted average across all classes, important for imbalanced datasets)

F1-Score (Weighted Avg): 0.90 (Average weighted by class support)

Detailed Classification Report:
Category

Precision

Recall

F1-Score

Support

Blood Donor (0)

0.95

0.99

0.97

213

Hepatitis (1)

0.67

0.20

0.31

10

Fibrosis (2)

0.29

0.25

0.27

8

Cirrhosis (3)

0.73

0.67

0.70

12

Suspect Blood Donor (4)

0.50

0.33

0.40

3

Note: The lower F1-scores for minority classes (Hepatitis, Fibrosis, Suspect Blood Donor) indicate areas for future improvement in correctly identifying these less frequent but clinically critical conditions.

Install dependencies:

pip install -r requirements.txt

Running the Application
Ensure you are in the flaskapp_hepatitis directory and your virtual environment is active.

Start the Flask development server:

python app.py

You should see output indicating the server is running on http://127.0.0.1:5000/. Keep this terminal window open.

Accessing the Web Interface
Open your web browser.

Navigate to: http://127.0.0.1:5000/
You should see the Hepatitis C Prediction form. Enter values for AST, ALP, BIL, and CREA, then click "Get Prediction."

Testing the API Endpoint (Optional)
You can also test the raw API endpoint using curl in a separate terminal window (while the Flask server is still running):

curl -X POST -H "Content-Type: application/json" -d "{\"AST\": 60.0, \"ALP\": 100.0, \"BIL\": 1.0, \"CREA\": 1.0}" http://127.0.0.1:5000/predict
