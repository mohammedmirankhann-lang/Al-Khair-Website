"""School facts and external links.

Everything that describes the school itself (name, phone, address, board,
social accounts) lives here, so a change is made once and appears on every page.
"""

DOMAIN = 'https://alkhairacademy.in'

NAME = 'Al-Khair Academy'
TAGLINE = 'Nurturing Every Child Like a Seed'
VISION = 'Success Here and the Hereafter'
FOUNDED = '2018'
BOARD = 'State Board · CBSE Pattern'
CLASSES = 'Nursery to Class 8'
DISE_CODE = '23260104272'
AFFILIATION_NO = '82237'

# Contact
PHONE_DISPLAY = '+91 62646 72034'
PHONE_TEL = '+916264672034'
WHATSAPP = '916264672034'            # country code first, digits only (also set in public/assets/js/main.js)
EMAIL = 'alkhair.indore176@gmail.com'
STREET = '57/2, Haji Colony, Khajrana'
ADDRESS = f'{STREET}, Indore, Madhya Pradesh 452016'
MAPS = ('https://www.google.com/maps/dir/?api=1&destination='
        'Al-Khair+Academy+57%2F2+Haji+Colony+Khajrana+Indore+452016')

# Social accounts
INSTAGRAM = 'https://www.instagram.com/al_khairacademy/'
INSTAGRAM_HANDLE = '@al_khairacademy'
YOUTUBE = 'https://www.youtube.com/@AL-KHAIRACADEMYY'
YOUTUBE_HANDLE = '@AL-KHAIRACADEMYY'

# Partners
UNDERSTAND_QURAN = 'https://understandquran.com/'
PROPEL = 'https://propelschool.co/'
UROOJ = 'https://myurooj.in/'

FONTS = ('https://fonts.googleapis.com/css2?family=Amiri&family=Cinzel:wght@500;600;700'
         '&family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500'
         '&family=Lato:ital,wght@0,400;0,700;1,400&display=swap')

# Pages: key -> URL slug ('' is the home page). Order is the sitemap order.
PAGES = {
    'home': '',
    'leadership': 'leadership',
    'community': 'community',
    'gallery': 'gallery',
    'admissions': 'admissions',
    'contact': 'contact',
    'privacy': 'privacy',
}
SITEMAP_PRIORITY = {'home': '1.0', 'admissions': '0.9', 'leadership': '0.8', 'contact': '0.8',
                    'community': '0.7', 'gallery': '0.6', 'privacy': '0.3'}

# Structured data (JSON-LD) for the home page
SCHOOL_SCHEMA = {
    '@context': 'https://schema.org', '@type': 'School',
    'name': NAME,
    'alternateName': ['Al Khair Academy', 'Al-Khair Academy Indore', 'Al-Khair Academy Khajrana', 'Al-Khair School Indore'],
    'url': DOMAIN + '/', 'logo': DOMAIN + '/assets/img/icon-512.png', 'image': DOMAIN + '/assets/img/og-image.jpg',
    'description': ('State Board school in Khajrana, Indore, teaching in the CBSE pattern from Montessori Nursery '
                    'to Class 8, with Understanding Quran, Propel smart classes and the Creativity, Confidence and '
                    'Character framework.'),
    'slogan': TAGLINE, 'foundingDate': FOUNDED,
    'founder': {'@type': 'Person', 'name': 'Adv. Rehana Khan'},
    'employee': [{'@type': 'Person', 'name': 'Adv. Parvez Khan', 'jobTitle': 'Director'},
                 {'@type': 'Person', 'name': 'Adv. Rehana Khan', 'jobTitle': 'Founder & Principal'}],
    'telephone': PHONE_TEL, 'email': EMAIL,
    'address': {'@type': 'PostalAddress', 'streetAddress': STREET, 'addressLocality': 'Indore',
                'addressRegion': 'Madhya Pradesh', 'postalCode': '452016', 'addressCountry': 'IN'},
    'areaServed': 'Indore', 'award': 'National Winner, Propel Shiksha Awards',
    'sameAs': [INSTAGRAM, YOUTUBE],
}
