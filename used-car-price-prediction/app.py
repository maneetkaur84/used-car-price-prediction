from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle
app = Flask(__name__)
prediction_model=pickle.load(open("Random_Forest_Regression.pkl", 'rb'))

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def price_predict():
        year=int(request.form.get("year"))
        km_driven=int(request.form.get("km_driven"))
        fuel=int(request.form.get("fuel"))
        seller_type=int(request.form.get("seller_type"))
        transmission=int(request.form.get("transmission"))
        owner=int(request.form.get("owner"))
        mileage=float(request.form.get("mileage"))
        engine=int(request.form.get("engine"))
        max_power=float(request.form.get("max_power"))
        torque=float(request.form.get("torque"))
        seats=int(request.form.get("seats"))
        
        result= prediction_model.predict([[year, km_driven, fuel, seller_type,transmission, owner, mileage, engine,max_power, torque, seats]])
        price=round(result[0])
        
        return render_template("index.html", result="Price of your car is ₹{}".format(price))
        
if __name__ == "__main__": 
    app.run(debug=True)
    
    