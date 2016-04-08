'''
Created on Mar 22, 2016
to test the simpleSplit function
@author: thanuja
'''
from chunk import Tile

inputFileName = '/home/thanuja/projects/data/drosophilaLarva_ssTEM/isbiSegmentations/raw/test-volume0000.tif'
outputDirectory = '/home/thanuja/projects/RESULTS/imageSlicer/20160407'
# numberOfTiles = 4
save = True
prefix = 't'
imgFormat = 'png'
tileWidth = 270
tileHeight = 270
overlap = 28

Tile.sliceImage(inputFileName, tileWidth, tileHeight,save, prefix, outputDirectory, imgFormat,overlap)



if __name__ == '__main__':
    pass