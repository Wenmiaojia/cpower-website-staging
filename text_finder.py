import pdfplumber
import pandas as pd
import re

PDF_PATH = "CATALOGUE 2023.pdf"
CSV_PATH = "cpower_products_master.csv"
OUTPUT_CSV = "cpower_products_master_with_text.csv"

print("Loading existing CSV and PDF...")
df = pd.read_csv(CSV_PATH)
df['Marketing_Copy'] = ""

# Create a dictionary to cache page text so we only read each page once
page_text_cache = {}

with pdfplumber.open(PDF_PATH) as pdf:
    # Get unique pages from the CSV
    pages_to_scan = df['page'].unique()
    
    for page_num in pages_to_scan:
        # pdfplumber is zero-indexed, your CSV is 1-indexed
        page = pdf.pages[page_num - 1]
        raw_text = page.extract_text()
        
        if not raw_text:
            continue
            
        clean_lines = []
        for line in raw_text.split('\n'):
            line = line.strip()
            # Filter out table rows by ignoring lines that are mostly numbers or very short
            # This keeps the descriptive bullet points but drops the raw specs
            numbers_count = sum(c.isdigit() for c in line)
            if len(line) > 15 and (numbers_count / len(line)) < 0.3:
                clean_lines.append(line)
                
        # Join the surviving descriptive lines into a single paragraph
        page_text_cache[page_num] = " ".join(clean_lines)

print("Appending marketing copy to SKUs...")
# Map the cached text to the corresponding SKUs
df['Marketing_Copy'] = df['page'].map(page_text_cache)

df.to_csv(OUTPUT_CSV, index=False)
print(f"Update complete. Saved as {OUTPUT_CSV}")