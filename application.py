from flask import Flask,request,jsonify,render_template

import pandas as pd
import numpy as np
import pickle
import os

application = Flask(__name__)
app = application

## import ridge regressor and standard scaler pickle
ridge_model = pickle.load(open('models/ridge.pkl','rb'))
standard_scaler = pickle.load(open('models/scaler.pkl','rb'))


@app.route('/',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='POST':
        Temperature=float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        new_scaled_data = standard_scaler.transform([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
        result = ridge_model.predict(new_scaled_data)
        return render_template('index.html',results = result[0])
    else :
        return render_template('home.html')

if __name__=="__main__":
    port = int(os.environ.get("PORT", 5000))  # default to 5000 for local
    app.run(host='0.0.0.0', port=5000 , debug=True)