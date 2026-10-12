"""Privacy policy."""
import config as cfg
from components import MAIL_URL, breadcrumb_schema, page_head
from pages import Page


def render():
    body = page_head('Policy', 'Privacy Policy',
                     'How Al-Khair Academy handles information shared through this website. Last updated October 2026.',
                     'Privacy Policy') + f'''
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
  <p>For any privacy question or request, write to <a href="{MAIL_URL}">{cfg.EMAIL}</a> or call {cfg.PHONE_DISPLAY}.</p>
</div></section>'''
    return Page(
        key='privacy', file='privacy.html',
        title='Privacy Policy | Al-Khair Academy',
        description=('Privacy policy of Al-Khair Academy, Indore: what information the admission enquiry form '
                     'collects and how it is used.'),
        body=body, schema=[breadcrumb_schema('privacy', 'Privacy Policy')], nav='none',
    )
