#Kayne Ryan
#DS5010 Spring 2022

#gif for vax project

#adapted code from https://stackoverflow.com/questions/41228209/making-gif-from-images-using-imageio-in-python
import imageio as io
import os

def create_gif(filename_save):
    images = []
    
    for filename in sorted(os.listdir('img')):
        if filename.endswith('.png'):
            f = os.path.join('img',filename)
            images.append(io.imread(f))

    #making the gif from the pngs
    io.mimsave(filename_save,images,duration = 1)

create_gif('img/vax_effectiveness.gif')