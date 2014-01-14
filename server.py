# encoding: utf-8

import json
from flask import Flask
from flask import Response
app = Flask(__name__)

# load model form one single JSON file
model = json.load(open("data.json", "rb"))


def jsonify(data):
    return Response(content_type="application/json",
        response=json.dumps(data, sort_keys=True, indent=4))


@app.route("/")
def root():
    """
    Root: Show information on this system
    """
    return jsonify(model["system"])


@app.route("/bodies/")
def bodies_list():
    """
    Show list of bodies
    """
    return jsonify(model["bodies"])


@app.route("/bodies/<int:body>")
def body_details(body):
    """
    Show information on a certain body
    """
    return jsonify(model["bodies"][body])


@app.route("/bodies/0/committees/")
def committees_list():
    """
    Show all committees
    """
    return jsonify(model["committees"])


@app.route("/bodies/0/meetings/")
def meetings_list():
    """
    Show all meetings
    """
    return jsonify(model["meetings"])


@app.route("/bodies/0/organisations/")
def organisations_list():
    """
    Show all organisations
    """
    return jsonify(model["organisations"])


@app.route("/bodies/0/people/")
def people_list():
    """
    Show all people
    """
    return jsonify(model["people"])



if __name__ == "__main__":
    app.run(debug=True)
