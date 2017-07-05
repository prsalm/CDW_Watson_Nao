import datetime
import json
import os
import tempfile

from flask import Flask, request

from WatsonVRController import WatsonVRController

app = Flask(__name__)
wvrc = WatsonVRController()

FORCE_NONE = -1
FORCE_MALE = 0
FORCE_FEMALE = 1


forceGender = FORCE_NONE
genderUrls = ["http://cdxn.playbuzz.com/cdn/6f967c71-542b-4183-8bbb-254ad4da076e/d3bcddef-73ea-43ce-ab0a-b1998b788357.jpg",
             "https://www.biography.com/.image/t_share/MTE4MDAzNDEwNDM1NzM3MTAy/jennifer-aniston-9185599-1-402.jpg"]

def processUrl(url, vrMethod):
    global forceGender

    targetUrl = url;
    if forceGender != FORCE_NONE:
        targetUrl = genderUrls[forceGender]

    response = vrMethod(images_url = targetUrl)

    forceGender = FORCE_NONE
    return response


@app.route("/classify/url/<path:url>")
def classifyUrl(url):
    return json.dumps(processUrl(url, wvrc.vr.classify), indent=4)


@app.route("/detect/url/<path:url>")
def detectUrl(url):
    return json.dumps(processUrl(url, wvrc.vr.detect_faces), indent=4)


def processFile(request, vrMethod):
    global forceGender

    if forceGender == FORCE_NONE:
        tempFileName = next(tempfile._get_candidate_names()) + ".jpg"
        file = request.files["file"]
        file.save(tempFileName)

        with open(tempFileName, "rb") as imageFile:
            response = vrMethod(images_file = imageFile)
            imageFile.close()
            os.unlink(imageFile.name)

    else:
        response = processUrl(genderUrls[forceGender], wvrc.vr.detect_faces)

    forceGender = FORCE_NONE
    return response


@app.route("/classify/file/", methods=["POST"])
def classifyFile():
    return json.dumps(processFile(request, wvrc.vr.classify), indent=4)


@app.route("/detect/file/", methods=["POST"])
def detectFile():
    return json.dumps(processFile(request, wvrc.vr.detect_faces), indent=4)


@app.route("/male")
def forceMale():
    global forceGender
    forceGender = FORCE_MALE
    return "Male"


@app.route("/female")
def forceFemale():
    global forceGender
    forceGender = FORCE_FEMALE
    return "Female"


# #############################################
# #############################################
# #############################################


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
