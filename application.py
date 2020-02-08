import os

from flask import Flask, render_template, request

from app import exceptions, sitemap_generator, utils


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home_form.html')


@app.route('/generate_sitemap', methods=['POST'])
def generate_sitemap():
    input_url = request.form['input_url']
    utils.validate_url(input_url)
    sitemap_png = sitemap_generator.make_sitemap_png(input_url)
    return render_template('sitemap.html', sitemap=sitemap_png)


# Exception handling
@app.errorhandler(exceptions.InvalidURLException)
def exception_handler(e):
    error_message = 'Your URL is invalid. Is it missing a scheme or a path?'
    return render_template('exception.html', error_message=error_message)


@app.errorhandler(500)
def error_handler(e):
    error_message = 'Something went wrong! Try again...'
    return render_template('exception.html', error_message=error_message)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
