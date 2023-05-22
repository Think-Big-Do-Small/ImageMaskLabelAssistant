# ImageFormatOpStack.py

from PIL import Image, ImageQt
import cv2
import numpy as np
from PyQt5.QtGui import QImage,QPixmap


def QPixmap2Image(pix):
    # QPixmap to Image
    # pix to QImage 
    qimage = pix.toImage()
    # QImage to Image 
    dst = ImageQt.fromqimage(qimage)
    return dst

def Image2QPixmap(image):
    if image.mode == "RGB":
        image = image.convert("RGBA")
    #Image to QPixmap
    dst = ImageQt.toqpixmap(image)
    return dst


def QPixmap2CvMat(pix):
    # QPixmap to cv mat 
    image = QPixmap2Image(pix)
    dst = None 
    if image.mode == 'RGBA':
        image = np.array(image)
        dst = cv2.cvtColor(image, cv2.COLOR_RGBA2BGR)
    elif image.mode == 'RGB':
        image = np.array(image)
        dst = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    return dst

def CvMat2QPixmap(mat_image):
    # cv mat to QPixmap 
    image = cv2.cvtColor(mat_image, cv2.COLOR_BGR2RGBA)
    image = Image.fromarray(image)
    pix = Image2QPixmap(image)
    return pix



