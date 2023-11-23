import numpy as np
import cv2
from utils import *
import itertools

fpath="./lena.png"

# grayscale image
img = cv2.imread(fpath, cv2.IMREAD_GRAYSCALE)
shape = img.shape
img = np.float32(img)
block_size = 8

# Calculate the number of blocks in height and width
nbh = shape[0] // block_size
nbw = shape[1] // block_size

# Quantization Matrix 
QUANTIZATION_MAT = np.array([[16,11,10,16,24,40,51,61],
                             [12,12,14,19,26,58,60,55],
                             [14,13,16,24,40,57,69,56 ],
                             [14,17,22,29,51,87,80,62],
                             [18,22,37,56,68,109,103,77],
                             [24,35,55,64,81,104,113,92],
                             [49,64,78,87,103,121,120,101],
                             [72,92,95,98,112,100,103,99]])

# Split into 8x8 pixels blocks
img_blocks = [img[j:j + 8, i:i + 8]
                for (j, i) in itertools.product(range(0, shape[0], 8),
                                                range(0, shape[1], 8))]

# DCT transform on every 8x8 block
dct_blocks = [cv2.dct(img_block) for img_block in img_blocks]

# Initialize the lists
quantized_dct_blocks = []
encoded_blocks = []

for block in dct_blocks:
    # Quantize the DCT coefficients
    block = np.divide(block, QUANTIZATION_MAT) 
    quantized_dct_blocks.append(block)
    
    # Perform Zigzag scan and RLE encoding
    zigzag_scanned_block = zigzag(block)
    encoded_block = RLE_encode(zigzag_scanned_block)
    encoded_blocks.append(encoded_block)

# Initialize an array for the decoded blocks
decoded_blocks = np.zeros(img.shape)

# Decode and reconstruct the image
for i in range(nbh):
    for j in range(nbw):
        # Get the RLE-encoded block
        block = encoded_blocks[i * nbw + j]
        
        # Decode the RLE-encoded block
        decoding_block = RLE_decode(block, (block_size, block_size))
        
        # Inverse Zigzag scan
        zigzag_scanned_block = inverse_zigzag(decoding_block.flatten(), block_size, block_size)
        
        # De-quantize the block using the quantization matrix
        de_quantize_block = np.multiply(zigzag_scanned_block, QUANTIZATION_MAT)   
        
        # Perform Inverse DCT transform to reconstruct the block
        decoded_blocks[i*8:(i+1)*8, j*8:(j+1)*8] = cv2.idct(de_quantize_block) 

cv2.imwrite("compressed_image.png",np.uint8(decoded_blocks))
print(get_size("compressed_image.png"))
print(get_size("lena.png"))

