import os

CSS_STYLES = """
  <style>
    :root { --primary: #cc4400; --primary-hover: #a33600; --dark: #050505; --text-main: #262626; --text-light: #737373; --surface: #ffffff; --bg-body: #f1f5f9; --border: #e2e8f0; --transition: all 0.3s ease; }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Plus Jakarta Sans', sans-serif; background-color: var(--bg-body); color: var(--text-main); line-height: 1.6; }
    
    .top-bar { background-color: var(--dark); color: #a3a3a3; font-size: 0.85rem; padding: 0.5rem 2rem; display: flex; justify-content: flex-end; gap: 1.5rem; }
    header { background: var(--surface); border-bottom: 1px solid var(--border); position: sticky; top: 0; z-index: 100; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }
    .nav-container { max-width: 1400px; margin: 0 auto; padding: 1rem 2rem; display: flex; align-items: center; justify-content: space-between; }
    .brand-logo img { max-height: 45px; display: block; }
    .main-menu { display: flex; gap: 1.5rem; list-style: none; align-items: center; }
    .main-menu a { text-decoration: none; color: var(--dark); font-weight: 700; font-size: 0.95rem; text-transform: uppercase; transition: var(--transition); padding: 0.5rem 0; }
    .main-menu a:hover, .main-menu a.active { color: var(--primary); border-bottom: 2px solid var(--primary); }

    .page-header { background: linear-gradient(to right, rgba(5, 5, 5, 0.9) 0%, rgba(5, 5, 5, 0.7) 100%), url('web_assets/factory/factory_floor_2.jpg') center/cover; color: white; padding: 4rem 2rem; margin-bottom: 3rem; }
    .page-header-inner { max-width: 1400px; margin: 0 auto; }
    .page-title { font-size: 2.5rem; font-weight: 800; margin-bottom: 0.5rem; }
    .breadcrumbs { color: #a3a3a3; font-size: 0.9rem; font-weight: 500; }
    .breadcrumbs a { color: white; text-decoration: none; }
    .breadcrumbs a:hover { color: var(--primary); }

    .layout-grid { max-width: 1400px; margin: 0 auto 4rem; padding: 0 2rem; display: grid; grid-template-columns: 280px 1fr; gap: 2.5rem; }
    
    .sidebar { background: var(--surface); border-radius: 12px; border: 1px solid var(--border); padding: 1.5rem; height: fit-content; position: sticky; top: 90px; }
    .sidebar-title { font-size: 1.1rem; font-weight: 800; color: var(--dark); padding-bottom: 1rem; margin-bottom: 1rem; border-bottom: 2px solid var(--primary); }
    .cat-menu { list-style: none; }
    .cat-menu a { display: flex; align-items: center; justify-content: space-between; text-decoration: none; color: var(--text-main); font-size: 0.95rem; font-weight: 500; padding: 0.6rem 0.5rem; border-radius: 6px; transition: var(--transition); }
    .cat-menu a:hover { background: var(--bg-body); color: var(--primary); padding-left: 1rem; }

    .article-container { background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 3rem; box-shadow: 0 4px 15px rgba(0,0,0,0.02); margin-bottom: 4rem; }
    .article-title { font-size: 2rem; font-weight: 800; color: var(--dark); margin-bottom: 0.5rem; line-height: 1.2; }
    .article-meta { display: flex; align-items: center; gap: 1.5rem; font-size: 0.9rem; color: var(--text-light); margin-bottom: 2rem; padding-bottom: 1rem; border-bottom: 1px solid var(--border); }
    .article-hero-img { width: 100%; height: auto; max-height: 500px; object-fit: cover; border-radius: 8px; margin-bottom: 2.5rem; border: 1px solid var(--border); }
    .article-body { font-size: 1.1rem; color: var(--text-main); line-height: 1.8; }
    .article-body p { margin-bottom: 1.5rem; }
    
    .news-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 2rem; }
    .news-card { background: var(--surface); border: 1px solid var(--border); border-radius: 8px; overflow: hidden; transition: var(--transition); display: flex; flex-direction: column; }
    .news-card:hover { border-color: var(--primary); transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.05); }
    .news-card-img { width: 100%; height: 200px; object-fit: cover; border-bottom: 1px solid var(--border); }
    .news-card-content { padding: 1.5rem; display: flex; flex-direction: column; flex-grow: 1; }
    .news-card-date { font-size: 0.85rem; color: var(--primary); font-weight: 700; margin-bottom: 0.5rem; }
    .news-card-title { font-size: 1.25rem; font-weight: 800; color: var(--dark); margin-bottom: 1rem; line-height: 1.3; }
    .news-card-excerpt { font-size: 0.95rem; color: var(--text-light); margin-bottom: 1.5rem; flex-grow: 1; }
    .news-card-link { font-weight: 700; color: var(--dark); text-decoration: none; display: flex; align-items: center; gap: 0.5rem; transition: var(--transition); }
    .news-card-link:hover { color: var(--primary); }

    footer { background: var(--dark); color: #a3a3a3; padding: 3rem 2rem; text-align: center; margin-top: auto; }
    .footer-links { display: flex; justify-content: center; gap: 1.5rem; flex-wrap: wrap; margin-bottom: 1.5rem; }
    .footer-links a { color: white; text-decoration: none; font-weight: 600; transition: color 0.2s; }
    .footer-links a:hover { color: var(--primary); }
  </style>
"""

header_html = """
  <div class="top-bar">
    <span>Tel: 0086-29-88455900</span>
    <span>Email: jack.jia@cpowertoolsco.com</span>
  </div>
  <header>
    <div class="nav-container">
      <a href="index.html" class="brand-logo"><img src="photos/cpowerlogo1.jpg" alt="CPower Tools" width="150"></a>
      <ul class="main-menu">
        <li><a href="index.html">Home</a></li>
        <li><a href="about.html">About us</a></li>
        <li><a href="news.html" class="active">News</a></li>
        <li><a href="products.html">Products</a></li>
        <li><a href="new_products/index.html">New Products</a></li>
        <li><a href="web_assets/docs/cpower_iso_9001_certificate.pdf" target="_blank">Download</a></li>
        <li><a href="contact.html">Contact us</a></li>
      </ul>
    </div>
  </header>
"""

footer_html = """
  <footer>
    <div class="footer-links">
      <a href="index.html">Home</a> ｜ <a href="about.html">About us</a> ｜ <a href="news.html">News</a> ｜ <a href="products.html">Products</a> ｜ <a href="new_products/index.html">New products</a> ｜ <a href="web_assets/docs/cpower_iso_9001_certificate.pdf" target="_blank">Download</a> ｜ <a href="contact.html">Contact us</a>
    </div>
    <div style="font-size: 0.9rem;">Copyright @ 2026 CPOWER ALL rights reserved.</div>
  </footer>
  <script>lucide.createIcons();</script>
"""

sidebar_html = """
    <aside class="sidebar">
      <div class="sidebar-title">News Archives</div>
      <ul class="cat-menu">
        <li><a href="news.html" style="color:var(--primary); font-weight: 700;">Latest Updates <i data-lucide="chevron-right" style="width:16px;"></i></a></li>
        <li><a href="news_canton_2026.html">Canton Fair 2026 <i data-lucide="chevron-right" style="width:16px;"></i></a></li>
        <li><a href="news_product_launch.html">2026 Product Launch <i data-lucide="chevron-right" style="width:16px;"></i></a></li>
        <li><a href="news_logistics.html">Facility Expansion <i data-lucide="chevron-right" style="width:16px;"></i></a></li>
        <li><a href="news_koln.html">Global Exhibitions <i data-lucide="chevron-right" style="width:16px;"></i></a></li>
      </ul>
    </aside>
"""

# The News Database (Notice the varied images: Products, Logistics, Historical Fairs)
articles = [
    {
        "filename": "news_canton_2026.html",
        "title": "Unveiling 2026 Flagship Innovations at the Canton Fair",
        "date": "APRIL 15, 2026",
        "image": "web_assets/fairs/2026_spring_canton_fair.jpg",
        "excerpt": "CPOWER Tools showcases our newest industrial-grade hand tools to global buyers at the 139th China Import and Export Fair.",
        "content": "<p>CPOWER Tools Co., Ltd. is proud to announce our successful exhibition at the 2026 Spring Canton Fair in Guangzhou. As a leading manufacturer of industrial hardware, our booth attracted hundreds of international distributors and wholesale partners.</p><p>This year, we highlighted our expanded portfolio of heavy-duty hand tools, featuring our newly engineered push-button pump pliers, professional PU foam guns, and multi-functional bit adapters. The response from the global market has been overwhelmingly positive, leading to several major OEM tooling contracts for the North American and European sectors.</p><p>We thank all the buyers who visited our booth and look forward to forging resilient, long-term partnerships.</p>"
    },
    {
        "filename": "news_product_launch.html",
        "title": "CPOWER Announces 2026 Heavy-Duty Product Lineup",
        "date": "FEBRUARY 10, 2026",
        "image": "web_assets/products/new_foam_gun.jpg", # Using a product photo!
        "excerpt": "Introducing our next-generation PU Foam Guns and Quick-Adjust Pump Pliers, engineered for extreme job site durability.",
        "content": "<p>After rigorous R&D and field testing, CPOWER Tools is thrilled to officially launch our 2026 flagship product lineup. Engineered for professionals, this new series focuses on ergonomics, extreme durability, and job site efficiency.</p><p>Highlighting the release is our <strong>Professional PU Foam Gun</strong>, featuring a Teflon-coated barrel that completely eliminates adhesive buildup. Alongside it, our new <strong>Quick-Adjust Pump Pliers</strong> utilize an advanced push-button locking mechanism that dramatically reduces hand fatigue during heavy plumbing and HVAC applications.</p><p>These items are now available for bulk order and OEM customization. View our <a href='new_products/index.html' style='color:#cc4400; font-weight:bold;'>New Products Gallery</a> for full technical specifications.</p>"
    },
    {
        "filename": "news_logistics.html",
        "title": "Scaling Up: Major Upgrades to Our Global Logistics Facility",
        "date": "NOVEMBER 22, 2025",
        "image": "web_assets/factory/factory_floor_7.jpg", # Using the warehouse boxes photo!
        "excerpt": "To meet rising international demand, CPOWER has expanded its warehouse footprint to streamline port-to-port shipping.",
        "content": "<p>At CPOWER, we understand that manufacturing speed is only half the battle—getting the product to your port on time is critical. To support our growing international client base, we have successfully completed a major expansion of our warehouse and logistics facilities in Xi'an.</p><p>Our upgraded inventory management system allows us to stage massive bulk orders and consolidate shipments faster than ever. By integrating directly with major freight forwarders, we have reduced our average port-to-port lead times by 15%.</p><p>Whether you need custom palletizing or complex export documentation, our expanded facility ensures your inventory arrives safely and on schedule.</p>"
    },
    {
        "filename": "news_koln.html",
        "title": "A Decade of European Excellence: Reflecting on the Koln Fair",
        "date": "SEPTEMBER 05, 2025",
        "image": "web_assets/fairs/2012_koln.jpg", # Using a historical trade show photo!
        "excerpt": "Looking back at our foundational partnerships built at the Eisenwarenmesse Cologne Hardware Fair over the last decade.",
        "content": "<p>As we prepare for our upcoming European trade missions, we take a moment to reflect on our long-standing presence at the Eisenwarenmesse Cologne Hardware Fair in Germany.</p><p>Since our early exhibitions over a decade ago, the Koln Fair has been instrumental in establishing CPOWER as a trusted manufacturer for the European market. It was here that we formed our foundational partnerships with top-tier German, British, and French hardware distributors.</p><p>Our commitment to CE compliance and ISO 9001 standards continues to make us a preferred OEM partner across Europe. We look forward to returning to Cologne and showcasing our next generation of industrial tools.</p>"
    }
]

# 1. GENERATE THE MAIN NEWS PAGE (news.html)
news_index = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Company News | CPOWER TOOLS</title>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <script src="https://unpkg.com/lucide@latest"></script>
  {CSS_STYLES}
</head>
<body>
  {header_html}
  <div class="page-header">
    <div class="page-header-inner">
      <h1 class="page-title">Company News</h1>
      <div class="breadcrumbs"><a href="index.html">Home</a> &nbsp;/&nbsp; <span>News & Updates</span></div>
    </div>
  </div>

  <main class="layout-grid">
    {sidebar_html}
    <section class="content">
      
      <!-- FEATURED ARTICLE (Canton Fair) -->
      <article class="article-container">
        <h1 class="article-title">{articles[0]['title']}</h1>
        <div class="article-meta">
          <span><i data-lucide="calendar" style="width:16px;"></i> {articles[0]['date']}</span>
          <span><i data-lucide="folder" style="width:16px;"></i> Exhibitions</span>
        </div>
        <img src="{articles[0]['image']}" alt="Featured News" class="article-hero-img">
        <div class="article-body">
          {articles[0]['content']}
        </div>
      </article>

      <!-- RECENT NEWS GRID -->
      <h2 class="article-title" style="border-bottom: 2px solid #050505; padding-bottom: 10px; margin-bottom: 20px;">Latest Updates</h2>
      <div class="news-grid">
"""

# Add the remaining 3 articles to the grid
for art in articles[1:]:
    news_index += f"""
        <div class="news-card">
          <img src="{art['image']}" alt="{art['title']}" class="news-card-img" style="object-position: center; background: #fff;">
          <div class="news-card-content">
            <div class="news-card-date">{art['date']}</div>
            <h3 class="news-card-title">{art['title']}</h3>
            <p class="news-card-excerpt">{art['excerpt']}</p>
            <a href="{art['filename']}" class="news-card-link">Read Full Article <i data-lucide="arrow-right" style="width:16px;"></i></a>
          </div>
        </div>
    """

news_index += """
      </div>
    </section>
  </main>
  {footer_html}
</body>
</html>
"""

with open("news.html", "w", encoding="utf-8") as f:
    f.write(news_index)

# 2. GENERATE THE INDIVIDUAL ARTICLE PAGES
for art in articles:
    article_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{art['title']} | CPOWER TOOLS</title>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <script src="https://unpkg.com/lucide@latest"></script>
  {CSS_STYLES}
</head>
<body>
  {header_html}
  <div class="page-header" style="padding: 2rem 2rem;">
    <div class="page-header-inner">
      <div class="breadcrumbs"><a href="news.html">News Directory</a> &nbsp;/&nbsp; <span>Article</span></div>
    </div>
  </div>

  <main class="layout-grid">
    {sidebar_html}
    <section class="content">
      <article class="article-container">
        <h1 class="article-title">{art['title']}</h1>
        <div class="article-meta">
          <span><i data-lucide="calendar" style="width:16px;"></i> {art['date']}</span>
        </div>
        <img src="{art['image']}" alt="{art['title']}" class="article-hero-img" style="background: #fff; object-fit: contain; padding: 10px;">
        <div class="article-body">
          {art['content']}
        </div>
        <div style="margin-top: 3rem; border-top: 1px solid #e2e8f0; padding-top: 1.5rem;">
            <a href="news.html" style="color: #cc4400; font-weight: bold; text-decoration: none;">← Back to News Directory</a>
        </div>
      </article>
    </section>
  </main>
  {footer_html}
</body>
</html>
"""
    with open(art['filename'], "w", encoding="utf-8") as f:
        f.write(article_page)

print("SUCCESS: Rebuilt news.html and generated 4 individual article pages!")