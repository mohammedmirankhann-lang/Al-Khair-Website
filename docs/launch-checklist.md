# Launch status and open items

Live at **https://alkhairacademy.in** since October 2026.

## Done

- [x] Seven pages: Home, Leadership, Community, Gallery, Admissions, Contact, Privacy, plus a 404 page
- [x] Domain `alkhairacademy.in` (Hostinger) connected to Vercel, HTTPS on
- [x] Google Search Console verified, sitemap submitted
- [x] Google Business Profile: website, phone and description added
- [x] SEO basics: unique titles and descriptions, one H1 per page, canonical URLs, School / FAQ /
      Breadcrumb structured data, Open Graph share image, descriptive alt text, sitemap and robots.txt
- [x] Photos graded to one consistent look; every photo grid uses uniform shapes
- [x] Code organised into `src/` (generator) and `public/` (served site); see README.md
- [x] Government recognition details added (Recognition Code 82237, School ID PS82237, Zila Shiksha Kendra Indore, valid to 31 March 2028)
- [x] Admissions wording follows the RTE Act: no admission test or screening
- [x] Gallery in sections with sub-headings; photo guidelines in docs/photo-guidelines.md

## Content to confirm with the school

- [ ] **Address:** the site uses "57/2, Haji Colony, Khajrana"; Google Maps shows "59". Use one version
      everywhere (website, Google Business Profile, letterhead, Justdial). Change it in `src/config.py`.
- [ ] **Team:** add mid-level management (name, role) to `TEAM` in `src/content.py`.
- [ ] **Propel Shiksha Awards:** confirm the year and category of the National Winner recognition.
- [ ] **Uniform:** the green polo seen in many photos is not described yet; say when it is worn and where to buy.
- [ ] **Photo consent:** written permission from parents for children whose faces are clearly visible.
- [ ] **Class list in the form:** Nursery and Class 1–8. Add LKG/UKG if used (`CLASS_OPTIONS` in `src/content.py`).
- [ ] Still to add when available: school timings, achievements, leadership bios, genuine testimonials with consent.

## Enquiry form

The form opens WhatsApp with the parent's details filled in (`SETTINGS.whatsapp` in `public/assets/js/main.js`).
To also receive enquiries by email, create a free form endpoint (for example Formspree, connected to
`alkhair.indore176@gmail.com`) and put its URL in `SETTINGS.formEndpoint`.

## Ownership

Keep every account in the school's name: domain, GitHub, Vercel, Google Search Console,
Google Business Profile and (when added) Google Analytics.
