# app.py
# This Flask application serves a machine learning model for Hepatitis C prediction.

# --- IMPORTS ---
# Added 'render_template' to the import list from flask.
from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd # pandas is commonly used for data manipulation with scikit-learn models

# Initialize the Flask application
app = Flask(__name__)

# --- Model Loading ---
# Load the trained Hepatitis C model when the Flask application starts up.
# This ensures the model is loaded only once, making predictions faster.
try:
    # Ensure 'logistic_regression_HepatitisC_model.pkl' is in the same directory as app.py
    model = joblib.load('logistic_regression_HepatitisC_model.pkl')
    print("Hepatitis C model loaded successfully!")
except Exception as e:
    # If the model fails to load, print an error and set model to None.
    # This prevents the app from crashing and allows for graceful error handling.
    print(f"Error loading Hepatitis C model: {e}")
    model = None # Set model to None to indicate a loading failure

# --- Home Route (MODIFIED) ---
# This route will now serve your HTML frontend (index.html).
# Flask will automatically look for 'index.html' inside the 'templates' folder.
@app.route('/')
def home():
    return render_template('index.html') # Renders the HTML file

# --- Prediction Route (UNCHANGED) ---
# This route handles incoming prediction requests from the frontend.
# It expects a POST request with JSON data containing the features for prediction.
@app.route('/predict', methods=['POST'])
def predict():
    # Check if the model was loaded successfully.
    if model is None:
        return jsonify({'error': 'Prediction model not loaded. Please check server logs for details.'}), 500

    try:
        # Get the JSON data from the incoming request.
        # force=True will try to parse even if Content-Type header is not application/json.
        data = request.get_json(force=True)

        # --- Data Preprocessing for Prediction ---
        # IMPORTANT: The structure of 'data' must exactly match the features
        # and their order/format that your model was trained on.
        # For example, if your model expects features like 'AST', 'ALP', 'BIL', 'CREA',
        # the incoming JSON should have these keys.

        # Convert the incoming JSON data (which is a dictionary) into a pandas DataFrame.
        # This is crucial because scikit-learn models often expect DataFrame or NumPy array input.
        # We wrap 'data' in a list to create a DataFrame with a single row (one prediction).
        input_df = pd.DataFrame([data])

        # --- Apply any necessary preprocessing steps here ---
        # If your original model training involved steps like StandardScaler, MinMaxScaler,
        # or OneHotEncoder, you MUST apply the exact same transformations to 'input_df' here.
        # Ideally, you would have saved these preprocessors using joblib as well and loaded them.
        # Example (if you had a preprocessor saved as 'preprocessor.pkl'):
        # if 'preprocessor' in locals() and preprocessor is not None:
        #     input_df = preprocessor.transform(input_df)

        # Make a prediction using the loaded model.
        # For classification, you might use model.predict_proba for probabilities
        # or model.predict for the class label.
        prediction = model.predict(input_df)

        # Convert the prediction (which is typically a NumPy array) to a Python list
        # so it can be easily serialized to JSON.
        # We take the first element [0] assuming a single prediction for a single input.
        output = prediction[0].tolist()

        # Return the prediction as a JSON response.
        return jsonify({'prediction': output})

    except Exception as e:
        # Catch any errors during prediction and return a helpful error message.
        return jsonify({'error': f'An error occurred during prediction: {str(e)}'}), 400

# --- Run the Flask Application ---
# This block ensures the app runs only when the script is executed directly.
if __name__ == '__main__':
    # debug=True is useful for development as it provides detailed error messages
    # and reloads the server on code changes.
    # IMPORTANT: Set debug=False in a production environment for security and performance.
    app.run(debug=True)
