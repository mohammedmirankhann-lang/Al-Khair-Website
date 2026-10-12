"""Shared building blocks: URLs, images, icons, header, footers, forms and bands.

The site is built in one of two modes:
  prod     clean URLs (/leadership) and root-relative assets (/assets/...), for alkhairacademy.in
  preview  file links (leadership.html) and relative assets, for opening the pages without a server
"""
import hashlib
import json
import os

from PIL import Image

import config as cfg
from content import CLASS_OPTIONS, FOCUS

ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'public', 'assets')
IMG_DIR = os.path.join(ASSETS_DIR, 'img')

_prod = True


def set_mode(prod):
    global _prod
    _prod = prod


def is_prod():
    return _prod


# ---------- URLs ----------
def asset(path):
    """URL of a file under public/assets, e.g. asset('img/crest.png')."""
    return ('/assets/' if _prod else 'assets/') + path


def versioned(path):
    """Asset URL with a short content hash (?v=...), so browsers fetch the new file
    as soon as it changes even though /assets/css and /assets/js are cached for a year."""
    with open(os.path.join(ASSETS_DIR, path), 'rb') as fh:
        digest = hashlib.sha1(fh.read()).hexdigest()[:10]
    return f'{asset(path)}?v={digest}'


def root(path):
    """URL of a file at the site root, e.g. root('favicon.ico')."""
    return ('/' if _prod else '') + path


def link(key, anchor=''):
    """URL of a page by its key in config.PAGES, optionally with #anchor."""
    slug = cfg.PAGES[key]
    url = '/' + slug if _prod else (slug + '.html' if slug else './')
    return url + ('#' + anchor if anchor else '')


def canonical(key):
    return cfg.DOMAIN + '/' + cfg.PAGES.get(key, '')


WHATSAPP_URL = f'https://wa.me/{cfg.WHATSAPP}'
TEL_URL = f'tel:{cfg.PHONE_TEL}'
MAIL_URL = f'mailto:{cfg.EMAIL}'


def ext(url, text, cls=''):
    """External link opening in a new tab."""
    c = f' class="{cls}"' if cls else ''
    return f'<a{c} href="{url}" target="_blank" rel="noopener">{text}</a>'


# ---------- images ----------
_sizes = {}


def image_size(name):
    if name not in _sizes:
        with Image.open(os.path.join(IMG_DIR, name + '.jpg')) as im:
            _sizes[name] = im.size
    return _sizes[name]


def pic(name, alt, sizes='(max-width: 860px) 100vw, 50vw', eager=False, full=False):
    """Responsive photo: 800px file by default, full file (max 1400px) on wide screens.
    The focal point from content.FOCUS is applied automatically."""
    w, h = image_size(name)
    w_small = image_size(name + '-800')[0]
    attrs = f' style="object-position:{FOCUS[name]}"' if name in FOCUS else ''
    if full:
        attrs += f' data-full="{asset(f"img/{name}.jpg")}"'
    load = 'eager" fetchpriority="high' if eager else 'lazy'
    small, large = asset(f'img/{name}-800.jpg'), asset(f'img/{name}.jpg')
    return (f'<picture><img src="{small}" srcset="{small} {w_small}w, {large} {w}w" sizes="{sizes}" '
            f'width="{w}" height="{h}" alt="{alt}" loading="{load}" decoding="async"{attrs}></picture>')


def cell(name, alt, sizes, cls=''):
    """A photo that fills a fixed-shape box (shape set in CSS by the parent grid)."""
    return f'<div class="cell{" " + cls if cls else ""}">' + pic(name, alt, sizes) + '</div>'


# ---------- icons ----------
ICON = {
    'menu': '<svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18" stroke="currentColor" stroke-width="1.8" fill="none"/></svg>',
    'phone': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 3h4l2 5-2.5 1.5a11 11 0 005 5L15 12l5 2v4a2 2 0 01-2 2A16 16 0 013 5a2 2 0 012-2z"/></svg>',
    'wa': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3.5 20.5l1.3-4.2A8.5 8.5 0 1112 20.5a8.4 8.4 0 01-4.3-1.2z"/><path d="M9 8.5c0 3 2.5 6 6 6.5l1-1.5-2-1-1 1c-1-.5-2-1.5-2.5-2.5l1-1-1-2z"/></svg>',
    'tv': '<svg viewBox="0 0 36 36" aria-hidden="true"><rect x="4" y="7" width="28" height="18" rx="1"/><path d="M13 31h10M18 25v6"/><path class="g" d="M15 12v8l7-4z"/></svg>',
    'quran': '<svg viewBox="0 0 36 36" aria-hidden="true"><path d="M18 10c-4-3-9-3-13-2v19c4-1 9-1 13 2 4-3 9-3 13-2V8c-4-1-9-1-13 2z"/><path d="M18 10v19"/><path class="g" d="M9 14h5M9 18h5M22 14h5M22 18h5"/></svg>',
    'ig': '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".8"/></svg>',
    'yt': '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2.5" y="5.5" width="19" height="13" rx="3.5"/><path d="M10 9.5v5l4.5-2.5z"/></svg>',
}


# ---------- small pieces ----------
def rule(center=False):
    return f'<div class="rule{" center" if center else ""}"><i></i></div>'


def sec_head(eyebrow, title, intro='', center=False):
    p = f'\n  <p>{intro}</p>' if intro else ''
    return (f'<div class="sec-head{" center" if center else ""}"><span class="eyebrow">{eyebrow}</span>'
            f'<h2>{title}</h2>{rule(center)}{p}</div>')


def page_head(eyebrow, h1, lead, label):
    """Heading band at the top of every inner page, with breadcrumb."""
    return f'''<section class="page-head"><div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="{link('home')}">Home</a> / {label}</nav>
  <span class="eyebrow">{eyebrow}</span><h1>{h1}</h1>{rule()}
  <p class="lead">{lead}</p></div></section>'''


def legal_line():
    return (f'© <span id="year">2026</span> {cfg.NAME}, Khajrana, Indore · DISE Code {cfg.DISE_CODE} · '
            f'Affiliation No. {cfg.AFFILIATION_NO}')


# ---------- page frame ----------
def head(key, title, desc, schema=(), noindex=False):
    canon = canonical(key)
    ld = ''.join('<script type="application/ld+json">' + json.dumps(s, ensure_ascii=False) + '</script>\n'
                 for s in schema)
    robots = '<meta name="robots" content="noindex">' if noindex else ''
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
<meta property="og:site_name" content="{cfg.NAME}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{cfg.DOMAIN}/assets/img/og-image.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:locale" content="en_IN">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{root('favicon.ico')}" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="{asset('img/favicon-32.png')}">
<link rel="apple-touch-icon" href="{root('apple-touch-icon.png')}">
<link rel="manifest" href="{root('site.webmanifest')}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{cfg.FONTS}">
<link rel="stylesheet" href="{versioned('css/style.css')}">
{ld}</head>
<body>'''


NAV = [('home', 'Home'), ('leadership', 'Leadership'), ('community', 'Community'),
       ('gallery', 'Gallery'), ('admissions', 'Admissions'), ('contact', 'Contact')]


def header(active):
    current = ' aria-current="page"'
    items = '\n    '.join(
        f'<a href="{link(k)}"{current if k == active else ""}>{label}</a>' for k, label in NAV)
    return f'''<a class="skip" href="#main">Skip to content</a>
<div class="strip"><div class="wrap">
  <span>{cfg.BOARD} · {cfg.CLASSES} · Est. <b>{cfg.FOUNDED}</b></span>
  <span>Admissions: <a href="{TEL_URL}">{cfg.PHONE_DISPLAY}</a></span>
</div></div>
<header class="site-header"><div class="wrap hdr">
  <a class="brand" href="{link('home')}" aria-label="{cfg.NAME}, home">
    <img src="{asset('img/crest-160.png')}" width="54" height="52" alt="">
    <span><span class="brand-name">AL-KHAIR ACADEMY</span><span class="brand-tag">{cfg.TAGLINE}</span></span>
  </a>
  <button class="menu-btn" type="button" aria-controls="site-nav" aria-expanded="false" aria-label="Open menu">{ICON['menu']}</button>
  <nav class="nav" id="site-nav" aria-label="Main">
    {items}
    <a class="btn btn-primary" href="{link('admissions', 'enquiry')}">Enquire Now</a>
  </nav>
</div></header>'''


def actionbar():
    """Fixed Call / WhatsApp / Enquire bar on phones."""
    return f'''<nav class="actionbar" aria-label="Quick contact">
  <a href="{TEL_URL}">{ICON['phone']} Call</a>
  {ext(WHATSAPP_URL, ICON['wa'] + ' WhatsApp')}
  <a class="go" href="{link('admissions', 'enquiry')}">Enquire Now</a>
</nav>'''


def footer():
    """Footer for inner pages: brand, page links, contact links."""
    explore = [(link('home', 'methods'), 'How We Teach')] + [(link(k), label) for k, label in NAV[1:]]
    explore_li = '\n      '.join(f'<li><a href="{u}">{t}</a></li>' for u, t in explore)
    return f'''<footer class="site-footer">
  <div class="wrap foot">
    <div class="foot-brand">
      <img src="{asset('img/crest-160.png')}" width="64" height="62" alt="">
      <span class="n">AL-KHAIR ACADEMY</span>
      <span class="t">{cfg.VISION}</span>
      <span>{cfg.ADDRESS}</span>
    </div>
    <div><h4>Explore</h4><ul>
      {explore_li}
    </ul></div>
    <div><h4>Contact</h4><ul>
      <li><a href="{TEL_URL}">{cfg.PHONE_DISPLAY}</a></li>
      <li>{ext(WHATSAPP_URL, 'WhatsApp the office')}</li>
      <li><a href="{MAIL_URL}">{cfg.EMAIL}</a></li>
      <li>{ext(cfg.MAPS, 'Get directions')}</li>
    </ul></div>
  </div>
  <div class="foot-base"><div class="wrap">
    <span>{legal_line()}</span>
    <span><a href="{link('privacy')}">Privacy Policy</a></span>
  </div></div>
</footer>
{actionbar()}'''


def home_footer():
    """Footer for the home page: one complete contact block, no page links."""
    return f'''<footer class="h-contact pattern" id="contact-info">
  <div class="wrap">
    <div class="top">
      <img src="{asset('img/crest-160.png')}" width="72" height="69" alt="">
      <div class="stack-sm"><h2>{cfg.NAME}</h2><span class="t">{cfg.TAGLINE}</span></div>
      <div class="btn-row"><a class="btn btn-light" href="{link('admissions', 'enquiry')}">Enquire Now</a>{ext(cfg.MAPS, 'Get Directions', 'btn btn-outline-light')}</div>
    </div>
    <div class="grid">
      <div><span class="k">Address</span><span class="v plain">{cfg.ADDRESS}</span></div>
      <div><span class="k">Admissions · Call &amp; WhatsApp</span><a class="v" href="{TEL_URL}">{cfg.PHONE_DISPLAY}</a>{ext(WHATSAPP_URL, 'Message on WhatsApp →', 'wa-link')}</div>
      <div><span class="k">Email</span><a class="v" href="{MAIL_URL}">{cfg.EMAIL}</a></div>
    </div>
    <div class="grid row2c">
      <div><span class="k">Instagram</span>{ext(cfg.INSTAGRAM, ICON['ig'] + ' ' + cfg.INSTAGRAM_HANDLE, 'v social')}</div>
      <div><span class="k">YouTube</span>{ext(cfg.YOUTUBE, ICON['yt'] + ' ' + cfg.YOUTUBE_HANDLE, 'v social')}</div>
      <div><span class="k">School</span><span class="v plain">{cfg.BOARD} · {cfg.CLASSES} · Est. {cfg.FOUNDED}</span></div>
    </div>
    <div class="base">
      <span>{legal_line()}</span>
      <a href="{link('privacy')}">Privacy Policy</a>
    </div>
  </div>
</footer>
{actionbar()}'''


# ---------- shared sections ----------
def contact_band():
    return f'''<section class="cband pattern" aria-label="Contact"><div class="wrap">
  <div><span class="k">Visit us</span><h2>{cfg.NAME}</h2><p class="addr">{cfg.ADDRESS}</p>
    <p class="dir">{ext(cfg.MAPS, 'Get directions →')}</p></div>
  <div><span class="k">Call</span><a href="{TEL_URL}">{cfg.PHONE_DISPLAY}</a></div>
  <div><span class="k">WhatsApp</span>{ext(WHATSAPP_URL, 'Message the office')}</div>
  <div><span class="k">Email</span><a href="{MAIL_URL}">{cfg.EMAIL}</a></div>
</div></section>'''


def admissions_band():
    return f'''<section class="band pattern"><div class="wrap">
  <div class="stack-sm"><span class="eyebrow">Admissions</span><h2>Nursery to Class 8</h2>
  <p>Nursery admission from age 3+. Visit the school, meet our team and ask your questions.</p></div>
  <div class="btn-row"><a class="btn btn-light" href="{link('admissions', 'enquiry')}">Enquire Now</a>
  <a class="btn btn-outline-light" href="{link('admissions')}">Admission details</a></div>
</div></section>'''


def enquiry_form():
    """Admission enquiry form (handled by public/assets/js/main.js). Used on Admissions and Contact."""
    opts = ''.join(f'<option>{c}</option>' for c in CLASS_OPTIONS)
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
  <p class="hint">By sending this form you agree to be contacted about admissions. See our <a href="{link('privacy')}">privacy policy</a>.</p>
</form>
<div class="confirm" tabindex="-1" hidden>
  <b>Thank you</b>
  <p></p>
  <a class="btn btn-primary" href="#" target="_blank" rel="noopener">Send on WhatsApp</a>
</div>
</div>'''


def breadcrumb_schema(key, label):
    return {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': cfg.DOMAIN + '/'},
        {'@type': 'ListItem', 'position': 2, 'name': label, 'item': canonical(key)}]}
