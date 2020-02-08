from random import randint
from urllib.parse import urlparse

from bs4 import BeautifulSoup, SoupStrainer

import matplotlib.pyplot as plt
import networkx as nx

from .exceptions import BadLinkException
from .utils import *
from settings import STATIC_PATH


def make_sitemap_png(input_url):
    results = generate_graph_data(input_url)

    # Generate random name for temporary graph file
    file_name = f'{randint(100, 999)}.png'
    file_path = f'{STATIC_PATH}{file_name}'

    generate_and_save_graph(results, file_path)
    return file_name


def generate_and_save_graph(results, path):
    # Cleanup
    remove_old_static_files()

    # Generate network graph
    G = nx.OrderedGraph()
    G.add_nodes_from(results['nodes'])
    G.add_edges_from(results['edges'])
    degrees = dict(G.degree)
    nx.draw(
        G,
        pos=nx.spring_layout(G),
        edge_color='gray',
        node_color='y',
        node_size=[v * 50 for v in degrees.values()],
        with_labels=True,
    )

    # Save graph file
    plt.savefig(path)
    plt.close()


def generate_graph_data(base_url):
    base_url_detail = {'name': urlparse(base_url).netloc, 'url': base_url}
    nodes = [base_url_detail['name']]
    edges = []
    visited_links = {base_url_detail['url']: True}
    initial_internal_links = find_links(base_url, base_url)
    current_depth = 0
    max_depth = 5

    def link_loop(base_link, link_list, current_depth):
        nodes.extend([link['name'] for link in link_list])
        edges.extend([(base_link['name'], link['name']) for link in link_list])

        for link in link_list:
            if link.get(link['url']):
                continue

            new_link_list = find_links(base_url, link['url'])
            visited_links[link['url']] = True

            current_depth += 1
            if current_depth != max_depth:
                link_loop(link, new_link_list, current_depth)

    link_loop(base_url_detail, initial_internal_links, current_depth)

    return {
        'nodes': list(set(nodes)),
        'edges': edges_cleanup(edges),
        'visited': visited_links,
    }


def find_links(base_url, link_url):
    links = []

    # Rather than exiting, just skip this link if we can't successfully request it.
    try:
        response = make_request(link_url)
    except BadLinkException:
        return links

    soup = BeautifulSoup(
        response.content,
        'lxml',
        from_encoding='utf-8',
        parse_only=SoupStrainer('a', href=True),
    )

    for a in soup.find_all(href=href_validator):
        # We're only going one level deep with the URLs we find. This keeps us from
        # parsing every single path for a blog or a forum, etc., which isn't helpful
        # and just crowds the graph.
        href = dict(a.attrs).get('href').split('/')[1]
        new_url = f'{base_url}{href}'

        if new_url == base_url:
            continue

        links.append({
            'name': href,
            'url': new_url,
        })

    soup.decompose()

    return links
