import cv2
from camera.camera import Camera


def main():

    cam = Camera()

    while True:

        frame = cam.read()

        cv2.imshow("CATUP Vision", frame)

        key = cv2.waitKey(1)

        if key == ord("q"):
            break

    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()