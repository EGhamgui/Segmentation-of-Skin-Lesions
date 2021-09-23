#--------------------------Morphological------------------------#

## Import Libraries
import numpy as np
import scipy 

## The function 
def Morphological(im):
    
    """ This function is the morphological filling operation on
    the binary image. It takes an image as input and returns a
    filled image"""
    # Make a copy of the image to inverse its values
    im1 = np.copy(im)
    im1[im==0]=1
    im1[im==1]=0
    
    # Perform the morphological filling
    res = scipy.ndimage.morphology.binary_fill_holes(im1)
    
    # Re-inverse the image 
    res1 = np.copy(res)
    res1[res==0]=1
    res1[res==1]=0
    
    return(res1)
