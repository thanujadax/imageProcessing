'''
Created on Mar 22, 2016

@author: thanuja

File name string operations
'''

import os

def getFileBaseName(fileName):
    """ Return the name of the file without the path and extension"""
    return os.path.splitext(os.path.basename(fileName))[0]

def getColumnsRows(fileNames):
    """ Extract the number of rows and columns using the fileNames"""
    tiles = [];
    for fileName in fileNames:
        row, column = os.path.splitext(fileName)[0][-11:].split('_')
        tiles.append(int(row), int(column))
        
    rows = [pos[0] for pos in tiles]; columns = [pos[1] for pos in tiles]
    numRows = max(rows); numColumns = max(columns)
    return(numColumns, numRows)

def getListOfFileNames(inputDirectory):
    """ Return a list containing the image file names inside inputDirectory"""
    return [ imageFileName for imageFileName in os.listdir(inputDirectory)]
        
def getTileCoordsFromNames(fileNames,tileSize,overlap):
    """
    When reading a set of tiles from a directory, we need the positions of the tiles to put them together into one image.
    This method parses the file names of the tiles to extract the row and column position for each tile
    returns a list of row,column tuples
    """
    listOfCoords = []
    
    tiles = [];
    for fileName in fileNames:
        row,column = os.path.splitext(fileName)[0][-11:].split('_')
        y = (int(row)-1) * (tileSize[1] - overlap)
        x = (int(column)-1) * (tileSize[0] - overlap)
        tiles.append((int(row), int(column)))
        listOfCoords.append((x,y))
        
    rows = [pos[0] for pos in tiles]; columns = [pos[1] for pos in tiles]
    numRows = max(rows); numColumns = max(columns)
    tileColumnsRows = (numColumns,numRows)
    
    return listOfCoords,tileColumnsRows 
    
         
        