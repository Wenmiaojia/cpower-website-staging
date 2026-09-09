import os

# --- 2026 PRODUCT DATABASE ---
catalog = [
    {
        "id": "new_pump_pliers",
        "title": "NEW PUMP PLIERS",
        "image": "new_pump_pliers.png",
        "video": "new_pump_pliers.mp4",
        "desc": "Engineered with a quick-adjust push-button mechanism for rapid sizing.|Features induction-hardened asymmetric teeth for a self-locking grip on pipes and nuts.|Reduces hand fatigue during heavy-duty plumbing and HVAC applications."
    },
    {
        "id": "nail_puller",
        "title": "HEAVY-DUTY NAIL PULLER",
        "image": "nail_puller.jpg",
        "video": None,
        "desc": "Drop-forged from high-carbon steel with a rust-resistant finish.|Precision-honed, low-profile claws easily penetrate tight spaces.|High-leverage heel maximizes extraction force for demolition and framing."
    },
    {
        "id": "2in1_bit_adaptor",
        "title": "2-IN-1 BIT ADAPTOR",
        "image": "2in1_bit_adaptor.jpg",
        "video": "2in1_adaptor.mp4",
        "desc": "Impact-rated, dual-function driver accessory machined from premium S2 steel.|Quick-release locking mechanism seamlessly transitions between driving profiles.|Built specifically to withstand high-torque power tools."
    },
    {
        "id": "new_foam_gun",
        "title": "PROFESSIONAL PU FOAM GUN",
        "image": "new_foam_gun.jpg",
        "video": "new_foam_gun.mp4",
        "desc": "Designed for precision insulation and sealing.|Teflon-coated barrel and needle prevent adhesive buildup.|Ergonomic grip and micro-adjustable flow valve for ultimate expansion control and zero-waste application."
    },
    {
        "id": "knife_and_scraper",
        "title": "2-IN-1 UTILITY KNIFE & SCRAPER",
        "image": "knife_and_scraper.jpg",
        "video": "2_in_1_utility_knife_and_scrper.mp4",
        "desc": "Heavy-duty zinc-alloy frame featuring a patented dual-action mechanism.|Instantly snaps from a standard cutting blade into a rigid flat scraper.|Includes a quick-change blade release and a secure safety lock for job site versatility."
    }
]

# Add the generic numbered products
for num, ext in [('6', 'png'), ('7', 'jpg'), ('8', 'png'), ('9', 'jpeg'), ('10', 'png')]:
    catalog.append({
        "id": f"tool_{num}",
        "title": f"INDUSTRIAL TOOL MODEL {num}",
        "image": f"{num}.{ext}",
        "video": None,
        "desc": "High-performance industrial tool precision-forged for heavy-duty applications.|Engineered to withstand extreme torque and repeated job site wear.|ISO 9001 and CE compliant for global distribution."
    })

os.makedirs("new_products", exist_ok=True)

# EXACT CSS FROM YOUR REFERENCE
CSS_STYLES = """
  <style>
    :root { --primary: #cc4400; --primary-hover: #a33600; --dark: #050505; --text-main: #262626; --text-light: #737373; --surface: #ffffff; --bg-body: #f1f5f9; --border: #e2e8f0; --transition: all 0.3s ease; }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Plus Jakarta Sans', sans-serif; background-color: var(--bg-body); color: var(--text-main); line-height: 1.6; }
    
    .top-bar { background-color: var(--dark); color: #a3a3a3; font-size: 0.85rem; padding: 0.5rem 2rem; display: flex; justify-content: flex-end; gap: 1.5rem; }
    header { background: var(--surface); border-bottom: 1px solid var(--border); position: sticky; top: 0; z-index: 100; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }
    .nav-container { max-width: 1400px; margin: 0 auto; padding: 1rem 2rem; display: flex; align-items: center; justify-content: space-between; }
    .brand-logo img { display: block; }
    .main-menu { display: flex; gap: 1.5rem; list-style: none; }
    .main-menu a { text-decoration: none; color: var(--dark); font-weight: 700; font-size: 0.95rem; text-transform: uppercase; transition: var(--transition); padding: 0.5rem 0; }
    .main-menu a:hover, .main-menu a.active { color: var(--primary); border-bottom: 2px solid var(--primary); }

    .page-header { background: linear-gradient(to right, rgba(5, 5, 5, 0.9) 0%, rgba(5, 5, 5, 0.6) 100%), url('https://images.unsplash.com/photo-1504328345606-18bbc8c9d7d1?auto=format&fit=crop&w=1400&q=80') center/cover; color: white; padding: 4rem 2rem; margin-bottom: 3rem; }
    .page-header-inner { max-width: 1400px; margin: 0 auto; }
    .page-title { font-size: 2.2rem; font-weight: 800; margin-bottom: 0.5rem; }
    .breadcrumbs { color: #94a3b8; font-size: 0.9rem; font-weight: 500; }
    .breadcrumbs a { color: white; text-decoration: none; }
    .breadcrumbs a:hover { color: var(--primary); }

    .layout-grid { max-width: 1400px; margin: 0 auto 4rem; padding: 0 2rem; display: grid; grid-template-columns: 280px 1fr; gap: 2.5rem; }
    .sidebar { background: var(--surface); border-radius: 12px; border: 1px solid var(--border); padding: 1.5rem; height: fit-content; position: sticky; top: 90px; }
    .sidebar-title { font-size: 1.1rem; font-weight: 800; color: var(--dark); padding-bottom: 1rem; margin-bottom: 1rem; border-bottom: 2px solid var(--primary); }
    .cat-menu { list-style: none; }
    .cat-menu a { display: flex; align-items: center; justify-content: space-between; text-decoration: none; color: var(--text-main); font-size: 0.95rem; font-weight: 500; padding: 0.6rem 0.5rem; border-radius: 6px; transition: var(--transition); }
    .cat-menu a:hover { background: var(--bg-body); color: var(--primary); padding-left: 1rem; }

    .product-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 1.5rem; margin-bottom: 3rem; }
    .product-card { background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 1rem; text-align: center; transition: var(--transition); display: flex; flex-direction: column; }
    .product-card:hover { border-color: var(--primary); box-shadow: 0 10px 20px rgba(0,0,0,0.05); transform: translateY(-3px); }
    .product-card img { width: 100%; height: 180px; object-fit: contain; margin-bottom: 1rem; border-radius: 4px; }
    .product-name { font-weight: 700; color: var(--dark); font-size: 1rem; margin-bottom: 1rem; flex-grow: 1; }
    .btn-rfq { display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; width: 100%; padding: 0.6rem; background: var(--bg-body); color: var(--primary); font-weight: 700; font-size: 0.9rem; text-decoration: none; border-radius: 4px; transition: var(--transition); }
    .btn-rfq:hover { background: var(--primary); color: white; }

    .detail-container { background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 2.5rem; box-shadow: 0 4px 15px rgba(0,0,0,0.02); }
    .back-link { display: inline-flex; align-items: center; gap: 0.5rem; color: var(--text-light); text-decoration: none; font-weight: 700; font-size: 0.95rem; margin-bottom: 2rem; transition: var(--transition); }
    .back-link:hover { color: var(--primary); }
    .detail-image { width: 100%; max-width: 550px; height: auto; object-fit: contain; display: block; margin: 0 auto 2rem auto; }
    .detail-title { font-size: 2rem; font-weight: 800; color: var(--dark); border-bottom: 2px solid var(--bg-body); padding-bottom: 1rem; margin-bottom: 1.5rem; }
    .detail-specs { line-height: 1.8; color: var(--text-main); font-size: 1.05rem; margin-bottom: 2.5rem; padding-left: 1.5rem; }
    .detail-specs li { margin-bottom: 0.5rem; }
    
    .btn-quote { display: inline-flex; align-items: center; gap: 0.5rem; background: var(--primary); color: white; padding: 1rem 2rem; font-weight: 700; border-radius: 6px; text-decoration: none; transition: var(--transition); font-size: 1.1rem; margin-bottom: 2rem; }
    .btn-quote:hover { background: var(--primary-hover); transform: translateY(-2px); box-shadow: 0 5px 15px rgba(204, 68, 0, 0.2); }
    
    .page-nav { display: flex; justify-content: space-between; border-top: 1px solid var(--border); padding-top: 1.5rem; margin-top: 2rem; }
    .nav-btn { display: inline-flex; align-items: center; gap: 0.5rem; font-weight: 700; color: var(--dark); text-decoration: none; transition: var(--transition); }
    .nav-btn:hover { color: var(--primary); }

    footer { background: var(--dark); color: #a3a3a3; padding: 3rem 2rem; text-align: center; margin-top: auto; }
    .footer-links { display: flex; justify-content: center; gap: 1.5rem; flex-wrap: wrap; margin-bottom: 1.5rem; }
    .footer-links a { color: white; text-decoration: none; font-weight: 600; transition: color 0.2s; }
    .footer-links a:hover { color: var(--primary); }
  </style>
"""

# GLOBAL HEADER & FOOTER
def get_header(active_nav):
    return f"""
  <div class="top-bar">
    <span>Tel: 0086-29-88455900</span>
    <span>Email: jack.jia@cpowertoolsco.com</span>
  </div>
  <header>
    <div class="nav-container">
      <a href="../index.html" class="brand-logo"><img src="../photos/cpowerlogo1.jpg" alt="CPower Tools" width="150"></a>
      <ul class="main-menu">
        <li><a href="../index.html">Home</a></li>
        <li><a href="../about.html">About us</a></li>
        <li><a href="../news.html">News</a></li>
        <li><a href="../products.html">Products</a></li>
        <li><a href="index.html" class="{'active' if active_nav == 'new' else ''}">New Products</a></li>
        <li><a href="#">Download</a></li>
        <li><a href="../contact.html">Contact us</a></li>
      </ul>
    </div>
  </header>
"""

footer_html = """
  <footer>
    <div class="footer-links">
      <a href="../index.html">Home</a> ｜ <a href="../about.html">About us</a> ｜ <a href="../news.html">News</a> ｜ <a href="../products.html">Products</a> ｜ <a href="index.html">New products</a> ｜ <a href="#">Download</a> ｜ <a href="../contact.html">Contact us</a>
    </div>
    <div style="font-size: 0.9rem;">Copyright @ 2026 CPOWER ALL rights reserved.</div>
  </footer>
  <script>lucide.createIcons();</script>
"""

# SIDEBAR (REUSED ACROSS PAGES)
sidebar_html = """
    <aside class="sidebar">
      <div class="sidebar-title">CPOWER Categories</div>
      <ul class="cat-menu">
        <li><a href="../products.html?category=all">All Products <i data-lucide="chevron-right"></i></a></li>
        <li><a href="index.html" style="color:var(--primary);">2026 New Arrivals <i data-lucide="chevron-right"></i></a></li>
        <li><a href="../products.html?category=sockets">Ratchet & Socket Sets <i data-lucide="chevron-right"></i></a></li>
        <li><a href="../products.html?category=bits">Bits & Accessories <i data-lucide="chevron-right"></i></a></li>
        <li><a href="../products.html?category=pliers">Pliers & Cutters <i data-lucide="chevron-right"></i></a></li>
        <li><a href="../products.html?category=hammers">Hammers & Axes <i data-lucide="chevron-right"></i></a></li>
        <li><a href="../products.html?category=wrenches">Wrenches & Spanners <i data-lucide="chevron-right"></i></a></li>
        <li><a href="../products.html?category=screwdrivers">Screwdrivers <i data-lucide="chevron-right"></i></a></li>
      </ul>
    </aside>
"""

# 1. BUILD THE GALLERY PAGE
gallery_cards = ""
for item in catalog:
    gallery_cards += f"""
        <div class="product-card">
          <img src="../web_assets/products/{item['image']}" alt="{item['title']}" loading="lazy">
          <div class="product-name">{item['title']}</div>
          <a href="{item['id']}.html" class="btn-rfq">View Details <i data-lucide="arrow-right" style="width: 16px;"></i></a>
        </div>
    """

gallery_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>2026 New Arrivals | CPOWER TOOLS</title>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <script src="https://unpkg.com/lucide@latest"></script>
  {CSS_STYLES}
</head>
<body>
  {get_header('new')}
  <div class="page-header">
    <div class="page-header-inner">
      <h1 class="page-title">2026 NEW ARRIVALS</h1>
      <div class="breadcrumbs"><a href="../index.html">Home</a> &nbsp;/&nbsp; <span>New Products</span></div>
    </div>
  </div>
  <main class="layout-grid" style="margin-top: 3rem;">
    {sidebar_html}
    <section class="content">
        <div class="product-grid">{gallery_cards}</div>
    </section>
  </main>
  {footer_html}
</body>
</html>
"""

with open("new_products/index.html", "w", encoding="utf-8") as f:
    f.write(gallery_page)

# 2. BUILD INDIVIDUAL PRODUCT PAGES
for i, item in enumerate(catalog):
    # Setup prev/next links
    prev_item = catalog[i-1] if i > 0 else catalog[-1]
    next_item = catalog[i+1] if i < len(catalog)-1 else catalog[0]
    
    # Format the bullets cleanly
    bullets = "\n".join([f"<li>{bullet.strip()}</li>" for bullet in item['desc'].split('|')])
    
    # Inject Video if it exists, otherwise standard image
    if item['video']:
        media_element = f"""
            <video class="detail-image" controls autoplay muted loop>
                <source src="../web_assets/videos/{item['video']}" type="video/mp4">
            </video>
        """
    else:
        media_element = f'<img class="detail-image" src="../web_assets/products/{item["image"]}" alt="{item["title"]}">'

    detail_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{item['title']} | CPOWER TOOLS</title>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <script src="https://unpkg.com/lucide@latest"></script>
  {CSS_STYLES}
</head>
<body>
  {get_header('new')}
  <div class="page-header">
    <div class="page-header-inner">
      <h1 class="page-title">{item['title']}</h1>
      <div class="breadcrumbs">
        <a href="index.html">New Products</a> &nbsp;/&nbsp; <span>{item['title']}</span>
      </div>
    </div>
  </div>
  <main class="layout-grid" style="margin-top: 3rem;">
    {sidebar_html}
    <section class="content">
        <div class="detail-container">
            <a href="index.html" class="back-link">
                <i data-lucide="arrow-left" style="width: 18px;"></i> Back to New Arrivals
            </a>
            
            {media_element}
            
            <h1 class="detail-title">{item['title']}</h1>
            
            <!-- Specs formatted as a clean bulleted list -->
            <ul class="detail-specs">
                {bullets}
            </ul>
            
            <a href="mailto:jack.jia@cpowertoolsco.com?subject=Wholesale Quote Request: {item['title']}" class="btn-quote">
                Request Bulk Quote <i data-lucide="mail" style="width: 20px;"></i>
            </a>

            <div class="page-nav">
                <a href="{prev_item['id']}.html" class="nav-btn"><i data-lucide="arrow-left"></i> Previous Tool</a>
                <a href="{next_item['id']}.html" class="nav-btn">Next Tool <i data-lucide="arrow-right"></i></a>
            </div>
        </div>
    </section>
  </main>
  {footer_html}
</body>
</html>
"""
    with open(f"new_products/{item['id']}.html", "w", encoding="utf-8") as f:
        f.write(detail_page)

print("SUCCESS: Pages generated using your exact layout! Open 'new_products/index.html' to verify.")