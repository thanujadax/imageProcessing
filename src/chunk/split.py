'''
Created on Feb 12, 2016

@author: thanuja
'''

from scipy import ndimage

def simpleSplit(inputImageMat,outputSavePath,tileW,tileH,paddingPix):
    
    '''
    Input parameters:
    inputImageMat - input image as a matrix (numpy 2D array)
    tileW - tile width (#pix)
    tileH - tile height (#pix)
    paddingPix - number of pixels added to the border from the adjoining tile
    
    Output:
    output tiles are saved in the outputSavePath with file names inputFileName_tile_r000001_c000001.png
    
    '''
    
    
