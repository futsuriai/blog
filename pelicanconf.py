#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from datetime import date

AUTHOR = u'Andres Franceschi'
SITENAME = u'Futsuriai'
SITEURL = 'futsuriai.com/blog'

TIMEZONE = 'America/New_York'

THEME = 'themes/futsuriaibootstrap'

DEFAULT_LANG = u'en'

GOOGLE_ANALYTICS = 'UA-39351368-1'

COPYRIGHT = 'Copyright &copy; %s Andres Franceschi. All rights reserved.' % date.today().year
COPYRIGHT_NAME = 'Andres Franceschi'

DEFAULT_LANG = u'en'

DEFAULT_PAGINATION = 3

DISQUS_SITENAME = 'futsuriai'

IGNORE_FILES = ['^.#', '~$']

FB_ADMINS = 'futsuriai'

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

ARTICLE_DIR = 'posts'
ARTICLE_URL = 'blog/posts/{slug}/'
ARTICLE_SAVE_AS = 'blog/posts/{slug}/index.html'

CATEGORY_URL = 'blog/articles/{slug}/'
CATEGORY_SAVE_AS = 'blog/articles/{slug}/index.html'
CATEGORIES_SAVE_AS = False
#GOOGLE_CUSTOM_SEARCH_SIDEBAR = '018193035311198604531:sstiw_ahsvu'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'blog_index')

SUMMARY_MAX_LENGTH = None

BLOG_INDEX_SAVE_AS = 'blog/index.html'

FILES_TO_COPY = (
    ('extra/.htaccess', '.htaccess'), 
    ('extra/robots.txt', 'robots.txt'),
    ('extra/favicon.ico', 'favicon.ico'),
    )
