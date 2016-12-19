/*
 * Macro template to process multiple images in a folder
 */

//input = getDirectory("Input directory");
//output = getDirectory("Output directory");

input = "/home/thanuja/DATA/ssSEM/20161215/tiff/"
output = "/home/thanuja/DATA/ssSEM/20161215/contrastAdjusted/"

Dialog.create("File type");
Dialog.addString("File suffix: ", ".tif", 5);
Dialog.show();
suffix = Dialog.getString();

processFolder(input);

function processFolder(input) {
	print("test 1")
	list = getFileList(input);
	for (i = 0; i < list.length; i++) {
		if(File.isDirectory(input + list[i])){
			print("test!")
			processFolder("" + input + list[i]);
		}
		if(endsWith(list[i], suffix)){
			print("Processing: " + input + list[i]);
			action(list[i],input, output);
		}
	}
}

function processFile(input, output, file) {
	// do the processing here by replacing
	// the following two lines by your own code
	print("Processing: " + input + file);
	print("Saving to: " + output);
}

function action(fileName,inputPath,outputPath) {

open(inputPath+fileName);

blocksize = 127;
histogram_bins = 256;
maximum_slope = 3;
mask = "*None*";
fast = true;
process_as_composite = true;


run("Invert");
getDimensions( width, height, channels, slices, frames );
isComposite = channels > 1;
parameters =
  "blocksize=" + blocksize +
  " histogram=" + histogram_bins +
  " maximum=" + maximum_slope +
  " mask=" + mask;
if ( fast )
  parameters += " fast_(less_accurate)";
if ( isComposite && process_as_composite ) {
  parameters += " process_as_composite";
  channels = 1;
}
/*   
for ( f=1; f<=frames; f++ ) {
  Stack.setFrame( f );
  for ( s=1; s<=slices; s++ ) {
    Stack.setSlice( s );
    for ( c=1; c<=channels; c++ ) {
      Stack.setChannel( c );
      run( "Enhance Local Contrast (CLAHE)", parameters );
    }
  }
}
*/
run( "Enhance Local Contrast (CLAHE)", parameters );
saveAs("Tiff",outputPath + fileName);
close();
}