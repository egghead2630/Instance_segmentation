import pycocotools._mask as mask
from pycococreatortools import pycococreatortools as cocotools
import numpy as np
import cv2
from PIL import Image
import os
import random
path = 'train/'
train_path = './train.json'
vali_path = './vali.json'


def create_bbox_seg(o, dirs):
    o.write('\"annotations\":\n[\n')
    anno_id = 0
    first = True
    img_id = 0
    for mask_dir in dirs:
        for file in os.listdir(mask_dir):
            if file[-3:] == 'png':
                if first is False:
                    o.write(',\n')
                else:
                    first = False
                f = cv2.imread(mask_dir + '/' + file, cv2.IMREAD_GRAYSCALE)
                f = f / 255
                c_info = {}
                c_info["id"] = 1
                c_info["is_crowd"] = False
                a = cocotools.create_annotation_info(anno_id, img_id,
                                                     c_info, f)
                a = str(a)
                a = a.replace("\'", "\"")
                o.write(a)
                anno_id += 1
        img_id += 1
    o.write('\n],\n')


def create_classes(o):

    o.write('\"categories\":\n')
    o.write('[\n')
    o.write('{\"id\": 1, \"name\": \"1\"}\n')
    o.write(']\n')


def create_names(o, dirs):
    id = 0
    first = True
    o.write('\"images\":\n')
    o.write('[\n')
    for image_dir in dirs:
        for file in os.listdir(image_dir):
            if file[-3:] == 'png':
                if first is False:
                    o.write(',\n')
                else:
                    first = False
                f = Image.open(image_dir + '/' + file)
                image_size = [f.width, f.height]
                file_name = image_dir + '/' + file
                info = cocotools.create_image_info(id, file_name, image_size)
                info = str(info)
                info = info.replace("\'", "\"")
                o.write(info)
                id += 1
    o.write('\n],\n')
f = open(train_path, 'w')
f2 = open(vali_path, 'w')

ps = os.listdir(path)

mask_dirs = []
image_dirs = []

for name in ps:
    if name[0] == '.':
        continue
    mask_dir = path + name + '/masks'
    mask_dirs.append(mask_dir)
    image_dir = path + name + '/images'
    image_dirs.append(image_dir)

ind = random.randint(0, (len(image_dir) - 1))

vali_mask_dirs = []
vali_mask_dirs.append(mask_dirs.pop(ind))
vali_image_dirs = []
vali_image_dirs.append(image_dirs.pop(ind))


ind = random.randint(0, (len(image_dir)-1))

vali_mask_dirs.append(mask_dirs.pop(ind))
vali_image_dirs.append(image_dirs.pop(ind))


f.write('{\n')
create_names(f, image_dirs)
create_bbox_seg(f, mask_dirs)
create_classes(f)
f.write('}\n')

f2.write('{\n')
create_names(f2, vali_image_dirs)
create_bbox_seg(f2, vali_mask_dirs)
create_classes(f2)
f2.write('}\n')

