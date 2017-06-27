import datetime
import json
import os
import tempfile

from flask import Flask, request
from WatsonVRController import WatsonVRController

app = Flask(__name__)

@app.route("/classify/url/<path:url>")
def classifyUrl(url):
    response = wvrc.vr.classify(images_url=url)
    return json.dumps(response, indent=4)

    # return response["images"][0]["classifiers"][0]["classes"][0]["class"]

@app.route("/classify/file/", methods=["POST"])
def classifyFile():
    tempFileName = next(tempfile._get_candidate_names()) + ".jpg"

    file = request.files["file"]
    file.save(tempFileName)

    with open(tempFileName, "rb") as imageFile:
        response = wvrc.vr.classify(images_file=imageFile, classifier_ids=["default"], threshold=0.1)
        imageFile.close()
        os.unlink(imageFile.name)
        return json.dumps(response, indent=4)

        # return respon    se["images"][0]["classifiers"][0]["classes"][0]["class"]

@app.route("/pi/url/<path:url>")
def piUrl(url):
    return url

@app.route("/")
@app.route("/test")
def chester():
    return "This is /test @ " + str(datetime.datetime.now().time())

@app.route("/abc/<p1>/<p2>", methods=["GET", "POST"])
def abc(p1, p2):

    if "abc" in request.form:
        if "xyz" in request.headers:
            return "{0} {1} {2} {3}".format(request.headers["xyz"], request.form["abc"], p1, p2)
        else:
            return "{0} {1} {2}".format(request.form["abc"], p1, p2)
    else:
        return "p1: {0}, p2: {1}".format(p1, p2)


# #############################################
# #############################################
# #############################################


wvrc = WatsonVRController()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
