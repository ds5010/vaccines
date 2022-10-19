#Sophia Cofone 2.26.22
#https://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python
#https://imageio.readthedocs.io/en/stable/examples.html
#This is option 2 for how we could make a gif. 
#The function actually reads a folder for the images so the user would not have to change anything, but its important that the files are named correctly when they are saved/created

import imageio as iio
import os
import numpy as np

def create_gif(filename_save):
    """This function creates a gif animation from a folder of png images
    Parameters:
        filename_save: str, the filename to save the gif as
    """
    #makes a list of im NumPy arrays based on a list of .png images (read from folder)
    images = list()

    #changes to ensure propper order of figures in gif
    filenames=sorted(os.listdir('img'))
    international_dates=[file[-8:-4]+'-'+file[0:-9] for file in filenames]
    idxs=np.argsort(international_dates)
    sorted_filenames=np.array(filenames)[idxs]

    #this part looks at the img directory and reads in all the files that end with .png (only going to bring in those)
    for filename in sorted_filenames:
        if filename[-4:] == '.png' and not filename == 'comparison.png':
            f = os.path.join('img',filename)
            im = iio.imread(f)
            images.append(im)

    #making the gif from the pngs
    iio.mimsave(filename_save,images,duration = 1)

if __name__ == "__main__":
    create_gif('img/animation.gif')
