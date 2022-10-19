#Sophia Cofone 2.26.22
#https://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python
#https://imageio.readthedocs.io/en/stable/examples.html
#This is option 2 for how we could make a gif. 
#The function actually reads a folder for the images so the user would not have to change anything, but its important that the files are named correctly when they are saved/created

import imageio as iio
import os
from datetime import datetime #NEW

def create_gif(filename_save):
    """This function creates a gif animation from a folder of png images
    Parameters:
        filename_save: str, the filename to save the gif as
    """
    #makes a list of im NumPy arrays based on a list of .png images (read from folder)
    images = list()
    
    #new code below
    #created a dictionary that has datetime objects as keys and values as filenames as strings
    newsort=dict()
    for file in os.listdir('img'):
        try:
           newsort[datetime.strptime(file[:10],'%m-%d-%Y')]=file  #if filename can be interpreted as datetime object then add it to dictionary w/ key=datetime obj and value=filename
        except:
            print('')
    #sort the dictionary using sorted. Sorted returns a list, so the dict function and the items method are required to get back to the sorted dictionary
    newsort=dict(sorted(newsort.items())) #sorts the dictionary by datetime obj keys
    #end new code block, but the following for loop loops through newsort values instead of the img drive like it did before

    #this part looks at the img directory and reads in all the files that end with .png (only going to bring in those)
    for filename in newsort.values(): #loop through dictionary values, which are filenames, loops in order of keys, which have been sorted chronologically
        if filename[-4:] == '.png' and not filename == 'comparison.png': #this isn't needed anymore
            #print(filename)
            f = os.path.join('img',filename)
            im = iio.imread(f)
            images.append(im)

    #making the gif from the pngs
    iio.mimsave(filename_save,images,duration = 1)

if __name__ == "__main__":
    create_gif('img/animation.gif')
