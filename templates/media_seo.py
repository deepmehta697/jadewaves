"""Factual metadata for visible media; no dependency on browser/encoding tools."""
from html.parser import HTMLParser
from urllib.parse import urlsplit


# First public availability of these new encodes, recorded by completed Pages
# deployments (39403517318, 39406564517, 39408379119), not camera/file timestamps.
# Legacy Operations clips have no verified first-publication date here: do not
# invent one or emit incomplete Google VideoObject markup for them.
VIDEOS = {
    '/assets/bentonite/bentonite-clip.mp4': {
        'name': 'Bentonite yard footage',
        'description': 'A view of material stockpiles, a loader and the yard shown on the Bentonite product page.',
        'thumbnail': '/assets/bentonite/bentonite-clip-poster.webp',
        'uploadDate': '2026-10-20T09:50:24Z', 'duration': 'PT16.125S',
    },
    '/assets/product-handling/material-handling.mp4': {
        'name': 'Quartz material stockpiles',
        'description': 'Quartz stockpile footage supplied for the Quartz product page, showing mineral lumps and the yard.',
        'thumbnail': '/assets/product-handling/material-handling-poster.webp',
        'uploadDate': '2026-10-20T10:15:24Z', 'duration': 'PT22.542S',
    },
    '/assets/feldspar/feldspar-footage.mp4': {
        'name': 'Feldspar bagged-material footage',
        'description': 'Footage supplied for the Feldspar product page, showing bagged material and the packing area.',
        'thumbnail': '/assets/feldspar/feldspar-footage-poster.webp',
        'uploadDate': '2026-10-20T10:15:24Z', 'duration': 'PT17.875S',
    },
    '/assets/dispatch/dispatch-loading.mp4': {
        'name': 'Packed quartz silica bags in the dispatch yard',
        'description': 'Packed bags marked Jade Waves Quartz Silica arranged in the dispatch yard before shipment.',
        'thumbnail': '/assets/dispatch/dispatch-loading-poster.webp',
        'uploadDate': '2026-10-20T10:30:40Z', 'duration': 'PT8.875S',
    },
}


class PageMedia(HTMLParser):
    def __init__(self, body):
        super().__init__()
        self.images, self.videos = [], []
        self.in_main = False
        self.video = None
        self.feed(body)

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == 'main': self.in_main = True
        if not self.in_main: return
        if tag == 'img': self.images.append(attrs)
        if tag == 'video':
            self.video = {**attrs, 'sources': []}
            self.videos.append(self.video)
        if tag == 'source' and self.video is not None:
            self.video['sources'].append(attrs.get('src', ''))

    def handle_endtag(self, tag):
        if tag == 'video': self.video = None
        if tag == 'main': self.in_main = False


def video_schemas(base, path, media):
    result = []
    for video in media.videos:
        source = next((src for src in video['sources'] if src in VIDEOS), None)
        if not source: continue
        data = VIDEOS[source]
        if video.get('poster') != data['thumbnail']:
            raise ValueError('Video poster and SEO thumbnail differ: ' + source)
        result.append({
            '@context': 'https://schema.org', '@type': 'VideoObject',
            '@id': base + source + '#video', 'name': data['name'],
            'description': data['description'], 'contentUrl': base + source,
            'thumbnailUrl': [base + data['thumbnail']],
            'uploadDate': data['uploadDate'], 'duration': data['duration'],
            'encodingFormat': 'video/mp4',
            'isPartOf': {'@type': 'WebPage', '@id': base + path},
        })
    return result


def social_image(base, schema, media, company):
    """Use the actual product/article image, then visible main-content imagery."""
    image = next((item.get('image') for item in schema
                  if item.get('@type') in {'Product', 'BlogPosting'} and item.get('image')), None)
    if isinstance(image, list): image = image[0]
    if not image and media.images: image = media.images[0].get('src')
    image = image or '/assets/jade-waves-logo-transparent.png'
    if not image.startswith('https://'): image = base + '/' + image.lstrip('/')
    matching = next((item for item in media.images
                     if urlsplit(item.get('src', '')).path.lstrip('/') == urlsplit(image).path.lstrip('/')), {})
    alt = matching.get('alt') or next((item['name'] for item in schema
                                      if item.get('@type') == 'Product'), company)
    card = 'summary' if image.endswith('/jade-waves-logo-transparent.png') else 'summary_large_image'
    return image, alt, card
