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
                
            
            
        