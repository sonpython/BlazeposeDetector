import cv2
import mediapipe as mp
from flask import Flask, Response

# Khởi tạo các thành phần của Mediapipe BlazePose
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
pose = mp_pose.Pose()

# Flask để stream video lên web
app = Flask(__name__)

# Mở camera (sử dụng camera mặc định)
cap = cv2.VideoCapture(0)


def generate_frames():
    while True:
        try:
            # Đọc khung hình từ camera
            success, frame = cap.read()
            if not success:
                break

            # Chuyển đổi khung hình từ BGR sang RGB cho Mediapipe
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Xử lý BlazePose
            results = pose.process(frame_rgb)

            # Nếu tìm thấy khung hình, vẽ kết quả BlazePose
            if results.pose_landmarks:
                mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            # Mã hóa lại khung hình thành JPEG để stream qua HTTP
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Tạo response trả về kiểu "multipart/x-mixed-replace" để stream liên tục
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        except Exception as e:
            print(e)


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    # Chạy server Flask trên cổng 5000
    app.run(host='0.0.0.0', port=5000)
