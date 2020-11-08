import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
#model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate',methods=['POST'])
def calculate():
    bmi=''
    if request.method=='POST' and 'weight' in request.form and 'height' in request.form:
        Weight=float(request.form.get('weight'))
        Height=float(request.form.get('height'))
        bmi=round(((Weight/(Height**2))*703),2)
    return render_template("index.html",bmi=bmi)

if __name__ == '__main__':
    app.run()