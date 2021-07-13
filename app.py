from flask import Flask, render_template, url_for, request
import pandas as pd
import pickle

loaded_model = pickle.load(open('xgboost_model.pkl', "rb"))

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods=["POST"])
def predict():
    df = pd.read_csv("real_2016.csv")
    prediction = loaded_model.predict(df.iloc[:, :-1].values)
    prediction = prediction.tolist()

    return render_template("result.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
