# ----------------------- Clustering-based Histogram Thresholding ----------------------- #

# Import libraries
import numpy as np
import cv2
import matplotlib.pyplot as plt


def Otsu (im): 
    """" This function takes as input an image and returns the optimal threshold calculated using Otsu method """

    # Calculate the histogram
    histo = cv2.calcHist([im], [0], None, [256], [0, 256])

    # 'bins' : list of gey levels of the image
    bins = np.arange(0,255)
    
    # 'proba' : list of probabilities associated to grey levels
    proba = histo/histo.sum()

    # 'l' : list of inter-class variance values for each grey level t in [1..255]
    l = []

    # Loop over all grey levels and create the list l
        # We'll divide the levels into two classes according to the threshold t
        # Calculate class probability and mean value for each class
        # calculate inter-class variance for each threshold t
    for t in range(1,255):
        w1 = proba[:t+1].sum() # Probability of class 1 (under threshhold t)
        mu1 = (1/w1)*(proba[:t+1]*bins[:t+1]).sum() # Mean value of class 1
        w2 = proba[t+1:].sum() # Probability of class 2 (over threshhold t)
        mu2 = (1/w2)*(proba[t+1:]*bins[t+1:]).sum() # Mean value of class 2
        sigma_c = w1*w2*(mu1 - mu2)**2 # Inter-class variance
        l.append(sigma_c)

    # the threshold selected maximizes the inter-class variance
    th = l.index(max(l)) + 1
    
    return(th)


def Histogram_Thresholding (im):
    """" This function takes as input an image and returns the thresholded image according to Otsu method """

       # variables :
           # im : original image
           # th : Otsu's threshold
           # im1 : thresholded image
        
    im = im * 255
    im1 = im.copy()
    th = Otsu(im)
    im1[im<=th] = 0
    im1[im>th] = 1 
    
    return(im1)
