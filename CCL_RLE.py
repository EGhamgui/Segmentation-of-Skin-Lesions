# ------------------ Connected Component analysis ------------------ # 


# Import libraries
import numpy as np
import operator

def intersection(I,J):
    """ This function takes as input two tuples of the format (start,end) and returns a
        tuple (start,end) representing the intersection interval of pixels. """
    a=max(I[0],J[0])
    b=min(I[1],J[1])
    if a<=b:
        return (a,b)
    else:
        return None


def CCL_RLE(im):
     """ This function takes as input a binary image, searches for all connected objects and returns
        a binary image containg only the biggest connected objects : lesion and background. """

    # Labels matrix : defines the different objects represented with the same label
    labels = np.zeros((im.shape[0]+1,im.shape[1]+2))

    # im1 : the image padded with zeros in order to calculate labels of edge pixels
    im1=np.ones((im.shape[0]+1,im.shape[1]+2))
    im1[1:,1:-1]=im
  
    # --------- First pass : construct labels matrix --------- #
    labels_num=0 # number of labels

    # Loop over the image pixels and check if the associated mask contains labels
    for i in range(1,im1.shape[0]) :
        for j in range(1,im1.shape[1]-1)  :
            if im1[i,j] != 1 :
                L=[] # list of labels

                # Append labels to L in case a pixel of the mask is equal to the pixel in question
                if im1[i,j-1]==im1[i,j]:
                    L.append(labels[i,j-1])
                if im1[i-1,j-1]==im1[i,j]:
                    L.append(labels[i-1,j-1])
                if im1[i-1,j]==im1[i,j]:
                    L.append(labels[i-1,j])
                if im1[i-1,j+1]==im1[i,j]:
                    L.append(labels[i-1,j+1])

                # In case there are no labels identified, we add a new label to L
                if len(L)==0:
                    labels_num+=1
                    labels[i,j]=labels_num
                else:
                # In case we find multiple labels, we assign the minimum one to the pixel in question
                    labels[i,j]=min(L)
                    
    # ----------- second pass : Run Length Encoding  ----------- #

    # This step determines the list of tuples used to determine the overlap region in the next step.
    # Each tuple defines the start and end of the object area.
    
    # L_codes is the list of all the tuples 
    L_codes = []
    for i in range(1,im1.shape[0]) :
        
        # L will contain the first and the last elements of objects for each row of the image
        L = []
        
        # Looping over each row and column in the image 
        for j in range(1,im1.shape[1]-1)  :
            
            # Insertion of the first index when the object first meets
            if (im1[i,j-1]==1) and (im1[i,j]==0):
                first=j
                
            # Insertion of the last index of the object
            if (im1[i,j]==0) and (im1[i,j+1]==1):
                L.append((first,j))
       
        # Add the tuple in the list 
        L_codes.append(L)
    
    # Overlap (Merge)
    # This step is used to find the overlapping areas. 
    
    # Looping over each tuple
    for i in range(len(L_codes)-1):
        
        # Finding the overlapped area 
        for l1 in L_codes[i]:
            for l2 in L_codes[i+1]:
                
                # Keeping the minimum value between the two overlapped areas
                if intersection(l1,l2)!= None:
                    
                    min_label = min(labels[i,l1[0]],labels[i+1,l2[0]])
                    
                    # Changing the labels of each part with the minimum label found
                    labels[i,l1[0]:l1[1]+1] = min_label
                    labels[i+1,l2[0]:l2[1]+1] = min_label
    
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
    



                    
                    
                
   
