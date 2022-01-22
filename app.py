from flask import Flask
import cv2
import base64
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/camera")
def camera():
    cap = cv2.VideoCapture(0)
    retval, image = cap.read()
    retval, buffer = cv2.imencode('.jpg', image)
    jpg_as_text = base64.b64encode(buffer)
    cap.release()
    return 'data: image/png;base64,' + jpg_as_text.decode("utf-8")