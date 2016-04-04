'''
Created on Mar 22, 2016
to test the simpleSplit function
@author: thanuja
'''
from chunk import Tile

inputFileName = '/home/thanuja/projects/data/drosophilaLarva_ssTEM/isbiSegmentations/raw/test-volume0000.tif'
outputDirectory = '/home/thanuja/projects/RESULTS/imageSlicer/20160401'
numberOfTiles = 4
save = True
prefix = 't'
imgFormat = 'png'

Tile.sliceImage(inputFileName, numberOfTiles, save, prefix, outputDirectory, imgFormat)



if __name__ == '__main__':
    pass