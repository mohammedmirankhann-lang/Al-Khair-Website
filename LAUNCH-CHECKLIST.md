# Al-Khair Academy Website — Launch Package

Domain: **alkhairacademy.in** · Version: V1 (October 2026)

This folder is the complete website, ready to upload. It needs no database or build step.

## What is inside

| File / folder | Purpose |
|---|---|
| `index.html` | Home: crest, tagline, vision, belief, 3C, teaching methods (Montessori, Propel smart class, Understanding Quran, activities), school life, notices |
| `leadership.html` | Director's and Principal's messages, team, Propel Shiksha Awards, our story |
| `community.html` | KES, Urooj, community celebrations, educational visits |
| `gallery.html` | Gallery with category filter and full-screen viewer |
| `admissions.html` | Admissions process, documents, enquiry form |
| `contact.html` | Address, phone, WhatsApp, email, directions, enquiry form |
| `privacy.html` | Privacy policy |
| `404.html` | "Page not found" page |
| `sitemap.xml`, `robots.txt` | For Google Search Console |
| `site.webmanifest`, `favicon.ico`, `apple-touch-icon.png` | Browser and phone icons |
| `_redirects` | Sends old /about and /academics links to the new pages |
| `vercel.json` | Vercel settings: clean URLs, redirects, security headers |
| `_headers` | Security and caching headers (Cloudflare Pages / Netlify) |
| `assets/css/style.css` | All design styles (brand colours and fonts at the top) |
| `assets/js/main.js` | Menu, gallery and enquiry form. **Settings at the top of the file.** |
| `assets/img/` | Optimised photos (JPG + WebP, two sizes each), crest, icons, share image |

## Before launch: content to confirm

- [ ] **Team** (`leadership.html`): add mid-level management (name, role, optional photo).
- [ ] **Community photos** (`community.html`): confirm the Jashn-e-Azadi and UROOJ event photos may be published and that the captions are right.
- [ ] **Propel Shiksha Awards** (Home, About, Gallery): confirm the year and category of the National Winner recognition, and whether it is the school's or individual teachers' award.
- [ ] **Partners named on the site**: Propel (LEAD Group), Understand Al-Qur'an Academy, Khajrana Educational Society (KES) and Urooj. Confirm the wording about each and that the school is happy to name them.
- [ ] **Uniform** (`admissions.html`): confirm the description, and add where to buy it. The green polo seen in many photos is not described yet; tell us when it is worn.
- [ ] **Board wording**: the site says "State Board, CBSE Pattern" with Affiliation No. 82237. Confirm this is exactly how the school wants it stated.
- [ ] **Understand Quran attribution** (`academics.html`): confirm which courses are taught and that the school is happy to name Understand Al-Qur'an Academy publicly.
- [ ] **Admission process and documents** (`admissions.html`): confirm the five steps, the entrance test wording and the document list.
- [ ] **Class list in the form**: currently Nursery and Class 1–8. Add LKG/UKG or KG if the school uses them (in `build` or directly in the `<select>` in `admissions.html` and `contact.html`).
- [ ] **Address**: brief uses "57/2, Haji Colony, Khajrana"; the letterhead adds "Nipaniya Road". Use one version everywhere (website, Google Business Profile, Justdial, letterhead).
- [ ] **Notices** (`index.html`, section "Notices & Updates"): edit the two starter notices.
- [ ] **Photo consent**: written permission from parents for children whose faces are clearly visible, especially the prize distribution photo.
- [ ] Still to add when available: achievements, leadership bios, school timings, official Instagram/YouTube links, genuine testimonials with consent.

## Enquiry form

By default the form opens WhatsApp with the parent's details filled in (number set in `assets/js/main.js`, `SETTINGS.whatsapp`).

To also receive enquiries by email, create a free form endpoint (for example Formspree, connected to `alkhair.indore176@gmail.com`) and paste its URL into `SETTINGS.formEndpoint`. Parents then see the confirmation message from the brief, and WhatsApp remains the fallback.

## Going live on Vercel (chosen)

1. Unzip `al-khair-academy-website.zip` on a computer.
2. On github.com, create a new repository (for example `alkhair-academy-website`, Private is fine). Choose **uploading an existing file**, drag in **everything inside** the unzipped folder (not the folder itself), and press **Commit changes**.
3. On vercel.com, open the **AL-KHAIR** team, choose **Add New → Project**, import that repository, keep Framework Preset as **Other**, and press **Deploy**. You get a test link ending in `.vercel.app`.
4. Connect `alkhairacademy.in` to the project, then add the DNS records Vercel shows at the place where the domain was bought (usually an **A** record for `@` and a **CNAME** for `www`). HTTPS is added automatically.
5. `vercel.json` already gives clean URLs (`/leadership`), redirects for old links and security headers.

Keep ownership with the school: the school's own accounts own the domain, GitHub, Vercel, Google Analytics, Search Console and Google Business Profile.

## Launch-day checks

1. Open every page on a phone and a computer; test the enquiry form, WhatsApp, call and directions buttons.
2. **Google Search Console**: add `alkhairacademy.in`, verify, submit `https://alkhairacademy.in/sitemap.xml`.
3. **Google Analytics 4**: create a property and add its tag to every page's `<head>`.
4. **Google Business Profile**: add the website link; keep name, address and phone identical to the website.
5. Paste the link in WhatsApp and check the preview image appears.

## Already built in (SEO)

- Unique page titles and meta descriptions, one H1 per page, clean URLs and canonical tags
- School structured data (JSON-LD) on the home page; breadcrumbs on inner pages
- Open Graph share image (`assets/img/og-image.jpg`) and social tags
- Descriptive alt text on every photo; lazy-loaded, responsive WebP/JPG images
- `sitemap.xml`, `robots.txt`, 404 page, mobile-first layout
