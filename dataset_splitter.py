import os
import shutil
import random
from dotenv import dotenv_values
from tqdm import tqdm

# Load the environment variables from the .env file
env_vars = dotenv_values(".env")

# Set the path to the dataset directory
dataset_dir = env_vars["DATASET_DIR"]

# Set the paths to the train, test, and validation directories
train_dir = os.path.join(dataset_dir, "train")
test_dir = os.path.join(dataset_dir, "test")
validation_dir = os.path.join(dataset_dir, "validation")

# Set the split ratios
train_ratio = 0.7  # 70% for training
test_ratio = 0.2   # 20% for testing
validation_ratio = 0.1  # 10% for validation

# Get the list of class directories in the dataset directory
class_dirs = [d for d in os.listdir(dataset_dir) if os.path.isdir(os.path.join(dataset_dir, d))]

# Create the train, test, and validation directories if they don't exist
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)
os.makedirs(validation_dir, exist_ok=True)

# Iterate over each class directory
for class_dir in tqdm(class_dirs):
    # Create subdirectories for the class in train, test, and validation directories
    train_class_dir = os.path.join(train_dir, class_dir)
    test_class_dir = os.path.join(test_dir, class_dir)
    validation_class_dir = os.path.join(validation_dir, class_dir)
    
    os.makedirs(train_class_dir, exist_ok=True)
    os.makedirs(test_class_dir, exist_ok=True)
    os.makedirs(validation_class_dir, exist_ok=True)

    # Set the path to the class directory
    class_path = os.path.join(dataset_dir, class_dir)

    # Get the list of files in the class directory
    file_list = os.listdir(class_path)

    # Shuffle the file list randomly
    random.shuffle(file_list)

    # Calculate the split indices
    train_split = int(train_ratio * len(file_list))
    test_split = int((train_ratio + test_ratio) * len(file_list))

    # Split the class dataset and move the files to their respective directories
    for i, file_name in tqdm(enumerate(file_list)):
        src_path = os.path.join(class_path, file_name)

        if i < train_split:
            dst_path = os.path.join(train_class_dir, file_name)
        elif i < test_split:
            dst_path = os.path.join(test_class_dir, file_name)
        else:
            dst_path = os.path.join(validation_class_dir, file_name)

        # Move the file to the destination directory
        shutil.move(src_path, dst_path)