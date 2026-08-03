import cv2
import time
from camera.camera import Camera


def main():

    cam = Camera()
    prev_time = time.time()

    while True:

        frame = cam.read()
        h, w = frame.shape[:2]

        cx = w // 2
        cy = h // 2

        # Crosshair
        cv2.line(frame, (cx - 20, cy), (cx + 20, cy), (0,255,0), 2)
        cv2.line(frame, (cx, cy - 20), (cx, cy + 20), (0,255,0), 2)

        # ROI
        size = 100

        cv2.rectangle(
            frame,
            (cx-size//2, cy-size//2),
            (cx+size//2, cy+size//2),
            (255,255,0),
            2
        )

        # FPS
        current = time.time()

        fps = 1/(current-prev_time)

        prev_time = current

        cv2.putText(
            frame,
            f"FPS : {fps:.1f}",
            (10,30),
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