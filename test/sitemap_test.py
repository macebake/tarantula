from nose.tools import raises
from random import randint

from .utils.constants import *
from app import exceptions, utils, sitemap_generator


def test_number_of_static_files_never_excedes_one():
    for url in ALL_VALID_TEST_URLS:
        files = utils.find_png_files_in_static_folder()
        sitemap_generator.make_sitemap_png(url)
        assert len(files) <= 1


def test_input_url_is_invalid():
    for url in INVALID_TEST_URLS:
        _invalid_url_exception_raised(url)


def test_link_is_invalid():
    for url in INVALID_REQUEST_URLS:
        _bad_link_exception_raised(url)


def test_bad_link_does_not_break_everything():
    index = randint(0, len(INVALID_REQUEST_URLS) - 1)
    bad_url = INVALID_REQUEST_URLS[index]
    links = sitemap_generator.find_links(bad_url, bad_url)
    assert links == []


def test_href_is_invalid():
    for href in INVALID_HREFS:
        assert utils.href_validator(href) is False


def test_graph_generates_as_expected():
    results = sitemap_generator.generate_graph_data(TINY_EXAMPLE_URL)
    for key in results:
        # We expect the same values, but possibly in a different order.
        assert sorted(results[key]) == sorted(EXPECTED_GRAPH_DATA[key])


@raises(exceptions.InvalidURLException)
def _invalid_url_exception_raised(url):
    utils.validate_url(url)


@raises(exceptions.BadLinkException)
def _bad_link_exception_raised(url):
    utils.make_request(url)
