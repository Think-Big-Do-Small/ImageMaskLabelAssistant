
# test_draw_polygon_json.py 
import os 
import cv2 
import json 
import numpy as np 


pic_dir = 'test2.png' 
img = cv2.imread(pic_dir) 

pic_name = "".join(pic_dir.split('.')[:-1])

json_dir = pic_name + '_label.json' 
#json_dir = './test2_label.json'

fp = open(json_dir, 'r') 
pic_label_dict = json.load(fp) 
fp.close() 


FINAL_LINE_COLOR_WHITE = (255, 255, 255)
FINAL_LINE_COLOR_BLACK = (0, 0, 0)

keys = pic_label_dict.keys() 
ind = 0 

for key in keys: 
    img_copy = img.copy() 
    points = pic_label_dict[key] 
    if (len(points) > 0):
        cv2.fillPoly(img_copy, np.array([points]), FINAL_LINE_COLOR_BLACK)
    cv2.imwrite(f'./test_000{ind}.png', img_copy) 
    ind += 1 

    # seg 
    seg = cv2.bitwise_xor(img, img_copy) 
    cv2.imwrite(f'./seg_000{ind}.png', seg) 

    # mask 
    mask = np.zeros(img.shape, np.uint8) 
    if (len(points) > 0):
        cv2.fillPoly(mask, np.array([points]), FINAL_LINE_COLOR_WHITE)
    cv2.imwrite(f'./mask_000{ind}.png', mask) 


