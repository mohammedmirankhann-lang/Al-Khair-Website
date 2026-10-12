"""Contact: address, phone, WhatsApp, email, directions and the enquiry form."""
import config as cfg
from components import (MAIL_URL, TEL_URL, WHATSAPP_URL, breadcrumb_schema, enquiry_form, ext, page_head, pic)
from pages import Page


def render():
    body = page_head('Contact', 'Visit us in Khajrana',
                     'We are happy to answer your questions. Call, send a WhatsApp message or visit the school.',
                     'Contact') + f'''
<section class="sec"><div class="wrap split align-start">
  <div class="stack">
    <div class="contact-grid">
      <div><span class="k">Address</span><span class="v">{cfg.ADDRESS}</span></div>
      <div><span class="k">Admissions phone</span><a class="v" href="{TEL_URL}">{cfg.PHONE_DISPLAY}</a></div>
      <div><span class="k">WhatsApp</span>{ext(WHATSAPP_URL, cfg.PHONE_DISPLAY, 'v')}</div>
      <div><span class="k">Email</span><a class="v" href="{MAIL_URL}">{cfg.EMAIL}</a></div>
    </div>
    <div class="btn-row">
      {ext(cfg.MAPS, 'Get Directions', 'btn btn-primary')}
      {ext(WHATSAPP_URL, 'Chat on WhatsApp', 'btn btn-ghost')}
    </div>
    <div class="frame r43">{pic('campus', 'Students walking to class at Al-Khair Academy')}</div>
    <p class="hint">Office &amp; Administration: Mrs. Rahat Ali</p>
  </div>
  {enquiry_form()}
</div></section>'''
    return Page(
        key='contact', file='contact.html',
        title='Contact & Directions | Al-Khair Academy, Khajrana Indore',
        description=('Contact Al-Khair Academy, 57/2 Haji Colony, Khajrana, Indore 452016. Call or WhatsApp '
                     f'{cfg.PHONE_DISPLAY}, email or get directions.'),
        body=body, schema=[breadcrumb_schema('contact', 'Contact')],
    )
