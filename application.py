import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from flask_restful import Resource, Api

app = Flask(__name__)
cardioPrediction = pickle.load(open('cardioPrediction.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/calculate',methods=['POST'])
def calculate():
    bmi=''
    if request.method=='POST' and 'weight' in request.form and 'height' in request.form:
        Weight=float(request.form.get('weight'))
        Height=float(request.form.get('height'))
        bmi=round(((Weight/(Height**2))*703),2)
    return render_template("index2.html",bmi=bmi)

@app.route('/machinelearning',methods=['POST'])
def machinelearning():
    inputArray=[]
    if request.method=='POST' and 'age' in request.form and 'gender' in request.form and 'bmi' in request.form and 'ap_hi' in request.form and 'ap_lo' in request.form and 'chol' in request.form and 'gluc' in request.form:
        Age=float(request.form.get('age'))
        Gender=float(request.form.get('gender'))
        BMI=float(request.form.get('bmi'))
        Systolic=float(request.form.get('ap_hi'))
        Diastolic=float(request.form.get('ap_lo'))
        Cholesterol=float(request.form.get('chol'))
        Glucose=float(request.form.get('gluc'))
#Creating an Array 
        #answer=Age+Gender+BMI+Systolic+Diastolic+Cholesterol+Glucose
        inputArray.append([Age,Gender,Systolic,Diastolic,Cholesterol,Glucose, BMI])
        inputScaler = scaler.transform(inputArray)
        outputValue = cardioPrediction.predict(inputScaler)
        outputValue = outputValue[0]
    return render_template("index2.html",outputValue=outputValue)

if __name__ == '__main__':
    app.run()