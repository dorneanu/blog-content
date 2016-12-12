#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Victor Dorneanu'
SITENAME = 'blog.dornea.nu'
SITESUBTITLE = 'Hack, code and drink some țuică. Personal blog of Victor Dorneanu.'
SITEURL = 'http://blog.dornea.nu'

# Banner related
# BANNER = '/images/header.jpg'
# BANNER_SUBTITLE = 'Hack, code and drink some țuică. Personal blog of Victor Dorneanu.'
# BANNER_ALL_PAGES = False

TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = 'en'

# Feeds
FEED_DOMAIN = SITEURL
FEED_ATOM = 'feeds/atom.xml'
FEED_RSS = 'feeds/rss.xml'
CATEGORY_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
TRANSLATION_FEED = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

# Blogroll
LINKS =  (('dornea.nu', 'http://dornea.nu/'),
          ('nullsecurity.net', 'http://nullsecurity.net'),
          ('github.com/dorneanu', 'https://github.com/dorneanu'),
          ('github.com/nullsecurity', 'https://github.com/nullsecurity'))

MENUITEMS = [('Archives', '/archives'), ('About', 'http://dornea.nu')]

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)
SOCIAL = (('twitter', 'http://twitter.com/victordorneanu'),
          ('github', 'http://github.com/dorneanu'),
          ('xing', 'http://xing.to/dorneanu'),)
TWITTER_CARDS = True
TWITTER_USERNAME = "victordorneanu"

DEFAULT_PAGINATION = 15

# Set theme
THEME = "custom-themes/pelican-octopress-theme"
# THEME = "custom-themes/pelican-bootstrap3"

# Set default category
DEFAULT_CATEGORY = 'blog'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PAGE_URL = 'pages/{slug}'
PAGE_SAVE_AS = 'pages/{slug}.html'

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

ARCHIVES_URL = 'archives'
ARCHIVES_SAVE_AS = 'archives.html'

MARKUP = ('md', 'ipynb', 'markdown')
IGNORE_FILES = ['.vim*']
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['liquid_tags.img',
           'liquid_tags.graphviz',
           'liquid_tags.diag',
           'liquid_tags.video',
           'liquid_tags.youtube',
           'liquid_tags.vimeo',
           'liquid_tags.include_code',
           'liquid_tags.notebook',
           'sitemap',
           'related_posts',
           'extract_toc',
           'feed_summary',
           'pelican_dynamic']

# Set Tags settings
DISPLAY_TAGS_INLINE = True

# Set IPython notebooks settins
NOTEBOOK_DIR = 'ipython'
EXTRA_HEADER = open('nb_header.html').read().decode('utf-8')

# Set sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Lightbox2 settings
LIGHTBOX_PREFIX = ''
LIGHTBOX_SET = 'images'

# Cname settings
STATIC_PATHS = ['images', 'extra/CNAME']

# Metadata information
#DEFAULT_METADATA = (('yeah', 'it is'),)
PATH_METADATA = '(?P<date>\d{4}\/\d{2}\/\d{2})\/(?P<slug>.*)'
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/monokai.css': {'path': 'css/monokai.css'},
}

CUSTOM_CSS = 'css/custom.css'
CUSTOM_JS = 'js/custom.js'
SITE_KEYWORDS = "victor dorneanu, dorneanu, dornea.nu, blog, web, application security, linux, unix, hacking, assembler, python, ipython, javascript, c, c++, freebsd, netbsd, openbsd, debian, arch linux, blacktrack, kali linux"

# Social
DISQUS_SITENAME = "dorneanu"

# Pygments
PYGMENTS_STYLE = "native"

### Theme optimizations
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
RECENT_POST_COUNT = 7
SHOW_ARTICLE_CATEGORY = True
GITHUB_USER = "dorneanu"

# Twitter settinsg
TWITTER_USER = "victordorneanu"
TWITTER_TWEET_BUTTON = True
TWITTER_FOLLOW_BUTTON = True
TWITTER_WIDGET_ID = '468295751982784514'

# Google analytics
GOOGLE_ANALYTICS = 'UA-7161767-3'

SEARCH_BOX = True
# SITESEARCH = 'http://google.com/search'
QR_CODE = True

# Cache settings
LOAD_CONTENT_CACHE = False

# Markdown extensions
MD_EXTENSIONS = ['toc', 'fenced_code', 'codehilite(css_class=highlight, guess_lang=False)', 'extra']

# Use summaries instead of full article
FEED_USE_SUMMARY=True
# DISPLAY_ARTICLE_INFO_ON_INDEX = True

# BOOTSTRAP_THEME='spacelab'
# ADDTHIS_PROFILE = 'ra-559fc4045bb79811'
# ADDTHIS_DATA_TRACK_ADDRESSBAR = False
# SHOW_ARTICLE_AUTHOR = True

#SHARIFF = True
#SHARIFF_BACKEND_URL = 'http://blog.dornea.nu'
#SHARIFF_ORIENTATION = 'vertical'

# License settings
# CC_LICENSE = 'CC-BY'
