# encoding: utf-8

import json
from flask import Flask
from flask import Response
app = Flask(__name__)

# load model form one single JSON file
model = json.load(open("data.json", "rb"))


def jsonify(data):
    """
    Create JSON response
    """
    return Response(content_type="application/json",
        response=json.dumps(data, sort_keys=True, indent=4))


def gather_ids(thelist):
    """
    Collect item ids from a list of dicts
    """
    return [x["@id"] for x in thelist]


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
    return jsonify(gather_ids(model["bodies"]))


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
    return jsonify(gather_ids(model["committees"]))


@app.route("/bodies/0/committees/<int:committee>")
def committee_details(committee):
    """
    Show details of a committee
    """
    return jsonify(model["committees"][committee])


@app.route("/bodies/0/meetings/")
def meetings_list():
    """
    Show all meetings
    """
    return jsonify(gather_ids(model["meetings"]))


@app.route("/bodies/0/meetings/<int:meeting>")
def meeting_details(meeting):
    """
    Show details of a meeting
    """
    return jsonify(model["meetings"][meeting])


@app.route("/bodies/0/organisations/")
def organisations_list():
    """
    Show all organisations
    """
    return jsonify(gather_ids(model["organisations"]))


@app.route("/bodies/0/organisations/<int:organisation>")
def organisation_details(organisation):
    """
    Show details of an organisation
    """
    return jsonify(model["organisations"][organisation])


@app.route("/bodies/0/people/")
def people_list():
    """
    Show all people
    """
    return jsonify(gather_ids(model["people"]))


@app.route("/bodies/0/people/<int:person>")
def person_details(person):
    """
    Show details of a person
    """
    return jsonify(model["people"][person])


if __name__ == "__main__":
    app.run(debug=True)
