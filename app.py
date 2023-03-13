from flask import Flask, request, jsonify
import pickle
import numpy as np

# create a Flask app
app = Flask(_name_)

# define the route for the prediction API
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

if _name_ == '_main_':
    app.run(debug=True)