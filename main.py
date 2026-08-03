import cv2
import time
import numpy as np
from camera.camera import Camera
from vision.color_detector import detect_color
from sorter.sorter_queue import SortQueue

queue = SortQueue()


def main():

    cam = Camera()

    prev_time = time.time()

    while True:

        frame = cam.read()

        h, w = frame.shape[:2]

        cx = w // 2
        cy = h // 2

        # ---------- ROI ----------
        size = 100

        x1 = cx - size // 2
        y1 = cy - size // 2
        x2 = cx + size // 2
        y2 = cy + size // 2

        roi = frame[y1:y2, x1:x2]

        # ---------- HSV ----------
        hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

        avg = np.mean(hsv_roi.reshape(-1, 3), axis=0)

        H = int(avg[0])
        S = int(avg[1])
        V = int(avg[2])
        color = detect_color(H, S, V)
        
        last_color = ""
        if color != last_color:
            queue.push(color)
            last_color = color

        # ---------- Crosshair ----------
        cv2.line(frame, (cx - 20, cy), (cx + 20, cy), (0, 255, 0), 2)
        cv2.line(frame, (cx, cy - 20), (cx, cy + 20), (0, 255, 0), 2)

        # ---------- ROI ----------
        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (255, 255, 0),
            2
        )

        # ---------- FPS ----------
        current = time.time()

        fps = 1 / (current - prev_time)

        prev_time = current

        cv2.putText(
            frame,
            f"FPS : {fps:.1f}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        # ---------- HSV ----------
        cv2.putText(
            frame,
            f"H:{H} S:{S} V:{V}",
            (10, 65),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 255),
            2
        )

        cv2.putText(
            frame,
            f"COLOR : {color}",
            (10,95),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0,255,0),
            2
        )

        cv2.imshow("CATUP Vision", frame)

        key = cv2.waitKey(1)

        if key == ord("q"):
            break

    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()