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
        fruits_size = [(3541, 183), (48, 48), (561, 27), (20, 20), (593, 512), (420, 23), (561, 27), (446, 149),
                       (256, 256), (24, 24), (16, 16), (16, 16), (16, 16), (16, 16), (16, 16), (256, 256), (48, 48),
                       (148, 58), (18, 18)]
        Image_name = ['au_bg.png', 'au_icon.png', 'au_loginbutton.png', 'au_mainicon.png', 'au_msgbox.png',
                      'button.png', 'button_style.png', 'bw8dll_bg.png', 'gnLan.ico', 'login_logo.png',
                      'logo-link1.ico', 'logo-link2.ico', 'logo-link3.ico', 'logo-link4.ico', 'logo-link5.ico',
                      'logo.ico', 'uninst.ico', 'windows_1_gnwaylogo.png', 'windows_1_logo.png']
        if len(files) == 19:
            for index in range(len(Image_name)):
                if files[index] != Image_name[index]:
                    print("图片名字不正确"), files[index]
                    print("正确的名字"), Image_name[index]

            for index in range(len(fruits_size)):
                img = Image.open(root + Image_name[index])

                if fruits_size[index] != img.size:
                    print("图片尺寸不对")
                    print("错误图片:" + Image_name[index],)
                    print("所给错误尺寸:"),  print(img.size)
                    print("正确的尺寸"), print(fruits_size[index])


        else:
            print("图片数量不对")
            if len(files) > 19:
                for index in range(len(files)):
                    if (files[index] in ['au_bg.png', 'au_icon.png', 'au_loginbutton.png', 'au_mainicon.png',
                                         'au_msgbox.png', 'button.png', 'button_style.png', 'bw8dll_bg.png',
                                         'gnLan.ico', 'login_logo.png', 'logo-link1.ico', 'logo-link2.ico',
                                         'logo-link3.ico', 'logo-link4.ico', 'logo-link5.ico', 'logo.ico', 'uninst.ico',
                                         'windows_1_gnwaylogo.png', 'windows_1_logo.png']) == False:
                        print("多余的图片：" + files[index])

            else:
                for index in range(len(fruits_size)):
                    if (Image_name[index] in files) == False:
                        print("缺少的图片"), Image_name[index]

                        print("-")
file_name(r"C:\Users\lz\Desktop\OEM\TK\oem_pics\\")
