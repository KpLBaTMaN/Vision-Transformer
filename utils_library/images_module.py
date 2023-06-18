from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import random
import os
from tqdm import tqdm

def list_image_files(directory):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']  # Add more extensions if needed
    image_files = []

    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_ext = os.path.splitext(filename)[1].lower()
            if file_ext in image_extensions:
                image_files.append(filename)

    return image_files

def display_images(images_path: str, num_display: int = 5):
  plt.figure(figsize=(20,20))
  for i in range(num_display):
      file = random.choice(os.listdir(images_path))
      image_path= os.path.join(images_path, file)
      img=mpimg.imread(image_path)
      ax=plt.subplot(1,5,i+1)
      ax.title.set_text(file)
      plt.imshow(img)


# find the different sizes of images

from PIL import Image
from collections import defaultdict

def analysis_of_image_sizes(images_path) -> dict:

    # Define a dictionary to store the width and height ranges
    ranges = defaultdict(int)

    # List of image file paths
    image_files = list_image_files(images_path)

    pbar = tqdm(image_files)
    # Iterate through each image file
    for file_path in pbar:
        # Open the image
        image = Image.open(os.path.join(images_path, file_path))

        # Get the width and height of the image
        width, height = image.size

        # Increment the count for the width and height range
        ranges[(width, height)] += 1

        # Close the image
        image.close()

    # # Display the results
    # for (width, height), count in ranges.items():
    #     print(f"Image size: {width}x{height} - Count: {count}")

    return ranges
  