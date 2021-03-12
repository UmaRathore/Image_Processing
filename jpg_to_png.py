import sys
import os
from PIL import Image

# source and destination folders from terminal

image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if folder "output_folder" exist and if not then create it

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# open each image and convert it to png format

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]

    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('done!')
