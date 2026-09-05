import fitz  # PyMuPDF
import os

pdf_path = "CATALOGUE 2023.pdf"
output_dir = "catalog_images"

# Create the output folder if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

doc = fitz.open(pdf_path)
img_count = 0

print(f"Extracting images from {pdf_path}...")

for page_num in range(len(doc)):
    page = doc[page_num]
    images = page.get_images(full=True)
    
    for img_index, img in enumerate(images):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        
        # Save the image
        image_filename = os.path.join(output_dir, f"img_p{page_num+1}_{img_index}.{image_ext}")
        with open(image_filename, "wb") as f:
            f.write(image_bytes)
            
        img_count += 1

print(f"Successfully extracted {img_count} images into the '{output_dir}' folder.")