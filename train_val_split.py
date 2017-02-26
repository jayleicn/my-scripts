# @jayleicn

import os
import time
import random
from shutil import copyfile

def train_val_split(src_dir, tar_dir, nVal_cls):
    """Split a set of images into train/val

    The images are stored in folders named after their class_name, 
    which is common for most computer vision dataset.

    Parameters:
        src_dir: A string indicates the path to the source dataset to be splited.
        tar_dir: A string indicates the path to store the splited sets.
        nVal_cls: An integer, nVal_cls of images in each class will be collected into the validation set,
                  while the rest of them go to the training set.
    """
    start = time.time()
    cls_dirs = [f for f in os.listdir(src_dir)]
    for i in xrange(len(cls_dirs)):
        sub_dir = os.path.join(src_dir, cls_dirs[i])
        cur_imgs = [os.path.join(sub_dir,f) for f in os.listdir(sub_dir) if f.endswith(('.jpg', '.png'))]
        random.shuffle(cur_imgs)
        val_imgs = cur_imgs[0:nVal_cls]
        assert(len(val_imgs)==nVal_cls)
        train_imgs = cur_imgs[nVal_cls:len(cur_imgs)]

        for j in xrange(len(train_imgs)):
            tmp_path = os.path.join(tar_dir, 'train', cls_dirs[i] ,os.path.split(train_imgs[j])[1])
            if j == 0:
                try:
                    os.makedirs(os.path.split(tmp_path)[0])
                except:
                    print('Error makedirs')
            copyfile(train_imgs[j], tmp_path)

        for j in xrange(len(val_imgs)):
            tmp_path = os.path.join(tar_dir, 'val', cls_dirs[i] ,os.path.split(val_imgs[j])[1])
            if j == 0:
                try:
                    os.makedirs(os.path.split(tmp_path)[0])
                except:
                    print('Error makedirs')
            copyfile(val_imgs[j], tmp_path)
        if i % 10 == 0:
            print('Processing the %03d-th class' % i)
    t = time.time()- start
    print('Total elapsed time %.2f seconds.' % t)


src_dir = '/home/jielei/data/danbooru-faces'
tar_dir = '/home/jielei/data/danbooru-faces-classification'
nVal_cls = 100

train_val_split(src_dir, tar_dir, nVal_cls)
