import os
from PIL import Image

def find_bad_imgs(base_dir, format=('.jpg', '.png', '.jpeg')):
    """ Find bad images inside a two-level directory, 
    which is a common structure for most computer vision image dataset.
    
    i.e.
    base_dir/cls1/img1.png
    base_dir/cls1/img2.png
    base_dir/cls2/img1.png
    base_dir/cls2/img2.jpg
    
    usage:
    bad_list = find_bad_imgs('/home/jielei/images/')
    """
    cls_dirs = [f for f in os.listdir(base_dir)]
    len1 = len(cls_dirs)
    
    imgs = []
    for i in xrange(len1):
        sub_dir = os.path.join(base_dir, cls_dirs[i])
        imgs_tmp = [os.path.join(sub_dir,f) for f in os.listdir(sub_dir) if f.endswith(format)]
        imgs = imgs + imgs_tmp

    err_paths = []
    for i in xrange(len(imgs)):
        try:
            Image.open(imgs[i])
        except:
            err_paths = err_paths + [imgs[i]]
    print(' %d bad images in total.\n' % len(err_paths))
    return err_paths

base_dir = '/home/jielei/data/danbooru-faces'
bad_img_paths = find_bad_imgs(base_dir)
for i in xrange(len(bad_img_paths)):
    os.remove(bad_img_paths[i])
