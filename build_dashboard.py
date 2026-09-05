import os
import pandas as pd

CSV_PATH = "cpower_products_master.csv"
IMG_DIR = "catalog_images"
OUTPUT_HTML = "mapping_dashboard.html"

def generate_interactive_dashboard():
    df = pd.read_csv(CSV_PATH)
    all_images = os.listdir(IMG_DIR)
    
    html_content = [
        "<html><head><style>",
        "body { font-family: Arial, sans-serif; background: #f4f4f9; padding: 20px; }",
        ".page-block { background: #fff; padding: 20px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }",
        ".sku-list { font-weight: bold; color: #333; margin-bottom: 15px; }",
        ".image-gallery { display: flex; flex-wrap: wrap; gap: 15px; }",
        ".img-card { border: 2px solid transparent; padding: 5px; text-align: center; background: #fafafa; cursor: pointer; transition: 0.2s; }",
        ".img-card:hover { border-color: #007bff; }",
        ".img-card img { max-width: 180px; max-height: 180px; display: block; }",
        ".img-card span { font-size: 12px; color: #666; display: block; margin-top: 5px; }",
        "</style>",
        "<script>",
        "function copyText(text, el) {",
        "  navigator.clipboard.writeText(text);",
        "  el.style.borderColor = '#28a745'; el.style.background = '#e9f7ef';",
        "}",
        "function dimTrash(e, el) {",
        "  e.preventDefault(); el.style.opacity = '0.15';",
        "}",
        "</script></head><body>",
        "<h1>Interactive SKU Mapping Dashboard</h1>",
        "<p><b>Left-click</b> a tool photo to copy its filename. <b>Right-click</b> a trash image to dim it.</p>"
    ]
    
    grouped = df.groupby("page")
    
    for page_num, group in grouped:
        skus = group["sku"].tolist()
        sku_string = ", ".join(skus)
        
        page_prefix = f"img_p{page_num}_"
        page_images = [img for img in all_images if img.startswith(page_prefix)]
        
        if not page_images:
            continue
            
        html_content.append(f"<div class='page-block'>")
        html_content.append(f"<h2>Page {page_num}</h2>")
        html_content.append(f"<div class='sku-list'>SKUs: {sku_string}</div>")
        
        html_content.append("<div class='image-gallery'>")
        for img in page_images:
            img_path = os.path.join(IMG_DIR, img)
            html_content.append(
                f"<div class='img-card' onclick=\"copyText('{img}', this)\" oncontextmenu=\"dimTrash(event, this)\">"
                f"<img src='{img_path}' loading='lazy'>"
                f"<span>{img}</span>"
                f"</div>"
            )
        html_content.append("</div></div>")
        
    html_content.append("</body></html>")
    
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write("\n".join(html_content))
        
    print(f"Interactive dashboard generated: {OUTPUT_HTML}")

if __name__ == "__main__":
    generate_interactive_dashboard()