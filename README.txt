1. The project directory contains 7 files .py representing the different functions used to implement the segmentation algorithm:

	Canal.py : Color space transformation
	Pillbox_Filter.py : Noise filtering function
	Intensity_Adjustement.py : Histogram stretching function
	Histogram_Thresholding.py : Otsu's thresholding 
	CCL_RLE.py / CCL.py : two methods for Connected Component Labeling (CCL)
	Morphological.py : Filling function

2. All these functions are combined in Main.py for the test step on all provided images. The main.py uses also Filelist.py to read all data.

3. In order to evaluate the segmentation algorithm, we used multiple performance indexes defined in the file Metrics.py.

4. The notebook Projet IMA201.ipynb shows all the results.
