'''
Created on Mar 22, 2016

@author: thanuja
'''

import os
from PIL import Image

def openImages(inputDirectory):
    """ Open all the images inside the directory and return a tuple containing these images """
    return [Image.open(os.path.join(inputDirectory,imageFile)) for imageFile in os.listdir(inputDirectory)]
    