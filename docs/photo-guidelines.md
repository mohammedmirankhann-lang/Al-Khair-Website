# Photo guidelines: Al-Khair Academy website

Follow these rules for every photo you send for the website, so the site stays neat, consistent and safe for our children.

## 1. Before you click

- **Permission first.** Only send photos of children whose parents have agreed to school photos online. If a parent asks, the photo is removed.
- **Uniform and dignity.** Children in proper uniform or event dress, hair and dupatta/cap neat. No photos of a child crying, eating, or in an awkward pose.
- **Good light.** Daylight or a well-lit stage. Stand with the light behind you, not behind the children.
- **Hold the phone steady** and tap on the faces to focus.

## 2. How to frame the photo

- **Landscape (sideways) is best** for groups, stages and events. Portrait (upright) is fine for one or two children.
- **Keep faces in the middle third** of the frame, and leave some space around the group. The website shows photos in fixed boxes (mostly 4:3), so edges may be cut.
- **One clear subject:** one activity, one group. Avoid busy backgrounds, crowds of parents, or mobile screens.
- **Show the school when you can:** the crest backdrop, the banner, the uniform.

## 3. What not to send

- Screenshots, WhatsApp-forwarded photos, or photos with a time or date stamp, camera watermark, stickers, filters or text on them.
- Blurry, dark or very small photos (less than 1000 pixels wide).
- Photos where a child's name, phone number or address is readable.
- Two almost identical photos of the same moment: choose the best one.

## 4. How to send photos for the website

1. Send the **original file**, not a forwarded copy. On WhatsApp use *Attach → Document* so the quality is not reduced, or share through Google Drive.
2. Write one line per photo:
   **section** · **what is happening** · **date or event name**
   Example: *Plantation Drive · Class 5 students planting saplings · July 2026*
3. Gallery sections to choose from:
   - Events & Celebrations
   - Achievements & Sports
   - Montessori & Nursery
   - Plantation Drive
   - Educational Visits
   - Community
   - Campus & Leadership

## 5. How the website team adds a photo

1. Remove any stamp or watermark by cropping, if needed.
2. Prepare the photo: `python3 tools/add_photo.py photo.jpg short-name`
   This makes two sizes (1400px and 800px) and applies the same light colour grading as every other photo on the site.
   Use short lowercase names with hyphens, for example `sports-day-2026`.
3. Add one line to the right section of `GALLERY` in `src/content.py`:
   `('sports-day-2026', 'Students at Sports Day 2026'),`
   The caption is also the description read by Google and by screen readers: say what is happening, in plain words.
4. If faces are not in the centre, add a focal point to `FOCUS` in the same file, for example `'sports-day-2026': '50% 30%'` (30% keeps the top of the photo in view).
5. Keep each section to **a multiple of 3 photos** where possible, so every row on a computer is full. A short last row is centred automatically.
6. Run `python3 src/build.py`, check the Gallery page on a computer and a phone, then commit and push.
