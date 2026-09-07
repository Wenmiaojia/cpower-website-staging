import os
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin

SITE_ROOT = "http://www.cpowerco.com/"
OUTPUT_CSV = "cpower_verified_catalog.csv"
IMG_DIR = "web_ready_images"

os.makedirs(IMG_DIR, exist_ok=True)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8",
    "Referer": "http://www.cpowerco.com/"
}

session = requests.Session()
session.headers.update(headers)

print("Initializing session...")
try:
    session.get(SITE_ROOT, timeout=10)
    time.sleep(2)
except Exception as e:
    print("Failed to load homepage.")

# Helper function to prevent Windows path crashing on broken URLs
def clean_ext(url):
    ext = url.split('.')[-1].split('?')[0].lower()
    ext = ''.join(e for e in ext if e.isalnum())
    if ext not in ['jpg', 'jpeg', 'png', 'gif', 'webp']:
        return 'jpg'
    return ext

verified_products = {}

print("\n--- PHASE 1: SCANNING CATEGORIES FOR THUMBNAILS ---")
for cat_id in range(1, 50):
    url = f"http://www.cpowerco.com/Product.aspx?Id={cat_id}"
    print(f"Scanning Category {cat_id}...", end=" ", flush=True)
    
    try:
        response = session.get(url, timeout=10)
        if response.status_code != 200:
            print("Failed.")
            continue
            
        soup = BeautifulSoup(response.content, "html.parser")
        links = soup.find_all("a")
        
        found_on_page = 0
        for a in links:
            href = a.get('href', '')
            if 'ProductDetail.aspx?id=' in href:
                img = a.find('img')
                title = a.get('title') or (img.get('alt') if img else None) or a.get_text(strip=True)
                
                if img and title and len(title) > 2:
                    prod_id = href.split('id=')[-1].split('&')[0]
                    img_src = img.get('src')
                    
                    if prod_id not in verified_products:
                        verified_products[prod_id] = {
                            'product_id': prod_id,
                            'sku_title': title.strip(),
                            'image_url': urljoin(SITE_ROOT, img_src),
                            'detail_url': urljoin(SITE_ROOT, href)
                        }
                        found_on_page += 1
                        
        print(f"Found {found_on_page} verified tools.")
    except Exception as e:
        print("Error.")
        
    time.sleep(1)

print(f"\nPhase 1 Complete! Total verified tools found: {len(verified_products)}")
print("\n--- PHASE 2: DOWNLOADING THUMBNAILS, DETAIL IMAGES, AND SPECS ---")

final_data = []

for prod_id, data in verified_products.items():
    title = data['sku_title']
    img_url = data['image_url']
    detail_url = data['detail_url']
    
    print(f"Processing ID {prod_id}: '{title[:30]}...' ->", end=" ", flush=True)
    
    try:
        # 1. Download the Category Thumbnail
        thumb_ext = clean_ext(img_url)
        thumb_filename = f"sku_{prod_id}_thumb.{thumb_ext}"
        thumb_path = os.path.join(IMG_DIR, thumb_filename)
        
        if not os.path.exists(thumb_path):
            img_data = session.get(img_url, timeout=10).content
            with open(thumb_path, "wb") as f:
                f.write(img_data)
                
        # 2. Visit the Detail Page to grab specs AND the rich "in-person" image
        desc_text = title
        detail_img_filename = ""
        
        detail_resp = session.get(detail_url, timeout=10)
        if detail_resp.status_code == 200:
            dsoup = BeautifulSoup(detail_resp.content, "html.parser")
            main_div = dsoup.find("div", class_="dir_main")
            
            if main_div:
                # Specs extraction
                raw_text = main_div.get_text(separator=" | ", strip=True)
                if " | Time：" in raw_text:
                    desc_parts = raw_text.split(" | Time：")
                    if len(desc_parts) > 1:
                        desc_text = raw_text
                
                # Detail image extraction
                embedded_img = main_div.find("img")
                if embedded_img and embedded_img.get("src"):
                    embed_src = embedded_img.get("src")
                    embed_url = urljoin(SITE_ROOT, embed_src)
                    
                    embed_ext = clean_ext(embed_url)
                    detail_img_filename = f"sku_{prod_id}_detail.{embed_ext}"
                    detail_img_path = os.path.join(IMG_DIR, detail_img_filename)
                    
                    if not os.path.exists(detail_img_path):
                        embed_data = session.get(embed_url, timeout=10).content
                        with open(detail_img_path, "wb") as f:
                            f.write(embed_data)
                        
        # 3. Save the clean data
        final_data.append({
            "product_id": prod_id,
            "sku_title": title,
            "description": desc_text,
            "thumbnail_file": thumb_filename,
            "detail_image_file": detail_img_filename,
            "url": detail_url
        })
        print("Success!")
        
    except Exception as e:
        print(f"Failed ({e})")
        
    time.sleep(1)

if final_data:
    df = pd.DataFrame(final_data)
    df.to_csv(OUTPUT_CSV, index=False)
    print(f"\nMaster database complete! Data saved to {OUTPUT_CSV}.")
else:
    print("\nBatch complete, but no valid products were found.")