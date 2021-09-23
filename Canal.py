# -------------------------- Canal Transformation -------------------------- #


# Import libraries
import numpy as np
from skimage.color import rgb2xyz

def Canal(im,choix):
    """ This function takes as input the image 'im' and a caracter 'choix'
        to choose the canal to which the image will be transformed.  """

    # Canals of RGB color space
    if choix=='R' :
        return(im[:,:,0])
    if choix=='G' :
        return(im[:,:,1])
    if choix=='B' :
        return(im[:,:,2])
    
    # Canals of HSI color space
    if choix=='H' :
        H=np.zeros((im.shape[0],im.shape[1]))
        for i in range(im.shape[0]):
            for j in range(im.shape[1]):
                w=np.arccos((im[i,j,0]-1/2*(im[i,j,1]+im[i,j,2])) / np.sqrt((im[i,j,0]-im[i,j,1])**2+(im[i,j,0]-im[i,j,2])*(im[i,j,1]-im[i,j,2])))

                if im[i,j,1]> im[i,j,2] :
                    H[i,j]= w
                else :
                    H[i,j]= 2*np.pi - w
        return(H)
    if choix=='S' :
        return(1-(3*np.minimum(np.minimum(im[:,:,0],im[:,:,1]),im[:,:,2]))/(im[:,:,0]+im[:,:,1]+im[:,:,2]))
    if choix=='I' :
        return((im[:,:,0]+im[:,:,1]+im[:,:,2])/3)


    # Canals of XYZ color space
    if choix == 'X':
        return(rgb2xyz(im)[:,:,0])
    if choix=='Y':
        return(rgb2xyz(im)[:,:,1])
    if choix == 'Z':
        return(rgb2xyz(im)[:,:,2])   
