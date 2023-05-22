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
    #dst.save("d:/12345XXXXXXXXXXX_pix.png")
    return dst


def QPixmap2CvMat(pix):
    # QPixmap to cv mat 
    image = QPixmap2Image(pix)
    #print ('image mode -> ', image.mode, ' , image type -> ', type(image))
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
    #image.save("d:/test_pil.png")
    pix = Image2QPixmap(image)
    #print (' image type ---> ', type(pix))
    return pix



def Cv2QImage(self, image):
    #width, height = image.shape[1], image.shape[0]
    ConvertToQtFormat = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_RGB888)
    return ConvertToQtFormat

def QImage2Cv(self, image):
    image = image.convertToFormat(QImage.Format_RGBX8888)        
    ptr = image.constBits()
    ptr.setsize(image.byteCount())
    dst = np.array(ptr, copy=True).reshape(image.height(), image.width(), 4)
    #dst = cv2.cvtColor(dst, cv2.COLOR_BGRA2BGR)
    #dst = cv2.cvtColor(dst, cv2.COLOR_BGRA2RGB)
    return dst

