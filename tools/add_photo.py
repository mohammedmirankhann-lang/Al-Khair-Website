"""Prepare a new photo for the website.

    python3 tools/add_photo.py PHOTO.jpg NAME

Writes public/assets/img/NAME.jpg (max 1400px) and NAME-800.jpg with the same light
grading used on every photo on the site, so new photos match the old ones:
gentle auto-contrast, a lift for dark photos, a touch less brightness for very bright
ones, slightly richer colour and light sharpening.

Then use the photo in src/ (for example add a line to GALLERY in src/content.py,
and a focal point to FOCUS if the subject is not centred) and run python3 src/build.py.
"""
import os
import sys

from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageStat

IMG_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'public', 'assets', 'img')
SIZES = [('', 1400, 84), ('-800', 800, 80)]   # (file suffix, longest side, JPEG quality)


def grade(im):
    im = ImageOps.autocontrast(im, cutoff=0.6, preserve_tone=True)
    lum = ImageStat.Stat(im.convert('L')).mean[0] / 255
    if lum < 0.42:                                   # dark photo: lift the mid-tones
        gamma = 0.82
        im = im.point(lambda v: round(255 * (v / 255) ** gamma))
    elif lum > 0.68:                                 # very bright photo: tone down a little
        im = ImageEnhance.Brightness(im).enhance(0.96)
    im = ImageEnhance.Color(im).enhance(1.06)
    return im.filter(ImageFilter.UnsharpMask(radius=1.2, percent=55, threshold=3))


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    src, name = sys.argv[1], sys.argv[2]
    im = ImageOps.exif_transpose(Image.open(src)).convert('RGB')
    im = grade(im)
    for suffix, longest, quality in SIZES:
        out = im.copy()
        out.thumbnail((longest, longest), Image.LANCZOS)
        path = os.path.join(IMG_DIR, f'{name}{suffix}.jpg')
        out.save(path, 'JPEG', quality=quality, optimize=True, progressive=True)
        print(f'  {os.path.relpath(path)}  {out.size[0]}x{out.size[1]}')


if __name__ == '__main__':
    main()
