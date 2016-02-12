'''
Created on Feb 12, 2016

@author: thanuja
'''

from scipy import ndimage
from numpy import tile

def simpleSplit(inputImageMat,outputSavePath,maxTileR,maxTileC,paddingPix):
    
    '''
    Input parameters:
    inputImageMat - input image as a matrix (numpy 2D array)
    maxTileR - max number of rows per tile (#pix)
    maxTileC - max number of columns per tile (#pix)
    paddingPix - number of pixels added to the border from the adjoining tile
    
    Output:
    output tiles are saved in the outputSavePath with file names inputFileName_tile_r000001_c000001.png
    
    '''