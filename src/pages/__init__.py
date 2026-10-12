"""One module per page. Each module has a render() function that returns a Page."""
from dataclasses import dataclass, field


@dataclass
class Page:
    key: str                  # key in config.PAGES (used for the canonical URL)
    file: str                 # output file name in public/
    title: str                # <title> and social share title
    description: str          # meta description and social share text
    body: str                 # HTML inside <main>
    schema: list = field(default_factory=list)   # JSON-LD objects
    nav: str = ''             # menu item to highlight; defaults to key
    noindex: bool = False
    home_footer: bool = False  # the home page uses the full contact block instead of the standard footer


from . import home, leadership, community, gallery, admissions, contact, privacy, not_found  # noqa: E402

ALL = [home, leadership, community, gallery, admissions, contact, privacy, not_found]
