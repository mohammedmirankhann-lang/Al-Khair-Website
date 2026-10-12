"""Editable content: lists and text blocks that change more often than the page layout.

To add a gallery photo: put it in public/assets/img with tools/add_photo.py,
then add one line to GALLERY below.
"""
from config import PHONE_DISPLAY, EMAIL

# Latest announcement, shown on the home page above the footer.
NOTICE = 'Admission enquiries are welcome for Nursery to Class 8. Nursery admission from age 3+.'

# Classes offered in the enquiry form.
CLASS_OPTIONS = ['Nursery'] + [f'Class {i}' for i in range(1, 9)]

# Focal point of each photo (CSS object-position), used wherever the photo is cropped
# into a fixed-shape box. Photos not listed are centred.
FOCUS = {
    'stage-dance': '50% 62%',
    'plant-girl-1': '50% 72%', 'plant-girl-2': '50% 72%', 'plant-girl-3': '50% 72%', 'plant-boy': '50% 72%',
    'tricolour-dance': '50% 25%', 'freedom-fighters': '50% 25%',
    'gandhi-smile': '50% 30%', 'costume-drama': '50% 30%', 'prizes': '50% 30%',
    'confidence': '50% 30%', 'flags': '50% 30%',
    'football-team': '50% 35%', 'jashn-group': '50% 35%',
    'awards': '50% 40%', 'kes-olympiad': '50% 45%',
    'principal-office': '50% 55%', 'trip-lalbagh': '50% 55%',
    'hero-children': '50% 60%', 'campus': '50% 60%',
    'trip-rajwada': '50% 72%',
    'urooj-speech': '65% 40%', 'jashn-speech': '30% 40%',
}

# Gallery page: (image name, caption / alt text, categories separated by spaces)
GALLERY = [
    ('stage-dance', 'Nursery students performing on Independence Day', 'events'),
    ('independence', 'Independence Day programme on the school stage', 'events'),
    ('tricolour-dance', 'Tricolour ribbon dance on stage', 'events'),
    ('gandhi-smile', 'A student dressed as Mahatma Gandhi', 'events'),
    ('freedom-fighters', 'Students dressed as freedom fighters', 'events'),
    ('costume-drama', 'Students in costume for a history drama', 'events'),
    ('plant-girl-1', 'Plantation drive: planting a sapling', 'plantation'),
    ('plant-boy', 'Plantation drive: potting a plant', 'plantation'),
    ('plant-girl-2', 'Plantation drive: a student with her plant', 'plantation'),
    ('plant-girl-3', 'Plantation drive: caring for a young plant', 'plantation'),
    ('football-team', 'Students lined up for a football match', 'sports'),
    ('principal-office', 'The Principal welcoming a young student', 'campus'),
    ('dance', 'Students forming a human pyramid at the annual function', 'events'),
    ('awards', 'National Winner recognition at the Propel Shiksha Awards', 'achievements'),
    ('kes-olympiad', 'Trophy presentation at the KES Olympiad 2025', 'achievements sports'),
    ('montessori-hospital', 'Montessori role play: the hospital corner', 'classrooms'),
    ('montessori-grocer', 'Montessori role play: the green grocer stall', 'classrooms'),
    ('trip-rajwada', 'Educational visit to Rajwada, Indore', 'visits'),
    ('trip-lalbagh', 'Educational visit to Lal Bagh Palace, Indore', 'visits'),
    ('sports-trophy', 'Al-Khair team with their trophy at an inter-school event', 'sports achievements'),
    ('prizes', 'Young students with their prize trophies', 'achievements'),
    ('hero-children', 'Students in festive dress at a school celebration', 'events'),
    ('trip-heritage', 'Students on a heritage visit', 'visits'),
    ('confidence', 'A student speaking on stage', 'events'),
    ('trip-hall', 'Students on an educational visit', 'visits'),
    ('urooj-stage', 'UROOJ 2026, Unfolding Stories of Success, Indore', 'community'),
    ('urooj-girls', 'Students registering at UROOJ 2026', 'community'),
    ('jashn-group', 'Jashn-e-Azadi community celebration', 'community'),
    ('football', 'Students heading onto the football ground', 'sports'),
    ('flags', 'Young students performing with the tricolour', 'events'),
    ('trip-garden', 'Girls on an educational visit', 'visits'),
    ('award', 'A student receiving a prize with his family', 'events achievements'),
    ('campus', 'Students walking to class past the school bus', 'campus'),
]

GALLERY_FILTERS = [
    ('all', 'All'), ('events', 'Events'), ('achievements', 'Achievements'), ('classrooms', 'Classrooms'),
    ('sports', 'Sports'), ('plantation', 'Plantation Drive'), ('visits', 'Educational Visits'),
    ('community', 'Community'), ('campus', 'Campus'),
]

# Leadership messages: (photo, name, role, paragraphs)
MESSAGES = [
    ('director', 'Adv. Parvez Khan', 'Director', [
        'Assalamu Alaikum. A school is more than a building; it is a trust that parents place in us. '
        'At Al-Khair Academy, we take that trust seriously.',
        'Our aim is to give the children of Khajrana an education that prepares them for the world while keeping '
        'them rooted in their values: sound academics in the CBSE pattern, modern tools such as smart classes, '
        'and a clear understanding of their faith.',
        "We are grateful to work alongside the schools, organisations and well-wishers of Khajrana who share this "
        "commitment to our children's future.",
    ]),
    ('principal', 'Adv. Rehana Khan', 'Founder &amp; Principal', [
        'Assalamu Alaikum. When we founded Al-Khair Academy in 2018, we began with one belief: every child is '
        'unique, and every child carries potential that deserves to be discovered.',
        'Education should not only fill a child with knowledge. It should help the child grow in creativity, in '
        'confidence and in good character. We try to understand each student, notice where they need support, '
        'and give that support with patience.',
        'Our aim is success for our children here and in the Hereafter. You are welcome to visit the school, '
        'meet our teachers and see this work for yourself.',
    ]),
]

# Academic & administrative team: (initials, name, role). Add one line per person.
TEAM = [
    ('SF', 'Mrs. Shabehina Farooqui', 'Coordinator'),
    ('RA', 'Mrs. Rahat Ali', 'Office &amp; Administration'),
]

FAQ = [
    ('Which board does Al-Khair Academy follow?',
     'Al-Khair Academy is a State Board school (Madhya Pradesh), and classes are taught in the CBSE pattern.'),
    ('Which classes are offered?', 'Nursery to Class 8.'),
    ('What is the age for Nursery admission?', 'Children aged 3 years and above are eligible for Nursery.'),
    ('How is Nursery taught?',
     'Our Nursery follows the Montessori method: children learn by doing, through hands-on materials, '
     'activities and role play.'),
    ('Is there an entrance test?',
     'Yes. Students appear for an entrance test, and the school office shares the details for each class.'),
    ('Which documents are needed for admission?',
     'Aadhaar Card, Samagra ID, Birth Certificate and Caste Certificate.'),
    ('Is religious education included?',
     'Yes. Through Understanding Quran, children learn the meaning of the Quran from a young age, along with '
     'hadith, duas and the sunnah of the Prophet ﷺ.'),
    ('Does the school have smart classes?', 'Yes. Lessons use Propel audio-visual content on smart TVs in the classroom.'),
    ('Is transport available?', 'Yes, a rickshaw transport facility is available. Please ask the office about routes.'),
    ('How do I contact the school?',
     f'Call or WhatsApp {PHONE_DISPLAY}, email {EMAIL}, or send the enquiry form on this page.'),
]
