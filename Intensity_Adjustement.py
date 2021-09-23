# --------------------------- Intensity Adjustement --------------------------- #

# Import libraries
import numpy as np
from skimage import exposure
import matplotlib.pyplot as plt
import cv2


def Intensity_Adjustement(im, p1, p2) :
    """" This function takes as input an image and two pencentiles, computes the
         stretched histogram and returns the image with adjusted intensity. """
    
    per1, per2 = np.percentile(im/255, (p1, p2))
    img_stretched = exposure.rescale_intensity(im/255, in_range = (per1, per2))

    return (img_stretched)

