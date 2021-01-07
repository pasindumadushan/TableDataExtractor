import sys
import cv2
import numpy as np
from math import atan2, degrees
import matplotlib.pyplot as plt
import imutils
from PIL import Image, ImageOps, ImageDraw
from scipy.ndimage import morphology, label
from Boxes import boxes

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:/nsbm pasindu/Sem8/CGV/Project/Course work/textrecognitionproject-286815-953b78fd8b00.json"
from google.cloud import vision
import io

try:
    from PIL import Image
except ImportError:
    import Image

dir = "D:\\nsbm pasindu\\Sem8\\CGV\\Project\\Course work\\"

def rotate(vhPath, file):

    orig = Image.open(vhPath, "r")
    im, box = boxes(orig,)

    img = Image.open(file, "r")
    visual = img.convert('RGB')
    draw = ImageDraw.Draw(visual)


    countSignature = 0
    w, h = 5, 20;
    AttendentSheet = [[0 for x in range(w)] for y in range(h)]
    arrRowCount = 0
    arrColCount = 0
    previousCol = 0
    SignMinWidth = 0
    SignMaxWidth = 0
    SignMinHeight = 0
    SignMaxHeight = 0
    AngleX1 = 0
    AngleY1 = 0
    AngleX2 = 0
    AngleY2 = 0
    i = 0
    j = 0
    for b, centroid in box:
        draw.line(b + [b[0]], fill='green')
        cx, cy = centroid
        draw.ellipse((cx - 2, cy - 2, cx + 2, cy + 2), fill='red')
        x1, y1 = b[0]
        x2, y2 = b[1]
        x3, y3 = b[2]
        x4, y4 = b[3]



        if x3 - x1 <= 1000:

            img3 = img.crop((x1, y1, x3, y3))
            path = dir+"segments\\" + str((x1, y1, x3, y3)) + " aa.jpg"
            img3.save(path)

            client = vision.ImageAnnotatorClient()
            with io.open(path, 'rb') as image_file:
                content = image_file.read()

            image = vision.types.Image(content=content)
            response = client.text_detection(image=image)
            texts = response.text_annotations

            if texts:
                texts[0].description = texts[0].description.rstrip('\n')

                if texts[0].description == "Student Name":
                    #print("Student Name coordinate", x1,y1," - ", x2,y2," - ", x3,y3," - ", x4,y4,)
                    AngleX1 = x4
                    AngleY1 = y4

                if texts[0].description == "Signature":
                    AngleX2 = x4
                    AngleY2 = y4

                if AngleX1 != 0 and AngleX2 !=0:
                    break

            if response.error.message:
                raise Exception(
                    '{}\nFor more info on error messages, check: '
                    'https://cloud.google.com/apis/design/errors'.format(response.error.message))

    angle = degrees(atan2(AngleY1-AngleY2,AngleX2-AngleX1))

    img = cv2.imread(file)
    img = imutils.rotate(img, angle=360 - angle)
    cv2.imwrite(dir+"rotated.png",img)

    vhimg = cv2.imread(vhPath)
    vhimg = imutils.rotate(vhimg, angle=360 - angle)
    cv2.imwrite(dir+"img_vh.jpg", vhimg)