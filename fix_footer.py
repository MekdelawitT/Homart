from pathlib import Path
import re

root = Path(r"c:\Users\dell\OneDrive\Documents\Homart\Front-end")
footer = '''        <footer>
            <div class="footflex">
            <div class="ffx1">
            <p id="fname">Homart</p>
            <p id="slogan">Find a place. Find your home</p>
            <div class="footerflex">
                <div class="cus"><p>Contact us</p>
                <a href="info@homarteth.com"><p class="footertext"><img id="email" src="email.jpg">info@homarteth.com</p></a>
                <p class="footertext"><img id="phone" src="phone.jpg">+251 911 234 56</p>
                </div> 
                <div class="fus"><p>Follow us </p>
                <a href="instagram.com/homarteth"><p class="footertext"><img id="insta" src="insta.jpg">instagram.com/homarteth</p></a>
                <a href="tiktok.com/@homarteth"><p class="footertext"><img id="tiktok" src="tiktok.jpg">tiktok.com/@homarteth</p></a>
                </div>
                </div>
            </div>
            <div class="ffx">
                <p class="com ">Company</p>
                <p class="supp"><a href="#">About us</p></a>
                <p class="supp"><a href="#">Our Mission</p></a>
                <p class="supp"><a href="#">Careers</p></a>
            </div>
            <div class="ffx">
                <p class="com">Support</p>
                <p class="supp"><a href="#">Contact us</p></a>
                <p class="supp"><a href="#">Help center</p></a>
                <p class="supp"><a href="#">FAQs</p></a>
            </div>
</div>
            <p id ="cp">&copy; 2026 HoMart. All rights reserved.</p>
            
        </footer>'''

changed = []
for path in sorted(root.glob("*.html")):
    text = path.read_text(encoding="utf-8")
    if "footflex" in text:
        continue
    start = text.find("<footer>")
    if start == -1:
        continue
    end = text.find("</footer>", start)
    if end == -1:
        continue
    end += len("</footer>")
    path.write_text(text[:start] + footer + text[end:], encoding="utf-8")
    changed.append(path.name)

print(f"Updated {len(changed)} files")
print("\n".join(changed))

image_paths = {
    "apartment1.jpg": "To buy images/apartment1.jpg",
    "apartment4.jpg": "To buy images/apartment 4.jpg",
    "condo3.jpg": "To buy images/condo3.jpg",
    "condo4.jpg": "To buy images/condo4.jpg",
    "G+1.avif": "To buy images/G+1.avif",
    "G+1,3.jpg": "To buy images/G+1,3.jpg",
    "G+2,3.jpg": "To buy images/G+2,3.jpg",
    "villa1.jpg": "To buy images/villa1.jpg",
    "villa4.jpg": "To buy images/villa4.avif",
    "studio1.jpg": "To buy images/studio1.avif",
    "studio2.jpg": "To buy images/studio2.avif",
    "apartment2.jpg": "To rent images/apartment2.jpg",
    "apartment3.jpg": "To rent images/apartment 3.jpg",
    "condo 3.jpg": "To rent images/condos 3.jpg",
    "G+1 , 1.jpg": "To rent images/G+1 , 1.jpg",
    "G+2 , 2.avif": "To rent images/G+2 , 2.avif",
    "G+2.avif": "To rent images/G+2.avif",
    "singleroom1.jpg": "To rent images/singleroom1.jpg",
    "singleroom2.jpg": "To rent images/singleroom2.jpg",
    "villa 2.jpg": "To rent images/villa 2.jpg",
    "villa2.jpg": "To rent images/villa 2.jpg",
    "villa3.jpg": "To rent images/villa3.avif",
    "studio1.avif": "To rent images/studio1.avif",
    "studio2.avif": "To rent images/studio2.avif",
}

buy_pages = {"lowpriceb.html", "mediumpriceb.html", "highpriceb.html", "veryhighpriceb.html", "luxurypriceb.html"}
rent_pages = {"lowpricer.html", "mediumpricer.html", "highpricer.html", "veryhighpricer.html", "luxurypricer.html"}

def normalize_card(match):
    card = match.group(1)
    image_match = re.search(r'(<img\b[^>]*>)', card)
    if not image_match:
        return match.group(0)
    image = image_match.group(1)
    details = card[image_match.end():]
    details = re.sub(r'<p(?![^>]*class=)(?=>ETB)', '<p class="gbirr"', details, count=1)
    details = re.sub(r'<p(?![^>]*class=)(?=>For (?:Sale|Rent))', '<p class="gsorr"', details, count=1)
    return f'<a href="#"><div class="ge">{image}<div class="gd">{details}</div></div></a>'

for path in sorted(root.glob("*price*.html")):
    text = path.read_text(encoding="utf-8")
    if 'href="propertydetails.css"' not in text:
        text = text.replace('href="index.css"', 'href="index.css"', 1)
        text = text.replace('</head>', '    <link rel="stylesheet" href="propertydetails.css">\n</head>', 1)
    for source, target in image_paths.items():
        if path.name in buy_pages and target.startswith("To buy images/"):
            text = text.replace(f'src="{source}"', f'src="{target}"')
        if path.name in rent_pages and target.startswith("To rent images/"):
            text = text.replace(f'src="{source}"', f'src="{target}"')
    if path.name in rent_pages:
        text = text.replace('src="studio1.jpg"', 'src="To rent images/studio1.avif"')
        text = text.replace('src="studio2.jpg"', 'src="To rent images/studio2.avif"')
    text = re.sub(r'<div id="view-details-[^"]+">.*?</div>', '', text, flags=re.DOTALL)
    text = text.replace('<button>View Details</button>', '')

    headings = {
        "lowpriceb.html": "Houses under ETB 2,000,000 For Sale in Ethiopia",
        "mediumpriceb.html": "ETB 2,000,000 - 10,000,000 Houses For Sale in Ethiopia",
        "highpriceb.html": "ETB 10,000,000 - 20,000,000 Houses For Sale in Ethiopia",
        "veryhighpriceb.html": "ETB 20,000,000 - 50,000,000 Houses For Sale in Ethiopia",
        "luxurypriceb.html": "Houses over ETB 50,000,000 For Sale in Ethiopia",
        "lowpricer.html": "ETB 5,000 - 10,000 Houses For Rent in Ethiopia",
        "mediumpricer.html": "ETB 10,000 - 20,000 Houses For Rent in Ethiopia",
        "highpricer.html": "ETB 20,000 - 50,000 Houses For Rent in Ethiopia",
        "veryhighpricer.html": "Houses over ETB 100,000 For Rent in Ethiopia",
        "luxurypricer.html": "ETB 50,000 - 100,000 Houses For Rent in Ethiopia",
    }
    main_match = re.search(r'(<main[^>]*>)(.*?)(</main>)', text, flags=re.DOTALL)
    if main_match:
        main_open, main_body, main_close = main_match.groups()
        main_open = re.sub(r' class="gc sec2"', '', main_open)
        main_body = re.sub(r'<h4>.*?</h4>', '', main_body, flags=re.DOTALL)
        main_body = re.sub(r'<div class="ge gd">(.*?)</div>', normalize_card, main_body, flags=re.DOTALL)
        heading = f'<h4>{headings[path.name]}</h4>\n'
        text = text[:main_match.start()] + main_open + heading + main_body + main_close + text[main_match.end():]
    path.write_text(text, encoding="utf-8")
