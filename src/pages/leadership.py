"""Leadership: Director's and Principal's messages, team, recognition, our story."""
import config as cfg
from components import (admissions_band, asset, breadcrumb_schema, contact_band, page_head, pic, rule,
                        sec_head)
from content import MESSAGES, TEAM
from pages import Page


def message_card(photo, name, role, paragraphs):
    text = ''.join(f'<p>{p}</p>' for p in paragraphs)
    return f'''<article class="msg-card">
  <div class="msg-top">
    <div class="portrait"><img src="{asset(f'img/{photo}.jpg')}" width="480" height="600" alt="{name}, {role}" loading="lazy"></div>
    <div class="stack-sm"><span class="eyebrow">{role}</span><h3>{name}</h3></div>
  </div>
  <blockquote>{text}</blockquote>
</article>'''


def team_member(initials, name, role):
    return (f'<div class="leader"><div class="mono" aria-hidden="true">{initials}</div>'
            f'<h3>{name}</h3><span class="role">{role}</span></div>')


def render():
    cards = '\n    '.join(message_card(*m) for m in MESSAGES)
    team = '\n    '.join(team_member(*t) for t in TEAM)
    body = page_head('Leadership', 'The people behind Al-Khair',
                     'Al-Khair Academy was founded in 2018 in Khajrana, Indore. '
                     'Here is a word from the people who lead it.', 'Leadership') + f'''
<section class="sec"><div class="wrap">
  {sec_head('Messages', 'From our Director and Principal')}
  <div class="duo">
    {cards}
  </div>
</div></section>

<section class="sec soft"><div class="wrap">
  {sec_head('Our Team', 'Academic &amp; administrative team', 'The people who run the school day to day and keep parents informed.')}
  <div class="team">
    {team}
  </div>
</div></section>

<section class="recog pattern" id="recognition"><div class="wrap">
  <div class="stack">
    <span class="award">PROPEL SHIKSHA AWARDS</span>
    <h2>National Winner</h2>
    <p class="lead">Al-Khair Academy's team was recognised as a National Winner at the Propel Shiksha Awards. For us, it reflects the daily work of our teachers in the classroom.</p>
  </div>
  <div class="frame">{pic('awards', 'Al-Khair Academy team receiving National Winner recognition at the Propel Shiksha Awards', '(max-width: 860px) 100vw, 45vw')}</div>
</div></section>

<section class="sec"><div class="wrap split">
  <div class="stack"><span class="eyebrow">Since 2018</span><h2>Our story</h2>{rule()}
    <p>Al-Khair Academy was founded by Adv. Rehana Khan with a clear purpose: a school where every child is seen as an individual, where good marks and good manners matter equally, and where faith and learning grow together.</p>
    <p>Today the school serves families across Khajrana and Indore from Nursery to Class 8. It is run by {cfg.SOCIETY} and recognised by the {cfg.RECOGNISED_BY}.</p></div>
  <div class="frame r43">{pic('independence', 'Al-Khair Academy students on stage at the school Independence Day programme')}</div>
</div></section>
{admissions_band()}
{contact_band()}'''
    return Page(
        key='leadership', file='leadership.html',
        title='Leadership | Director & Principal | Al-Khair Academy, Khajrana Indore',
        description=('Messages from Adv. Parvez Khan, Director, and Adv. Rehana Khan, Founder & Principal of '
                     'Al-Khair Academy, Khajrana, Indore, with the school team and Propel Shiksha Awards recognition.'),
        body=body, schema=[breadcrumb_schema('leadership', 'Leadership')],
    )
