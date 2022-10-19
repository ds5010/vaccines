
import imageio as iio
import os
import glob  #changes from meghDev
import time #changes from meghDev

def create_gif(filename_save):
    #This function creates a gif animation from a folder of png images
	#@@ -17,17 +15,8 @@ def create_gif(filename_save):
    #makes a list of im NumPy arrays based on a list of .png images (read from folder)
    images = list() #Changes from meghDev
    dir_name = 'img/'
    list_of_files = filter( os.path.isfile,
                        glob.glob(dir_name + '*') )

    list_of_files = sorted( list_of_files,
                        key = os.path.getmtime) 
    #to here

    #this part looks at the img directory and reads in all the files that end with .png (only going to bring in those)
    for filename in list_of_files:  #changes from meghDev        #sorted(os.listdir('img')):
        if filename[-4:] == '.png' and not filename == 'comparison.png':
            f = os.path.join('img',filename)
            im = iio.imread(f)