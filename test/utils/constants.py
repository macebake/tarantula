TINY_EXAMPLE_URL = 'https://vine.co/'
ALL_VALID_TEST_URLS = [
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

# https://vine.co/ expected results
EXPECTED_GRAPH_DATA = {
    'nodes': [
        'attribution',
        'vine.co',
        'terms',
        'privacy',
    ],
    'edges': [
        ('privacy', 'vine.co'),
        ('attribution', 'vine.co'),
        ('terms', 'vine.co'),
    ],
    'visited': {
        'https://vine.co/': True,
        'https://vine.co/terms': True,
        'https://vine.co/privacy': True,
        'https://vine.co/attribution': True,
    }
}
