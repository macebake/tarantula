TINY_EXAMPLE_URL = 'https://byte.co/'
ALL_VALID_TEST_URLS = [
    'https://vine.co/',
    'https://yearhere.org/',
    TINY_EXAMPLE_URL,
]
INVALID_REQUEST_URLS = [
    'https://monzo.com/bananas',
    'https://www.amazon.com/some-random-domain',
    'https://vine.co/login',
]
INVALID_TEST_URLS = [
    'https://monzo.com',
    'www.google.com/',
    'mailto:testperson@domain.com',
    '/',
    'twitter.com',
]
INVALID_HREFS = ['/page#link', 'privacy', '']

# https://byte.co/ expected results
EXPECTED_GRAPH_DATA = {
    'nodes': [
        'contact',
        'dmca',
        'copyright',
        'terms',
        'privacy',
        'guidelines',
        'byte.co',
    ],
    'edges': [
        ('contact', 'privacy'),
        ('dmca', 'terms'),
        ('dmca', 'guidelines'),
        ('copyright', 'guidelines'),
        ('copyright', 'terms'),
        ('guidelines', 'privacy'),
        ('copyright', 'privacy'),
        ('contact', 'contact'),
        ('dmca', 'privacy'),
        ('privacy', 'terms'),
        ('byte.co', 'guidelines'),
        ('byte.co', 'terms'),
        ('guidelines', 'terms'),
        ('guidelines', 'guidelines'),
        ('contact', 'dmca'),
        ('privacy', 'privacy'),
        ('terms', 'terms'),
        ('byte.co', 'privacy'),
        ('contact', 'guidelines'),
        ('contact', 'terms'),
        ('contact', 'copyright'),
        ('byte.co', 'contact'),
    ],
    'visited': [
        'https://byte.co/',
        'https://byte.co/terms',
        'https://byte.co/privacy',
        'https://byte.co/guidelines',
        'https://byte.co/dmca',
        'https://byte.co/contact',
        'https://byte.co/copyright',
    ],
}
