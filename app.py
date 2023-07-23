from flask import Flask, request, jsonify
from flask_cors import CORS
from models import classification_model, regression_model

app = Flask(__name__)

CORS(app)

print("Running")


@app.get("/")
def home():
    return jsonify({"message": "Hello World"})


@app.post("/classification")
def classification():
    data = request.get_json()
    print(data)
    x_data = [
        [
            data["day"],
            data["month"],
            data["Temperature"],
            data["RH"],
            data["Ws"],
            data["Rain"],
            data["FFMC"],
            data["DMC"],
            data["DC"],
            data["ISI"],
            data["Region"],
        ]
    ]
    pred = classification_model.predict(x_data)
    class_list = ["Not Fire", "Fire"]
    return jsonify({"Output": class_list[pred[0]]})


@app.post("/regression")
def regression():
    data = request.get_json()
    print(data)
    x_data = [
        [
            data["day"],
            data["month"],
            data["RH"],
            data["Ws"],
            data["Rain"],
            data["FFMC"],
            data["DMC"],
            data["DC"],
            data["ISI"],
            data["Classes"],
            data["Region"],
        ]
    ]
    pred = regression_model.predict(x_data)
    return jsonify({"Temperature": round(pred[0], 2)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    # app.run(debug=True)
    # print(models.classification_model_path)
