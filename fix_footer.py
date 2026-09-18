from pathlib import Path

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
