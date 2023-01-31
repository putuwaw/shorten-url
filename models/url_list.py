from utils.db import db


class UrlList(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(256), nullable=False)
    url_short = db.Column(db.String(256), nullable=False)

    def __init__(self, url, url_short):
        self.url = url
        self.url_short = url_short

    def __repr__(self):
        return '<UrlList %r>' % self.url
