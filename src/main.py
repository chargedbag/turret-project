import cv2
import time

from vision import get_target
from control import PController
from serial_comm import SerialComm
from utils import clamp
import configs.config as cfg

# Camera
cap = cv2.VideoCapture(cfg.CAMERA_INDEX)
cap.set(3, cfg.FRAME_WIDTH)
cap.set(4, cfg.FRAME_HEIGHT)

center_x = cfg.FRAME_WIDTH // 2
center_y = cfg.FRAME_HEIGHT // 2

# Control
controller_x = PController(cfg.Kp)
controller_y = PController(cfg.Kp)

# Serial
ser = SerialComm(cfg.SERIAL_PORT, cfg.BAUD_RATE)

# Initial angles
pan = 90
tilt = 90

while True:
    ret, frame = cap.read()
    if not ret:
        break

    result = get_target(frame)

    if result:
        (tx, ty), (x, y, w, h) = result

        # Draw face box
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

        error_x = tx - center_x
        error_y = ty - center_y

        # Deadband
        if abs(error_x) < cfg.DEADBAND:
            error_x = 0
        if abs(error_y) < cfg.DEADBAND:
            error_y = 0

        # Control
        pan += controller_x.compute(error_x)
        tilt -= controller_y.compute(error_y)

        pan = clamp(pan, 0, 180)
        tilt = clamp(tilt, 0, 180)

        ser.send(pan, tilt)

        # Draw target
        cv2.circle(frame, (tx, ty), 5, (0,255,0), -1)

    # Draw center
    cv2.circle(frame, (center_x, center_y), 5, (0,0,255), -1)

    cv2.imshow("Turret", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

    time.sleep(0.02)

cap.release()
ser.close()
cv2.destroyAllWindows()
