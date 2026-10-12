"""Home: crest and vision, belief, 3C, how we teach, a glimpse of school life, notice."""
import config as cfg
from components import WHATSAPP_URL, ICON, asset, cell, ext, link, pic, rule, sec_head
from content import NOTICE
from pages import Page

QUARTER = '(max-width: 700px) 50vw, 25vw'
THIRD = '(max-width: 700px) 100vw, 33vw'
SEED = '(max-width: 700px) 33vw, 300px'

GLIMPSE = [
    ('stage-dance', 'Nursery students performing on Independence Day'),
    ('awards', 'Al-Khair Academy team receiving National Winner recognition at the Propel Shiksha Awards'),
    ('kes-olympiad', 'Al-Khair students receiving a trophy at the KES Olympiad 2025'),
    ('gandhi-smile', 'A smiling student dressed as Mahatma Gandhi on Independence Day'),
    ('hero-children', 'Smiling Al-Khair students in festive dress at a school celebration'),
    ('trip-lalbagh', 'Students on an educational visit to Lal Bagh Palace, Indore'),
    ('prizes', 'Young students with their prize trophies'),
    ('principal-office', 'The Principal welcoming a young student with a gift'),
]


def opening():
    return f'''<section class="opening"><div class="wrap">
  <img class="crest" src="{asset('img/crest.png')}" width="720" height="695" alt="Al-Khair Academy crest">
  <div class="est">Established {cfg.FOUNDED} · Khajrana, Indore</div>
  <h1>{cfg.NAME}</h1>
  <p class="sub">{cfg.TAGLINE}</p>
  <div class="vision"><span>Our Vision</span> {cfg.VISION}</div>
  <div class="btn-row"><a class="btn btn-primary" href="{link('admissions', 'enquiry')}">Enquire Now</a>
  {ext(WHATSAPP_URL, 'WhatsApp Us', 'btn btn-ghost')}</div>
  <div class="opening-photo"><div class="frame">{pic('stage-dance', 'Nursery students performing on the Al-Khair Academy stage in front of the school crest', '(max-width: 1140px) 100vw, 1140px', eager=True)}</div></div>
  <div class="facts">
    <div><b>State Board</b><span>CBSE Pattern</span></div>
    <div><b>Nursery–8</b><span>Classes</span></div>
    <div><b>Montessori</b><span>Nursery, age 3+</span></div>
    <div><b>{cfg.FOUNDED}</b><span>Established</span></div>
  </div>
</div></section>'''


def belief():
    return f'''<section class="sec"><div class="wrap seed">
  <div class="stack seed-text">
    <span class="eyebrow">Our Belief</span>
    <p class="h-quote">Every child is unique. Like a seed, each one already holds <em>everything it can become.</em></p>
    {rule(center=True)}
    <p class="muted">With care, patience and the right conditions, it grows. That is how we see every child who walks through our doors.</p>
  </div>
  <div class="seed-photos">
    {cell('plant-girl-1', 'A student planting a sapling in front of the Al-Khair Academy crest', SEED)}
    {cell('plant-boy', 'A student potting a plant during the school plantation drive', SEED)}
    {cell('plant-girl-3', 'A student caring for a young plant at school', SEED)}
  </div>
</div></section>'''


def three_c():
    def fig(name, alt, title, text):
        return f'<figure>{cell(name, alt, THIRD)}<figcaption><b>{title}</b><span>{text}</span></figcaption></figure>'
    return f'''<section class="sec soft"><div class="wrap">
  {sec_head('The 3C Framework', 'Creativity · Confidence · Character', center=True)}
  <div class="h-c3">
    {fig('costume-drama', 'Students in costume performing a history drama on stage', 'Creativity', 'Drama, craft and role play that spark imagination.')}
    {fig('tricolour-dance', 'Young students dancing with tricolour ribbons on stage', 'Confidence', 'A voice on every stage, from assembly to olympiad.')}
    {fig('freedom-fighters', 'Students dressed as freedom fighters on Independence Day', 'Character', 'Honesty, respect and love for the nation, every day.')}
  </div>
</div></section>'''


def how_we_teach():
    return f'''<section class="sec" id="methods"><div class="wrap">
  {sec_head('How We Teach', 'Modern methods, rooted in faith', center=True)}
  <div class="teach">
    <a href="{link('gallery')}">{cell('montessori-hospital', 'Nursery children playing doctor in a Montessori role-play corner', QUARTER)}<h3>Montessori Nursery</h3><p>Learning by doing, from age 3.</p></a>
    {ext(cfg.PROPEL, f'<div class="tv pattern">{ICON["tv"]}</div><h3>Smart Class</h3><p>Propel audio-visual lessons on smart TVs.</p>')}
    {ext(cfg.UNDERSTAND_QURAN, f'<div class="tv pattern">{ICON["quran"]}</div><h3>Understanding Quran</h3><p>Meaning, hadith, duas and sunnah, from a young age.</p>')}
    <a href="{link('community')}">{cell('football-team', 'Al-Khair students lined up for a football match', QUARTER)}<h3>Activities</h3><p>Olympiads, sports, visits and the annual function.</p></a>
  </div>
</div></section>'''


def glimpse():
    cells = '\n    '.join(cell(n, alt, QUARTER) for n, alt in GLIMPSE)
    return f'''<section class="sec soft"><div class="wrap">
  {sec_head('A Glimpse of Al-Khair', 'Life at our school', center=True)}
  <div class="glimpse">
    {cells}
  </div>
  <p class="more"><a class="link-arrow" href="{link('gallery')}">View the full gallery →</a></p>
</div></section>'''


def notice():
    return f'''<section class="sec tight"><div class="wrap">
  <div class="h-notice"><span class="tag">Notice</span><p>{NOTICE}</p><a class="link-arrow" href="{link('admissions')}">Admission details →</a></div>
</div></section>'''


def render():
    return Page(
        key='home', file='index.html',
        title='Al-Khair Academy, Khajrana Indore | State Board School, CBSE Pattern, Nursery to Class 8',
        description=('Al-Khair Academy, Khajrana, Indore: State Board school with CBSE pattern from Montessori '
                     'Nursery to Class 8, Understanding Quran, Propel smart classes and the 3C framework. Est. 2018.'),
        body='\n\n'.join([opening(), belief(), three_c(), how_we_teach(), glimpse(), notice()]),
        schema=[cfg.SCHOOL_SCHEMA],
        home_footer=True,
    )
