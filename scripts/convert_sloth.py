# -*- coding: utf-8 -*-
import os
from os import walk
from PIL import Image
import json


def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)
    
    
"""-------------------------------------------------------------------""" 

""" Configure Paths"""   
mypath = "../data/labels/mikan_original/anno_train.json"
outpath = "../data/labels/mikan/"

cls = "mikan"
cls_id = 0

list_file = open('../data/%s_list.txt'%(cls), 'w')

jpg_name_list = []
data = json.load(open(mypath))
for an in data:
    print ('file:{}, object count:{}'.format(an['filename'],len(an['annotations'])))
    jpg_name = an['filename'].replace('mikan/','../data/images/mikan/')
    txt_outpath = jpg_name.replace('images','labels').replace('.jpg','.txt')
    #print (jpg_name)
    #print (txt_outpath)

    im=Image.open(jpg_name)
    w= int(im.size[0])
    h= int(im.size[1])
    print(w, h)

    txt_outfile = open(txt_outpath, 'w')
    
    for bbox in an['annotations']:
        xmin = bbox['x']
        ymin = bbox['y']
        xmax = bbox['x'] + bbox['width']
        ymax = bbox['y'] + bbox['height']
        b = (float(xmin), float(xmax), float(ymin), float(ymax))
        #print(b)
        bb = convert((w,h), b)
        print ('{} {} {} {} {}'.format(str(cls_id),bb[0],bb[1],bb[2],bb[3]))
        txt_outfile.write('{} {} {} {} {}\n'.format(str(cls_id),bb[0],bb[1],bb[2],bb[3]))
    txt_outfile.close()

    print ('/home/suzuki/github/yolo/cpuNet/data/images/{}/{}\n'.format(cls, os.path.basename(jpg_name)))
    list_file.write('/home/suzuki/github/yolo/cpuNet/data/images/{}/{}\n'.format(cls, os.path.basename(jpg_name)))

list_file.close()
