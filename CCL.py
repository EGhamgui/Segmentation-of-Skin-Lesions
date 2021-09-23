# ------------------ Connected Component analysis ------------------ # 


import numpy as np
import operator

def CCL(im):
    """ This function takes as input a binary image, searches for all connected objects and returns
        a binary image containg only the biggest connected objects : lesion and background. """

    # Labels matrix : defines the different objects represented with the same label
    labels = np.zeros((im.shape[0]+1,im.shape[1]+2))

    # im1 : the image padded with zeros in order to calculate labels of edge pixels
    im1=np.ones((im.shape[0]+1,im.shape[1]+2))
    im1[1:,1:-1]=im


    # -------- First pass : construct labels matrix -------- #
    labels_num=0 # number of labels
    equiv_L=[] # list of labels that are equivalent i.e. corresponding to the same object 

    # Loop over the image pixels and check if the associated mask contains labels
    for i in range(1,im1.shape[0]) :
        for j in range(1,im1.shape[1]-1):
            if im1[i,j] != 1 : 
                L = [] # list of labels

                # Append labels to L in case a pixel of the mask is equal to the pixel in question
                if im1[i,j-1] == im1[i,j]:
                    L.append(labels[i,j-1])
                if im1[i-1,j-1] == im1[i,j]:
                    L.append(labels[i-1,j-1])
                if im1[i-1,j] == im1[i,j]:
                    L.append(labels[i-1,j])
                if im1[i-1,j+1] == im1[i,j]:
                    L.append(labels[i-1,j+1])

                # In case there are no labels identified, we add a new label to L
                if len(L) == 0:
                    labels_num+ = 1
                    labels[i,j] = labels_num
                else:
                # In case we find multiple labels, we assign the minimum one to the pixel in question
                # and we consider the found labels as equivalent and associate them to the same group
                    labels[i,j] = min(L)
                equiv_L.append(L)   

                
    # --------------------- second pass --------------------- #

    # Loop over the list of equivalent labels
    # Replace each label with the minimum value of its equivalents
    for l in equiv_L: 
        for i in l :
            labels[labels==i]=min(l)

    
    labels=labels[1:,1:-1]

    
    # ------------ Keep the two biggest regions ------------ #

    # Define a dictionary D that defines labels as keys and the number of associated pixels as values
    D={}
    for i in range(labels.shape[0]):
        for j in range(labels.shape[1]):
            if labels[i,j] in D.keys():
                D[labels[i,j]]+=1
            else :
                D[labels[i,j]]=1

    # Search for the two biggest regions (those with the two maximum values in dictionary D)
    Max_labels=[] # list of the two labels with biggest regions

    # First biggest region
    var=max(D.items(), key=operator.itemgetter(1))[0]
    Max_labels.append(var)
    D[var]=0

    # Second biggest region
    var=max(D.items(), key=operator.itemgetter(1))[0]
    Max_labels.append(var)
    D[var]=0

    # Loop over the image pixels, if the label pixel doesn't figure in Max_labels list assign it as background 
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            if labels[i,j] not in Max_labels:
                im[i,j]=1
    return(im)
                
   
