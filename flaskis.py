from flask import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/sendMan")
def sendMan():
    locations = [
        {"lat":22.638068,"lng":88.342307},{"lat":22.638016,"lng":88.342296},{"lat":22.638034,"lng":88.342150},{"lat":22.638090,"lng":88.342157}
    ]
    return jsonify(locations)


if __name__ == "__main__":
    app.run(port=8080,debug=True)