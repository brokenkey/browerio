#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Cameron Brower'
SITENAME = 'Brower.io'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%Y-%M-%D'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
GITHUB_URL = 'https://github.com/brokenkey/browerio'


# Social widget
SOCIAL = (
    ('github', 'https://github.com/brokenkey'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = 'themes/Peli-Kiera-Orange'
ARTICLE_URL = '{author}/{slug}/'
ARTICLE_SAVE_AS = '{author}/{slug}/index.html'
