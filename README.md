# VC_HW4_EntropyCoding

**NYCU Video Compression HW4**

- Run length encoding and run length decoding
  - 8x8 block-based DCT coefficients of “lena.png.”
  - Quantize the coefficients with 16-bit for DC and 8-bit for AC.
  - Use a raster scan to visit all 8x8 blocks in these images.
  - Do the run length encoding by using a zigzag scan to visit all pixels in one block.
  - Do the run length decoding and IDCT to recover the image.

## Introduction
This Python script demonstrates image compression using the Discrete Cosine Transform (DCT) and Run-Length Encoding (RLE) techniques. 

The compression is applied to a grayscale image, and the steps include DCT transformation, quantization, zigzag scanning, RLE encoding, decoding, and inverse DCT transformation.

## Project Structure
The project includes the following files:

```main.py``` - This file contains the main execution script. 

```utils.py``` - This file contains utility functions used in the compression process.

## Dependencies
To run this project, you need to have the following libraries installed:

- NumPy
- OpenCV

## Usage
### Clone Repository
```
git clone https://github.com/ting0602/VC_HW4_EntropyCoding.git
```

### Run the Code
```
python main.py
```

- ```main.py ``` performs the following steps:

  - Reads a grayscale image.
  - Divides the image into 8x8 blocks.
  - Applies the DCT transformation to each block.
  - Quantizes the DCT coefficients using a predefined quantization matrix.
  - Performs zigzag scanning on the quantized coefficients.
  - Applies Run-Length Encoding (RLE) to the zigzag-scanned coefficients.
  - Decodes the RLE-encoded data.
  - Applies inverse zigzag scanning and de-quantization.
  - Performs inverse DCT transformation to reconstruct the image.
  - Saves the compressed image, and prints the file sizes of the original and compressed images.
 
  ### Results
- The output includes:
  - The compressed image is saved as ```compressed_image.png```.
  - Print the file sizes of the original and compressed images.
