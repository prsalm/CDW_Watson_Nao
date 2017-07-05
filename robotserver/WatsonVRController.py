import os
from watson_developer_cloud import VisualRecognitionV3

class WatsonVRController:

    def __init__(self):
        self.apiKey = self.getApiKey()
        self.vr = VisualRecognitionV3('2016-05-20', api_key=self.apiKey)

    # Get the API key.
    # First try to find it in the ENV.  If not there, then go to watson_vr.key.
    # DO NOT commit watson_vr.key to Git.  Just keep it in the same project directory as this file.
    # It should contain the key text only.
    def getApiKey(self):
        key = ""
        try:
            key = os.environ["VR_WATSON_API_KEY"]
        except KeyError:
            f = open("watson_vr.key", "r+b")
            key = f.read()
            f.close()

        print(f"The key is {key}.")

        return key

