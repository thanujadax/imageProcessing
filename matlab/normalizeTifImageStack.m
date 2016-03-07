function normalizeTifImageStack(inputTifFileName,outputTifFileName)
% read tiff stack
% normalize by making mean = 0 and SD = 1
% uses matlab functions from 'common' directory

% read image stack into array
% for each image (independently of others), center pixel intensities around
% zero
