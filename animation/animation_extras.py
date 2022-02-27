#Sophia Cofone 2.26.22
#These are just extra imageio functions in case they are helpful. This file can be removed before merge.

import imageio as iio

def read_single(filepath,filename):
    #reading in a standard image, im is a NumPy array
    im = iio.imread(filepath+filename)
    return im

def write_single(filepath,filename,array,ext):
    #writing array to a file with specified extension
    write = iio.imwrite(filepath+filename+ext,array[:, :, 0])
    return write

if __name__ == "__main__":
    write_single('/Users/sophiacofone/Desktop/code/5010_code/assignment4/timeseries_animaiton_local/vaccines-main/img/','may1.png',read_single('/Users/sophiacofone/Desktop/code/5010_code/assignment4/timeseries_animaiton_local/vaccines-main/img/','may1.png'),'.jpg')
