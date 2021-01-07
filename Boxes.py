import sys
import cv2
import numpy as np
from math import atan2, degrees
import matplotlib.pyplot as plt
import imutils
from PIL import Image, ImageOps, ImageDraw
from scipy.ndimage import morphology, label



import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:/nsbm pasindu/Sem8/CGV/Project/Course work/textrecognitionproject-286815-953b78fd8b00.json"
from google.cloud import vision
import io

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import re

def boxes(img_vh):
    img2 = ImageOps.grayscale(img_vh)
    im = np.array(img2)

    # Inner morphological gradient.
    im = morphology.grey_dilation(im, (3, 3)) - im

    # Binarize.
    mean, std = im.mean(), im.std()
    t = mean + std
    im[im < t] = 0
    im[im >= t] = 1

    # Connected components.
    lbl, numcc = label(im)
    # Size threshold.
    min_size = 200 # pixels
    box = []
    for i in range(1, numcc + 1):
        py, px = np.nonzero(lbl == i)
        if len(py) < min_size:
            im[lbl == i] = 0
            continue

        xmin, xmax, ymin, ymax = px.min(), px.max(), py.min(), py.max()
        # Four corners and centroid.
        box.append([
            [(xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax)],
            (np.mean(px), np.mean(py))])

    return im.astype(np.uint8) * 255, box
