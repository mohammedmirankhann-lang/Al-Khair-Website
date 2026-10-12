"""Gallery: filterable photo grid with a full-screen viewer (behaviour in main.js)."""
from components import breadcrumb_schema, contact_band, page_head, pic
from content import GALLERY, GALLERY_FILTERS
from pages import Page


def render():
    filters = ''.join(f'<button type="button" data-filter="{k}" aria-pressed="{str(k == "all").lower()}">{label}</button>'
                      for k, label in GALLERY_FILTERS)
    photos = ''.join(f'<button type="button" data-cat="{cats}">{pic(n, alt, "(max-width: 760px) 50vw, 33vw", full=True)}</button>'
                     for n, alt, cats in GALLERY)
    body = page_head('Gallery', 'Life at Al-Khair',
                     'Moments from our classrooms, events, achievements, sports, visits and community. '
                     'Tap any photo to view it full screen.', 'Gallery') + f'''
<section class="sec"><div class="wrap">
  <div class="filters" role="group" aria-label="Filter photos">{filters}</div>
  <div class="gallery">{photos}</div>
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
        title='Gallery | School Life at Al-Khair Academy, Khajrana Indore',
        description=('Photos of school life at Al-Khair Academy, Indore: Montessori classrooms, annual function, '
                     'Propel Shiksha Awards, KES Olympiad, sports, community events and educational visits.'),
        body=body, schema=[breadcrumb_schema('gallery', 'Gallery')],
    )
