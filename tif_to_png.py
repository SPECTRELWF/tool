# !/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:WeiFeng Liu
# @Time: 2021/12/9 下午6:41

import cv2
import numpy as np
import os

def tif_to_png(image_path,save_path):
    """
    :param image_path: *.tif image path
    :param save_path: *.png image path
    :return:
    """
    img = cv2.imread(image_path,3)
    # print(img)
    # print(img.dtype)
    filename = image_path.split('/')[-1].split('_')[0]
    # print(filename)
    save_path = save_path + '/' + filename + '.png'
    cv2.imwrite(save_path,img)

if __name__ == '__main__':
    root_path = r'视网膜血管数据集/training/images/'
    save_path = r'Dataset/train/image/'
    image_files = os.listdir(root_path)
    for image_file in image_files:
        tif_to_png(root_path + image_file,save_path)

