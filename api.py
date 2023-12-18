from flask import Flask, jsonify, request
import joblib,numpy as np

app = Flask(__name__)

# Load the trained model

model = joblib.load('static/model.pkl')
le = joblib.load('static/label.pkl')
std = joblib.load('static/std.pkl')

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)

    x = data['input']

    #preprocessing on predicting data

    x[0] = le.transform([x[0]])
    x[0] = x[0][0]

    x = np.array(x, dtype = float).reshape(1,-1)

    x = std.transform(x)

    #predicting values

    y = model.predict(x)
    
    return jsonify({'prediction': y.tolist()})
    
if __name__ == '__main__':
    app.run(debug=True)
