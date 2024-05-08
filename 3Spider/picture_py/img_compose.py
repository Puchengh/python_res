# pip install pillow
from PIL import Image

im = Image.open('G:/picture/居家养眼高清美女何瑞贤壁纸.jpg')
# print(im.size)

w, h = im.size
image_row = 4
image_column = 4

import os

# print(os.listdir('G:/picture').__str__())

# 所有名字
# first_element = original_list[0]
first_element = os.listdir('G:/picture')
images = first_element[1:]

for image in images:
    print(image)

new_img = Image.new('RGB', (image_column * w, image_row * h))
for y in range(image_row):
    for x in range(image_column):
        #打开要合成的图片
        opne_image  = Image.open('G:/picture/' + images[image_column * y + x])
        new_img.paste(opne_image,(x*w,y*h))

new_img.save('G:/picture/compose/new.jpg')