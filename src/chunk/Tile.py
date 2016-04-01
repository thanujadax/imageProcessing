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
                         ext='png',path=True):
        """ create file name for this tile """
        fileName = prefix + '_{col:05d}_{row:05d}.{ext}'.format(col=self.column, row=self.row, ext)
        return fileName 
    
    def save(self,directory=os.getcwd(),fileName=None, ext='png'):
        if not fileName:
            fileName = self.generateFileName(ext)
        fullFileName = os.path.join(directory,fileName)
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
    tileSize = tiles[0].image.size
    return (tileSize[0]*columns, tileSize[1]*rows)
    

def join(tiles,imMode):
    """
    @param 
    tiles - tuple of Image instances
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
    for tile in tiles:
        im.paste(tile.image, tile.coords)
    return im

def saveTile(tiles, prefix='', directory, format='png'):
    """
    Return: tuple of :class:'Tile' instances
    """
    for tile in tiles:
        tile.save(fileName=tile.generateFileName(prefix=prefix,
                                                 directory=directory,format=format))
    return tuple(tiles) 
        
def slice(fileName, numberOfTiles,save=True,prefix,outputDirectory,format='png'):
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
        saveTile(tiles, prefix=prefix, directory=outputDirectory, format=format)
    
                

        