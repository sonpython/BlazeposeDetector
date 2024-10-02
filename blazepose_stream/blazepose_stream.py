import cv2
import mediapipe as mp
from flask import Flask, Response
import os

# Initialize Mediapipe BlazePose and Flask
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
pose = mp_pose.Pose()
app = Flask(__name__)

# Get camera index from environment variable, default to 0
camera_index = int(os.getenv("CAMERA_INDEX", 0))

# Open camera (use specified camera index)
cap = cv2.VideoCapture(camera_index)


def generate_frames():
    while True:
        try:
            # Read frame from camera
            success, frame = cap.read()
            if not success:
                break

            # Convert frame from BGR to RGB for Mediapipe
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Process frame with BlazePose
            results = pose.process(frame_rgb)

            # If pose landmarks are found, draw them on the frame
            if results.pose_landmarks:
                mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            # Encode the frame as JPEG to stream over HTTP
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Create response as "multipart/x-mixed-replace" to continuously stream frames
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        except Exception as e:
            print(f"Error processing frame: {e}")


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    # Run Flask server on port 5001
    app.run(host='0.0.0.0', port=5001)
