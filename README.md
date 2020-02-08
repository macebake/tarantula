Welcome to `Tarantula`!

`Tarantula` is a simple flask app which, given a URL, generates a sitemap from internal links. You can visit the app [here](https://little-tarantula.herokuapp.com/), or follow the steps below to run locally.

## Run locally
From the root `tarantula/` directory:
- run `pip install -r requirements.txt`
- run `export FLASK_APP=application.py` to define the main app.
- run `flask run` and navigate to the local address provided.

## Functionality
Given a URL, `Tarantula` will create a network graph of connections to other internal URLs, until it has crawled the entire site -- within one subdirectory of the provided URL. This is done to avoid adding endless blog or forum posts (et cetera), but there is definitely a nicer way to handle these cases without omitting them entirely.

## Tests
From the root `tarantula/` directory, run `nosetests`.  

## Tradeoffs
`Tarantula` is so named because sometimes its output is a little hairy. Its output is most readable with compact websites (for example: try `https://byte.co`. `https://www.cityofsacramento.org/` is cool, but starts to get chaotic). The nodes of the network graph are labelled, but given some more time I prefer to color them, and include a corresponding legend.

A couple of other things I think `Tarantula` is sorely missing, but I am pushing time:
- A loading state for the sitemap
- Directions of node connections (is the link between `/privacy` and `/tos` one-way, or do they link to each other?)
