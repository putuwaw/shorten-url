from flask import render_template, request, redirect, jsonify
from flask_cors import cross_origin
from modules import modules
from models.url_list import UrlList
from utils.db import db


def configure_routes(app):
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            url = request.form['name']
            customUrl = request.form['custom']

            shortUrl = ""

            if customUrl != "":
                shortUrl = modules.check_custom_url(customUrl)
                if shortUrl == "used":
                    templateData = {
                        'isPostCustom': True,
                        'customUrl': customUrl,
                        'url': url
                    }
                    return render_template("index.html", **templateData)
            else:
                length = modules.get_string_length()
                shortUrl = modules.random_string(length)

            modules.insert_to_database(db, url, shortUrl)

            templateData = {
                'isPost': True,
                'url': url,
                'shortUrl': shortUrl
            }
            return render_template("result.html", **templateData)
        else:
            return render_template("index.html")

    @app.route("/<shortUrl>")
    def redirecting(shortUrl):
        count = UrlList.query.filter(UrlList.url_short == shortUrl).count()

        if count == 0:
            return render_template("404.html")
        else:
            url = UrlList.query.filter(UrlList.url_short == shortUrl).first()
            return redirect(url.url, code=302)

    @app.route("/api", methods=['POST'])
    @cross_origin("*")
    def api():
        print("origin", request.environ.get('HTTP_ORIGIN'))
        req = request.get_json()
        url = req['url']
        customUrl = req['custom']

        shortUrl = ""

        if not modules.is_valid_url(url):
            return jsonify({
                'status': 'Error!',
                'message': 'Invalid URL.'
            })

        if customUrl != '':
            if not modules.is_valid_custom(customUrl):
                return jsonify({
                    'status': 'Error!',
                    'message': 'Invalid custom URL.'
                })
            shortUrl = modules.check_custom_url(customUrl)
            if shortUrl == "used":
                return jsonify({
                    'status': 'Error!',
                    'message': 'Custom URL is already used.'
                })
        else:
            length = modules.get_string_length()
            shortUrl = modules.random_string(length)

        modules.insert_to_database(db, url, shortUrl)

        return jsonify({
            'status': 'Success!',
            'message': 'Result: https://shrtn-url.vercel.app/{}'.format(shortUrl),
        })
