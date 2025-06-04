import os
import shutil
import random

# Configuration
SOURCE_DIR = "chest_xray/data/train"
DEST_DIR = "chest_xray/val"
SPLIT_RATIO = 0.15  # 15% for validation

# Make val folders
os.makedirs(DEST_DIR, exist_ok=True)
for class_name in os.listdir(SOURCE_DIR):
    class_path = os.path.join(SOURCE_DIR, class_name)
    dest_class_path = os.path.join(DEST_DIR, class_name)
    os.makedirs(dest_class_path, exist_ok=True)

    # Get list of files
    images = os.listdir(class_path)
    random.shuffle(images)
    val_count = int(len(images) * SPLIT_RATIO)

    # Move selected images to val
    for img in images[:val_count]:
        src = os.path.join(class_path, img)
        dst = os.path.join(dest_class_path, img)
        shutil.move(src, dst)

print("✅ Validation set created successfully.")
