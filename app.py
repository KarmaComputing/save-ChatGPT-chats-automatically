from flask import Flask, request
from flask_cors import CORS
from datetime import datetime


app = Flask(__name__)
cors = CORS(app, send_wildcard=True)


@app.route("/save", methods=["POST"])
def index():
    body = request.data.decode("utf-8")
    filename = int(datetime.now().timestamp())
    with open(f"./{filename}", "w") as fp:
        fp.write(body)
    return f"wrote file: {filename}"
