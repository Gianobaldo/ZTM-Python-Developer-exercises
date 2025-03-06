import sys
import os
from PIL import Image

# Grab first and second argument /Pokedex and /new folder
path = sys.argv[1]
directory = sys.argv[2]

# Check if /new exists, if not create it
if not os.path.exists(directory):
    os.mkdir(directory)

# Loop through files in the path
for image in os.listdir(path):
    if image.lower().endswith('.jpg'):  # Check if the file is a .jpg
        clean_name = os.path.splitext(image)[0]
        img = Image.open(os.path.join(path, image)) 
        img.save(os.path.join(directory, f'{clean_name}.png'), 'png')
        print(f'Converted {image} to {clean_name}.png')

print("All done!")


