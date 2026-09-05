import requests
from bs4 import BeautifulSoup

url_home = "http://www.cpowerco.com/"
url_product = "http://www.cpowerco.com/ProductDetail.aspx?id=90"

# Add standard browser headers and a Referer
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "http://www.cpowerco.com/"
}

# A Session holds cookies across requests
session = requests.Session()
session.headers.update(headers)

print("1. Visiting homepage to establish ASP.NET session cookies...", flush=True)
try:
    session.get(url_home, timeout=10)
except Exception as e:
    print(f"Failed to load homepage: {e}")

print(f"2. Connecting to {url_product}...", flush=True)
response = session.get(url_product, timeout=15)
print(f"Server responded with Status Code: {response.status_code}")

soup = BeautifulSoup(response.content, "html.parser")

print("\n--- HTML DIAGNOSTICS ---")
print(f"Page Title: {soup.title.text.strip() if soup.title else 'None'}")

# Look for the product image
images = soup.find_all("img")
print(f"\nFound {len(images)} total images. First few:")
for img in images[:10]:
    img_id = img.get('id', 'No ID')
    img_class = img.get('class', 'No Class')
    img_src = img.get('src', 'No Source')
    print(f" - ID: {img_id} | Class: {img_class} | SRC: {img_src}")

# Look for text containers
divs = soup.find_all("div")
print("\n--- Text Containers ---")
valid_divs = 0
for div in divs:
    div_id = div.get('id')
    div_class = div.get('class')
    if div_id or div_class:
        text = div.get_text(strip=True)
        if len(text) > 30:
            print(f"ID: {div_id} | Class: {div_class} | Text: {text[:60]}...")
            valid_divs += 1
            if valid_divs > 5:
                break