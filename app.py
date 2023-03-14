from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    
    with open('linear_regression_model.pkl', 'rb') as file:
        model = pickle.load(file)

    data = request.get_json()
    
    X = np.array([[data['yearsExperience']]])

    prediction = model.predict(X)
    response = {
        'prediction': prediction[0]
    }

    return jsonify(response)

if __name__ == '_main_':
    app.run(debug=True)