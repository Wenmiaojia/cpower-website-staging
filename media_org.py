import os
import shutil

source_dir = r"E:\cpower\updatePhotos"
dest_dir = r"E:\cpower\web_assets"

# Create clean destination folders
folders = ['docs', 'factory', 'fairs', 'products', 'videos']
for f in folders:
    os.makedirs(os.path.join(dest_dir, f), exist_ok=True)

print("Starting clean media transfer...\n")

factory_count = 1

for root, dirs, files in os.walk(source_dir):
    parent_folder = os.path.basename(root)
    
    for file in files:
        old_path = os.path.join(root, file)
        ext = file.split('.')[-1].lower()
        
        # 1. ISO Certificate
        if ext == 'pdf':
            new_name = "cpower_iso_9001_certificate.pdf"
            new_path = os.path.join(dest_dir, 'docs', new_name)
            
        # 2. Factory Photos (Rename WeChat and sequentialize)
        elif parent_folder == 'factoryPhotos':
            new_name = f"factory_floor_{factory_count}.{ext}"
            new_path = os.path.join(dest_dir, 'factory', new_name)
            factory_count += 1
            
        # 3. Fair Photos
        elif parent_folder == 'fairPhotos' or (parent_folder == 'videos' and ext == 'jpg'):
            # Convert "2026 spring canton fair.jpg" -> "canton_fair_2026_spring.jpg"
            clean_name = file.lower().replace(' ', '_').replace('__', '_')
            new_path = os.path.join(dest_dir, 'fairs', clean_name)
            
        # 4. Products & Videos (Fix misplaced files)
        elif parent_folder == 'photos' or parent_folder == 'videos':
            # Remove the numbers at the start (e.g., "1 New pump pliers" -> "new_pump_pliers")
            clean_name = file.lower()
            if clean_name[0].isdigit() and clean_name[1] == ' ':
                clean_name = clean_name[2:]
            clean_name = clean_name.replace(' ', '_').replace('-', '_')
            
            if ext == 'mp4':
                new_path = os.path.join(dest_dir, 'videos', clean_name)
            else:
                new_path = os.path.join(dest_dir, 'products', clean_name)
                
        else:
            continue # Skip unknowns
            
        # Copy the file
        shutil.copy2(old_path, new_path)
        print(f"Copied: {file} \n    -> {new_path}\n")

print("-" * 40)
print(f"SUCCESS! All media has been cleaned, renamed, and saved to: {dest_dir}")