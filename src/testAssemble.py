'''
Created on Apr 4, 2016

@author: thanuja
'''

from chunk import Tile

inputDirectory = '/home/thanuja/projects/RESULTS/imageSlicer/20160401'
outputDirectory = '/home/thanuja/projects/RESULTS/imageSlicer/20160401_assembled'
outputFileName = '01.png'
imgFormat = 'png'

Tile.assembleTiles(outputFileName, outputDirectory, inputDirectory, imgFormat)

if __name__ == '__main__':
    pass