#Sophia Cofone 2.26.22
#https://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python
#https://imageio.readthedocs.io/en/stable/examples.html
#This is option 1 for how we could make a gif. 
# The user would have to manually change the files list to the .png images they want to make into a gif
import imageio as iio

def create_gif(files,filename_save):
    #makes a list of im NumPy arrays based on a list of .png images
    images = []
    for filename in files:
        images.append(iio.imread(filename))

    #takes a list of im NumPy arrays and makes a gif
    iio.mimsave(filename_save,images,duration = 1)

#user changes these manually
files = ['img/1_may_placeholder.png','img/2_aug_placeholder.png','img/3_nov_placeholder.png']

if __name__ == "__main__":
    create_gif(files,'img/animation.gif')
