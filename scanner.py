import os

base_dir = r"E:\cpower\updatePhotos"

print(f"Scanning directory: {base_dir}\n")

if not os.path.exists(base_dir):
    print("Folder not found. Make sure the path is correct.")
else:
    for root, dirs, files in os.walk(base_dir):
        # Get the current folder name
        folder_name = os.path.basename(root)
        
        # We only want to print if there are actual files or if it's the main folder
        print(f"📁 [{folder_name}]")
        
        for f in files:
            print(f"   - {f}")
        print("-" * 40)