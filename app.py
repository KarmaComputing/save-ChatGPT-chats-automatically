from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from datetime import datetime
import os
import json
from pathlib import Path


app = Flask(__name__)
cors = CORS(app, send_wildcard=True)
CHATS_DIRECTORY = app.config.get("CHATS_DIRECTORY", "./chats/")


@app.route("/save", methods=["POST"])
def index():
    body = json.loads(request.data)["body"]
    filename = int(datetime.now().timestamp())
    with open(f"{CHATS_DIRECTORY}{filename}", "w") as fp:
        fp.write(body)
    return jsonify({"msg": f"wrote file: {filename}"})


def parse(filename):
    # Parse the HTML using BeautifulSoup
    path = Path("./", filename).absolute()
    with open(path, "r") as fp:
        text = fp.read()
        return text


@app.route("/chat/<timestamp>")
def show_chat(timestamp):
    path = Path(CHATS_DIRECTORY, timestamp).absolute()
    return parse(path)


@app.route("/parse")
def parse_latest():
    # Get a list of all the files in the directory
    files = os.listdir(CHATS_DIRECTORY)
    # Initialize a variable to keep track of the most recently modified file
    most_recent_file = None
    # Iterate over the list of files
    for file in files:
        # Get the full path of the current file
        file_path = os.path.join(CHATS_DIRECTORY, file)

        if most_recent_file is None or os.path.getmtime(
            file_path
        ) > os.path.getmtime(  # noqa: E501
            most_recent_file
        ):
            # If the current file is more recently modified, store
            # its path as the
            # most recently modified file
            most_recent_file = file_path
    parsed = parse(most_recent_file)
    return render_template("parsed.html", parsed=parsed)
