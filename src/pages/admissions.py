"""Admissions: key facts, process, documents, enquiry form, uniform, FAQ."""
from components import breadcrumb_schema, contact_band, enquiry_form, page_head, pic, rule
from content import FAQ
from pages import Page

STEPS = [
    ('Enquire', 'Send the enquiry form, message us on WhatsApp or call the school office.'),
    ('Visit the school', 'Meet the office team, see the campus and collect the admission form.'),
    ('Entrance test', "Students appear for an entrance test. The office shares the details for your child's class."),
    ('Submit documents', 'Hand in the completed form with the required documents.'),
    ('Confirmation', 'The office confirms admission and explains the next steps.'),
]
DOCUMENTS = ['Aadhaar Card', 'Samagra ID', 'Birth Certificate', 'Caste Certificate']
FACTS = [('Classes offered', 'Nursery to Class 8'), ('Nursery eligibility', '3 years and above'),
         ('Board', 'State Board, CBSE Pattern')]

FAQ_SCHEMA = {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
    {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in FAQ]}


def render():
    facts = '\n    '.join(f'<div class="info"><span class="k">{k}</span><span class="v">{v}</span></div>' for k, v in FACTS)
    steps = '\n      '.join(f'<li><div><b>{t}</b>{d}</div></li>' for t, d in STEPS)
    docs = ''.join(f'<li>{d}</li>' for d in DOCUMENTS)
    faq = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ)
    body = page_head('Admissions', 'Admissions &amp; Enquiry',
                     'Admission is open for Nursery to Class 8. Everything you need is on this page: eligibility, '
                     'process, documents, uniform and the enquiry form.', 'Admissions') + f'''
<section class="sec tight"><div class="wrap">
  <div class="info-grid">
    {facts}
  </div>
</div></section>

<section class="sec soft"><div class="wrap split align-start">
  <div class="stack">
    <span class="eyebrow">Admission Process</span><h2>How to apply</h2>{rule()}
    <ol class="steps">
      {steps}
    </ol>
    <div class="stack-sm docs"><span class="eyebrow">Required documents</span>
      <ul class="doclist">{docs}</ul>
      <p class="hint">Please confirm any class-specific requirements with the school office.</p></div>
  </div>
  {enquiry_form()}
</div></section>

<section class="sec"><div class="wrap split align-start">
  <div class="stack"><span class="eyebrow">School Uniform</span><h2>Our uniform</h2>{rule()}
    <p>A checked shirt in brown, orange and blue with brown trousers for boys, and a matching checked blouse with a brown pinafore for girls.</p>
    <p class="hint">Please ask the office where to buy the uniform.</p>
    <div class="uniform">
      <figure>{pic('uniform-girls', 'Girls uniform: checked blouse with brown pinafore', '(max-width: 860px) 50vw, 260px')}<figcaption>Girls</figcaption></figure>
      <figure>{pic('uniform-boys', 'Boys uniform: checked shirt with brown trousers', '(max-width: 860px) 50vw, 260px')}<figcaption>Boys</figcaption></figure>
    </div>
  </div>
  <div class="stack" id="faq"><span class="eyebrow">FAQ</span><h2>Questions parents ask</h2>{rule()}<div class="faq">{faq}</div></div>
</div></section>
{contact_band()}'''
    return Page(
        key='admissions', file='admissions.html',
        title='Admissions & Enquiry | Al-Khair Academy, Khajrana Indore',
        description=('Admissions at Al-Khair Academy, Indore for Nursery (age 3+, Montessori) to Class 8. State Board, '
                     'CBSE pattern. Process, entrance test, documents, uniform, FAQ and enquiry form.'),
        body=body, schema=[breadcrumb_schema('admissions', 'Admissions'), FAQ_SCHEMA],
    )
