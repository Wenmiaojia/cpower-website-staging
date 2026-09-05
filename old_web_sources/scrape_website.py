import os
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "http://www.cpowerco.com/ProductDetail.aspx?id="
SITE_ROOT = "http://www.cpowerco.com/"
OUTPUT_CSV = "cpower_website_scrape.csv"
IMG_DIR = "web_ready_images"

# Start with our known test batch
START_ID = 1
END_ID = 5000

os.makedirs(IMG_DIR, exist_ok=True)
scraped_data = []

# FULL HEADERS: Disguises the script and prevents the ASP.NET language translation crash
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8",
    "Referer": "http://www.cpowerco.com/"
}

# 1. Establish the session
session = requests.Session()
session.headers.update(headers)

print("Initializing session cookies...")
try:
    session.get(SITE_ROOT, timeout=15)
    print("Homepage loaded. Waiting 2 seconds for server to register session...")
    time.sleep(2) # CRITICAL: Gives the server time to log the ASP.NET_SessionId
except Exception as e:
    print(f"Failed to load homepage: {e}")

print(f"\nStarting scrape from ID {START_ID} to {END_ID}...")

for prod_id in range(START_ID, END_ID + 1):
    url = f"{BASE_URL}{prod_id}"
    print(f"Checking ID {prod_id}...", end=" ", flush=True)
    
    try:
        response = session.get(url, timeout=15)
        
        if response.status_code != 200:
            print(f"Failed (Status {response.status_code})")
            continue
            
        soup = BeautifulSoup(response.content, "html.parser")
        
        # 2. Target the exact main content block we found in the diagnostics
        main_div = soup.find("div", class_="dir_main")
        if not main_div:
            print("Failed (No product content on this page)")
            continue
            
        # Extract text and split it cleanly
        raw_text = main_div.get_text(separator=" | ", strip=True)
        
        # 3. The title sits right before the "Time：" stamp
        if " | Time：" in raw_text:
            title_text = raw_text.split(" | Time：")[0]
        else:
            title_text = raw_text.split(" | ")[0]
            
        # Ignore dead pages that throw the null reference string in the body
        if not title_text or "未将对象引用" in title_text:
            print("Failed (Dead page)")
            continue
            
        # 4. Find the actual product image (ignoring UI icons)
        images = main_div.find_all("img")
        img_filename = ""
        
        for img in images:
            img_src = img.get("src", "")
            if "UploadFile" in img_src or "kindeditor" in img_src:
                img_url = urljoin(SITE_ROOT, img_src)
                img_ext = img_url.split('.')[-1].split('?')[0]
                img_filename = f"sku_{prod_id}.{img_ext}"
                img_path = os.path.join(IMG_DIR, img_filename)
                
                # Download the image
                img_data = session.get(img_url).content
                with open(img_path, "wb") as f:
                    f.write(img_data)
                break # Stop after getting the first actual tool photo
                
        # 5. Log it to the database list
        scraped_data.append({
            "product_id": prod_id,
            "sku_title": title_text,
            "description": raw_text,
            "image_file": img_filename,
            "url": url
        })
        
        print(f"SUCCESS: '{title_text}'")
        
    except requests.exceptions.Timeout:
        print("Failed (Server took too long to respond)")
    except Exception as e:
        print(f"Error: {e}")
        
    time.sleep(1.5) # Prevent overloading the server

# Save everything cleanly to CSV
if scraped_data:
    df = pd.DataFrame(scraped_data)
    df.to_csv(OUTPUT_CSV, index=False)
    print(f"\nBatch complete! Data saved to {OUTPUT_CSV} and images in /{IMG_DIR}")
else:
    print("\nBatch complete, but no valid products were found to save.")