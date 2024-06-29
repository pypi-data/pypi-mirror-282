import base64
from io import BytesIO

import cv2
import imutils
import numpy as np
import pytesseract
from loguru import logger
from skimage import io

from .skew_detect import SkewDetect


class SauronRotate:

    def __init__(self, enable_logging=True):
        self.enable_logging = enable_logging
        if not self.enable_logging:
            logger.remove()

    def rotate_image_base64(self, img_b64):

        # Transforme base64 in opencv2 image or skimage.io image
        base64_string = img_b64.replace("\n", "").replace(" ", "")
        image_bytes = base64.b64decode(base64_string)
        nparr = np.frombuffer(image_bytes, np.uint8)
        byte_img = BytesIO(image_bytes)
        skimage_img = io.imread(byte_img, as_gray=True)
        opencv_img = cv2.imdecode(nparr, flags=cv2.IMREAD_COLOR)

        # Processing input image and determining resulting angle
        skewed_img = SkewDetect.processing_skew(skimage_img)
        angle = skewed_img["Estimated Angle"]
        angle = round(angle)
        logger.info(f"[ + ] Angle: {angle}")
        rotated_image = imutils.rotate(opencv_img, angle)

        # Determining the new rotation angle with Tesseract
        osd_output = pytesseract.image_to_osd(rotated_image)
        logger.info(f"[ + ] OSD output: {osd_output}")
        rotate_value = self._get_rotate_value(osd_output, angle)
        logger.info(f"[ + ] Rotate value: {rotate_value}")

        # Perform image rotation
        final_rotated_image = imutils.rotate(rotated_image, int(rotate_value))

        # Defines the final result
        data = {
            "angles_for_rotation": [angle, rotate_value],
            "rotated_img_base64": self._image_to_base64(final_rotated_image),
        }

        return data

    def _get_rotate_value(self, osd_output, angle):
        field = "Orientation in degrees" if angle >= 0 else "Rotate"

        for line in osd_output.split("\n"):
            if field in line:
                return int(line.split(":")[-1])
        return 0

    def _image_to_base64(self, image_cv2):
        _, buffer = cv2.imencode(".jpg", image_cv2)
        image_base64 = base64.b64encode(buffer).decode("utf-8")
        return image_base64
