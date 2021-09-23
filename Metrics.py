#------------------------------------Metrics-----------------------------------#

## Import Libraries
import cv2
import numpy as np
from sklearn.metrics import jaccard_score
from scipy.spatial.distance import directed_hausdorff
from sklearn.metrics.cluster import adjusted_rand_score 
from sklearn.metrics import normalized_mutual_info_score

## Dice function 
def Dice (im,gt):
    
    """ This function calculates the dice coeffient which is defined as the 
    fraction of the double intersection between the segmented image and the 
    ground truth and the union of these two images """ 
    
    # The variables :
        
        # gt_b : the boolean image transformed from the ground truth 
        # im_b : the boolean image transformed from the original truth 
        # union : the union of the two previous images 
        # intersection : the intersection between the two previous images
    
    gt_b = np.asarray(gt).astype(np.bool)
    im_b = np.asarray(im).astype(np.bool)
    union = true_mask.sum() + pred_mask.sum()
    if union == 0:
        return (-1)
    intersection = np.logical_and(gt_b, im_b)
    
    return (2. * intersection.sum() / union)

## Hausdorff function 
def Hausdorff_Distance (im ,gt):
    
    """ This function calculates the hausdorff distance which is the maximum 
    distance between the two images : between the segmented image and the 
    ground truth """
    
    return(directed_hausdorff(im, gt)[0])

## Jaccard Index function 
def Jaccard_Index (im,gt):
    
    """ This function calculates the jaccard index which is defined as the 
    cardinal of the intersection between the two images( the segmented image 
    and the ground truth) divided by the cardinality of their unions """
    
    # Tha variables: 
    
        # im_v : the linear vector constrcted from the original image 
        # gt_v : the linear vector constructed from the ground truth
    
    im_v = np.ravel(im)
    gt_v = np.ravel(gt)
    
    return(jaccard_score(gt_v,im_v))

## Adjusted Rand Index function 
def Ad_Rand_Index(im,gt):
    
    """ This function calculates the Adjusted rand index which is defined as 
    the sum of the number of true positive results and the number of true negative results 
    divided by the total number of items """
    
    # Tha variables: 
    
        # im_v : the linear vector constrcted from the original image 
        # gt_v : the linear vector constructed from the ground truth
    
    im_v = np.ravel(im)
    gt_v = np.ravel(gt)
    
    return(adjusted_rand_score(BW2,BW1))

## Volumetric similarity function 
def Volumetric_Similarity (im, gt) :
    
    """ This function calculates the volumetric similarity between the segmented 
    image and the ground truth which is defined as the average conditional 
    entropy of a segmentation knowing the image of the ground truth """ 
    
     # The variables :
        
        # gt_b : the boolean image transformed from the ground truth 
        # im_b : the boolean image transformed from the original truth 
        # union : the union of the two previous images 
        # diff : the difference between the two previous images
    
    gt_b = np.asarray(gt).astype(np.bool)
    im_b = np.asarray(im).astype(np.bool)
    union = true_mask.sum() + pred_mask.sum()
    diff = pred_mask.sum() -  true_mask.sum()
    if union == 0:
        return (-1)
    
    return(1-(abs(diff / union)))

## Normalized mutual information 
def Mutual_Normalized (im,gt):
    
    """ This function calculates the normalized mutual information between the
    segmeted image and the ground truth which is defined as the information 
    between the overlapping areas of two images """
    
    # Tha variables: 
    
        # im_v : the linear vector constructed from the original image 
        # gt_v : the linear vector constructed from the ground truth
        
    im_v = np.ravel(im)
    gt_v = np.ravel(gt)
    return(normalized_mutual_info_score(gt_v,im_v))
