'''
Created on Dec 9, 2015

@author: thanuja
'''

import Image
from PIL import ImageEnhance

inputImageFileName = "/home/thanuja/projects/data/ssSEM_dataset/tinyTiles/80/s108/Tile_r1-c1_Sample108_section_01_tinyTile_row01_col01.png"

# open image
im = Image.open(inputImageFileName)
im.show()

# change contrast. Contrast factor ranges from 0 (solid gray image) to 1 (original image)
contrastEnhancer = ImageEnhance.Contrast(im)
contrastFactor = 0.8
contrastEnhancer.enhance(contrastFactor).show("Contrast %f" % contrastFactor)
#im.show()


if __name__ == '__main__':
    pass