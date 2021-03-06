from flask import Flask, render_template, Response
import cv2

camera = cv2.VideoCapture(0)

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():  # put application's code here
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run()


def gen_frames():
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            print('Se rompio')
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
