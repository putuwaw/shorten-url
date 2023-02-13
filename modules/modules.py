import random
import re
from models.url_list import UrlList


def insert_to_database(db, url, shortUrl):
    new = UrlList(
        url=url,
        url_short=shortUrl
    )
    db.session.add(new)
    db.session.commit()


def get_string_length():
    count = UrlList.query.count()
    return (count // (50 ** 4)) + 4


def random_string(length):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'

    shortUrl = ''

    isValid = False
    while not isValid:
        isValid = True
        shortUrl = ''.join(random.choice(lower + upper + digits)
                           for i in range(length))
        count = UrlList.query.filter(UrlList.url_short == shortUrl).count()
        if count > 0:
            isValid = False

    return shortUrl


def check_custom_url(customUrl):
    count = UrlList.query.filter(UrlList.url_short == customUrl).count()
    if count > 0:
        return "used"
    else:
        return customUrl

def is_valid_url(url):
    pattern = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        # domain...
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(pattern, url) is not None


def is_valid_custom(custom):
    pattern = r'^[\w-]+$'
    return re.match(pattern, custom)