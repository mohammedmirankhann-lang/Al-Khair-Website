"""Gallery: photos in sections with sub-headings, a filter bar and a full-screen viewer (behaviour in main.js)."""
from components import breadcrumb_schema, contact_band, page_head, pic
from content import GALLERY
from pages import Page

SIZES = '(max-width: 760px) 50vw, 33vw'


def section(key, title, photos):
    tiles = ''.join(f'<button type="button">{pic(n, alt, SIZES, full=True)}</button>' for n, alt in photos)
    return f'''<section class="g-group" id="{key}" data-cat="{key}" aria-labelledby="{key}-title">
    <div class="g-head"><h2 id="{key}-title">{title}</h2><span class="g-count">{len(photos)} photos</span></div>
    <div class="g-grid">{tiles}</div>
  </section>'''


def render():
    chips = [('all', 'All')] + [(key, label) for key, _, label, _ in GALLERY]
    filters = ''.join(f'<button type="button" data-filter="{k}" aria-pressed="{str(k == "all").lower()}">{label}</button>'
                      for k, label in chips)
    sections = '\n  '.join(section(key, title, photos) for key, title, _, photos in GALLERY)
    body = page_head('Gallery', 'Life at Al-Khair',
                     'Moments from our classrooms, events, achievements, sports, visits and community. '
                     'Tap any photo to view it full screen.', 'Gallery') + f'''
<section class="sec"><div class="wrap gallery">
  <div class="filters" role="group" aria-label="Filter photos">{filters}</div>
  {sections}
</div></section>
<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Photo viewer" hidden>
  <figure><img alt=""></figure>
  <p class="lb-cap"></p>
  <button class="lb-btn lb-close" type="button" aria-label="Close">×</button>
  <button class="lb-btn lb-prev" type="button" aria-label="Previous photo">‹</button>
  <button class="lb-btn lb-next" type="button" aria-label="Next photo">›</button>
</div>
{contact_band()}'''
    return Page(
        key='gallery', file='gallery.html',
        title='Gallery: School Life | Al-Khair Academy, Khajrana Indore',
        description=('Photos of school life at Al-Khair Academy, Indore: events, Montessori classrooms, '
                     'KES Olympiad, plantation drive, educational visits and community.'),
        body=body, schema=[breadcrumb_schema('gallery', 'Gallery')],
    )
