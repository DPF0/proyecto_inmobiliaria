from flask import Flask, request, jsonify
import os
import pickle
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_absolute_error
import pandas as pd
import sqlite3
from flask_cors import CORS


os.chdir(os.path.dirname(__file__))

app = Flask(__name__)
CORS(app)
# app.config['DEBUG'] = True

@app.route("/", methods=['GET'])
def hello():
    return "Bienvenido a nuestra API de casas"

#1
@app.route('/predict', methods=['GET'])
def predict():

    surface = request.args.get('surface')
    bedrooms = request.args.get('bedrooms')
    restrooms = request.args.get('restrooms')
    ascensor = request.args.get('ascensor')

    if int(bedrooms) <= 1:
        model = pickle.load(open('./models/model_atico.pkl', 'rb'))

    elif int(bedrooms) <= 4:
        model = pickle.load(open('./models/model_apartamento.pkl', 'rb'))

    else:
        model = pickle.load(open('./models/model_chalet.pkl', 'rb'))

    X = pd.DataFrame(data= [[int(surface), int(bedrooms), int(restrooms), int(ascensor)]])

    prediction = model.predict(X)
    prediction = str(round(prediction[0],2))
    # return prediction
    return jsonify({'surface': surface, 'bedrooms': bedrooms, 'restrooms': restrooms, 'ascensor': ascensor, 'prediction': prediction})


# app.run()