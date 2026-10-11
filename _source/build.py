"""Builds the Al-Khair Academy site (V5).
   python3 build.py prod    -> /home/claude/al-khair-academy-site  (clean URLs, absolute asset paths)
   python3 build.py preview -> /home/claude/preview                (.html links, relative paths)"""
import sys, json, os
from PIL import Image

MODE = sys.argv[1] if len(sys.argv) > 1 else 'prod'
PROD = MODE == 'prod'
ROOT = '/home/claude/al-khair-academy-site'
OUT = ROOT if PROD else '/home/claude/preview'
DOMAIN = 'https://alkhairacademy.in'
A = '/assets/' if PROD else 'assets/'

PAGES = {'home': '', 'leadership': 'leadership', 'community': 'community', 'gallery': 'gallery',
         'admissions': 'admissions', 'contact': 'contact', 'privacy': 'privacy'}

def L(key, anchor=''):
    slug = PAGES[key]
    u = ('/' + slug) if PROD else ((slug + '.html') if slug else './')
    return u + (('#' + anchor) if anchor else '')

PHONE_DISPLAY = '+91 62646 72034'
PHONE_TEL = '+916264672034'
WA = '916264672034'
EMAIL = 'alkhair.indore176@gmail.com'
ADDRESS = '57/2, Haji Colony, Khajrana, Indore, Madhya Pradesh 452016'
MAPS = 'https://www.google.com/maps/dir/?api=1&destination=Al-Khair+Academy+57%2F2+Haji+Colony+Khajrana+Indore+452016'
UQ = 'https://understandquran.com/'
PROPEL = 'https://propelschool.co/'
UROOJ = 'https://myurooj.in/'
BOARD = 'State Board · CBSE Pattern'

DIM = {}
for f in os.listdir(ROOT + '/assets/img'):
    if f.endswith('.jpg') and '-800' not in f and f != 'og-image.jpg':
        DIM[f[:-4]] = Image.open(ROOT + '/assets/img/' + f).size

def pic(n, alt, sizes='(max-width: 860px) 100vw, 50vw', cls='', style='', eager=False, full=False):
    w, h = DIM[n]
    big = min(w, 1400)
    attrs = f' class="{cls}"' if cls else ''
    attrs += f' style="{style}"' if style else ''
    attrs += f' data-full="{A}img/{n}.jpg"' if full else ''
    load = 'eager" fetchpriority="high' if eager else 'lazy'
    return (f'<picture>'
            f'<img src="{A}img/{n}-800.jpg" srcset="{A}img/{n}-800.jpg 800w, {A}img/{n}.jpg {big}w" sizes="{sizes}" '
            f'width="{w}" height="{h}" alt="{alt}" loading="{load}" decoding="async"{attrs}></picture>')

def C(n, alt, sizes, cls='', style=''):
    return f'<div class="cell {cls}">' + pic(n, alt, sizes, style=style) + '</div>'

ICON = {
 'menu': '<svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18" stroke="currentColor" stroke-width="1.8" fill="none"/></svg>',
 'phone': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 3h4l2 5-2.5 1.5a11 11 0 005 5L15 12l5 2v4a2 2 0 01-2 2A16 16 0 013 5a2 2 0 012-2z"/></svg>',
 'wa': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3.5 20.5l1.3-4.2A8.5 8.5 0 1112 20.5a8.4 8.4 0 01-4.3-1.2z"/><path d="M9 8.5c0 3 2.5 6 6 6.5l1-1.5-2-1-1 1c-1-.5-2-1.5-2.5-2.5l1-1-1-2z"/></svg>',
 'tv': '<svg viewBox="0 0 36 36" aria-hidden="true"><rect x="4" y="7" width="28" height="18" rx="1"/><path d="M13 31h10M18 25v6"/><path class="g" d="M15 12v8l7-4z"/></svg>',
}

# ---------- shared ----------
def header(active):
    def a(key, label):
        cur = ' aria-current="page"' if key == active else ''
        return f'<a href="{L(key)}"{cur}>{label}</a>'
    return f'''<a class="skip" href="#main">Skip to content</a>
<div class="strip"><div class="wrap">
  <span>{BOARD} · Nursery to Class 8 · Est. <b>2018</b></span>
  <span>Admissions: <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></span>
</div></div>
<header class="site-header"><div class="wrap hdr">
  <a class="brand" href="{L('home')}" aria-label="Al-Khair Academy, home">
    <img src="{A}img/crest-160.png" width="54" height="52" alt="">
    <span><span class="brand-name">AL-KHAIR ACADEMY</span><span class="brand-tag">Nurturing Every Child Like a Seed</span></span>
  </a>
  <button class="menu-btn" type="button" aria-controls="site-nav" aria-expanded="false" aria-label="Open menu">{ICON['menu']}</button>
  <nav class="nav" id="site-nav" aria-label="Main">
    {a('home', 'Home')}
    {a('leadership', 'Leadership')}
    {a('community', 'Community')}
    {a('gallery', 'Gallery')}
    {a('admissions', 'Admissions')}
    {a('contact', 'Contact')}
    <a class="btn btn-primary" href="{L('admissions', 'enquiry')}">Enquire Now</a>
  </nav>
</div></header>'''

def footer():
    return f'''<footer class="site-footer">
  <div class="wrap foot">
    <div class="foot-brand">
      <img src="{A}img/crest-160.png" width="64" height="62" alt="">
      <span class="n">AL-KHAIR ACADEMY</span>
      <span class="t">Success Here and the Hereafter</span>
      <span>{ADDRESS}</span>
    </div>
    <div><h4>Explore</h4><ul>
      <li><a href="{L('home', 'methods')}">How We Teach</a></li>
      <li><a href="{L('leadership')}">Leadership</a></li>
      <li><a href="{L('community')}">Community</a></li>
      <li><a href="{L('gallery')}">Gallery</a></li>
      <li><a href="{L('admissions')}">Admissions</a></li>
      <li><a href="{L('contact')}">Contact</a></li>
    </ul></div>
    <div><h4>Contact</h4><ul>
      <li><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
      <li><a href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp the office</a></li>
      <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li><a href="{MAPS}" target="_blank" rel="noopener">Get directions</a></li>
    </ul></div>
  </div>
  <div class="foot-base"><div class="wrap">
    <span>© <span id="year">2026</span> Al-Khair Academy, Khajrana, Indore · DISE Code 23260104272 · Affiliation No. 82237</span>
    <span><a href="{L('privacy')}">Privacy Policy</a></span>
  </div></div>
</footer>
<nav class="actionbar" aria-label="Quick contact">
  <a href="tel:{PHONE_TEL}">{ICON['phone']} Call</a>
  <a href="https://wa.me/{WA}" target="_blank" rel="noopener">{ICON['wa']} WhatsApp</a>
  <a class="go" href="{L('admissions', 'enquiry')}">Enquire Now</a>
</nav>'''

def enquiry_form():
    classes = ['Nursery'] + [f'Class {i}' for i in range(1, 9)]
    opts = ''.join(f'<option>{c}</option>' for c in classes)
    return f'''<div class="stack" id="enquiry">
<form class="form-card enquiry" novalidate>
  <div class="stack-sm"><span class="eyebrow">Admission Enquiry</span><h3>Tell us about your child</h3>
  <p class="hint">The school office will contact you. Fields marked * are required.</p></div>
  <div class="row2">
    <div class="field"><label for="f-parent">Parent / Guardian name *</label><input id="f-parent" name="parent" autocomplete="name" required><span class="err-msg" hidden>Please enter your name.</span></div>
    <div class="field"><label for="f-student">Student name *</label><input id="f-student" name="student" required><span class="err-msg" hidden>Please enter the student's name.</span></div>
  </div>
  <div class="row2">
    <div class="field"><label for="f-cls">Class seeking admission *</label><select id="f-cls" name="cls">{opts}</select></div>
    <div class="field"><label for="f-phone">Phone number *</label><input id="f-phone" name="phone" type="tel" inputmode="numeric" autocomplete="tel" required><span class="err-msg" hidden>Please enter a 10-digit mobile number.</span></div>
  </div>
  <div class="field"><label for="f-wa">WhatsApp number</label><input id="f-wa" name="whatsapp" type="tel" inputmode="numeric">
    <label class="check"><input type="checkbox" id="f-same" name="same_wa"> Same as phone number</label></div>
  <fieldset class="field"><legend>Preferred contact method</legend>
    <div class="choices">
      <label><input type="radio" name="method" value="Phone call" id="f-m1" checked> Phone call</label>
      <label><input type="radio" name="method" value="WhatsApp" id="f-m2"> WhatsApp</label>
    </div></fieldset>
  <div class="field"><label for="f-msg">Message or question</label><textarea id="f-msg" name="message" rows="3"></textarea></div>
  <button class="btn btn-primary" type="submit">Send Enquiry</button>
  <p class="hint">By sending this form you agree to be contacted about admissions. See our <a href="{L('privacy')}">privacy policy</a>.</p>
</form>
<div class="confirm" tabindex="-1" hidden>
  <b>Thank you</b>
  <p></p>
  <a class="btn btn-primary" href="#" target="_blank" rel="noopener">Send on WhatsApp</a>
</div>
</div>'''

def contact_band():
    return f'''<section class="cband pattern" aria-label="Contact"><div class="wrap">
  <div><span class="k">Visit us</span><h2>Al-Khair Academy</h2><p style="margin-top:6px">{ADDRESS}</p>
    <p style="margin-top:12px"><a href="{MAPS}" target="_blank" rel="noopener" style="border-bottom:1px solid var(--gold)">Get directions →</a></p></div>
  <div><span class="k">Call</span><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></div>
  <div><span class="k">WhatsApp</span><a href="https://wa.me/{WA}" target="_blank" rel="noopener">Message the office</a></div>
  <div><span class="k">Email</span><a href="mailto:{EMAIL}">{EMAIL}</a></div>
</div></section>'''

def admissions_band():
    return f'''<section class="band pattern"><div class="wrap">
  <div class="stack-sm"><span class="eyebrow">Admissions</span><h2>Nursery to Class 8</h2>
  <p>Nursery admission from age 3+. Visit the school, meet our team and ask your questions.</p></div>
  <div class="btn-row"><a class="btn btn-light" href="{L('admissions', 'enquiry')}">Enquire Now</a>
  <a class="btn btn-outline-light" href="{L('admissions')}">Admission details</a></div>
</div></section>'''

FAQ = [
 ('Which board does Al-Khair Academy follow?', 'Al-Khair Academy is a State Board school (Madhya Pradesh), and classes are taught in the CBSE pattern.'),
 ('Which classes are offered?', 'Nursery to Class 8.'),
 ('What is the age for Nursery admission?', 'Children aged 3 years and above are eligible for Nursery.'),
 ('How is Nursery taught?', 'Our Nursery follows the Montessori method: children learn by doing, through hands-on materials, activities and role play.'),
 ('Is there an entrance test?', 'Yes. Students appear for an entrance test, and the school office shares the details for each class.'),
 ('Which documents are needed for admission?', 'Aadhaar Card, Samagra ID, Birth Certificate and Caste Certificate.'),
 ('Is religious education included?', 'Yes. Through Understanding Quran, children learn the meaning of the Quran from a young age, along with hadith, duas and the sunnah of the Prophet ﷺ.'),
 ('Does the school have smart classes?', 'Yes. Lessons use Propel audio-visual content on smart TVs in the classroom.'),
 ('Is transport available?', 'Yes, a rickshaw transport facility is available. Please ask the office about routes.'),
 ('How do I contact the school?', f'Call or WhatsApp {PHONE_DISPLAY}, email {EMAIL}, or send the enquiry form on this page.'),
]
def faq_html():
    return '<div class="faq">' + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ) + '</div>'
FAQ_SCHEMA = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}

FONTS = 'https://fonts.googleapis.com/css2?family=Amiri&family=Cinzel:wght@500;600;700&family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Lato:ital,wght@0,400;0,700;1,400&display=swap'

SCHOOL = {
  "@context": "https://schema.org", "@type": "School",
  "name": "Al-Khair Academy", "alternateName": ["Al Khair Academy", "Al-Khair Academy Indore", "Al-Khair Academy Khajrana", "Al-Khair School Indore"],
  "url": DOMAIN + "/", "logo": DOMAIN + "/assets/img/icon-512.png", "image": DOMAIN + "/assets/img/og-image.jpg",
  "description": "State Board school in Khajrana, Indore, teaching in the CBSE pattern from Montessori Nursery to Class 8, with Understanding Quran, Propel smart classes and the Creativity, Confidence and Character framework.",
  "slogan": "Nurturing Every Child Like a Seed", "foundingDate": "2018",
  "founder": {"@type": "Person", "name": "Adv. Rehana Khan"},
  "employee": [{"@type": "Person", "name": "Adv. Parvez Khan", "jobTitle": "Director"},
               {"@type": "Person", "name": "Adv. Rehana Khan", "jobTitle": "Founder & Principal"}],
  "telephone": PHONE_TEL, "email": EMAIL,
  "address": {"@type": "PostalAddress", "streetAddress": "57/2, Haji Colony, Khajrana", "addressLocality": "Indore",
              "addressRegion": "Madhya Pradesh", "postalCode": "452016", "addressCountry": "IN"},
  "areaServed": "Indore", "award": "National Winner, Propel Shiksha Awards"
}

def head(key, title, desc, schema=None, noindex=False):
    canon = DOMAIN + '/' + PAGES.get(key, '')
    ld = ''.join('<script type="application/ld+json">' + json.dumps(s, ensure_ascii=False) + '</script>\n' for s in (schema or []))
    robots = '<meta name="robots" content="noindex">' if noindex else ''
    r = '/' if PROD else ''
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#1F3A5F">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Al-Khair Academy">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{DOMAIN}/assets/img/og-image.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:locale" content="en_IN">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{r}favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="{A}img/favicon-32.png">
<link rel="apple-touch-icon" href="{r}apple-touch-icon.png">
<link rel="manifest" href="{r}site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="{A}css/style.css">
{ld}</head>
<body>'''

def crumbs(key, label):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": DOMAIN + "/"},
        {"@type": "ListItem", "position": 2, "name": label, "item": DOMAIN + "/" + PAGES[key]}]}

def page_head(eyebrow, h1, lead, label):
    return f'''<section class="page-head"><div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="{L('home')}">Home</a> / {label}</nav>
  <span class="eyebrow">{eyebrow}</span><h1>{h1}</h1><div class="rule"><i></i></div>
  <p class="lead">{lead}</p></div></section>'''

def write(key, filename, title, desc, body, schema=None, noindex=False, active=None, footer_html=None):
    doc = head(key, title, desc, schema, noindex) + '\n' + header(active or key) + '\n<main id="main">\n' + body + '\n</main>\n' + (footer_html or footer()) + f'\n<script src="{A}js/main.js" defer></script>\n</body>\n</html>\n'
    with open(os.path.join(OUT, filename), 'w') as fh:
        fh.write(doc)
    if not PROD and filename == 'index.html':
        inner = doc.split('<head>', 1)[1]
        headpart, rest = inner.split('</head>', 1)
        keep = '<title>Al-Khair Academy Website</title>\n' + '\n'.join(l for l in headpart.splitlines() if l.startswith(('<link rel="stylesheet"', '<link rel="preconnect"')))
        rest = rest.replace('<body>', '', 1).replace('</body>\n</html>\n', '')
        with open(os.path.join(OUT, 'preview-entry.html'), 'w') as fh:
            fh.write(keep + rest)

# ================= HOME (V6 minimal) =================
IG = 'https://www.instagram.com/al_khairacademy/'
YT = 'https://www.youtube.com/@AL-KHAIRACADEMYY'
SCHOOL['sameAs'] = [IG, YT]
ICON['ig'] = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".8"/></svg>'
ICON['yt'] = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2.5" y="5.5" width="19" height="13" rx="3.5"/><path d="M10 9.5v5l4.5-2.5z"/></svg>'
ICON['pin'] = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7-6.2-7-11.5A7 7 0 0119 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>'
ICON['mail'] = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="1"/><path d="M3 7l9 6 9-6"/></svg>'

def home_footer():
    return f'''<footer class="h-contact pattern" id="contact-info">
  <div class="wrap">
    <div class="top">
      <img src="{A}img/crest-160.png" width="72" height="69" alt="">
      <div class="stack-sm"><h2>Al-Khair Academy</h2><span class="t">Nurturing Every Child Like a Seed</span></div>
      <div class="btn-row"><a class="btn btn-light" href="{L('admissions', 'enquiry')}">Enquire Now</a><a class="btn btn-outline-light" href="{MAPS}" target="_blank" rel="noopener">Get Directions</a></div>
    </div>
    <div class="grid">
      <div><span class="k">Address</span><span class="v" style="font-weight:400">{ADDRESS}</span></div>
      <div><span class="k">Admissions · Call &amp; WhatsApp</span><a class="v" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><a href="https://wa.me/{WA}" target="_blank" rel="noopener" style="color:#C5CFDB;font-size:.9rem">Message on WhatsApp →</a></div>
      <div><span class="k">Email</span><a class="v" href="mailto:{EMAIL}">{EMAIL}</a></div>
    </div>
    <div class="grid row2c">
      <div><span class="k">Instagram</span><a class="v social" href="{IG}" target="_blank" rel="noopener">{ICON['ig']} @al_khairacademy</a></div>
      <div><span class="k">YouTube</span><a class="v social" href="{YT}" target="_blank" rel="noopener">{ICON['yt']} @AL-KHAIRACADEMYY</a></div>
      <div><span class="k">School</span><span class="v" style="font-weight:400">{BOARD} · Nursery to Class 8 · Est. 2018</span></div>
    </div>
    <div class="base">
      <span>© <span id="year">2026</span> Al-Khair Academy, Khajrana, Indore · DISE Code 23260104272 · Affiliation No. 82237</span>
      <a href="{L('privacy')}">Privacy Policy</a>
    </div>
  </div>
</footer>
<nav class="actionbar" aria-label="Quick contact">
  <a href="tel:{PHONE_TEL}">{ICON['phone']} Call</a>
  <a href="https://wa.me/{WA}" target="_blank" rel="noopener">{ICON['wa']} WhatsApp</a>
  <a class="go" href="{L('admissions', 'enquiry')}">Enquire Now</a>
</nav>'''

S = '(max-width: 700px) 50vw, 25vw'
home = f'''
<section class="opening"><div class="wrap">
  <img class="crest" src="{A}img/crest.png" width="720" height="695" alt="Al-Khair Academy crest">
  <div class="est">Established 2018 · Khajrana, Indore</div>
  <h1>Al-Khair Academy</h1>
  <p class="sub">Nurturing Every Child Like a Seed</p>
  <div class="vision"><span>Our Vision</span> Success Here and the Hereafter</div>
  <div class="btn-row"><a class="btn btn-primary" href="{L('admissions', 'enquiry')}">Enquire Now</a>
  <a class="btn btn-ghost" href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp Us</a></div>
  <div class="opening-photo"><div class="frame">{pic('hero-children', 'Al-Khair Academy students together at a school celebration', '(max-width: 1140px) 100vw, 1140px', eager=True)}</div></div>
  <div class="facts">
    <div><b>State Board</b><span>CBSE Pattern</span></div>
    <div><b>Nursery–8</b><span>Classes</span></div>
    <div><b>Montessori</b><span>Nursery, age 3+</span></div>
    <div><b>2018</b><span>Established</span></div>
  </div>
</div></section>

<section class="sec"><div class="wrap stack" style="justify-items:center;text-align:center">
  <span class="eyebrow">Our Belief</span>
  <p class="h-quote">Every child is unique. Education should help each child <em>discover their own potential.</em></p>
  <div class="rule center"><i></i></div>
</div></section>

<section class="sec soft"><div class="wrap">
  <div class="sec-head center"><span class="eyebrow">The 3C Framework</span><h2>Creativity · Confidence · Character</h2><div class="rule center"><i></i></div></div>
  <div class="h-c3">
    <figure>{C('montessori-grocer', 'Nursery children running a green grocer stall in a role-play activity', '(max-width: 700px) 100vw, 33vw', style='object-position:50% 40%')}<figcaption><b>Creativity</b><span>Imagining, making and solving, by hand.</span></figcaption></figure>
    <figure>{C('confidence', 'A student speaking on stage with a microphone', '(max-width: 700px) 100vw, 33vw', style='object-position:50% 22%')}<figcaption><b>Confidence</b><span>A voice on every stage, from assembly to olympiad.</span></figcaption></figure>
    <figure>{C('trip-heritage', 'Students standing together on an educational heritage visit', '(max-width: 700px) 100vw, 33vw')}<figcaption><b>Character</b><span>Honesty, respect and kindness, every day.</span></figcaption></figure>
  </div>
</div></section>

<section class="sec" id="methods"><div class="wrap">
  <div class="sec-head center"><span class="eyebrow">How We Teach</span><h2>Modern methods, rooted in faith</h2><div class="rule center"><i></i></div></div>
  <div class="teach">
    <a href="{L('gallery')}">{C('montessori-hospital', 'Nursery children playing doctor in a Montessori role-play corner', S)}<h3>Montessori Nursery</h3><p>Learning by doing, from age 3.</p></a>
    <a href="{PROPEL}" target="_blank" rel="noopener"><div class="tv pattern">{ICON['tv']}</div><h3>Smart Class</h3><p>Propel audio-visual lessons on smart TVs.</p></a>
    <a href="{UQ}" target="_blank" rel="noopener">{C('dua', 'Teachers and staff in dua at the annual function', S, style='object-position:50% 70%')}<h3>Understanding Quran</h3><p>Meaning, hadith, duas and sunnah, from a young age.</p></a>
    <a href="{L('community')}">{C('dance', 'Students forming a human pyramid at the annual function', S)}<h3>Activities</h3><p>Olympiads, sports, visits and the annual function.</p></a>
  </div>
</div></section>

<section class="sec soft"><div class="wrap">
  <div class="sec-head center"><span class="eyebrow">A Glimpse of Al-Khair</span><h2>Life at our school</h2><div class="rule center"><i></i></div></div>
  <div class="glimpse">
    <div class="cell big">{pic('independence', 'Independence Day programme on the Al-Khair Academy stage', '(max-width: 700px) 100vw, 50vw')}</div>
    <div class="cell wide">{pic('awards', 'Al-Khair Academy team receiving National Winner recognition at the Propel Shiksha Awards', '(max-width: 700px) 100vw, 50vw')}<span class="tag">National Winner · Propel Shiksha Awards</span></div>
    {C('kes-olympiad', 'Al-Khair students receiving a trophy at the KES Olympiad 2025', S)}
    {C('prizes', 'Young students with their prize trophies', S, style='object-position:50% 30%')}
    <div class="cell tall">{pic('trip-rajwada', 'Students on an educational visit to Rajwada, Indore', S, style='object-position:50% 75%')}</div>
    <div class="cell wide">{pic('trip-lalbagh', 'Students on an educational visit to Lal Bagh Palace, Indore', '(max-width: 700px) 100vw, 50vw')}</div>
    <div class="cell tall">{pic('flags', 'Young students performing with the tricolour', S, style='object-position:50% 30%')}</div>
    {C('sports-trophy', 'Al-Khair team with their trophy at an inter-school event', S)}
    {C('urooj-girls', 'Students at the UROOJ 2026 programme in Indore', S)}
  </div>
  <p style="margin-top:28px;text-align:center"><a class="link-arrow" href="{L('gallery')}">View the full gallery →</a></p>
</div></section>

<section class="sec tight"><div class="wrap">
  <!-- NOTICE: edit this line for the latest school announcement -->
  <div class="h-notice"><span class="tag">Notice</span><p>Admission enquiries are welcome for Nursery to Class 8. Nursery admission from age 3+.</p><a class="link-arrow" href="{L('admissions')}">Admission details →</a></div>
</div></section>'''
write('home', 'index.html',
      'Al-Khair Academy, Khajrana Indore | State Board School, CBSE Pattern, Nursery to Class 8',
      'Al-Khair Academy, Khajrana, Indore: State Board school with CBSE pattern from Montessori Nursery to Class 8, Understanding Quran, Propel smart classes and the 3C framework. Est. 2018.',
      home, [SCHOOL], footer_html=home_footer())

# ================= LEADERSHIP =================
def msg_card(initials, name, role, paras):
    body = ''.join(f'<p>{p}</p>' for p in paras)
    photo = {'PK': 'director', 'RK': 'principal'}[initials]
    return f'''<article class="msg-card">
  <div class="msg-top">
    <div class="portrait"><img src="{A}img/{photo}.jpg" width="480" height="600" alt="{name}, {role}" loading="lazy" style="width:100%;height:100%;object-fit:cover"></div>
    <div class="stack-sm"><span class="eyebrow">{role}</span><h3 style="font-size:1.7rem">{name}</h3></div>
  </div>
  <blockquote>{body}</blockquote>
</article>'''

leadership = page_head('Leadership', 'The people behind Al-Khair', 'Al-Khair Academy was founded in 2018 in Khajrana, Indore. Here is a word from the people who lead it.', 'Leadership') + f'''
<section class="sec"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Messages</span><h2>From our Director and Principal</h2><div class="rule"><i></i></div></div>
  <div class="duo">
    {msg_card('PK', 'Adv. Parvez Khan', 'Director', [
      'Assalamu Alaikum. A school is more than a building; it is a trust that parents place in us. At Al-Khair Academy, we take that trust seriously.',
      'Our aim is to give the children of Khajrana an education that prepares them for the world while keeping them rooted in their values: sound academics in the CBSE pattern, modern tools such as smart classes, and a clear understanding of their faith.',
      'We are grateful to work alongside the schools, organisations and well-wishers of Khajrana who share this commitment to our children\'s future.'])}
    {msg_card('RK', 'Adv. Rehana Khan', 'Founder &amp; Principal', [
      'Assalamu Alaikum. When we founded Al-Khair Academy in 2018, we began with one belief: every child is unique, and every child carries potential that deserves to be discovered.',
      'Education should not only fill a child with knowledge. It should help the child grow in creativity, in confidence and in good character. We try to understand each student, notice where they need support, and give that support with patience.',
      'Our aim is success for our children here and in the Hereafter. You are welcome to visit the school, meet our teachers and see this work for yourself.'])}
  </div>
</div></section>

<section class="sec soft"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Our Team</span><h2>Academic &amp; administrative team</h2><div class="rule"><i></i></div>
  <p>The people who run the school day to day and keep parents informed.</p></div>
  <!-- TEAM: duplicate a .leader block for each member of mid-level management -->
  <div class="team">
    <div class="leader"><div class="mono" aria-hidden="true">SF</div><h3>Mrs. Shabehina Farooqui</h3><span class="role">Coordinator</span></div>
    <div class="leader"><div class="mono" aria-hidden="true">RA</div><h3>Mrs. Rahat Ali</h3><span class="role">Office &amp; Administration</span></div>
  </div>
</div></section>

<section class="recog pattern" id="recognition"><div class="wrap">
  <div class="stack">
    <span class="award">PROPEL SHIKSHA AWARDS</span>
    <h2>National Winner</h2>
    <p class="lead" style="color:#D5DEE9">Al-Khair Academy's team was recognised as a National Winner at the Propel Shiksha Awards. For us, it reflects the daily work of our teachers in the classroom.</p>
  </div>
  <div class="org-media" style="grid-template-columns:1fr">
    <div class="frame">{pic('awards', 'Al-Khair Academy team receiving National Winner recognition at the Propel Shiksha Awards', '(max-width: 860px) 100vw, 45vw')}</div>
  </div>
</div></section>

<section class="sec"><div class="wrap split">
  <div class="stack"><span class="eyebrow">Since 2018</span><h2>Our story</h2><div class="rule"><i></i></div>
    <p>Al-Khair Academy was founded by Adv. Rehana Khan with a clear purpose: a school where every child is seen as an individual, where good marks and good manners matter equally, and where faith and learning grow together.</p>
    <p>Today the school serves families across Khajrana and Indore from Nursery to Class 8.</p></div>
  <div class="frame r43">{pic('awards-2', 'Al-Khair Academy team at the Propel Shiksha Awards')}</div>
</div></section>
{admissions_band()}
{contact_band()}'''
write('leadership', 'leadership.html', 'Leadership | Director & Principal | Al-Khair Academy, Khajrana Indore',
      'Messages from Adv. Parvez Khan, Director, and Adv. Rehana Khan, Founder & Principal of Al-Khair Academy, Khajrana, Indore, with the school team and Propel Shiksha Awards recognition.',
      leadership, [crumbs('leadership', 'Leadership')])

# ================= COMMUNITY =================
community = page_head('Community', 'Learning Together in Khajrana', 'Khajrana is a diverse neighbourhood of Indore. Its schools, organisations and well-wishers work together so that every child has more chances to learn, compete and grow.', 'Community') + f'''
<section class="sec"><div class="wrap">

  <div class="org" style="border-top:0;padding-top:0">
    <div class="stack">
      <span class="org-badge" aria-hidden="true">KES</span>
      <span class="eyebrow">Khajrana Educational Society</span><h2>Schools of Khajrana, together</h2><div class="rule"><i></i></div>
      <p>The Khajrana Educational Society (KES) brings the schools of Khajrana together under one common society. Through KES, children from different schools meet in inter-school competitions, olympiads and sports.</p>
      <p>Al-Khair students take part every year, and have brought home trophies from the KES Olympiad and inter-school events.</p>
    </div>
    <div class="org-media">
      {C('kes-olympiad', 'Al-Khair students receiving a trophy at the KES Olympiad 2025', '(max-width: 860px) 100vw, 50vw', cls='wide')}
      {C('sports-trophy', 'Al-Khair team with their trophy at an inter-school event', '(max-width: 860px) 50vw, 25vw')}
      {C('prizes', 'Young students with their prize trophies', '(max-width: 860px) 50vw, 25vw', style='object-position:50% 30%')}
    </div>
  </div>

  <div class="org flip">
    <div class="org-media">
      {C('urooj-stage', 'UROOJ 2026, Unfolding Stories of Success, held in Indore', '(max-width: 860px) 100vw, 50vw', cls='wide')}
      {C('urooj-girls', 'Students registering at the UROOJ 2026 programme', '(max-width: 860px) 50vw, 25vw')}
      {C('urooj-speech', 'A speaker addressing students at UROOJ 2026', '(max-width: 860px) 50vw, 25vw', style='object-position:65% 40%')}
    </div>
    <div class="stack">
      <span class="org-badge" aria-hidden="true">U</span>
      <span class="eyebrow">Urooj</span><h2>Guidance for our girls</h2><div class="rule"><i></i></div>
      <p>Urooj is a non-profit organisation in Khajrana that supports students, mainly girls, with guidance and support for their education.</p>
      <p>Its programmes, such as <em>UROOJ 2026: Unfolding Stories of Success</em> held in Indore, bring students together for recognition, mentorship and direction for the future.</p>
      <a class="link-arrow" href="{UROOJ}" target="_blank" rel="noopener">myurooj.in →</a>
    </div>
  </div>

  <div class="org">
    <div class="stack">
      <span class="org-badge" aria-hidden="true">★</span>
      <span class="eyebrow">Community &amp; Well-wishers</span><h2>A neighbourhood that celebrates together</h2><div class="rule"><i></i></div>
      <p>Philanthropists and well-wishers of Khajrana support education in many ways, from encouraging students to bringing the community together for occasions such as Jashn-e-Azadi, our celebration of Independence.</p>
    </div>
    <div class="org-media">
      {C('jashn-group', 'Community members at the Jashn-e-Azadi celebration', '(max-width: 860px) 100vw, 50vw', cls='wide', style='object-position:50% 35%')}
      {C('jashn-speech', 'Address at the Jashn-e-Azadi celebration', '(max-width: 860px) 50vw, 25vw', style='object-position:30% 40%')}
      {C('independence', 'Al-Khair students on stage on Independence Day', '(max-width: 860px) 50vw, 25vw')}
    </div>
  </div>
</div></section>

<section class="sec soft" id="visits"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Educational Visits</span><h2>Learning from our city</h2><div class="rule"><i></i></div>
  <p>Indore's heritage is our classroom too. Students visit places such as Rajwada and Lal Bagh Palace, where history and culture become real.</p></div>
  <div class="visits">
    <div class="tall cell">{pic('trip-rajwada', 'Students at Rajwada, Indore', '(max-width: 760px) 100vw, 25vw', style='object-position:50% 75%')}</div>
    <div class="wide cell">{pic('trip-lalbagh', 'Students at Lal Bagh Palace, Indore', '(max-width: 760px) 50vw, 50vw')}</div>
    {C('trip-hall', 'Students on an educational visit', '(max-width: 760px) 50vw, 25vw')}
    <div class="wide cell">{pic('trip-garden', 'Girls on an educational visit', '(max-width: 760px) 50vw, 50vw')}</div>
    {C('trip-heritage', 'Students at a heritage site', '(max-width: 760px) 50vw, 25vw')}
  </div>
</div></section>
{admissions_band()}
{contact_band()}'''
write('community', 'community.html', 'Community | KES, Urooj & Learning in Khajrana | Al-Khair Academy Indore',
      'How Al-Khair Academy learns together with Khajrana: Khajrana Educational Society olympiads and sports, Urooj guidance for girls, community celebrations and educational visits in Indore.',
      community, [crumbs('community', 'Community')])

# ================= GALLERY =================
G = [
 ('independence', 'Independence Day programme on the school stage', 'events', True),
 ('dance', 'Students forming a human pyramid at the annual function', 'events', False),
 ('awards', 'National Winner recognition at the Propel Shiksha Awards', 'achievements', False),
 ('kes-olympiad', 'Trophy presentation at the KES Olympiad 2025', 'achievements sports', False),
 ('montessori-hospital', 'Montessori role play: the hospital corner', 'classrooms', False),
 ('montessori-grocer', 'Montessori role play: the green grocer stall', 'classrooms', False),
 ('trip-rajwada', 'Educational visit to Rajwada, Indore', 'visits', False),
 ('trip-lalbagh', 'Educational visit to Lal Bagh Palace, Indore', 'visits', True),
 ('sports-trophy', 'Al-Khair team with their trophy at an inter-school event', 'sports achievements', False),
 ('prizes', 'Young students with their prize trophies', 'achievements', False),
 ('hero-children', 'Students in festive dress at a school celebration', 'events', False),
 ('trip-heritage', 'Students on a heritage visit', 'visits', False),
 ('confidence', 'A student speaking on stage', 'events', False),
 ('craft', 'Nursery children with their classroom craft wall', 'classrooms', False),
 ('trip-hall', 'Students on an educational visit', 'visits', False),
 ('urooj-stage', 'UROOJ 2026, Unfolding Stories of Success, Indore', 'community', True),
 ('urooj-girls', 'Students registering at UROOJ 2026', 'community', False),
 ('jashn-group', 'Jashn-e-Azadi community celebration', 'community', False),
 ('football', 'Students heading onto the football ground', 'sports', False),
 ('dua', 'Teachers and staff in dua at the annual function', 'events', False),
 ('flags', 'Young students performing with the tricolour', 'events', False),
 ('trip-garden', 'Girls on an educational visit', 'visits', False),
 ('awards-2', 'Al-Khair team at the Propel Shiksha Awards', 'achievements', False),
 ('award', 'A student receiving a prize with his family', 'events achievements', False),
 ('campus', 'Students walking to class past the school bus', 'campus', False),
 ('jashn-speech', 'Address at the Jashn-e-Azadi celebration', 'community', False),
]
POS = {'confidence': 'object-position:50% 30%', 'flags': 'object-position:50% 30%', 'trip-rajwada': 'object-position:50% 75%', 'campus': 'object-position:50% 60%'}
gal = ''.join(f'<button type="button" class="{"wide" if w else ""}" data-cat="{c}">{pic(n, a, "(max-width: 760px) 50vw, 33vw", full=True, style=POS.get(n, ""))}</button>' for n, a, c, w in G)
filters = ''.join(f'<button type="button" data-filter="{k}" aria-pressed="{"true" if k == "all" else "false"}">{v}</button>' for k, v in
  [('all', 'All'), ('events', 'Events'), ('achievements', 'Achievements'), ('classrooms', 'Classrooms'), ('sports', 'Sports'), ('visits', 'Educational Visits'), ('community', 'Community'), ('campus', 'Campus')])
gallery = page_head('Gallery', 'Life at Al-Khair', 'Moments from our classrooms, events, achievements, sports, visits and community. Tap any photo to view it full screen.', 'Gallery') + f'''
<section class="sec"><div class="wrap">
  <div class="filters" role="group" aria-label="Filter photos">{filters}</div>
  <div class="gallery">{gal}</div>
</div></section>
<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Photo viewer" hidden>
  <figure><img alt=""></figure>
  <p class="lb-cap"></p>
  <button class="lb-btn lb-close" type="button" aria-label="Close">×</button>
  <button class="lb-btn lb-prev" type="button" aria-label="Previous photo">‹</button>
  <button class="lb-btn lb-next" type="button" aria-label="Next photo">›</button>
</div>
{contact_band()}'''
write('gallery', 'gallery.html', 'Gallery | School Life at Al-Khair Academy, Khajrana Indore',
      'Photos of school life at Al-Khair Academy, Indore: Montessori classrooms, annual function, Propel Shiksha Awards, KES Olympiad, sports, community events and educational visits.',
      gallery, [crumbs('gallery', 'Gallery')])

# ================= ADMISSIONS =================
admissions = page_head('Admissions', 'Admissions &amp; Enquiry', 'Admission is open for Nursery to Class 8. Everything you need is on this page: eligibility, process, documents, uniform and the enquiry form.', 'Admissions') + f'''
<section class="sec tight"><div class="wrap">
  <div class="info-grid">
    <div class="info"><span class="k">Classes offered</span><span class="v">Nursery to Class 8</span></div>
    <div class="info"><span class="k">Nursery eligibility</span><span class="v">3 years and above</span></div>
    <div class="info"><span class="k">Board</span><span class="v">State Board, CBSE Pattern</span></div>
  </div>
</div></section>

<section class="sec soft"><div class="wrap split" style="align-items:start">
  <div class="stack">
    <span class="eyebrow">Admission Process</span><h2>How to apply</h2><div class="rule"><i></i></div>
    <ol class="steps">
      <li><div><b>Enquire</b>Send the enquiry form, message us on WhatsApp or call the school office.</div></li>
      <li><div><b>Visit the school</b>Meet the office team, see the campus and collect the admission form.</div></li>
      <li><div><b>Entrance test</b>Students appear for an entrance test. The office shares the details for your child's class.</div></li>
      <li><div><b>Submit documents</b>Hand in the completed form with the required documents.</div></li>
      <li><div><b>Confirmation</b>The office confirms admission and explains the next steps.</div></li>
    </ol>
    <div class="stack-sm" style="margin-top:12px"><span class="eyebrow">Required documents</span>
      <ul class="doclist"><li>Aadhaar Card</li><li>Samagra ID</li><li>Birth Certificate</li><li>Caste Certificate</li></ul>
      <p class="hint">Please confirm any class-specific requirements with the school office.</p></div>
  </div>
  {enquiry_form()}
</div></section>

<section class="sec"><div class="wrap split" style="align-items:start">
  <div class="stack"><span class="eyebrow">School Uniform</span><h2>Our uniform</h2><div class="rule"><i></i></div>
    <p>A checked shirt in brown, orange and blue with brown trousers for boys, and a matching checked blouse with a brown pinafore for girls.</p>
    <p class="hint">Please ask the office where to buy the uniform.</p>
    <div class="uniform">
      <figure>{pic('uniform-girls', 'Girls uniform: checked blouse with brown pinafore', '(max-width: 860px) 50vw, 260px')}<figcaption>Girls</figcaption></figure>
      <figure>{pic('uniform-boys', 'Boys uniform: checked shirt with brown trousers', '(max-width: 860px) 50vw, 260px')}<figcaption>Boys</figcaption></figure>
    </div>
  </div>
  <div class="stack" id="faq"><span class="eyebrow">FAQ</span><h2>Questions parents ask</h2><div class="rule"><i></i></div>{faq_html()}</div>
</div></section>
{contact_band()}'''
write('admissions', 'admissions.html', 'Admissions & Enquiry | Al-Khair Academy, Khajrana Indore',
      'Admissions at Al-Khair Academy, Indore for Nursery (age 3+, Montessori) to Class 8. State Board, CBSE pattern. Process, entrance test, documents, uniform, FAQ and enquiry form.',
      admissions, [crumbs('admissions', 'Admissions'), FAQ_SCHEMA])

# ================= CONTACT =================
contact = page_head('Contact', 'Visit us in Khajrana', 'We are happy to answer your questions. Call, send a WhatsApp message or visit the school.', 'Contact') + f'''
<section class="sec"><div class="wrap split" style="align-items:start">
  <div class="stack">
    <div class="contact-grid">
      <div><span class="k">Address</span><span class="v">{ADDRESS}</span></div>
      <div><span class="k">Admissions phone</span><a class="v" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></div>
      <div><span class="k">WhatsApp</span><a class="v" href="https://wa.me/{WA}" target="_blank" rel="noopener">{PHONE_DISPLAY}</a></div>
      <div><span class="k">Email</span><a class="v" href="mailto:{EMAIL}">{EMAIL}</a></div>
    </div>
    <div class="btn-row">
      <a class="btn btn-primary" href="{MAPS}" target="_blank" rel="noopener">Get Directions</a>
      <a class="btn btn-ghost" href="https://wa.me/{WA}" target="_blank" rel="noopener">Chat on WhatsApp</a>
    </div>
    <div class="frame r43">{pic('campus', 'Students walking to class at Al-Khair Academy', style='object-position:50% 60%')}</div>
    <p class="hint">Office &amp; Administration: Mrs. Rahat Ali</p>
  </div>
  {enquiry_form()}
</div></section>'''
write('contact', 'contact.html', 'Contact & Directions | Al-Khair Academy, Khajrana Indore',
      'Contact Al-Khair Academy, 57/2 Haji Colony, Khajrana, Indore 452016. Phone and WhatsApp +91 62646 72034, email, directions and admission enquiry.',
      contact, [crumbs('contact', 'Contact')])

# ================= PRIVACY / 404 =================
privacy = page_head('Policy', 'Privacy Policy', 'How Al-Khair Academy handles information shared through this website. Last updated October 2026.', 'Privacy Policy') + f'''
<section class="sec"><div class="wrap prose">
  <h2>Information we collect</h2>
  <p>When you send an admission enquiry, we collect the details you enter: parent or guardian name, student name, class sought, phone and WhatsApp numbers, preferred contact method and your message.</p>
  <h2>How we use it</h2>
  <ul><li>To respond to your enquiry and guide you through admission.</li><li>To contact you by your preferred method about that enquiry.</li></ul>
  <p>We do not sell or share your information with others for marketing. Enquiry data is kept only as long as needed for admission purposes.</p>
  <h2>WhatsApp and third-party services</h2>
  <p>If you choose to send your enquiry through WhatsApp, the message is handled under WhatsApp's own terms and privacy policy. This website may use Google Analytics to understand visits in aggregate.</p>
  <h2>Photographs</h2>
  <p>Photos on this website show school events and activities. If you would like a photo of your child removed, please contact the school office and we will remove it.</p>
  <h2>Student records</h2>
  <p>This website does not hold student records, results or other private school data.</p>
  <h2>Contact</h2>
  <p>For any privacy question or request, write to <a href="mailto:{EMAIL}">{EMAIL}</a> or call {PHONE_DISPLAY}.</p>
</div></section>'''
write('privacy', 'privacy.html', 'Privacy Policy | Al-Khair Academy',
      'Privacy policy of Al-Khair Academy, Indore: what information the admission enquiry form collects and how it is used.',
      privacy, [crumbs('privacy', 'Privacy Policy')], active='none')

nf = f'''<section class="sec"><div class="wrap" style="text-align:center;display:grid;gap:18px;justify-items:center">
  <img src="{A}img/crest-160.png" width="96" height="92" alt="">
  <span class="eyebrow">Page not found</span><h1>This page could not be found</h1><div class="rule center"><i></i></div>
  <p class="lead">The link may be old or mistyped. Use the menu above, or go back to the home page.</p>
  <div class="btn-row" style="justify-content:center"><a class="btn btn-primary" href="{L('home')}">Go to Home</a><a class="btn btn-ghost" href="{L('contact')}">Contact the school</a></div>
</div></section>'''
write('home', '404.html', 'Page Not Found | Al-Khair Academy', 'The page you are looking for could not be found.', nf, noindex=True, active='none')
print('built', MODE)
