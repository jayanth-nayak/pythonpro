import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import joblib


app = Flask(__name__) #Initialize the flask App

model = joblib.load('price.pkl')

@app.route('/')
def home():
    return render_template('Property_price.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    inp_features = [[x for x in request.form.values()]]

    print(inp_features)

    x_cols = ['city2', 'Bedrooms', 'Bathrooms', 'Transaction', 'StatusOfElectricity','Furnishing', 'LoanOffered', 'superarea', 'WaterAvailable', 'floors']

    inputdata = pd.DataFrame(inp_features, columns = x_cols)

    prediction = model.predict(inputdata)

    output = round(prediction[0], 0)

    return render_template('Property_price.html', Text = "This the Price for the given values: ", price=output, pricein = 'lacs')

if __name__ == "__main__":
    app.run(debug=True)