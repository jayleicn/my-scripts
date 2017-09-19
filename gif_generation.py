# GIF generation from multuple images with imageio
# https://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python

import imageio

filenames = []
for i in range(12):
    f_str = "dolly_zoom_%02d.png" % i
    filenames.append(f_str)
images = []
for filename in filenames:
    images.append(imageio.imread(filename))
    
imageio.mimsave('dolly_zoom.gif', images)
