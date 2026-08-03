from picamera2 import Picamera2
import cv2


class Camera:

    def __init__(self):
        self.picam2 = Picamera2()

        config = self.picam2.create_preview_configuration(
            main={"size": (1280, 720)}
        )

        self.picam2.configure(config)
        self.picam2.start()

    def read(self):
        frame = self.picam2.capture_array()
        return frame

    def release(self):
        self.picam2.stop()