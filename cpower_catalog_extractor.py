#!/usr/bin/env python3
"""
cpower_catalog_extractor.py
Extracts all tabular product data and SKUs from CATALOGUE 2023.pdf
and exports a normalized CSV ready for CMS/database import.
"""

import re
import json
import pdfplumber
import pandas as pd

PDF_PATH = "CATALOGUE 2023.pdf"
OUTPUT_CSV = "cpower_products_master.csv"

def clean_cell(val):
    if val is None:
        return ""
    # Strip line breaks, multiple spaces, and non-standard whitespace
    cleaned = re.sub(r"\s+", " ", str(val)).strip()
    return cleaned

def parse_side_by_side_table(table, page_num, default_category):
    """
    Handles tables where multiple products are listed side-by-side
    (e.g., [Item No, Size, Inner, Outer, Item No, Size, Inner, Outer]).
    """
    records = []
    if not table or len(table) < 2:
        return records

    header = [clean_cell(c).lower() for c in table[0]]
    
    # Identify split indices if multiple 'item' columns exist in one row
    item_col_indices = [i for i, col in enumerate(header) if "item" in col or "sku" in col]
    
    # Single-block table
    if len(item_col_indices) <= 1:
        headers = [clean_cell(c) for c in table[0]]
        for row in table[1:]:
            cleaned_row = [clean_cell(c) for c in row]
            if not any(cleaned_row):
                continue
            
            # Match SKU format (e.g., CP11001, CP301201, or 811600)
            sku_match = re.search(r"(CP\d{5,6}|\b\d{6}\b)", " ".join(cleaned_row))
            if not sku_match:
                continue

            row_dict = {}
            for h, v in zip(headers, cleaned_row):
                if h and v:
                    row_dict[h] = v
                    
            records.append({
                "sku": sku_match.group(1),
                "category": default_category,
                "raw_specs": json.dumps(row_dict, ensure_ascii=False),
                "page": page_num
            })
    else:
        # Multi-column table: slice row into chunks based on Item No positions
        slices = []
        for i, start_idx in enumerate(item_col_indices):
            end_idx = item_col_indices[i + 1] if i + 1 < len(item_col_indices) else len(header)
            slices.append((start_idx, end_idx))

        for row in table[1:]:
            cleaned_row = [clean_cell(c) for c in row]
            for start, end in slices:
                sub_row = cleaned_row[start:end]
                sub_header = header[start:end]
                
                joined_text = " ".join(sub_row)
                sku_match = re.search(r"(CP\d{5,6}|\b\d{6}\b)", joined_text)
                if not sku_match:
                    continue

                sub_dict = {}
                for h, v in zip(sub_header, sub_row):
                    if h and v:
                        sub_dict[h] = v

                records.append({
                    "sku": sku_match.group(1),
                    "category": default_category,
                    "raw_specs": json.dumps(sub_dict, ensure_ascii=False),
                    "page": page_num
                })

    return records

def extract_all_products(pdf_path):
    all_records = []
    
    with pdfplumber.open(pdf_path) as pdf:
        total_pages = len(pdf.pages)
        print(f"Loaded {pdf_path}: {total_pages} pages detected.")

        for idx, page in enumerate(pdf.pages):
            page_num = idx + 1
            text = page.extract_text() or ""
            lines = [l.strip() for l in text.split("\n") if l.strip()]
            
            # Infer category name from header text lines
            category = "General Hardware"
            for line in lines[:5]:
                if any(k in line.upper() for k in [
                    "SOCKET", "PLIER", "HAMMER", "WRENCH", "SCREWDRIVER", 
                    "DRILL", "SAW", "VISE", "CLAMP", "PLUMBING", "TAPE", 
                    "MEASURING", "AXE", "CABINET", "CUTTER"
                ]):
                    category = line
                    break

            tables = page.extract_tables()
            page_records_count = 0
            
            for table in tables:
                records = parse_side_by_side_table(table, page_num, category)
                all_records.extend(records)
                page_records_count += len(records)
                
            # Fallback regex search on plain text for un-tabled SKUs
            if page_records_count == 0:
                sku_matches = re.findall(r"(CP\d{5,6})", text)
                for sku in set(sku_matches):
                    all_records.append({
                        "sku": sku,
                        "category": category,
                        "raw_specs": json.dumps({"text_snippet": text[:200]}),
                        "page": page_num
                    })

    # Deduplicate entries by SKU
    df = pd.DataFrame(all_records)
    if not df.empty:
        df.drop_duplicates(subset=["sku"], keep="first", inplace=True)
        df.sort_values(by=["page", "sku"], inplace=True)

    return df

if __name__ == "__main__":
    df_products = extract_all_products(PDF_PATH)
    print(f"Extracted {len(df_products)} unique SKUs across the catalog.")
    df_products.to_csv(OUTPUT_CSV, index=False)
    print(f"Master file saved to {OUTPUT_CSV}")