# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 17:24:08 2020

@author: Ramachandran
"""

import pandas as pd
import numpy as np
from flask import Flask, request
import pickle
import flasgger
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)


pickle_in = open('rf.pkl','rb')
rf = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict', methods = ['GET'])
def predict_note_authentication():
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: RI
        in: query
        type: number
        required: true
      - name: Na
        in: query
        type: number
        required: true
      - name: Mg
        in: query
        type: number
        required: true
      - name: Al
        in: query
        type: number
        required: true     
      - name: Si
        in: query
        type: number
        required: true
      - name: K
        in: query
        type: number
        required: true
      - name: Ca
        in: query
        type: number
        required: true
      - name: Ba
        in: query
        type: number
        required: true
      - name: Fe
        in: query
        type: number
        required: true
              
    responses:
        200:
            description: The output values
        
    """
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
    print(prediction)
    return str(prediction)


if __name__=='__main__':
    app.run()
