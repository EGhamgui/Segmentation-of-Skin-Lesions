#-----------------------------------Pillbox_Filter------------------------------------#

## Import Libraries
from scipy import signal
import numpy as np

## The function 
def pillbox(im,radius) :
    
    """" This function uses a circular averaging low-pass filter with radius equal to 
    5 to remove the artefacts present in the original image. It takes as input the 
    original image and the value of the radius and returns the filtered image """
    
    # The variables : 
        # r : the radius of the filter.
        # y,x : the two-dimensional “meshgrid”.
        # disk : the disk filter.
        # smooth : the filtered image. 
    
    r = radius
    y,x = np.ogrid[-r: r+1, -r: r+1]
    disk = x**2+y**2 <= r**2
    disk = disk.astype(float)
    smooth = signal.convolve2d(im, disk, mode='same', boundary='fill', fillvalue=0)
    return smooth