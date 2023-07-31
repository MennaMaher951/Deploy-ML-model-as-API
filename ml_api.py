# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 21:43:17 2023

@author: Lenovo
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

class model_input(BaseModel):
    
    Pregnancies : int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int
    
# loading the saved model 
diabetes_model = pickle.load(open('diabetes_model.sav','rb'))
    
@app.post('/diabetes_predicton')
def diabetes_pred(input_parameters : model_input) :
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    preg = input_dictionary['Pregnancies']
    gluc = input_dictionary['Glucose']
    bp = input_dictionary['BloodPressure']
    skinth = input_dictionary['SkinThickness']
    ins = input_dictionary['Insulin']
    bmi = input_dictionary['BMI']
    dpf = input_dictionary['DiabetesPedigreeFunction']
    age = input_dictionary['Age']
    
    input_list = [preg, gluc, bp, skinth, ins, bmi, dpf, age]
    prediction = diabetes_model.predict([input_list])
    
    if prediction[0]==0:
        return 'the person is not diabetic'
    else :
        return 'the person is diabetic'

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    