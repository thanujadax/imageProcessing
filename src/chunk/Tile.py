'''
Created on Mar 22, 2016

@author: thanuja
'''

import os
from math import sqrt, ceil, floor
from PIL import Image

from common import fileNameOps
from common import fileOps

class Tile(object):
    '''
    Tile
    '''
    def __init__(self, image,number,position,coords,fileName=None):
        '''
        Constructor
        '''
        self.image = image
        self.number = number
        self.position = position
        self.coords = coords
        self.fieName = fileName
        
    @property
    def row(self):
        return self.position[0]
    
    @property
    def column(self):
        return self.position[1]
    
    @property
    def basename(self):
        """ extract the base file name without the path and extension """
        return fileNameOps.getFileBaseName(self)
    
    def generateFileName(self,prefix='tile',
                         ext='png'):
        """ create file name for this tile """
        fileName = prefix + '_{col:05d}_{row:05d}.{ext}'.format(col=self.column, row=self.row, ext=ext)
        return fileName 
    
    def save(self,outputDirectory=os.getcwd(),fileName=None, ext='png'):
        if not fileName:
            fileName = self.generateFileName(ext=ext)
        fullFileName = os.path.join(outputDirectory,fileName)
        self.image.save(fullFileName,ext)
        self.fileName = fullFileName
        
    def __repr__(self):
        """ show tile number. if saved to disk show file name"""
        if self.fileName:
            return '<Tile #{} - {}>'.format(self.number, os.path.basename(self.fileName))
        return '<Tile #{}>'.format(self.number)    
                
def calcColumnsRows(n):
    """
    calculate the number of columns and rows to divide the an image into n parts
    Return a tuple of integers in the format (numColumns,numRows)
    TODO: ???
    """
    numColumns = int(ceil(sqrt(n)))
    numRows = int(ceil(n / float(numColumns)))
    return (numColumns,numRows)

def getCombinedSize(tiles):
    """
    Calculate combined size of tiles
    """
    columns, rows = calcColumnsRows(len(tiles))
    tileSize = tiles[0].size
    return (tileSize[0]*columns, tileSize[1]*rows)
    

def join(tiles,listOfCoords,imMode):
    """
    @param 
    tiles - tuple of Image instances
    listOfPositions - columnInd,rowInd tuples for each tile parsed from the file names
    imMode - imageMode (PIL):
        L : 8-bit pixels black and white
        RGB : 3x8-bit pixels, true color
        RGBA : 4x8-bit pixels, true color with transparency mask
        I : 32-bit signed integer pixels
        F : 32 bit floating point pixels
    @return: Image instance
    """
    im = Image.new(imMode, getCombinedSize(tiles), None)
    # columns,rows = calcColumnsRows(len(tiles))
    for (tile,coord) in zip(tiles,listOfCoords):
        # im.paste(tile.image, tile.coords) 
        im.paste(tile, coord)
    return im

def saveTile(tiles, prefix='', outputDirectory=os.getcwd(), imgFormat='png'):
    """
    Return: tuple of :class:'Tile' instances
    """
    for tile in tiles:
        tile.save(outputDirectory=outputDirectory,fileName=tile.generateFileName(prefix=prefix,
                                                 ext=imgFormat))
    return tuple(tiles) 
        
def sliceImage(fileName, numberOfTiles,save=True,prefix='',outputDirectory=os.getcwd(),imgFormat='png',overlap=0):
    """
    Split an image into a specified number of tiles
    Inputs:
    fileName: image to be split into tiles
    Return: 
    Tuple of :class:'Tile' instances
    """
    im = Image.open(fileName)
    # validate image?
    
    imWidth, imHeight = im.size
    columns, rows = calcColumnsRows(numberOfTiles)
    extras = (columns*rows) - numberOfTiles 
    tileWidth, tileHeight = int(floor(imWidth/columns)), int(floor(imHeight/rows))
    
    tiles = []
    i = 1
    for posY in range(0, imHeight - rows, tileHeight):
        for posX in range(0, imWidth-columns, tileWidth):
            area = (posX,posY, posX+tileWidth, posY+tileHeight)
            image = im.crop(area)
            position = (int(floor(posX/tileWidth))+1, int(floor(posY/tileHeight))+1)
            coords = (posX,posY)
            tile = Tile(image,i,position,coords)
            tiles.append(tile)
            i += 1
    if save:
        saveTile(tiles, prefix=prefix, outputDirectory=outputDirectory, imgFormat=imgFormat)
    
def assembleTiles(outputFileName,outputDirectory,inputDirectory,imgFormat):
    """
    Assembles the tiles in the inputDirectory into one composite image
    and saves in the outputDirectory
    """
    tiles = fileOps.openImages(inputDirectory)
    # tiles contain a tuple of the image tiles inside the inputDirectory
    listOfFileNames = fileNameOps.getListOfFileNames(inputDirectory)
    tileSize = tiles[0].size
    listOfCoords = fileNameOps.getTileCoordsFromNames(listOfFileNames,tileSize)
    image = join(tiles=tiles,listOfCoords=listOfCoords, imMode='L')
    fullFileName = os.path.join(outputDirectory,outputFileName)
    image.save(fp=fullFileName, format=imgFormat)

                    

        