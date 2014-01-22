# encoding: utf-8

import os
import json
import copy
from flask import Flask
from flask import Response
app = Flask(__name__)

# load model form one single JSON file
model = json.load(open("data.json", "rb"))

files = {}
dirlist = os.listdir('documents')
for f in dirlist:
    (num, suffix) = f.split(".")
    if num != '' and suffix != '':
        files[num] = f


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


@app.route("/bodies/0/papers/<int:paper>/auxiliary_documents/")
def aux_documents_list(paper):
    """
    Show auxiliary documents for paper
    """
    #print(model["papers"][paper])
    return jsonify(model["papers"][paper]["_refserver_links"]["auxiliary_documents"])


@app.route("/bodies/0/papers/<int:paper>/documents/<int:document>")
def document_details(paper, document):
    """
    Show details of one document
    """
    return jsonify(model["documents"][document])


@app.route("/bodies/0/papers/<int:paper>/documents/<int:document>/access")
def document_access(paper, document):
    """
    Send the document file
    """
    path = os.path.join("documents", files[str(document)])
    app.logger.debug(path)
    content = open(path, "rb").read()
    headers = {
        "X-TODO": "Last-Modified",
        "Content-Length": len(content)
    }
    return Response(
        headers=headers,
        content_type=model["documents"][document]["mime_type"],
        response=content)


@app.route("/bodies/0/papers/<int:paper>/documents/<int:document>/download")
def document_download(paper, document):
    """
    Send the document file with content-disposition
    """
    path = os.path.join("documents", files[str(document)])
    app.logger.debug(path)
    content = open(path, "rb").read()
    headers = {
        "X-TODO": "Last-Modified",
        "Content-Length": len(content),
        "Content-Disposition": 'attachment; filename="%s"' % model["documents"][document]["filename"]
    }
    return Response(
        headers=headers,
        content_type=model["documents"][document]["mime_type"],
        response=content)


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


@app.route("/bodies/0/papers/")
def papers_list():
    """
    Show all papers
    """
    return jsonify(gather_ids(model["papers"]))


@app.route("/bodies/0/papers/<int:paper>")
def paper_details(paper):
    """
    Show details of one paper
    """
    p = copy.deepcopy(model["papers"][paper])
    # delete links to related items
    if "_refserver_links" in p:
        del p["_refserver_links"]
    return jsonify(p)


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
else:
    # production mode - replace all URLs
    print("WARNING: Running reference server in production mode.")
    print("You don't want that unless you are hosting http://refserv.oparl.de/")
    app.config["SERVER_NAME"] = "refserv.oparl.de"

    def replace_hostname(m, hostname):
        if type(m) == dict:
            for key in m.keys():
                m[key] = replace_hostname(m[key], hostname)
        elif type(m) == list:
            for n in range(len(m)):
                m[n] = replace_hostname(m[n], hostname)
        elif type(m) == unicode:
            m = m.replace("127.0.0.1:5000", hostname)
        return m

    model = replace_hostname(model, app.config["SERVER_NAME"])

    print(app.config)
