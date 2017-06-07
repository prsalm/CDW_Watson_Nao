# Grab the p3c_watson image from Bluemix with
#
#   bx cr login
#   docker pull registry.ng.bluemix.net/cdw_dev/p3c_waton:0.1
#
# If that doesn't work, you can simply use the FROM python:3.6.1.
# The build will take slightly longer as the pip_install will be run.
# IOW... the only difference between these two FROM images is that
# p3c_watson has the pip install already processed for efficiency.

FROM registry.ng.bluemix.net/cdw_dev/p3c_watson:0.1
# FROM  python:3.6.1

WORKDIR /usr/src/app

COPY app.py ./
COPY WatsonVRController.py ./

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./app.py" ]