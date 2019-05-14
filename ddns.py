# coding: utf8
# 获取指定图片的长和宽
# -*- coding: utf-8 -*-  
from PIL import Image

# -*- coding: utf-8 -*-   

import os


def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # print(root) #当前目录路径
        # print(dirs) #当前路径下所有子目录
        # print(files) #当前路径下所有非目录子文件
        fruits_size = [(92, 93), (72, 72), (560, 400), (560, 400)]
        Image_name = ['common_logo.png', 'GkylinFree.ico', 'installing_banner_2.png', 'install_banner_bg.png']
        if len(files) == 4:

            for index in range(len(Image_name)):

                if files[index] != Image_name[index]:
                    print("图片名字不正确"), files[index]
                    print("正确的名字"), Image_name[index]

            for index in range(len(fruits_size)):
                img = Image.open(root + Image_name[index])

                if fruits_size[index] != img.size:
                    print("图片尺寸不对")
                    print("错误图片:"), Image_name[index]
                    print("所给错误尺寸:"), img.size
                    print("正确的尺寸"), fruits_size[index]



        else:

            print("图片数目不对")
            print("=======")
            if len(files) > 4:
                for index in range(len(files)):
                    if (files[index] in ['common_logo.png', 'GkylinFree.ico', 'installing_banner_2.png',
                                         'install_banner_bg.png']) == False:
                        print("多余的图片"), files[index]
            else:
                for index in range(len(fruits_size)):
                    if (Image_name[index] in files) == False:
                        print("缺少的图片"), Image_name[index]


file_name(r"C:\Users\lz\Desktop\OEM\DDNS\oem_pics\\")
