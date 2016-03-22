'''
Created on Mar 22, 2016

@author: thanuja
'''

import os

def openImages(directory):
    """ Open all the images inside the directory and return a tuple containing these images """
    return [Image.open(file) for file in os.listdir(directory)]
    