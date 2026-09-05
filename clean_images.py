import os
from PIL import Image

IMG_DIR = "catalog_images"
# Thresholds: adjust these if your tool photos are smaller/larger
MIN_WIDTH = 150
MIN_HEIGHT = 150

removed_count = 0
total_checked = 0

print("Scanning for junk images...")

for filename in os.listdir(IMG_DIR):
    filepath = os.path.join(IMG_DIR, filename)
    
    # Skip directories just in case
    if not os.path.isfile(filepath):
        continue
        
    total_checked += 1
    
    try:
        with Image.open(filepath) as img:
            w, h = img.size
            
        # Delete if the image is too small (icons/logos) 
        # OR if it is an extreme rectangle (like a page border or line)
        aspect_ratio = w / h
        if w < MIN_WIDTH or h < MIN_HEIGHT or aspect_ratio > 10 or aspect_ratio < 0.1:
            os.remove(filepath)
            removed_count += 1
            
    except Exception as e:
        print(f"Skipping {filename}: {e}")

print(f"Scan complete. Checked {total_checked} images.")
print(f"Deleted {removed_count} nonsense images.")