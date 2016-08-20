import os
import time
import shutil

def collect_data(image_ids_path, src_dir_root, dst_dir_root):
    start = time.time()
    num_not_exist = {}
    d = {}
    with open(image_ids_path) as f:
        lines = f.readlines()
    for line in lines:    
        l_1 = line.strip("\n").split("_")[0]
        l_2 = line.strip("\n").split("_")[1]
        if l_1 in d:
            d[l_1].append(l_2)
        else:
            d[l_1] = []

    for wnid in d.keys():
   
        num_not_exist[wnid] = 0
        dst_dir_sub = os.path.join(dst_dir_root, wnid)
        if not os.path.isdir(dst_dir_sub):
            os.makedirs(dst_dir_sub)
	
        src_dir_sub = os.path.join(src_dir_root,wnid)
        for image_id in d[wnid]:
            file_name = wnid + "_" + image_id + ".JPEG"
            src_file_path = os.path.join(src_dir_sub, file_name)
            dst_file_path = os.path.join(dst_dir_sub, file_name)
            if os.path.isfile(src_file_path):
                if not os.path.isfile(dst_file_path):
                    shutil.copy(src_file_path, dst_dir_sub)
            else:
                print "file %s does not exists" % src_file_path
                num_not_exist[wnid] = num_not_exist[wnid] + 1
    #print src_file_path
    #print dst_file_path
    end = time.time()
    print "Total processing time %f seconds " % (end - start)
    print "There are %d files not exist." % sum(num_not_exist.values())
    print "Processing %s done." % image_ids_path

src_1 = "/home/jielei/data/ristin_et_al_cvpr15_data/s_fine_0.1/image_ids.txt"
src_2 = "/home/jielei/data/ristin_et_al_cvpr15_data/s_fine_0.2/image_ids.txt"
src_3 = "/home/jielei/data/ristin_et_al_cvpr15_data/s_fine_0.5/image_ids.txt"
src_4 = "/home/jielei/data/ristin_et_al_cvpr15_data/s_coarse_0.1/image_ids.txt"
src_5 = "/home/jielei/data/ristin_et_al_cvpr15_data/s_coarse_0.2/image_ids.txt"
src_6 = "/home/jielei/data/ristin_et_al_cvpr15_data/s_coarse_0.5/image_ids.txt"
dst_1 = "/home/jielei/data/ristin_et_al_cvpr15_data/s_fine_0.1/data/"
dst_2 = "/home/jielei/data/ristin_et_al_cvpr15_data/s_fine_0.2/data/"
dst_3 = "/home/jielei/data/ristin_et_al_cvpr15_data/s_fine_0.5/data/"
dst_4 = "/home/jielei/data/ristin_et_al_cvpr15_data/s_coarse_0.1/data/"
dst_5 = "/home/jielei/data/ristin_et_al_cvpr15_data/s_coarse_0.2/data/"
dst_6 = "/home/jielei/data/ristin_et_al_cvpr15_data/s_coarse_0.5/data/"
ilsvrc_data_path = "/home/jielei/data/ilsvrc2010_train"

#collect_data(src_1, ilsvrc_data_path, dst_1)
collect_data(src_2, ilsvrc_data_path, dst_2)
collect_data(src_3, ilsvrc_data_path, dst_3)
collect_data(src_4, ilsvrc_data_path, dst_4)
collect_data(src_5, ilsvrc_data_path, dst_5)
collect_data(src_6, ilsvrc_data_path, dst_6)





