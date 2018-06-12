from flask import Flask
from flask import jsonify


app = Flask(__name__)


@app.route("/fruits")
def fruits():
    return jsonify({"fruits": ["mango", "banana", "orange"]})


if __name__ == '__main__':
    app.run(debug=True, port='5002')
