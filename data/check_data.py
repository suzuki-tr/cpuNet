import os
import cv2


def deconvert(size, box):
    dw = size[0]
    dh = size[1]
    x = box[0]*dw
    y = box[1]*dh
    w = box[2]*dw
    h = box[3]*dh
    x1 = int(x - w/2)
    y1 = int(y - h/2)
    x2 = int(x + w/2)
    y2 = int(y + h/2)
    return (x1,y1,x2,y2)

with open('mikan_list.txt','r') as f:
    count = 0
    for line in f:
        count += 1
        jpg = line.replace('\n','')
        txt = jpg.replace('images','labels').replace('.jpg','.txt')
        if os.path.exists(jpg):
            print jpg
        else:
            print 'Error: NOT FOUND',jpg
        if os.path.exists(txt):
            print txt
        else:
            print 'Error: NOT FOUND',txt

        im = cv2.imread(jpg)
        im_width = im.shape[1]
        im_height = im.shape[0]
        print (im_width,im_height)


        with open(txt,'r') as ft:
            for anno in ft:
                values = anno.rstrip().split(' ')
                x = float(values[1])
                y = float(values[2])
                w = float(values[3])
                h = float(values[4])
                x1,y1,x2,y2 = deconvert((im_width,im_height),(x,y,w,h))

                print (' x1:{},y1:{},x2:{},x2:{}'.format(x1,y1,x2,y2))
                cv2.rectangle(im, (x1,y1), (x2,y2), (0,0,255),4);
        cv2.imshow('img',im)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        if count > 17:
            break

