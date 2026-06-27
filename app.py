from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
import keras
import tensorflow as tf
import numpy as np

load_dotenv()

model_path = os.getenv("MODEL_PATH")

model = keras.models.load_model(model_path)

app = Flask(__name__)

@app.route('/')
def home():
    data = request.args.get("inpt")

    try:
        if data:
            if float(data) > 2*np.pi or float(data) < 0:
                return render_template("index.html", error = "Invalid range!")
            elif data.isalpha():
                return render_template("index.html", error = "Invalid input!")
            radian = np.array([float(data)]).reshape(-1,1)
            rad_value = f"{float(radian[0][0]):.2f}"
            act_value = f"{np.sin(float(radian[0][0])):.2f}"
            p = model.predict(radian, verbose = 0)
            res = f"{float(p[0][0]):.2f}"
            return render_template("index.html", result = res, rad = rad_value, act = act_value)
        
        return render_template("index.html")
    
    except Exception as e:
        return render_template("index.html", error = e)
        

app.run(debug = True)
