# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
from PIL import Image


def resize(img):
    im = Image.open(img)
    end_largest_size = 1920

    width, height = im.size

    #
    if (width > height):

        ratio = width / end_largest_size
        ratio_height = int(height/ratio)

        im1 = im.resize((end_largest_size,ratio_height))
        im1.save(os.path.split(img)[0]+"/res_"+os.path.split(img)[1])


    if (width < height):

        ratio = height / end_largest_size
        ratio_width = int(width/ratio)

        im1 = im.resize((ratio_width,end_largest_size))

        im1.save(os.path.split(img)[0]+"/res_"+os.path.split(img)[1])
    
    if (width == height):
        im1 = im.resize((end_largest_size,end_largest_size))
        im1.save(os.path.split(img)[0]+"/res_"+os.path.split(img)[1])
        
    #os.remove(img)