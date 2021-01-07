import sys
import cv2
import numpy as np
from math import atan2, degrees
import matplotlib.pyplot as plt
import imutils
from PIL import Image, ImageOps, ImageDraw
from scipy.ndimage import morphology, label
from SQLquery import insertRecord
from Boxes import boxes
from Rotate import rotate
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "textrecognitionproject-286815-953b78fd8b00.json"
from google.cloud import vision
import io

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import re

dir = "D:\\nsbm pasindu\\Sem8\\CGV\\Project\\Course work\\"
dirSegments = "D:\\nsbm pasindu\\Sem8\\CGV\\Project\\Course work\\segments\\"

file = dir+'\\5.jpeg'
img = cv2.imread(file,0)

# thresholding the image to a binary image
thresh, img_bin = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# inverting the image
img_bin = 255 - img_bin
cv2.imwrite(dir+'cv_inverted.png', img_bin)
# Plotting the image to see the output
#plotting = plt.imshow(img_bin, cmap='gray')
plt.show()

# countcol(width) of kernel as 100th of total width
kernel_len = np.array(img).shape[1] // 100
# Defining a vertical kernel to detect all vertical lines of image
ver_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_len))
# Defining a horizontal kernel to detect all horizontal lines of image
hor_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_len, 1))
# A kernel of 2x2
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))

# Use vertical kernel to detect and save the vertical lines in a jpg
image_1 = cv2.erode(img_bin, ver_kernel, iterations=3)
vertical_lines = cv2.dilate(image_1, ver_kernel, iterations=3)
cv2.imwrite(dir+"vertical.jpg", vertical_lines)
# Plot the generated image
#plotting = plt.imshow(image_1, cmap='gray')
#plt.show()

# Use horizontal kernel to detect and save the horizontal lines in a jpg
image_2 = cv2.erode(img_bin, hor_kernel, iterations=3)
horizontal_lines = cv2.dilate(image_2, hor_kernel, iterations=3)
cv2.imwrite(dir+"horizontal.jpg", horizontal_lines)
# Plot the generated image
#plotting = plt.imshow(image_2, cmap='gray')
#plt.show()

# Combine horizontal and vertical lines in a new third image, with both having same weight.
img_vh = cv2.addWeighted(vertical_lines, 0.5, horizontal_lines, 0.5, 0.0)
# Eroding and thesholding the image
img_vh = cv2.erode(~img_vh, kernel, iterations=2)
thresh, img_vh = cv2.threshold(img_vh, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imwrite(dir+"img_vh.jpg", img_vh)
bitxor = cv2.bitwise_xor(img, img_vh)
bitnot = cv2.bitwise_not(bitxor)
# Plotting the generated image
#plotting = plt.imshow(bitnot, cmap='gray')
#plt.show()

rotate(dir+"img_vh.jpg", file)

file = dir+'rotated.png'
img = cv2.imread(file,0)

orig = Image.open(dir+"img_vh.jpg")
im, box = boxes(orig)

img = Image.open(file)
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
        path = dirSegments + str((x1, y1, x3, y3)) + ".jpg"
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
                AngleX1 = x4
                AngleY1 = y4

            if texts[0].description == "No":
                countSignature = countSignature + 1

            if texts[0].description == "Signature":
                SignMinWidth = x1
                SignMaxWidth = x3
                AngleX2 = x4
                AngleY2 = y4

            if countSignature == 1:
                previousCol = arrColCount

                if (re.compile('[ABCDEFGHIJKLMN]').search(format(texts[0].description)) != None and len(texts[0].description) >= 6 and arrRowCount != 0):
                    arrColCount = 1
                    SignMinHeight = y1
                    SignMaxHeight = y3
                    #Sign Crop
                    img3 = img.crop((SignMinWidth, SignMinHeight, SignMaxWidth, SignMaxHeight))
                    path = dirSegments+"\\sign" + str(
                        (x1, y1, x3, y3)) + ".jpg"
                    img3.save(path)



                    #sign Recognition
                    # Define a range for blue color for remove signatures
                    img3 = np.array(img3)
                    hsv = cv2.cvtColor(img3, cv2.COLOR_RGB2HSV)
                    # Define a range for blue color
                    hsv_l = np.array([100, 100, 0])
                    hsv_h = np.array([240, 255, 255])

                    # Find blue pixels in the image
                    mask = cv2.inRange(hsv, hsv_l, hsv_h)
                    img3[mask > 0] = (255, 255, 255)
                    print(np.sum(img3 == 255))

                    cv2.imwrite(dir + 'SignColor identify' + str(
                        (x1, y1, x3, y3)) + ".jpg", img3)

                    if np.sum(img3 == 255) > 1500:
                        SignDetect = "true"
                    else:
                        SignDetect = "false"



                elif (re.compile('[Mrs]').search(format(texts[0].description)) != None and len(texts[0].description) <= 3 and arrRowCount != 0):
                    arrColCount = 2

                elif (re.compile('[1234567890]').search(format(texts[0].description)) != None and len(texts[0].description) >= 7 and len(texts[0].description) <= 9 and arrRowCount != 0):
                    arrColCount = 3

                elif (re.compile('[1234567890]').search(format(texts[0].description)) != None and len(texts[0].description) <= 3 and len(texts[0].description) >= 1 and arrRowCount != 0):
                    arrColCount = 4

                if arrRowCount == 0:
                    AttendentSheet[i][j] = "0"
                    j = j + 1
                    if j == 5:
                        arrRowCount = 1

                else:
                    for k in range(len(AttendentSheet)):
                        if AttendentSheet[k][arrColCount] == 0:
                            if arrColCount == 1:
                                AttendentSheet[k][0] = SignDetect
                            AttendentSheet[k][arrColCount] = format(texts[0].description)
                            arrRowCount = k
                            break


        if response.error.message:
            raise Exception(
                '{}\nFor more info on error messages, check: '
                'https://cloud.google.com/apis/design/errors'.format(response.error.message))

#remove title column
AttendentSheet = np.delete(AttendentSheet, (0), axis=0)
#Fitted to filled size
AttendentSheet = np.resize(AttendentSheet,(arrRowCount+1,5))

insertRecord(AttendentSheet)


