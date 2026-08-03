import cv2
import time
from camera.camera import Camera


def main():

    cam = Camera()
    prev_time = time.time()

    while True:

        frame = cam.read()
        height, width = frame.shape[:2]

        cv2.line(frame, (width//2 - 20, height//2),
                (width//2 + 20, height//2), (0,255,0), 2)

        cv2.line(frame, (width//2, height//2 - 20),
                (width//2, height//2 + 20), (0,255,0), 2)

        current_time = time.time()
        fps = 1 / (current_time - prev_time)
        prev_time = current_time

        cv2.putText(frame,
                    f"FPS: {fps:.1f}",
                    (10,30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0,255,0),
                    2)

        cv2.imshow("CATUP Vision", frame)

        key = cv2.waitKey(1)

        if key == ord("q"):
            break

    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()