from feature_extraction.object_detection.detector import ObjectDetector
from rembg import remove
import cv2

class BGRemoveObjectDetector(ObjectDetector):
    def __init__(self):
        super().__init__()


    def remove_background(self, img):
        output = remove(img)
        return output

    def postprocessing(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, thresholded_image = cv2.threshold(gray_image, 10, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresholded_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        max_area = 0
        max_bbox = None
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if (w * h) <= max_area: continue
            max_area = (w * h)
            max_bbox = (x, y, w, h)
        return max_bbox


    def detect_object(self, img, extract_bbox = True):
        img_result = self.remove_background(img)
        if extract_bbox:
            (x, y, w, h) = self.postprocessing(img_result)
            img_result = img_result[y:y+h, x:x+w]
        return img_result