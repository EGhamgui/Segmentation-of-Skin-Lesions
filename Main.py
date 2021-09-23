#-------------------------------------------------Main------------------------------------------------#

## Import Libraries
from CCL import *
from CCL_RLE import *
from Morphological import *
from Pillbox_Filter import *
from Intensity_Adjustement import *
from Histogram_Thresholding import *

## Main function 
def Main(im, labeling2=False):
    
    """ this function allows us to combine all the functions defined on an input image and it returns
    all the transformed images (the filtered image, the stretched image, the image after the thresholding,
    the labeled image and finally the filled image) """
    
    # The variables: 
        
        # radius : the radius used in the filtering step 
        # percentile1 / percentile2 : the two percentiles used in the intensity adjustement
        # labeling2 : if this is False, we use the run length encoding method otherwise we use the second method 
    
    # Noise filtering
    radius = 5
    im_filtered = pillbox(im,radius)

    # Intensity Adjustement
    percentile1 = 1
    percentale2 = 99
    im_stretched = Intensity_Adjustement(im_filtered,percentile1,percentale2)

    # Thresholding
    im_th = Histogram_Thresholding(np.float32(im_stretched))

    # CCL
    if labeling2 == False :
        
        # Run Length Encoding method 
        im_labeled = CCL_RLE(im_th)
        
    else :
        
        # Method 2
        im_labeled = CCL(im_th)

    # Holes filling
    im_filled = 1-(Morphological(im_labeled).astype(int))
    
    return [ im_filtered,im_stretched,im_th,im_labeled,im_filled ]
