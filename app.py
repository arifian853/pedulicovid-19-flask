from flask import Flask, render_template, url_for, request
import os, random, json, requests

app = Flask(__name__)


@app.route('/')
def index():
    response = requests.get("https://api.kawalcorona.com/indonesia/")
    data = response.json()

    response = requests.get("https://disease.sh/v3/covid-19/all/")
    dataDunia = response.json()
    total = 0
    return render_template("index.html", data=data[0], dataDunia=dataDunia)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)