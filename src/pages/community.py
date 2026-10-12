"""Community: KES, Urooj, community celebrations, educational visits."""
import config as cfg
from components import admissions_band, breadcrumb_schema, cell, contact_band, ext, page_head, rule, sec_head
from pages import Page

WIDE = '(max-width: 860px) 100vw, 50vw'
SMALL = '(max-width: 860px) 50vw, 25vw'


def org(badge, eyebrow, title, text, photos, flip=False):
    """A partner block: text on one side, one wide and two square photos on the other."""
    (n1, a1), (n2, a2), (n3, a3) = photos
    media = f'''<div class="org-media">
      {cell(n1, a1, WIDE, 'wide')}
      {cell(n2, a2, SMALL)}
      {cell(n3, a3, SMALL)}
    </div>'''
    words = f'''<div class="stack">
      <span class="org-badge" aria-hidden="true">{badge}</span>
      <span class="eyebrow">{eyebrow}</span><h2>{title}</h2>{rule()}
      {text}
    </div>'''
    inner = media + '\n    ' + words if flip else words + '\n    ' + media
    return f'''<div class="org{' flip' if flip else ''}">
    {inner}
  </div>'''


def render():
    kes = org('KES', 'Khajrana Educational Society', 'Schools of Khajrana, together', '''<p>The Khajrana Educational Society (KES) brings the schools of Khajrana together under one common society. Through KES, children from different schools meet in inter-school competitions, olympiads and sports.</p>
      <p>Al-Khair students take part every year, and have brought home trophies from the KES Olympiad and inter-school events.</p>''', [
        ('kes-olympiad', 'Al-Khair students receiving a trophy at the KES Olympiad 2025'),
        ('sports-trophy', 'Al-Khair team with their trophy at an inter-school event'),
        ('prizes', 'Young students with their prize trophies')])

    urooj = org('U', 'Urooj', 'Guidance for our girls', f'''<p>Urooj is a non-profit organisation in Khajrana that supports students, mainly girls, with guidance and support for their education.</p>
      <p>Its programmes, such as <em>UROOJ 2026: Unfolding Stories of Success</em> held in Indore, bring students together for recognition, mentorship and direction for the future.</p>
      {ext(cfg.UROOJ, 'myurooj.in →', 'link-arrow')}''', [
        ('urooj-stage', 'UROOJ 2026, Unfolding Stories of Success, held in Indore'),
        ('urooj-girls', 'Students registering at the UROOJ 2026 programme'),
        ('urooj-speech', 'A speaker addressing students at UROOJ 2026')], flip=True)

    well_wishers = org('★', 'Community &amp; Well-wishers', 'A neighbourhood that celebrates together', '''<p>Philanthropists and well-wishers of Khajrana support education in many ways, from encouraging students to bringing the community together for occasions such as Jashn-e-Azadi, our celebration of Independence.</p>''', [
        ('jashn-group', 'Community members at the Jashn-e-Azadi celebration'),
        ('jashn-speech', 'Address at the Jashn-e-Azadi celebration'),
        ('independence', 'Al-Khair students on stage on Independence Day')])

    body = page_head('Community', 'Learning Together in Khajrana',
                     'Khajrana is a diverse neighbourhood of Indore. Its schools, organisations and well-wishers '
                     'work together so that every child has more chances to learn, compete and grow.',
                     'Community') + f'''
<section class="sec"><div class="wrap">
  {kes}
  {urooj}
  {well_wishers}
</div></section>

<section class="sec soft" id="visits"><div class="wrap">
  {sec_head('Educational Visits', 'Learning from our city', "Indore's heritage is our classroom too. Students visit places such as Rajwada and Lal Bagh Palace, where history and culture become real.")}
  <div class="visits">
    {cell('trip-lalbagh', 'Students at Lal Bagh Palace, Indore', '(max-width: 760px) 100vw, 50vw', 'w')}
    {cell('trip-garden', 'Girls on an educational visit', '(max-width: 760px) 100vw, 50vw', 'w')}
    {cell('trip-rajwada', 'Students at Rajwada, Indore', '(max-width: 760px) 50vw, 33vw')}
    {cell('trip-hall', 'Students on an educational visit', '(max-width: 760px) 50vw, 33vw')}
    {cell('trip-heritage', 'Students at a heritage site', '(max-width: 760px) 50vw, 33vw')}
  </div>
</div></section>
{admissions_band()}
{contact_band()}'''
    return Page(
        key='community', file='community.html',
        title='Community | KES, Urooj & Learning in Khajrana | Al-Khair Academy Indore',
        description=('How Al-Khair Academy learns together with Khajrana: Khajrana Educational Society olympiads '
                     'and sports, Urooj guidance for girls, community celebrations and educational visits in Indore.'),
        body=body, schema=[breadcrumb_schema('community', 'Community')],
    )
