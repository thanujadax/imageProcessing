'''
Created on Apr 4, 2016

@author: thanuja
'''

from chunk import Tile

inputDirectory = '/home/thanuja/projects/RESULTS/imageSlicer/20160407'
outputDirectory = '/home/thanuja/projects/RESULTS/imageSlicer/20160401_assembled'
outputFileName = '07.png'
imgFormat = 'png'
overlap = 28

Tile.assembleTiles(outputFileName, outputDirectory, inputDirectory, imgFormat,overlap)

if __name__ == '__main__':
    pass