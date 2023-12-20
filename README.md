# SVC Flask local API

This Python project utilizes a Flask API employing an SVM model to predict whether a user will purchase a product offered by Delta Company. The prediction is based on the user's input of gender (Male/Female), age (int), and salary (int), processed through `client.py`, sent as a POST request to the API (`api.py`), where the trained models are loaded to generate predictions.

## Project Structure

- **model.py:** Demonstrates the creation of the prediction model using the provided CSV file. Users can modify this file to create and train their custom models.
- **client.py:** Handles user input for gender, age, and salary, sending it to the API for predictions.
- **api.py:** Sets up the Flask API, loads trained models, and predicts the likelihood of a user purchasing the product.

## Requirements

Ensure you have the following dependencies installed:
- Flask
- NumPy
- Pandas
- Scikit-learn

Install the required dependencies using:

`pip install -r requirements.txt`

## Usage

- **Run `api.py`** to start the Flask API.
- Use **`client.py`** to input user data for prediction.
  
`python client.py`

## Custom Model Creation

Modify model.py to create and train your custom machine-learning models using different datasets or algorithms. Adjust preprocessing steps, model training, and serialization as needed.

## Future Scope

To host the API in a production environment, consider deploying it to a hosting service or a cloud platform. Ensure security measures, input validation, and scalability for real-world usage.

## Additional Notes

- Data File: The provided CSV file Social_Network_Ads.csv is used for demonstration purposes. Replace it with your dataset for training custom models.
- Endpoint: The API endpoint for predictions is /predict. Modify client.py if the API is hosted elsewhere.
- Security: Sanitize user inputs and implement error handling for robustness.
