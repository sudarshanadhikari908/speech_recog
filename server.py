import random
import os
from flask import Flask, request, jsonify, render_template
from keyword_spotting_service import Keyword_Spotting_Service
import pickle

# instantiate flask app
app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        print("form fata")
    return render_template("base.html")


@app.route("/predict", methods=["POST", "GET"])
def predict():
    """Endpoint to predict keyword
:return (json): This endpoint returns a json file with the following format:
    {
        "keyword": "down"
    }

    """
    # if request.method == "POST":
    #     print("form fata")
    # data = {}
    # get file from POST request and save it
    if request.method == "POST":
        print("form fata")
    audio_file = request.files["file"]

    file_name = str(random.randint(0, 100000))
    audio_file.save(file_name)

    # instantiate keyword spotting service singleton and get prediction
    kss = Keyword_Spotting_Service()
    predicted_keyword = kss.predict(file_name)

    # we don't need the audio file any more - let's delete it!
    os.remove(file_name)

    # send back result as a json file
    # result = {"keyword": predicted_keyword}
    # return jsonify(result)
    # data = {'result': result}
    # return render_template('result.html', data)
    return render_template('base.html', result=predicted_keyword)


if __name__ == "__main__":
    app.run(debug=True)
