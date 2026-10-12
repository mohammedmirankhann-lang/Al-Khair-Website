"""Build the Al-Khair Academy website.

    python3 src/build.py                    writes the HTML pages and sitemap.xml into public/
    python3 src/build.py --preview DIR      writes a self-contained copy with relative links into DIR

Only the HTML pages and sitemap.xml are generated. Styles, scripts, images and icons in
public/ are edited directly.
"""
import argparse
import datetime
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import components as ui          # noqa: E402
import config as cfg             # noqa: E402
import pages                     # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC = os.path.join(REPO, 'public')


def render_document(page):
    footer = ui.home_footer() if page.home_footer else ui.footer()
    return (ui.head(page.key, page.title, page.description, page.schema, page.noindex) + '\n'
            + ui.header(page.nav or page.key) + '\n<main id="main">\n' + page.body + '\n</main>\n'
            + footer + f'\n<script src="{ui.versioned("js/main.js")}" defer></script>\n</body>\n</html>\n')


def write_sitemap(out):
    today = datetime.date.today().isoformat()
    rows = ''.join(f'  <url><loc>{ui.canonical(k)}</loc><lastmod>{today}</lastmod>'
                   f'<priority>{cfg.SITEMAP_PRIORITY[k]}</priority></url>\n' for k in cfg.PAGES)
    with open(os.path.join(out, 'sitemap.xml'), 'w') as fh:
        fh.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                 '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + rows + '</urlset>\n')


def write_preview_entry(out, html):
    """Body-only copy of the home page for the claude.ai preview (it supplies its own document shell)."""
    head, rest = html.split('<head>', 1)[1].split('</head>', 1)
    keep = [line for line in head.splitlines() if line.startswith(('<link rel="stylesheet"', '<link rel="preconnect"'))]
    rest = rest.replace('<body>', '', 1).replace('</body>\n</html>\n', '')
    with open(os.path.join(out, 'preview-entry.html'), 'w') as fh:
        fh.write('<title>Al-Khair Academy Website</title>\n' + '\n'.join(keep) + rest)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--preview', metavar='DIR', help='build a preview copy with relative links into DIR')
    args = parser.parse_args()

    prod = not args.preview
    out = PUBLIC if prod else os.path.abspath(args.preview)
    ui.set_mode(prod)
    if not prod:
        shutil.copytree(PUBLIC, out, dirs_exist_ok=True,
                        ignore=shutil.ignore_patterns('*.html', 'sitemap.xml'))

    for module in pages.ALL:
        page = module.render()
        html = render_document(page)
        with open(os.path.join(out, page.file), 'w') as fh:
            fh.write(html)
        if not prod and page.file == 'index.html':
            write_preview_entry(out, html)
        print('  ' + page.file)

    if prod:
        write_sitemap(out)
        print('  sitemap.xml')
    print(f'Built {len(pages.ALL)} pages into {out}')


if __name__ == '__main__':
    main()
