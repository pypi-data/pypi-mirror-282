import cv2
import numpy as np

def read_img(img):
    if type(img) == str:
        return cv2.imread(img)
    elif type(img) == np:
        return img
    else:
        raise Exception(f'Image type is not supported')