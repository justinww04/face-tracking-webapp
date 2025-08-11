from flask import Flask, render_template, Response, send_file
import cv2, time, os
from io import BytesIO
from threading import Lock

app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.secret_key = "supersecretkey"

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

lock = Lock()
cam = cv2.VideoCapture(0)
if not cam.isOpened():
    raise RuntimeError("❌ Could not open webcam.")


def gen_frames():
    min_face_size = 80 

    while True:
        success, frame = cam.read()
        if not success:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)
        faces = [f for f in faces if f[2] >= min_face_size and f[3] >= min_face_size]

        for (x, y, w, h) in faces:
            
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            
            cv2.putText(frame, "Face in Frame", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            break

        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/snapshot')
def snapshot():
    success, frame = cam.read()
    if not success:
        return "❌ Could not capture frame", 500
    _, buffer = cv2.imencode('.jpg', frame)
    return send_file(BytesIO(buffer.tobytes()), mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)