# !/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:WeiFeng Liu
# @Time: 2021/12/9 下午6:54
import numpy as np
import cv2
import os

def gif_to_png(image_path,save_path):
    gif = cv2.VideoCapture(image_path)
    ret,frame = gif.read()
    filename = image_path.split('/')[-1].split('_')[0]
    save_path = save_path + filename + '.png'
    cv2.imwrite(save_path,frame)
if __name__ == '__main__':
    root_path = r'视网膜血管数据集/training/label/'
    save_path = r'Dataset/train/label/'
    image_files = os.listdir(root_path)
    for image_file in image_files:
        gif_to_png(root_path + image_file,save_path)

