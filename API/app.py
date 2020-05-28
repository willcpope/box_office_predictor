import numpy as np

from flask import Flask
from flask import Flask, jsonify
from flask_cors import CORS

import pickle
from sklearn.linear_model import LinearRegression

import locale
locale.setlocale( locale.LC_ALL, '' )

# setup Flask
app = Flask(__name__)
CORS(app)

# load model
model = pickle.load(open("../Resources/Data/regression_model_trained.sav", "rb"))

@app.route("/")
def welcome():
    return (
        f"<h1>Sturdy Waddle API Routes</h1>"
        f"/api/v1.0/linear_regression/"
    )

@app.route("/api/v1.0/linear_regression/<value>")
def linear_regression(value):
    try:
        if float(value) < 0 or float(value) > 100:
            raise Exception
        result = locale.currency(model.predict(np.array([[float(value)]]))[0][0], grouping=True)
        return jsonify(result)
    except:
        return jsonify({"error": f"{value} is not valid."}), 404

if __name__ == "__main__":
    app.run(debug=True)