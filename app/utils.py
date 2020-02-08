import os
from urllib.parse import urlparse

import requests

from settings import STATIC_PATH

from .exceptions import BadLinkException, InvalidURLException


def validate_url(url):
    parsed_url = urlparse(url)
    all_components = all([parsed_url.scheme, parsed_url.netloc, parsed_url.path])
    correct_scheme = parsed_url.scheme in ['http', 'https']
    if not all_components or not correct_scheme:
        raise InvalidURLException('Something is weird about your URL. Try again!')


def find_png_files_in_static_folder():
    return [file for file in os.listdir(STATIC_PATH) if file.endswith('.png')]


def remove_old_static_files():
    files = find_png_files_in_static_folder()
    for f in files:
        os.remove(f'{STATIC_PATH}{f}')


def make_request(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise BadLinkException(f'This link looks dodgy: {url}')
    return response


def edges_cleanup(edges):
    cleaned_edges = list(set([tuple(sorted(edge)) for edge in edges]))
    return cleaned_edges


def href_validator(href):
    # We define an internal link as an href that starts with `/`.
    # We're excluding fragments as well.
    internal_url_conditions = bool(
        href and href.startswith('/') and '#' not in href
    )
    return internal_url_conditions
