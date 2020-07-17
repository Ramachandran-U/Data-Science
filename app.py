# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 17:24:08 2020

@author: Ramachandran
"""

import pandas as pd
import numpy as np
from flask import Flask, request
import pickle

app = Flask(__name__)
pickle_in = open('rf.pkl','rb')
rf = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict', methods = ['GET'])
def predict_glass():
    RI = request.args.get('RI')
    Na = request.args.get('Na')
    Mg = request.args.get('Mg')
    Al = request.args.get('Al')
    Si = request.args.get('Si')
    K = request.args.get('K')
    Ca = request.args.get('Ca')
    Ba = request.args.get('Ba')
    Fe = request.args.get('Fe')
    prediction = rf.predict([[RI, Na, Mg, Al, Si, K, Ca, Ba, Fe]])
    if prediction == [1]:
        print("prediction is coral")
    else:
        print("didn't work")
    #return "Predicted values is" + str(prediction)


if __name__=="__main__":
    app.run()