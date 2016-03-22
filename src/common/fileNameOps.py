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
        row, column = os.path.splitext(fileName)[0][-5:].split('_')
        tiles.append(int(row), int(column))
        
    rows = [pos[0] for pos in tiles]; columns = [pos[1] for pos in tiles]
    numRows = max(rows); numColumns = max(columns)
    return(numColumns, numRows)
        
        
        